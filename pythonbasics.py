import time

print("Hello World")

fname = 'John'
sname = 'Smith'
course = 'Computer Science'

for x in range(0, 3):
    print("Hello, my name is " + fname + " " + sname + " and I study " + course)

time.sleep(2)
print("- - -")
print("Introduction while loop")

x = 0
while (x < 6):
    print("Hello, my name is " + fname + " " + sname + " and I study " + course)
    x = x + 1

time.sleep(2)
print("- - -")
print("Weekday If loop")

x = input("Enter a number: ")


def weekDay(x):
    x = int(x)
    if x == 1:
        print("Monday")
    elif x == 2:
        print("Tuesday")
    elif x == 3:
        print("Wednesday")
    elif x == 4:
        print("Thursday")
    elif x == 5:
        print("Friday")
    elif x == 6:
        print("Saturday")
    elif x == 7:
        print("Sunday")
    else:
        print("Invalid")


weekDay(x)

print("- - -")
time.sleep(2)
print("String splitting")


def chunk(x):
    print("Let's try splitting a string, call it 'Artificial Intelligence'")
    print(x[:3] + " - This is the first 3 letters of the string")
    print(x[3:] + " - This is the remainder of the string after removing the first 3 letters")


chunk("Artificial Intelligence")

time.sleep(2)
print("- - -")
print("Argument Function")


def func1(*args):
    result = 0
    for y in args:
        result = y + result
    return result


time.sleep(1)
print("Let's try the arguments: 1, 13, 4, 5")
func1(1, 13, 4, 5)

print("Now let's try the arguments: 1, 13, 4, 5, 7, 8")
func1(1, 13, 4, 5, 7, 8)