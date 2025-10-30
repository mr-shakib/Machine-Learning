#--- Print ---
print("Python Revision for Machine Learning!")

#--- Variables (string, int, float, boolean) ---
full_name = "Shakib Howlader"
age = 23
gpa = 3.92
is_student = False

print(f"Full Name: {full_name}")
print(f"I am {age} years old")
print(f"Gpa is {gpa}")

if is_student:
    print("I am a Student!")
else:
    print("I am not a Student!")

#--- Arithmetic : + addition
#                 - subtraaction
#                 * multiplication
#                 / division (return float)
#                 // integer division (return int)
#                 % reminder

apples = 5
print(apples)

#--- addition(+)
apples = apples + 1
print(apples)
apples += 1
print(apples)

#--- subtraaction(-)

apples = apples - 1
print(apples)
apples -= 1
print(apples)

#--- multiplication(*)

apples = apples * 2
print(apples)
apples *= 3
print(apples)

#--- division(/) --- returns float

apples = apples / 2
print(apples)
apples /= 2
print(apples)

#--- division(//) --- returns int

apples = apples // 2
print(apples)
apples //= 2
print(apples)

#--- reminder(%)

apples = 10
remaining_apples = apples % 3
print(remaining_apples)

apples = 10
apples %= 3
print(apples)

#--- Typecsting = the process of converting aa variable from one datatype to another 
#                 str(), int(), float(), bool()

name = "Shakib Howlader"
age = 23
gpa = 3.92
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

#--- typecast ---

gpa = int(gpa)
print(gpa)
print(type(gpa))

age = float(age)
print(age)
print(type(age))

age = str(age)
print(age)
print(type(age))

name = bool(name)
print(name)


#--- User Input ---
name = input("Enter your name: ")
print(type(name))
print(f"Hello {name}")

age = int(input("Enter your age: "))
print(type(age))
print(f"You are {age} years old")


#--- If statement = execute some code only if a condition is true
#                   allow: if, elif, else

age = int(input("Enter you age: "))
has_ticket = True
price = 10.00


if age >= 65:
    print("You are a senior citizen")
    print(f"The ticket price for you is ${price * 0.5}")
elif age >= 20:
    print("You are an adult!")
    print(f"The ticket price for adult is ${price}")
elif age >= 13 and age <= 19:
    print("You are a teen!")
else:
    print("Kids stay away!")

if has_ticket:
    print("You may enter. you have a ticket!")
else:
    print("You have to buy a ticket!")



#--- Logical Operators = evalute multiple conditions (or, and, not)
#                       or = at least one condition must be true
#                       and = both condition must be true
#                       not = invert the condition (not False, not True)

#--- or ---
temp = 25
is_raining = True

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled!")
else:
    print("The outdoor event is still scheduled")

#--- and ---
temp = 25
is_sunny = True

if temp >= 30 and is_sunny:
    print("Damn it's hot 🥵 !")
elif temp <= 0 and is_sunny:
    print("Oof it's cold 🥶!")
elif temp >= 20 and temp <= 30 and is_sunny:
    print("The Weather is comfortable 😊")
else:
    print("Don't like this weaather")

#--- not ---
temp = 26
is_sunny = False

if temp <= 0 and not is_sunny:
    print("Gonna die 💀 !")
elif temp >= 25 and not is_sunny:
    print("Comfy!")
else:
    print("Don't like this weaather")


#--- while loop = used to repeat a block of code asa long as a condition remains 
#                 we re-check the condition at the end of the loop
name = input("Enter your name: ")
while name == "":
    name = input("Enter your name: ")

age = int(input("Enter your age:"))

while age < 0:
    print("Kididng me?")
    age = int(input("Enter your age:"))

print(f"Hi {name}")
print(f"You are {age} year's old!")


#-- For Loop = used to iterate over a sequence (string, list, tuple, set)
#               repeat a block of code and exact amount of times

for i in range(1,11, 2): #first number inclusive and second number is exclusive in range, lasat number is increment
    print(i)

name = "Shakib Howlader"
for letter in name:
    print(letter, end = "") #if we do not use end it will prnt on new line

#--- countdown timer ---
import time
for i in range(10,0,-1):
    print(i)
    time.sleep(1)
print("Happy New Year")




# list[] = mutable, most flexible
# tuple() = immutable , faster
# set{} = mutable(add,remove) , unordered, 
#         no duplicates, best for membership testing


#--- list[] ---

fruits = ["apple","banana", "coconut","orange"]
print(fruits)
print(fruits[0])
print(fruits[-1])

for fruit in fruits:
    print(fruit, end=" ")

fruits[0] = "pineapple"
fruits[3] = "mango"
print(fruits)

fruits.append("litchi")
print(fruits)

fruits.remove("banana")
print(fruits)

fruits.pop()
print(fruits)

fruits.pop(2)
print(fruits)

fruits.clear()
print(fruits)



#--- tuples() ---
fruits = ("apple","banana", "coconut","orange")
print(fruits)


#--- sets{} ---
fruits = {"apple","banana", "coconut","orange", "coconut", "coconut", "coconut", "coconut"}
print(fruits)

fruits.add("mango")
print(fruits)

fruits.remove("coconut")
print(fruits)

fruits.pop()
print(fruits)


fruit = input("Enter a fruit to search for: ")

if fruit in fruits:
    print(f"{fruit} was found")
else:
    print(f"{fruit} was not found")
