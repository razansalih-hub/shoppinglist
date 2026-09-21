#Updated version of Shopping list using Loops

user = input("What do you want to be called? ").strip().title()
print(" ") 
print(f"Okay dear {user}, let's start your shopping list,")
print(" ")
# A shopping list
My_shoppinglist = []
item1 = input("What do you want to buy? ")
qt1 = input("How much? ")
name1 = (item1, qt1)
My_shoppinglist.append(name1)
print(" ")
keep_going = True

while keep_going :
    
    addm = input("Do you want to add more items? (Yes, No) ").strip().lower()
    if addm == "yes" :
        item2 = input("What more? ")
        qt2 = input("How much? ")
        name2 = (item2, qt2)
        My_shoppinglist.append(name2)
        print(" ")
    elif addm == "no" :
        keep_going = False

print(" ")
print("-" *50)
print(f"Okay, {user}, this is your shopping list".center(50, "-"))
a = 0
while a < len(My_shoppinglist):
    print(f"{a+1}. {My_shoppinglist[a][0]} — {My_shoppinglist[a][1]}")
    a += 1
print("-" *50)
print("Happy shopping!".center(50, "-"))
    
