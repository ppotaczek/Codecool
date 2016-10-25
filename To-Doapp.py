stuff=[]
marks=[]

with open("zbior.txt", "r") as file1:                           #Loading content files
    stuff=file1.read().splitlines()
with open("zbior2.txt", "r") as file2:
    marks=file2.read().splitlines()

while True:
    order=input ("Please specify a command [list, add, mark, archive, exit]: ") #Menu

    if order==("add"):                          #Adding new element in list of stuff
        item=input("Add an item: ")
        tem="[ ]"
        stuff.append(item)
        marks.append(tem)
        print("Item added!")

    elif order==("list"):                           #Showing element in list of stuff
        if len(stuff)<1:
            print ("The list is empty!")
        else:
            for index, value in enumerate(stuff, 1):
                print(index, marks[index-1] , value)

    elif order==("exit"):                           #Saving and exit
        file1=open("zbior.txt", "w")
        for el in stuff:
            file1.write(str(el)+"\n")
        file1.close()
        file2=open("zbior2.txt", "w")
        for el in marks:
            file2.write(str(el)+"\n")
        file2.close()
        break

    elif order==("archive"):                            #Deleting marked stuff
        while "[X]" in marks:
            position=marks.index("[X]")
            del stuff[position]
            del marks[position]

    elif order==("mark"):                           #Marking stuff
        if len(stuff)<1:
            print ("The list is empty!")
        else:
            try:
                to_kick=int(input("Which one you want to mark as completed: "))
                del marks[to_kick-1]
                marks.insert(to_kick-1, "[X]")
                print (stuff[to_kick-1], "is completed")
            except:
                print ("Try again")

    else:
        print ("Please again")
