"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  : Cyber     (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
def check_records(value, limit):
    """calculates difference, percentage and status"""
    difference = limit - value
    percent = (value/limit) * 100
    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
    return difference, percent, status

def print_report(label, value, limit, difference, percent, status):
    """Print the formatted record report to the console."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)

    print(f"{'Failed Logins':<17} :{value:>10.2f}")
    print(f"{'Total Logins':<17} :{limit:>10.2f}")
    print(f"{'Succesful Logins':<17} :{difference:>10.2f}")
    print(f"{'Failure Percent':<17} :{percent:>10.2f}%")
    print(f"{'Status':<17} : {status:>9}")
    print("=" * 34)

def load_records(path):
    """Load comma-separated values from a file into a list of dictionaries."""
    records_list = []
    try:
        with open(path, "r") as f:
            for line in f:
                if not line.strip():
                    continue
                parts = line.strip().split(",")
                records_list.append({
                    "label": parts[0],
                    "value": float(parts[1]),
                    "limit": float(parts[2])
                })
        return records_list
    except FileNotFoundError:
        print(f"Error: The file '{path}' could not be found.")
        return []


records = load_records("lab/records_sample.txt")
over_limit_counting = 0

with open("results.txt", "w") as out_file:
    for rec in records:
        difference, percent, status = check_records(rec["value"], rec["limit"])

        if status == "OVER LIMIT":
            over_limit_counting += 1
            
        print_report(rec["label"], rec["value"], rec["limit"], difference, percent, status)

        out_file.write(f"{rec['label']},{status}\n")

print(f"Failed Logins over limit : {over_limit_counting}")
