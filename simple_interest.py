print("welcome to the investment calculator app")

Investment = int(input("Enter the amount you are investing: \n"))
Time = int(input("Enter the time: \n"))
Rate = int(input("Enter the rate: \n"))

numerator = Investment * Time * Rate
simple_interest = numerator / 100
Total = simple_interest + Investment

print(f"your investment {Investment} of {Time} years at a rate of {Rate}% is {Total}")
input()