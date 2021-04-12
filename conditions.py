x = 2
print(x == 2)
print(x == 3)
print(x < 3)
###

name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is %s, and you are also %d years old." % (name,age))

if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

statement = False
another_statement = True
if statement is True:
    pass
elif another_statement is True:
    pass
else:
    pass

x = [1,2,3]
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two")

y = [1,2,3]
print(x == y)
print(x is y) # is operator matches instances not values

print(not False)
print((not False) == (False))