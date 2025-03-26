**RILRecon - Baseband Command Analyzer**

RILRecon is a powerful tool that automates the reverse engineering of baseband commands from Android RIL binaries. It helps security researchers uncover hidden commands and potential vulnerabilities in mobile networks.

## Features
- Automatically detects and classifies RIL commands.
- Uses bidirectional taint analysis for improved accuracy.
- Tests and verifies extracted commands on rooted devices.
- Generates detailed reports on discovered commands and security risks.

## Installation
```bash
git clone https://github.com/bhavik-125/RILRecon.git
cd RILRecon
pip install -r requirements.txt
```

## Usage
```bash
# Analyze a RIL binary
python src/rilrecon.py samples/example_ril_binary.so --ghidra "C:/ghidra" --java "C:/java/bin/java.exe"
```

## System Requirements
- Python 3.8+
- Ghidra 9.2.2 or later
- Java 11 (OpenJDK recommended)
- A rooted Android device (for testing extracted commands)

## Disclaimer
This tool is intended for research and educational purposes only. Please ensure you have proper authorization before analyzing proprietary binaries.

