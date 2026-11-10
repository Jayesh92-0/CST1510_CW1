#Task 5 - total watch time
s1_min = 45
s1_sec = 35
s2_5_min = 35
s2_5_sec = 15

s1_total_seconds = ((s1_min * 60)+s1_sec) * 10
s2_total_seconds = ((s2_5_min * 60)+s2_5_sec) * 40
total_seconds = s1_total_seconds + s2_total_seconds

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60
print(f"Total time: {hours}h {minutes}m {seconds}s")

# Task 5 - total watch time
s1_min = 45
s1_sec = 35
s2_5_min = 35
s2_5_sec = 15

s1_total_seconds = ((s1_min * 60) + s1_sec) * 10
s2_total_seconds = ((s2_5_min * 60) + s2_5_sec) * 40
total_seconds = s1_total_seconds + s2_total_seconds

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"Total time: {hours}h {minutes}m {seconds}s")


