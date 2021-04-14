class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

#myobjectx.variable

myobjecty = MyClass()

myobjecty.variable = "yackity"

print(myobjectx.variable)
print(myobjecty.variable)

myobjectx.function()