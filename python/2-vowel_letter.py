#Write a Python program to test whether a passed letter is a vowel or not.
vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

letter = input("enter the letter:\n")

if letter in vowel:

    print ("It is a vowel")
else:
    print ("it is not vowel")