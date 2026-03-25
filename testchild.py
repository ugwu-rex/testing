# Display welcome message
message = "Hello"

name = input("Enter your name! ")

name = name.title()

print (message, name)


print("For the Party there\'s an age restrictions...")

age = int(input("what is your age? "))

if (age >= 18):
    print ( "welcome, " + name)
elif age >= 16 and age < 18:
    print(name + " You are not yet eligible, you still have a little way to go.")
else:
    print("You're too young " + name)

