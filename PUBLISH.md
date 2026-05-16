# 🚀 Publishing Mimic to PyPI

![PyPI - Status](https://img.shields.io/badge/PyPI-Publishing_Guide-blue?style=flat-square&logo=pypi)
![Python Versions](https://img.shields.io/badge/Python->=3.6-blue?style=flat-square&logo=python)

Welcome to the official publication guide for the **Mimic Hardware Bridge** (`mimic-fw`). This document outlines the step-by-step process for maintainers to build and publish the package, as well as the quick-start instructions for end-users.

---

## 🛠️ Part 1: For Maintainers
*A guide to building and uploading the package to the Python Package Index.*

### 1. Prerequisites
Before you begin, ensure you have the required build tools installed. We use the modern Python packaging pipeline (`build` and `twine`).

```bash
pip install --upgrade build twine
```

> **Note:** You will also need an account on [PyPI](https://pypi.org/) and an API token configured.

### 2. Building the Distribution
Navigate to the `Mimic-Core` directory (where `setup.py` resides) and invoke the build module. This step compiles your source code into a source archive (`.tar.gz`) and a built distribution (`.whl`).

```bash
cd Mimic-Core
python -m build
```

> 💡 **Tip:** Always check the `dist/` folder after building to ensure no stale artifacts from old builds are present. You can clear them via `rm -rf dist/*` before building if needed.

### 3. Uploading to PyPI
With the package built, use `twine` to securely push it to the world.

```bash
twine upload dist/*
```

<details>
<summary>🧪 <strong>Want to test before publishing?</strong> <em>(Click to expand)</em></summary>

If you want to verify the upload without using the official PyPI, upload it to TestPyPI first:
```bash
twine upload --repository testpypi dist/*
```
</details>

---

## 🎮 Part 2: For End-Users
*How to fetch from PyPI and interact with Mimic out of the box.*

### Installation
Gone are the days of manual Git cloning! Users can now install the entire suite universally using pip:

```bash
pip install mimic-fw
```

### 💻 Command Line Interface (CLI)
The package automatically exposes the `mimic` command globally. It ships with a beautiful Gruvbox-themed interactive terminal.

**Launch the Auto-Detecting Shell:**
```bash
mimic
```

**Specify a Hardware Port:**
```bash
# Windows
mimic --port COM3

# Linux / macOS
mimic --port /dev/ttyUSB0
```

### 🐍 Python API Usage
Building custom scripts? The `mimic-fw` package is cleanly structured for developer imports.

```python
from mimic import MimicBridge

def main():
    # Initialize the bridge (leave port=None to auto-discover)
    bridge = MimicBridge(port=None) 

    if bridge.connect():
        print("🟢 Connected successfully to Mimic board!")
        
        # Direct API interaction
        board_version = bridge.execute("VERSION")
        print(f"Board Response: {board_version}")
        
        bridge.disconnect()
    else:
        print("🔴 Could not locate Mimic hardware.")

if __name__ == "__main__":
    main()
```

---
*Maintained by Aegion Dynamics .*