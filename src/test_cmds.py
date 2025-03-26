import os
import subprocess
import argparse
import json
import time

class CommandTester:
    def __init__(self, adb="adb.exe"):
        self.adb = adb
        self.device = None

    def setup(self):
        try:
            subprocess.run([self.adb, "devices"], check=True, shell=True)
            pid = subprocess.run(
                [self.adb, "shell", "su -c 'pgrep rild'"], 
                capture_output=True, 
                text=True,
                shell=True
            ).stdout.strip()
            
            if not pid:
                raise RuntimeError("rild not running")
            
            self.device = pid
            return True
        except Exception as e:
            print(f"Setup error: {e}")
            return False

    def test_command(self, cmd):
        try:
            print(f"Testing {cmd['name']}")
            subprocess.run(
                [self.adb, "shell", f"su -c 'echo TEST > /dev/umts_ipc0'"],
                shell=True,
                check=True
            )
            time.sleep(1)
            return True
        except Exception as e:
            print(f"Test failed: {e}")
            return False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("result_file")
    parser.add_argument("--adb", default="adb.exe")
    args = parser.parse_args()

    with open(args.result_file) as f:
        data = json.load(f)

    tester = CommandTester(args.adb)
    if not tester.setup():
        return

    for cmd in data['commands']['write_commands'].values():
        tester.test_command(cmd)

if __name__ == "__main__":
    main()