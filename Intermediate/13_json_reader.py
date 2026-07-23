#!/usr/bin/python3
# Made By @Ericwasepic127

import json, os

def read_json(file):
    if not os.path.isfile(file):
        print("ERROR: Given location is not file or does not exists")
        return
    try:
        with open(file, encoding='utf-8') as obj:
            return json.load(obj)
    except json.JSONDecodeError:
        print("ERROR: Invaild JSON format")
    except Exception as e:
        print("ERROR:",e)

print("Welcome to JSON Reader")
print("Type 'exit' to exit")
print("Current directory:", os.getcwd())
print("In current directory:")
print(("- " + "\n- ".join(os.listdir())) if os.listdir() else "- No files found!")

loc = ''
while loc != "exit":
    if loc:
        dic = read_json(loc)
        if not dic:
            loc = ""
            continue
        for n, v in dic.items():
            print("Name:", repr(n), "|", "Value:", repr(v))

    loc = input("\nEnter path to your JSON to read:  ")
    
