# Python & VS Code Installation Guide

A comprehensive guide to setting up Python and Visual Studio Code across Windows, macOS, and Linux.

## Contents
- [Windows Installation](#windows-installation)
- [macOS Installation](#macos-installation)
- [Linux Installation (using pyenv)](#linux-installation-using-pyenv)
- [Visual Studio Code Installation](#visual-studio-code-installation)

---

## Windows Installation

We recommend choosing one of the following two methods to install Python on Windows:

### Method 1: Using the Python Install Manager (Recommended)
1. Open the Microsoft Store or use this [direct store link](https://apps.microsoft.com/detail/9nq7512cxl7t).
2. Search for **Python Install Manager** and click **Install**.
3. Open the application and follow the on-screen instructions to complete the setup.

### Method 2: Using the Direct Executable Installer
> ⚠️ **Note:** Standard `.exe` direct installers are deprecated starting from Python 3.15. For newer versions, please use Method 1.

1. Navigate to the official [Python Downloads page](https://python.org/downloads/).
2. Select the latest release, or download the [recommended Python 3.13 version](https://www.python.org/downloads/release/python-313/).
3. Download the **Windows installer** executable (`.exe`).
4. Double-click the downloaded file to run the installer.
5. **Crucial:** Ensure you check the box that says **"Add Python to PATH"** before clicking install, then follow the remaining prompts.

---

## macOS Installation

1. **Download the Installer:** Visit the official [Python Downloads page](https://python.org/downloads/) and download the macOS installer package (`.pkg`). The [recommended version is 3.13](https://www.python.org/downloads/release/python-313/).
2. **Run the Installer:** Open the downloaded `.pkg` file and follow the on-screen installation steps. You will be prompted to enter your Mac's administrator password.
3. **Install Certificates:** 
   - Once complete, open your `Applications` folder and locate the newly created `Python 3.x` directory.
   - Double-click the `Install Certificates.command` file. *This step is required to ensure Python can securely connect to the internet.*

---

## Linux Installation (using pyenv)

For Linux distributions, we recommend using `pyenv`, a robust Python environment manager that functions similarly to Windows' Install Manager.

### 1. Install Dependencies
Open your terminal and run the appropriate command for your package manager to install the required build dependencies:

* **Ubuntu / Debian / Mint:**
  ```bash
  sudo apt update
  sudo apt install -y git make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```


* **Fedora / RHEL / CentOS:**
   ```bash
   sudo dnf groupinstall "Development Tools"
   sudo dnf install git openssl-devel bzip2-devel libffi-devel readline-devel sqlite-devel xz-devel tk-devel  
   ```

* **Arch Linux:**
   ```bash
   sudo pacman -S --needed base-devel
   sudo pacman -S git openssl zlib bzip2 readline sqlite3 libffi xz tk
   ```
### 2. Install and Configure pyenv
 1. Run the automatic installer script:
   ```bash
   curl [https://pyenv.run](https://pyenv.run) | bash
   ```
2. Follow the instructions printed in the terminal to add pyenv to your shell profile configurations (e.g., .bashrc or .zshrc).
3. Restart your terminal or source your profile to apply the changes.

### 3. Install Python
Install your desired version using pyenv. We recommend version 3.13:
```bash
pyenv install 3.13
pyenv global 3.13
```

## Visual Studio Code Installation
Get your development environment ready by installing Visual Studio Code for your platform:
 * **Windows:** Download via the Microsoft Store Link.
 * **macOS:** Follow the official macOS Setup Guide.
 * **Linux:** Follow the official Linux Setup Guide for .deb, .rpm, or Snap packages.

<sub>Contributed by @Ericwasepic127</sub>