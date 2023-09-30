# Virtual Py

**Virtual Py** is a Discord bot designed for Python programming within your Discord server. With Virtual Py, you can create, read, and execute Python scripts within a simulated file system.

## Features

- **Simulated File System**: Organize your Python scripts in an in-memory file system.
- **Script Execution**: Run Python scripts and view the output directly in Discord.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- [discord.py](https://pypi.org/project/discord.py/)
- A Discord bot token

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/lawsus/virtual-py.git
    cd virtual-py
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up your Discord bot token:

    - Modify the `.env` file in the project root.
    - Replace YOUR_DISCORD_TOKEN with your token:

    ```env
    DISCORD_TOKEN=YOUR_DISCORD_TOKEN
    ```
4. Ensure message content privileged intent is enabled ([info](https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html)):
    - Go to the [developer portal](https://discord.com/developers/applications).
    - Enable message content in the Privileged Gateway Intents section of the Bot page.

### Running the Bot

1. Start the bot by running:

    ```bash
    python bot/main.py
    ```

2. Invite the bot to your Discord server and start using it !

## Usage

- Create or overwrite a Python file:

    ```
    vp write <filename.py>
    ```python
    (Your Python code here)```
    ```

- Read a Python file:

    ```
    vp read <filename.py>
    ```

- Run a Python file:

    ```
    vp run <filename.py>
    ```

- List directories:

    ```
    vp ls
    ```

- Create a new directory:

    ```
    vp mkdir <directory_name>
    ```

- Change directory:

    ```
    vp cd <directory_path>
    vp cd ..
    ```

## Safety Precautions

Virtual Py executes Python code, which can be dangerous if not handled properly. To mitigate the dangers, various safety measures have been implemented. These include rating limiting on commands, timeouts on code execution, and checks for forbidden imports and built-in commands within the code. Despite these precautions, it's important to use Virtual Py cautiously as these aren't guarantees.

## Future / TODO
- change to a whitelist over a blacklist for imports
- improve efficiency of code_validator
- conduct more tests to identify security vulnerabilities
- change from an in-memory file system to a database
- replace the subprocess implementation with a sandbox mechanism

## Contributing

Contributions are welcome.
