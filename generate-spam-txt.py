import sys
a = input("Enter your text here : ")
b = eval(input("How many text do you want : "))
sys.stdout = open("spam.txt", "w")
for i in range (b):
    print(a)

sys.stdout.close()
