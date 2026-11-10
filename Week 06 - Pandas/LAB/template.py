"""
RECORD CHECK  -  my version
===========================

Name  : Jayesh Jaiswal
Lane  :  Cyber
Date  : 4 - 11- 26

"""

import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv(r"Week 06 - Pandas\LAB\login_attempts.csv") # replace with pd.read_csv("your_file.csv")

df["percent"] = (df["failed_logins"]/df["total_attempts"])*100
df["status"] = df["percent"].apply(lambda p: "OVER LIMIT" if p>= 100 else "WARNING" if p>= 90 else "OK")



counts = df.groupby("status").size()
print("\nCount per status: ")
print(counts)

df.to_csv(r"Week 06 - Pandas\LAB\Login_attempts_processed.csv", index=False)

counts.plot(kind="bar", title="Rows per status")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(r"Week 06 - Pandas\LAB\status_label.png")

# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case
