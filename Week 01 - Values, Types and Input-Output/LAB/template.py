"""
RECORD CHECK  -  my version
===========================

Name  :Jayesh Jaiswal
Lane  :Cyber
Date  :23/09/2026
Run it:   python template.py

"""






label = input("source IP: ")      # : replace with an input() call
Failed_attempts = float(input("number of failed attempts: "))     # : replace with an input() call, converted
total_attempts = float(input("number of total attempts: "))    # : replace with an input() call, converted

difference = total_attempts - Failed_attempts   # 
percent = (Failed_attempts / total_attempts) * 100   #

print()
print("=" * 45)
print(f"  RECORD CHECK  -  {label}")
print("=" * 45)
print(f"  {'Failed attempts':<26} : {Failed_attempts:>10.2f}")
print(f"  {'Total attempts':<26} : {total_attempts:>10.2f}")
print(f"  {'Difference':<26} : {difference:>10.2f}")
print(f"  {'Percent of failed attempts'} : {percent:>10.2f}%")
print("=" * 45)
