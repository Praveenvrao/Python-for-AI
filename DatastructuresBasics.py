#Lists

MyList = ["Index0", 32, 4.33, "Micheal", True]
print(MyList)
print(MyList[0])
MyList.append("John")
MyList.insert(2, "Nallan")
print(MyList)


#Dictionary

MyDictionary = {"Name": "Micheal", "Age": 32, "Height": 5.9, "Weight": 70}
print(MyDictionary)
print(MyDictionary["Name"])
MyDictionary["Nickname"] = "Mike"
print(len(MyDictionary))
MyDictionary.pop("Weight")
print(MyDictionary)
print(MyDictionary.keys())
print(MyDictionary.values())

#Tuples
Names = ("Micheal", "John", "Nallan", "Mike")
print(Names)
print(Names[-1])
print(Names[-4:-1])


#sets
# Empty set (careful!)
empty_set = set()  # NOT {} - that's a dict!

# Set with values - both ways work
numbers = {1, 2, 3, 4, 5}
fruits = set(["apple", "banana", "orange"])

# From a list (removes duplicates)
scores = [85, 90, 85, 92, 90]
unique_scores = set(scores)  # {85, 90, 92}
print(unique_scores)
print(list(unique_scores))  # Convert back to a list if needed