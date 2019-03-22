import csv
import string

# Open the CSV File and read it in.
f = open(input("File name: "))
data = f.read()

# Split the data into an array of countries.
elementsList = data.split('\n')

# print length of the list
length = len(elementsList)
# print the first element
#print(elementsList[0])

# print the last element
#print(elementsList[len(elementsList)-1])
# print all the elements
#print(elementsList)
for item in elementsList:
    print(item)
# Start your search algorithm here.
countryName = input("Name: ")

beginningIndex = 0
endingIndex = length-1
index = int((endingIndex-beginningIndex)/2)
if countryName not in elementsList:
    print("Not an option.")
else:
    while elementsList[index] != countryName:
        if countryName < elementsList[index]:
            beginningIndex = beginningIndex
            endingIndex = index
            index = int((endingIndex-beginningIndex)/2)+ beginningIndex
        elif countryName > elementsList[index]:
            beginningIndex = index+1
            endingIndex = endingIndex
            index = int((endingIndex-beginningIndex)/2)+ beginningIndex
        else:
            print(index)

    print(index)
