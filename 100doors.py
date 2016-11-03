doors=["C"]*100
opened_doors=[]

for order, door in enumerate(doors):
    for number in range(0,99, order+1):
        if doors[number]=="C":
            doors[number]="O"
        else:
            doors[number]="C"
    if door is "O":
        opened_doors.append(order)
print("The following doors are open:", (opened_doors))
