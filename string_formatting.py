name = "John"
print("Hello, %s!" % name)

name = "John"
age = 23
print("%s is %s years old." % (name,age))

def what_class(what):
    what = str(type(what).__name__)
    return (what)

print("This class is a " + what_class(age))

mylist = [1,2,3]
print("A list: %s" % mylist)

numbers = 12.34

print("I wish for a %.0f" % numbers)