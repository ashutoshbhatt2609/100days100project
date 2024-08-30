print("Welcome to the tip calculator!")
amnt=float(input("What was the toatl bill? \n$"))
ppl=int(input("How many people to split the bill?\n"))
tip=int(input("How much percentage of tip you want to give? 10,12 or 15?\n"))
total=amnt +amnt*(tip/100)
each_pay=total/ppl
each_pay_format="{:.2f}".format(each_pay)
print("Each hss to pay $",each_pay_format)