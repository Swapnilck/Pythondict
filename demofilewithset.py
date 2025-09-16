citylist = []
with open('C:/Users/dell/Documents/item.csv.txt', 'r') as file:
    next(file)
    for line in file:
      cities= line.strip().split(",")[4]
      citylist.append(cities)
print(citylist)