#!/usr/bin/python3
'''7. Load, add, save'''


import os
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if os.path.exists("add_item.json"):
    liste = load_from_json_file("add_item.json")
    liste.extend(sys.argv[1:])
else:
    liste = sys.argv[1:]
save_to_json_file(liste, "add_item.json")
