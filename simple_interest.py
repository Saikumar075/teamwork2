
def interest():
    principle = int(input("enter the value: "))
    Time = int(input("enter time period: "))
    rate= int(input("enter the rate: "))

    result = (principle*Time*rate)/100
    print((result))