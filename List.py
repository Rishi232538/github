cities =  ["chennai", "maduari", "coimbatore", "Trichy"]
val = [3, 5, 7, 9, 5, 1, 6]

#Accessing List with indexing
print(cities[0])

#Modify
cities[3] = "Thiruchy"
print(cities)

#Append - Adding at the end
cities.append("virudhunagar")
print(cities)

#Insert
cities.insert(1, "ranipet")
print(cities)

#Remove the value
cities.remove("coimbatore")
print(cities)

#Accending order
val.sort()
print(val)

#Descending order
val.reverse()
print(val)