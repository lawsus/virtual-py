import ast


def check_length(code, max_length=3000):
    if len(code) > max_length:
        return False, f"Code length exceeds max length of {max_length}"
    return True, ""


def check_forbidden_builtins(code):
    forbidden_builtins = [
        "eval",
        "exec",
        "compile",
        "open",
        "globals",
        "locals",
        "__import__",
        "reload",
        "input",
        "help",
    ]
    try:
        tree = ast.parse(code)
        # generated with chat gpt
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                if node.func.id in forbidden_builtins:
                    return False, f"Forbidden built-in function: {node.func.id}"
            elif isinstance(node, ast.Attribute):
                if node.func.attr in forbidden_builtins:
                    return False, f"Forbidden built-in function: {node.func.attr}"
    except Exception as e:
        return False, "Errror: Failed to parse code"
    # no forbidden builtins
    return True, ""


def check_forbidden_imports(code):
    forbidden_imports = [
        "os",
        "sys",
        "subprocess",
        "shutil",
        "socket",
        "signal",
        "ctypes",
        "cffi",
        "thread",
        "threading",
        "multiprocessing",
        "dl",
        "fcntl",
        "mmap",
        "select",
        "grp",
        "pwd",
        "crypt",
        "tty",
        "termios",
        "pty",
        "resource",
        "gc",
        "inspect",
    ]
    try:
        tree = ast.parse(code)
        # generated with chat gpt
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name in forbidden_imports:
                        return False, f"Forbidden import: {alias.name}"
            elif isinstance(node, ast.ImportFrom):
                if node.module in forbidden_imports:
                    return False, f"Forbidden import {alias.name}"
    except Exception as e:
        return False, "Failed to parse code"
    # no forbidden imports
    return True, ""


def validate_code(code):
    checks = [check_length, check_forbidden_builtins, check_forbidden_imports]
    for check in checks:
        passed, message = check(code)
        if not passed:
            return False, message
    return True, ""
