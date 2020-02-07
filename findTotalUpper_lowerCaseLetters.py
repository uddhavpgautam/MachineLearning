#str = "Help me Boy!"

#def totalLowerCase(str):return sum(1 for i in str if i.islower())
#def totalUpperCase(str):return sum(1 for i in str if i.isupper())

#print(f"Total lower-case letters: {totalLowerCase(str)}")
#for python 3.8 version
#print(f"Total upper-case letters: {totalUpperCase(str)}")
#for python 3.8 version

#print("Total lower-case letters: {}".format(totalLowerCase(str)))
#print("Total upper-case letters: {}".format(totalUpperCase(str)))

print((lambda str: "Total upper-case letters: {} \nTotal lower-case letters: {}"\
    .format( sum(1 for x in str if x.isupper()), sum(1 for x in str if x.islower()))) ("Help me Boy!"))
