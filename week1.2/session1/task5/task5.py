# Week 1.2, Session 1: Task 5

rivers = {
    "London": "Thames",
    "Leeds": "Aire",
    "Liverpool": "Mersey"
}

print(rivers)

# Add two new entries to the rivers database
rivers["Torun"] = "Vistula"
rivers["Birmingham"] = "River Rea"
print(f"Operation 1 {rivers}")
# Display all the keys
print(f"Printing Keys {rivers.keys()}")
# Display all the values
print(f"Printing Value {rivers.values()}")
# Display all the key:value pairs, as tuples
print(f"Returning Key:Value pairs as a tuple {rivers.items()}")
# Delete an entry from the rivers database
rivers.pop("Leeds")
print(rivers)