import os
import sys
import json
import subprocess

issue = sys.argv[1]
#issue = "/repos/larsbuntemeyer/actions-sandbox/issues/54"
command = ["gh","api","--jq",".labels.[].name",issue]
result = subprocess.run(command, stdout=subprocess.PIPE)
labels = result.stdout.decode('utf-8').splitlines()

for l in labels:
    table = l.split("register")[1].strip() if "register" in l else None
    if table:
        break
print(f"{table}")
