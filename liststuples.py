# this is my second project with python

user = (input("What do you want to be called? ")) 
print("""

""") 
print(f"Okay dear,", user.title(), "let's start your shopping list,")
# A shopping list

My_shoppinglist = []

item1 = (input("What do you need to buy? "))
itq1 = input("How much you want to buy? ")

name1 = (item1, itq1)

item2 = input("What else? ")
itq2 = input("How much you want to buy? ")

name2 = (item2, itq2)

item3 = input("Is there anything else? ")
itq3 = input("How much do you want to buy? ")

name3 = (item3, itq3)

My_shoppinglist.append(name1)
My_shoppinglist.append(name2)
My_shoppinglist.append(name3)


#let's make it a list that is good-looking
print("""


""")
print("*" *50)
print("Here is what you need to buy today: ")
print (f"""
1= {name1}

2= {name2}

3= {name3}
""")
print("*" *50)
# print("The shopping list is:", My_shoppinglist)