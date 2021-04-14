# phonebook = {}
# phonebook["John"] = 938477566
# phonebook["Jack"] = 938477364
# phonebook["Jill"] = 947662781
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
#print(phonebook)

for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name,number))

# pop return the deleted value and del does not.

#del phonebook["John"]
phonebook.pop("John")
print(phonebook)