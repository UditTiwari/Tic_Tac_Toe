row1 = ['','','']
row2 = ['','','']
row3 = ['','','']

def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)
    

row2[1] = 'X'
print(display(row1,row2,row3))


position_index = int(input("Choose an index postion : "))

print(row2[position_index])