import argparse
import os
import subprocess
import sys

import pyperclip

parser = argparse.ArgumentParser()
parser.add_argument("command", help="the command to set as old_command")
args = parser.parse_args()


old_command = args.command
harness_folder = os.path.expanduser(".")

result = subprocess.run(old_command, shell=True, capture_output=True, text=True)
error_output = result.stderr
missing_include = ""

for line in error_output.splitlines():
    if "#include" in line:
        missing_include = line.split("#include")[1].strip().replace('"', '')
        break

if missing_include == "":
    print("No missing #include found")
    sys.exit(0)
    
print("Missing #include:", missing_include)

contiki_folder = os.path.expanduser("~/contiki")
missing_files = []

# i = 0
for root, dirs, files in os.walk(contiki_folder):
    for file in files:
        # print(missing_include, file)
        # i += 1
        # if i == 10:
        #     break
        if missing_include in file:
            missing_files.append(os.path.join(root, file))

if len(missing_files) > 0:
    print("Found missing file in these place, Select one to add to dependency:")
    for i, file in enumerate(missing_files):
        print(f"  {i}) {file.split(contiki_folder)[1]}")

    selected_folder = int(input("Select folder: "))
    selected_folder = os.path.dirname(missing_files[selected_folder]).replace(contiki_folder, "~/contiki")

    old_command_slices = old_command.split("--trace")
    new_command = f"{old_command_slices[0]} -I {selected_folder} --trace {old_command_slices[1]}"
    print("New command (also copied to clipboard):")
    pyperclip.copy(new_command)
    print(new_command)
else:
    print("No file found")
