row1=["😊","😊","😊"]
row2=["😊","😊","😊"]
row3=["😊","😊","😊"]
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
a=input("Enter the index you want to choose(Horzontal and vertical index):-\n")
a=a.split(" ")
vertical,horizontal=a[1],a[0]
map[int(vertical)-1][int(horizontal)-1]="X"
print(f"{row1}\n{row2}\n{row3}")