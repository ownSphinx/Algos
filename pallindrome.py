word = input("Enter your word: ")

temp = word
new = word[::-1]
if (temp == new):
    print("It is a pallindrome")
else:
    print("Not a pallindrome")