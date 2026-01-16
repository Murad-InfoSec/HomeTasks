#Task 1
age=int(input("Enter your age: "))
if age>=18:
    print("Enter allowed.")
else: 
    print("Enter forbidden.")

## Task 2 
name=input("Enter your name: ")
surname=input("Enter your surname: ")
age=int(input("Enter your age: "))
char=input("Enter your character: ")

print(name + surname,sep=" ")
print (f"Age: {age}")
print(age*char)