# LEGO League Team 69255 - PyBricks Python Project

Welcome to Team 69255's FIRST LEGO League competition programming project! This repository contains all the Python code for controlling our LEGO robots using PyBricks.

## Project Setup

### Prerequisites
- Python 3.12+ (or older as per PyBricks requirements)
- Visual Studio Code (VS Code)
- Git

### Initial Setup Steps

#### 1. Clone the Repository
```bash
git clone https://github.com/christopherl-git/lego-league.git
cd lego-league
```

#### 2. Create and Activate Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## VS Code Setup for PyBricks Development

### 1. Install VS Code Extensions

Open VS Code and install the following extensions:

1. **Python** - Microsoft (ms-python.python)
   - Provides Python language support, linting, and debugging

2. **Pylance** - Microsoft (ms-python.vscode-pylance)
   - Advanced Python language server for better IntelliSense

3. **PyBricks Visual Studio Code Extension**
   - Search for "pybricks" in VS Code extensions
   - Look for the official PyBricks extension

### 2. Configure Python Interpreter

1. Open the Command Palette (Ctrl+Shift+P)
2. Search for "Python: Select Interpreter"
3. Choose the interpreter from the `venv` folder: `./venv/Scripts/python.exe` (Windows) or `./venv/bin/python` (macOS/Linux)

### 3. VS Code Workspace Settings

Create or update `.vscode/settings.json` in the project root:

```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/venv/Scripts/python",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.formatting.provider": "black",
    "[python]": {
        "editor.formatOnSave": true,
        "editor.defaultFormatter": "ms-python.python"
    }
}
```

### 4. Connect Your LEGO Hub

1. Connect your LEGO Hub via USB or Bluetooth
2. Open the PyBricks extension in VS Code
3. Follow the pairing instructions to connect to your hub
4. Select your hub from the available devices

## Project Structure

```
lego-league/
├── venv/                    # Virtual environment (do not commit)
├── requirements.txt         # Python dependencies
├── .gitignore              # Git ignore rules
├── README.md               # This file
└── helloWorld.py           # First test program
```

## Running Your First Program

1. Activate the virtual environment (see steps above)
2. Connect your LEGO Hub
3. Open `helloWorld.py` in VS Code
4. Right-click and select "Run with PyBricks" or use the PyBricks extension panel
5. Watch your robot execute the program!

## Creating New Programs

1. Create a new `.py` file in the project root or in a subdirectory
2. Import PyBricks modules:
   ```python
   from pybricks.hubs import EV3Brick
   from pybricks.ev3devices import Motor, ColorSensor, DistanceSensor
   from pybricks.parameters import Port, Stop, Direction
   from pybricks.robotics import DriveBase
   from pybricks.tools import wait, StopWatch
   ```
3. Write your robot control code
4. Deploy to your hub using the PyBricks extension

## Documentation

- **PyBricks Documentation**: https://pybricks.com/
- **PyBricks API Reference**: https://docs.pybricks.com/
- **FIRST LEGO League Resources**: https://www.firstinspires.org/

## Team Members

Team 69255

## License

This project is created for FIRST LEGO League competition purposes.
