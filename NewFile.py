from random import randint

fullsentence = input( "Input sentence that you wanted mocked \n")
newsenctence = []
newsenctence = list(fullsentence)
mockedsentence = []
for letter in newsenctence:
    i = randint(0, 1)
    if i == 0:
        newletter = letter.upper()
        mockedsentence.append(newletter)
        continue
    if i == 1:
        newletter = letter.lower()
        mockedsentence.append(newletter)
        continue
newstring = ""
for letter in mockedsentence:
    newstring = newstring + letter
print(newstring)
