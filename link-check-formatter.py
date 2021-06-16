import re
import sys
import csv
import pdb

# print("waiting for debugger")
# mypdb = pdb.Pdb(stdin=open("/tmp/pdb_stdin", "r"), stdout=open("/tmp/pdb_stdout", "w"))

fields = ["source", "lines", "code", "link", "notes"]

output = csv.DictWriter(sys.stdout, fields)
output.writeheader()
source, lines, code, link, notes = None, None, None, None, []
in_todo = False

for line in sys.stdin:
    s = line.strip()

    if not s and not in_todo:
        continue

    if not source:
        if s.startswith("Processing"):
            source = s.split("\t")[1]
            continue

    if s.startswith("List of broken"):
        continue

    if s.startswith("----"):
        source = None
        continue

    if match := re.match(r"^Lines?: (.*)", s):
        lines = match.group(1)
    elif match := re.match(r"^Code: (.*)", s):
        code = match.group(1)
    elif match := re.match(r"^To do: (.*)", s):
        notes.append(match.group(1))
        in_todo = True
    elif in_todo:
        if match := re.match(r"^\s*(.+)$", s):
            notes.append(match.group(1))
        else:
            output.writerow({"source": source, "lines": lines, "code": code, "link": link, "notes": " ".join(notes)})
            lines = None
            code = None
            link = None
            notes = []
            in_todo = False
    else:
        link = s
        continue
