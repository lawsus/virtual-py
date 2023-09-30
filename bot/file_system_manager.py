import os
import subprocess
import uuid
from code_validator import validate_code


class FileSystemManager:
    def __init__(self):
        # user id to file system
        self.file_system = {}
        # user id to current paths
        self.current_paths = {}

    def _get_current_directory(self, path):
        current_folder = self.file_system
        for folder in path:
            if folder in current_folder:
                current_folder = current_folder[folder]
            else:
                return None
        return current_folder

    def _get_current_path(self, user_id):
        # default file system and current directory
        if user_id not in self.file_system:
            self.file_system[user_id] = {}
        if user_id not in self.current_paths:
            self.current_paths[user_id] = [user_id]
        # get current path
        return self.current_paths.get(user_id)

    def write_file(self, user_id, file_name, content):
        # navigate to current directory using current path
        current_path = self._get_current_path(user_id)
        current_directory = self._get_current_directory(current_path)

        # add file name and content to current directory
        current_directory[file_name] = content

    def read_file(self, user_id, file_name):
        # navigate to current directory using current path
        current_path = self._get_current_path(user_id)
        current_directory = self._get_current_directory(current_path)

        # return code from file name
        return current_directory.get(file_name, "File not found")

    def run_file(self, user_id, file_name):
        code = self.read_file(user_id, file_name)
        if code == "File not found":
            return code

        # validate code
        is_valid, validation_message = validate_code(code)
        if not is_valid:
            return validation_message

        # unique id so multiple users can run files with the same name
        temp_file_name = f"temp_{user_id}_{file_name}_{uuid.uuid4()}"
        with open(temp_file_name, "w") as temp_file:
            temp_file.write(code)

        # shell is left as False for security
        try:
            output = subprocess.check_output(
                ["python3", temp_file_name],
                stderr=subprocess.STDOUT,
                text=True,
                timeout=5,
            )
            os.remove(temp_file_name)
            return output
        except subprocess.CalledProcessError as e:
            os.remove(temp_file_name)
            return e.output
        except subprocess.TimeoutExpired:
            os.remove(temp_file_name)
            return "Execution timed out"

    def list_directories(self, user_id):
        # navigate to current directory using current path
        current_path = self._get_current_path(user_id)
        current_directory = self._get_current_directory(current_path)

        # return files/folders in current directory
        return list(current_directory.keys())

    def make_directory(self, user_id, dir_name):
        # navigate to current directory using current path
        current_path = self._get_current_path(user_id)
        current_directory = self._get_current_directory(current_path)

        if dir_name not in current_directory:
            current_directory[dir_name] = {}
            return f"Directory {dir_name} created successfully"
        else:
            return f"Directory {dir_name} already exists"

    def change_directory(self, user_id, path):
        # navigate to current directory using current path
        current_path = self._get_current_path(user_id)
        current_directory = self._get_current_directory(current_path)

        if path.strip() == "..":
            if len(current_path) > 1:
                current_path.pop()
                if len(current_path) == 1:
                    return "Changed to root directory successfully"
                else:
                    return f'Changed to directory {"/".join(current_path[1:])} successfully'
            else:
                return f"Already at root directory"
        else:
            path_elements = path.split("/")
            for folder in path_elements:
                if folder in current_directory and isinstance(
                    current_directory[folder], dict
                ):
                    current_directory = current_directory[folder]
                else:
                    return f'Directory {"/".join(path_elements)} does not exist'
            current_path.extend(path_elements)
            return f'Changed to directory {"/".join(path_elements)} successfully'
