# Renux

Renux is a simple Python application that provides a graphical user interface (GUI) for backing up and restoring installed packages on an Ubuntu system. The application uses `dpkg` and `apt-get` to manage package selections and installations.

## Features

- Backup the list of installed packages to a file.
- Restore packages from a backup file.
- Simple and intuitive GUI built with Tkinter.

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- `dpkg` and `apt-get` (available on Ubuntu systems)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/renux.git
    cd renux
    ```

2. Ensure you have the required dependencies:
    ```sh
    sudo apt-get install dpkg apt-get
    ```

## Usage

1. Run the application:
    ```sh
    python renux.py
    ```

2. The GUI will open with three buttons:
    - **Backup Installed Packages**: Click to backup the list of installed packages to a file.
    - **Restore Packages from Backup**: Click to restore packages from a previously saved backup file.
    - **Exit**: Click to exit the application.

## Code Overview

- `backup_packages()`: Prompts the user to save a backup file and saves the list of installed packages.
- `restore_packages()`: Prompts the user to select a backup file and restores the packages from the file.
- `create_gui()`: Creates the GUI for the application with Tkinter.