"""
RECORD CHECK  -  my version
===========================

Name  :  Jayesh Jaiswal
Lane  :  Cyber
Date  :  5/11/2026

Run it:   python template.py

"""

from pathlib import Path

FAILED_ATTEMPT_LIMIT = 5



def parse_line(raw_line):
    """Clean one messy 'KEY=value,KEY=value,...' line into a dict."""
    record = {}

    for piece in raw_line.strip().split(","):
        key, value = piece.split("=")
        record[key.strip().lower()] = value.strip()

    record["result"] = record["result"].upper()
    record["attempts"] = int(record["attempts"])
    return record


def status_of(record):
    """Return FLAGGED if a source has too many failed attempts, otherwise OK."""
    if record["result"] == "FAILED" and record["attempts"] >= FAILED_ATTEMPT_LIMIT:
        return "FLAGGED"
    return "OK"

records_file = Path(__file__).parent / "records.txt"

raw_records = []
with open(records_file) as f:
    for line in f:
        if line.strip():              # skip blank lines
            raw_records.append(line)


total_count = 0
flagged_count = 0
skipped_count = 0

for raw_record in raw_records:
    try:
        record = parse_line(raw_record)
    except ValueError as error:
        print(f"Could not parse: {raw_record.strip()}  ({error})")
        skipped_count += 1
        continue

    status = status_of(record)
    print(f"{record}  ->  {status}")

    total_count += 1
    if status == "FLAGGED":
        flagged_count += 1

print()
print(f"Summary: {total_count} records checked, {flagged_count} flagged, "
      f"{skipped_count} could not be parsed.")

