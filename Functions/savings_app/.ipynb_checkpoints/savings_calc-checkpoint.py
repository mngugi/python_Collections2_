

rate = float(input("Enter Interest Rate: "))
capital =  float(input("Enter Capital: "))
years = int(input("Enter number of years:"))

def final():
    total_sum = capital* (1.0+rate)**years
    return total_sum
