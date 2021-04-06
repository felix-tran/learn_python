astring = "Hello world!"
print("single quotes are ' '")

print(len(astring))

print(astring.index("o"))
# That prints out 4, because the location of the first occurrence of the letter "o" is 4 characters away from the first character.
# Notice how there are actually two o's in the phrase - this method only recognizes the first.

print(astring.count("lo"))

print(astring[3:7]) #Prints out hel"lo w"orld

print(astring[:7:2]) #The general form is [start:stop:step]

print(astring[::-1])

print(astring.upper())

print(astring.lower())

print(astring.startswith("Hello"))

print(astring.endswith("asdfasdfasdf"))

afewwords = astring.split(" ")

print(afewwords)