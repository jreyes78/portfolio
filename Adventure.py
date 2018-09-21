def adventure_1():
    print("Level 1: You are on a walk and approach a bridge. A troll says" 
    "You must add 2 + 2 to pass this bridge"
    "You get four tries. What is your answer?")
    for i in range(0, 3):
        choice = input()
        tires = i
        if tires == 3:
            print("You ran out of choices! Hahahaha")
        else:
            if choice == "4":
                print("Yes, you are correct. You may pass!")
                break
            else:
                print("Sorry. Try again")

print(adventure_1())

def adventure_2():
    print("Level 2: You keep walking and come to a river. The boatman says" 
    "You must multiply 4 * 4 to cross!"
    "You get four tries. What is your answer?")
    for i in range(0, 3):
        choice = input()
        tires = i
        if tires == 3:
            print("You ran out of choices! Hahahaha")
        else:
            if choice == "16":
                print("Yes, you are correct. You may pass!")
                break
            else:
                print("Sorry. Try again")


print(adventure_2())

def adventure_3():
    print("Level 3: Finally, you almost reach your destination, and a mugger on the road says" 
    "You must divide 6 / 2 to be set free!"
    "You get four tries. What is your answer?")
    for i in range(0, 3):
        choice = input()
        tires = i
        if tires == 3:
            print("You ran out of choices! Hahahaha")
        else:
            if choice == "3":
                print("Yes, you are correct. You may pass!")
                break
            else:
                print("Sorry. Try again")


print(adventure_3())