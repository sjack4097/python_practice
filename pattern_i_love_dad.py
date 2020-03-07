for row2 in range(7):
    for col2 in range(5):
        if col2==2 or((row2==0 or row2==6 )and (col2!=2)):
            print("i",end="")
        else:
            print(end=" ")
    print()
print()
print()
print()


for row4 in range(6):
    for col4 in range(7):
        if(row4==0 and col4%3!=0)or (row4==1 and col4%3==0)or (row4-col4==2)or (row4+col4==8):
            print("0",end="")
        else:
            print(end=" ")
    print()

print()
print()
print()


for row1 in range(7):
    for col1 in range(5):
        if(col1==0) or (col1==4 and (row1!=0 and row1!=6)) or (row1==0 or row1==6 )and (col1>0 and col1 <4):
            print("@",end="")
        else:
            print(end=" ")
    print()
print()
print()
print()


for row in range(7):
    for col in range(5):
        if((col==0 or col==4 )and row!=0) or((row==0 or row==3) and (col>0 and col<4)):
            print("@",end="")
        else:
            print(end=" ")
    print()
print()
print()
print()


for row3 in range(7):
    for col3 in range(5):
        if(col3==0) or (col3==4 and (row3!=0 and row3!=6)) or (row3==0 or row3==6 )and (col3>0 and col3<4):
            print("@",end="")
        else:
            print(end=" ")
    print()
