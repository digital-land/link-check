import re
import sys
import csv
import pdb

# print("waiting for debugger")
# mypdb = pdb.Pdb(stdin=open("/tmp/pdb_stdin", "r"), stdout=open("/tmp/pdb_stdout", "w"))

fields = ["source", "lines", "code", "link"]

output = csv.DictWriter(sys.stdout, fields)
output.writeheader()
source, lines, code, link = None, None, None, None

for line in sys.stdin:
    s = line.strip()

    if not s:
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
    elif re.match(r"^To do: ", s):
        output.writerow({"source": source, "lines": lines, "code": code, "link": link})
        lines = None
        code = None
        link = None
    else:
        link = s
        continue

    # sys.exit()
