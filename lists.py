# Lab 2 Code

#A table to store names of countries
countries = ["Italy", "France", "America", "England", "Germany"]

for x in countries:
    #Searches "countries" table and prints a welcome message
    print("- - -")
    print(f"Welcome to {x}")


countries.sort() #Sorts in order
for x in countries:
    print("- - -")
    print("Countries")
    print(f"Welcome to {x}")


# Inserts "India" and "China" in positions 2 and 3 respectively
countries[2:3]=["India", "China"]

print("- - -")
print("People")
# Dictionary for "people" instance
people = {"firstname":"John",
          "lastname":"Smith",
          "age":"20",
          "gender":"M",
          "city":"Brighton"
          }

print("- - -")
print("Person:")
print(people["firstname"])
print(people["lastname"])
print("Age: "+people["age"])
print("Gender: "+people["gender"])
print("Home: "+people["city"])

print("- - -")
print("Rivers")

rivers = {"Nile":"Egypt",
          "Danube":"Hungary",
          "Amazon":"Brazil",
          }

for x,y in rivers.items():
    print("- - -")
    print(f"The {x} runs through {y}")

for x in rivers.keys():
    print("- - -")
    print("Rivers:")
    print(x)

print("- - -")
print("Tuple")

a,b,c = ("Apple", "Banana", "Cherry")
#Fruit tuple
print(a),print(b),print(c)

a,*b,c = ("Apple", "Banana", "Cherry", "Strawberry", "Mango")
#Expanded Fruit Tuple
print(a),print(b),print(c)
