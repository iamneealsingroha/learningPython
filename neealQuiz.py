print("This is a quiz about Neeal.")
print("You will get a score at the end based on your answers.")
print("Please answer the following questions:")
a=0
print("1. What is Neeal's current email address?")
print("a) iamneealsingroha@gmail.com")
print("b) neealsingroha@gmail.com")
print("c) neeal.singroha@gmail.com")
print("d)maishaneeal@gmail.com")
z=input("Enter your answer here, only the letter: ")
if z=="a" or z=="A":
    print("Correct!")
    a=a+1
else:
    print("Incorrect. The correct answer is a)iamneealsingroha@gmail.com")
print("2. What is Neeal's favorite color?")
print("a) Yellow")
print("b) Red")
print("c) Blue")
print("d) Green")
y=input("Enter your answer here, only the letter: ")
if y=="c" or y=="C":
    print("Correct!")
    a=a+1
else:
    print("Incorrect. The correct answer is c)Blue")
print("3. What is Neeal's favorite hobby?")
print("a) Reading")
print("b) Playing video games")
print("c) Coding")
print("d) Watching TV")
x=input("Enter your answer here, only the letter: ")
if x=="a" or x=="A":
    print("Correct!")
    a=a+1
else:
    print("Incorrect. The correct answer is a)Reading")
print("4. What is Neeal's favorite food?")
print("a) Pizza")
print("b) Dal Makani")
print("c) Burgers")
print("d) Samosa")
print("e) Garlic Bread")
w=input("Enter your answer here, only the letter: ")
if w=="d" or w=="D":
    print("Correct!")
    a=a+1
else:
    print("Incorrect. The correct answer is d)Samosa")
print("5. What is Neeal's favorite sport?")
print("a) Football")
print("b) Basketball")
print("c) Cricket")
print("d) Tennis")
v=input("Enter your answer here, only the letter: ")
if v=="c" or v=="C":
    print("Correct!")
    a=a+1
else:
    print("Incorrect. The correct answer is c)Cricket")
print("You have completed the quiz!")
print("Calculating your score...")
print("You got", a, "out of 5 questions correct.")
if a==5:
    print("Excellent work! You really know Neeal well!")
elif a>=3:
    print("Good job! You have a decent knowledge about Neeal.")
else:
    print("You might want to get to know Neeal better!")