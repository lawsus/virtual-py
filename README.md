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

### Running the Bot

1. Start the bot by running:

    ```bash
    python bot/main.py
    ```

2. Invite the bot to your Discord server and start using it!

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

Virtual Py executes Python code, which can be dangerous if not handled properly. It's crucial to implement safety measures to prevent the execution of malicious code.

**To implement**:
- Rate limiting.
- Timeout for script execution.
- Restricted access to sensitive Python modules.

## Contributing

Contributions are welcome.
