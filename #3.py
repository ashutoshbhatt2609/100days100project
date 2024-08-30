#Love calculator
a1=input("Enter your name 1:-\n").lower()
a2=input("Enter your name 2:-\n").lower()
s=str(a1)+str(a2)
t,r,u,e,l,o,v,e=s.count("t"),s.count("r"),s.count("u"),s.count("e"),s.count("l"),s.count("o"),s.count("v"),s.count("e")
perc=(t+r+u+e)*10+(l+o+v+e)
print("Your love percentage is:-",perc)

