class Load:
    def load_stuff():
        with open("zbior.txt", "r") as file1:                           # Loading content files
            return file1.read().splitlines()

    def load_marks():
        with open("zbior2.txt", "r") as file2:
            return file2.read().splitlines()


class Menu:
    def add(works, prefixes):
        item = input("Add an item: ")
        pre = "[ ]"
        works.append(item)
        prefixes.append(pre)
        print("Item added!")

    def list(works, prefixes):
        if len(works) < 1:
            print ("The list is empty!")
        else:
            for index, value in enumerate(works, 1):
                print(index, prefixes[index-1], value)

    def exit(works, prefixes):
        file1 = open("zbior.txt", "w")
        for el in works:
            file1.write(str(el)+"\n")
        file1.close()
        file2 = open("zbior2.txt", "w")
        for el in prefixes:
            file2.write(str(el)+"\n")
        file2.close()

    def archive(works, prefixes):
        while "[X]" in prefixes:
            position = prefixes.index("[X]")
            del works[position]
            del prefixes[position]

    def mark(works, prefixes):
        if len(works) < 1:
            print ("The list is empty!")
        else:
            try:
                to_delete = int(input("Which one you want to mark as completed: "))
                del prefixes[to_delete-1]
                prefixes.insert(to_delete-1, "[X]")
                print (works[to_delete-1], "is completed")
            except:
                print ("Try again")


class Main:
    def main_func():
        stuff = Load.load_stuff()
        marks = Load.load_marks()

        while True:
            order = input("Please specify a command [list, add, mark, archive, exit]: ") #Menu
            if order == ("add"):                          # Adding new element in list of stuff
                Menu.add(stuff, marks)

            elif order == ("list"):                           # Showing element in list of stuff
                Menu.list(stuff, marks)

            elif order == ("exit"):                           # Saving and exit
                Menu.exit(stuff, marks)
                break

            elif order == ("archive"):                            # Deleting marked stuff
                Menu.archive(stuff, marks)

            elif order == ("mark"):                           # Marking stuff
                Menu.mark(stuff, marks)

            else:
                print ("Please again")

Main.main_func()
