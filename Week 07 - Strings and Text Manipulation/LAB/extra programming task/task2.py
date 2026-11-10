def is_valid_id(student_id):
    if not student_id.startswith("M00"):
        return False
    if len(student_id) != 9:
        return False
    if not student_id[3:].isdigit():
        return False
    return True

student_ids = ["M00123456", "M0012345", "X00123456", "M00ABCDEF", "M00987654"]

for sid in student_ids:
    print(f"{sid}: {is_valid_id(sid)}")