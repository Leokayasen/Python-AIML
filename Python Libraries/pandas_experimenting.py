import pandas
print("Currently running: Pandas",pandas.__version__)
print(" ")

mydataset = {
    "cars": ["Audi", "Toyota", "BMW"],
    "passing": [3,7,2]
}

print("Let's see an example dataset, formatted as a DataFrame using the pandas library:")
mycars = pandas.DataFrame(mydataset) #Formats the given dictionary above into a grid
print(mycars) #Prints the formatted grid

print("- - -")

print("Pandas Series")
a = [3,7,2]
print("Let's format",a, " as a Pandas Series:")
myseries = pandas.Series(a)
print(myseries)

print("- - -")

print("Labels")
print("If nothing is specified, values are labelled with their index number, starting from 0.")
print("With the 'Index' argument, we can write our own labels.")
print("Here is the original series:")
print(myseries)

print(" ")

print("And here is the labelled series:")
a = [3,7,2]
labelledseries = pandas.Series(a, index = ["X", "Y", "Z"])
print(labelledseries)
print("When you've created labels, you can refer an item with the label")
print(labelledseries["Z"])

print("- - -")

