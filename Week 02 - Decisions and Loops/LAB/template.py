"""
RECORD CHECK  -  my version
===========================

Name  :Jayesh Jaiswal
Lane  :Cyber
Date  :30 - 09 - 2026
"""
over_limit_counting = 0
while True:
    label = input("Enter I.P. adress :")   
    if label == "quit":
            print("loop quit successful")
            break   
    value = float(input("Enter the Value: "))    
    limit = float(input("Enter the limit: ")) 
    while limit == 0:
        print("Error: Limit cannot be zero.")
        limit = float(input("Enter the limit: "))

    difference = limit - value   
    percent = (value/limit) * 100  

    status = " "
    if(percent >=100):
        status = "OVER LIMIT"
    elif(percent >= 90):
        status = "WARNING"
    else:
        status = "OK" 
    if(status == "OVER LIMIT"):
        over_limit_counting += 1

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)

    print(f"{'Used':<10} :{value:>10.2f}")
    print(f"{'Total':<10} :{limit:>10.2f}")
    print(f"{'Free':<10} :{difference:>10.2f}")
    print(f"{'Percent':<10} :{percent:>10.2f}%")
    print(f"{'Status':<10} : {status:>9}")
    print("=" * 34)


print(f"Over Limit : {over_limit_counting}")
