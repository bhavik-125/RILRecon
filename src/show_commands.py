import json
import argparse
from tabulate import tabulate

def show_commands(result_file):
    with open(result_file) as f:
        data = json.load(f)
    
    table = []
    for cmd_type in data['commands']:
        for val, cmd in data['commands'][cmd_type].items():
            table.append({
                'Type': cmd_type.split('_')[0],
                'Value': val,
                'Name': cmd.get('name', 'UNKNOWN')
            })

    print(tabulate(table, headers="keys", tablefmt="grid"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("result_file")
    args = parser.parse_args()
    show_commands(args.result_file)