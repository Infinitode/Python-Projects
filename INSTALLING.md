# This is guide to install python

**Contents:**
- [Installing python at Windows](#install-at-windows)
- [Installing python at macOS](#install-at-macos)
- [Installing python using pyenv](#install-by-pyenv)
- [Installing VS Code](#installing-visual-studio-code)

## Install at Windows

There are several ways to install python in Windows, but we're recommending this 2 ways!
- Way 1. Install using **Python Install Manager**
  - Step 1. Open Microsoft store (*You can skip Step 1 & Step 2 by [this link](https://apps.microsoft.com/detail/9nq7512cxl7t)*)
  - Step 2. Search for `Python Install Manager` and install it
  - Step 3. Click open & Follow on screen instructions

  ***DONE!***
   
- Way 2. Install from direct .exe installer (not available from Python 3.15)
   - Step 1. Head to [python's downloads website](https://python.org/downloads/).
   - Step 2. Click latest or [this recommended version](https://www.python.org/downloads/release/python-313/)
   - Step 3. Download `Windows installer` to get .exe installer
   - Step 4. Double-click download .exe file and follow on screen instructions (plus checkmark at Add Python to PATH)

   ***DONE!***

## Install at macOS

- Step 1.  **Download the Installer**: Go to the official Python website at [python.org/downloads/](https://python.org/downloads/) and download the macOS installer package (`.pkg`).
  - Recommended version: [3.13](https://www.python.org/downloads/release/python-313/)

- Step 2.  **Run the Installer**: Open the downloaded `.pkg` file and follow the on-screen instructions. You'll need to enter your Mac's administrator password.
- Step 3.  **Complete the Setup**:
    *   Once the installation finishes, go to your `Applications` folder and open the new `Python 3.x` folder (the number will be the version you installed).
    *   Double-click on the `Install Certificates.command` file. This is an important step to ensure your Python can securely connect to websites.

## Install by Pyenv
There's simple way to install python in Linux. It's called pyenv, python environment manager, almost same functionatilly as Python Install Manager in Windows.
1. Install dependencies 
  * **Ubuntu/Debian/Mint:**
    ```bash
    sudo apt update
    sudo apt install -y git make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
    ```
  * **Fedore/RHEL/Red-Hat based OS:**
    ```bash
    sudo dnf groupinstall "Development Tools"
    sudo dnf install git openssl-devel bzip2-devel libffi-devel readline-devel sqlite-devel xz-devel tk-devel
    ```
  * **Arch:**
    ```bash
    sudo pacman -S --needed base-devel
    sudo pacman -S git openssl zlib bzip2 readline sqlite3 libffi xz tk
    ```
2. Run installer
  * `curl https://pyenv.run | bash`
3. Follow on-screen instructions
4. Install python using `pyenv install <version>`, replace `<version>` with actual version (like 3.14)
  * Recommended version: 3.13
    
***DONE!**

## Installing Visual Studio Code

- On Windows, go to [here](https://apps.microsoft.com/detail/xp9khm4bk9fz7q) and install the VS Code.
- On Linux, go to [here](https://code.visualstudio.com/docs/setup/linux) and install the VS Code 
- On macOS, go to [here](https://code.visualstudio.com/docs/setup/mac) and install the VS Code

###### <small>made by @Ericwasepic127</small> 
