

custdata:str= """CustomerID,Name,Email,Phone,Country
1,John Doe,john.doe@example.com,555-1234,USA
2,Jane Smith,jane.smith@example.com,555-5678,Canada
3,Ali Khan,ali.khan@example.com,555-8765,UK
4,Maria Garcia,maria.garcia@example.com,555-4321,Spain
5,Chen Wei,chen.wei@example.com,555-3456,China """

#headerdata
header=custdata.split("\n")[0]
#print(header)
#[CustomerID,Name,Email,Phone,Country]

#actualdata
actualdata=custdata.split("\n")[1:]
#print(actualdata)
#['1,John Doe,john.doe@example.com,555-1234,USA', '2,Jane Smith,jane.smith@example.com,555-5678,Canada']

#created new dictionary
newdict={}

#add actual data in new dict
for x in actualdata:
    newdict[x.split(",")[0]]= tuple(x.split(",")[1:])
#print(newdict)
#{'1': ('John Doe', 'john.doe@example.com', '555-1234', 'USA'), '2': ('Jane Smith', 'jane.smith@example.com', '555-5678', 'Canada')}

#find 0th position value of 1st key
#print(newdict["1"][0])
#John Doe

nesteddict={}

for key,value in newdict.items():
    nesteddict[key]={
        "name" : value[0],
        "mailid" : value[1],
        "mobileno" : value[2],
        "country" : value[3]

    }

#nested dict
#print(nesteddict)
#{'key': {'name': 'Chen Wei', 'mailid': 'chen.wei@example.com', 'mobileno': '555-3456', 'country': 'China '}}

print(nesteddict.get("1").get("mobileno"))

























