BaseMirror Setup Guide
System Requirements

    Python: 3.8+
    Memory: 16GB+ RAM recommended
    Storage: 10GB+ free space

1. Install System Dependencies
Windows

# Java (for Ghidra)
choco install jdk11 -y

# ADB (Android Debug Bridge)
choco install adb -y

# Ghidra (Manual install)
# Download from https://ghidra-sre.org/

Linux (Ubuntu)

sudo apt update
sudo apt install -y openjdk-11-jdk adb file

2. Python Environment

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install Python packages
pip install -r requirements.txt

3. Ghidra Setup

    Download Ghidra from official site
    Add to PATH:

    export PATH=$PATH:/path/to/ghidra_9.2.2_PUBLIC

    Test installation:

    analyzeHeadless -version

4. Android Device Configuration

adb devices                 # Verify connection
adb root                    # Get root access
adb shell pgrep rild        # Verify RIL daemon running

Troubleshooting

Q: Python-magic errors on Windows
A: Install magic-bin:

pip install python-magic-bin==0.4.14

Q: Ghidra headless mode fails
A: Ensure Java 11 is default:

sudo update-alternatives --config java

Q: ADB device not found
A: Enable USB debugging in Developer Options
