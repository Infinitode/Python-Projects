## This is guide to install python

Contents:
- [Installing python at Windows](#install-at-windows)
- [Installing python using pyenv](#install-by-pyenv)
- [Installing VS Code](#installing-visual-studio-code)

## Install at Windows

There are several ways to install python in Windows, but we're recommending this 2 ways!
1. Install using **Python Install Manager**
 - Step 1. Open Microsoft store (*You can skip Step 1 & Step 2 by [this link](https://apps.microsoft.com/detail/9nq7512cxl7t)*)
 - Step 2. Search for `Python Install Manager` and install it
 - Step 3. Click open & Follow on screen instructions

 ***DONE!***
   
2. Install from direct .exe installer (not available from Python 3.15)
  - Step 1. Head to [python's website](https://python.org/)
  - Step 2. Go to download python section, and click latest or [this recommended version](https://www.python.org/downloads/release/python-31314/)
  - Step 3. Download `Windows installer` to get .exe installer
  - Step 4. Double-click download .exe file and follow on screen instructions (plus checkmark at Add Python to PATH)

  ***DONE!***

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

- Go to [here](https://apps.microsoft.com/detail/xp9khm4bk9fz7q) and install the VS Code.

###### <small>made by @Ericwasepic127</small> 
