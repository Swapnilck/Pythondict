
#this is raw data
custdata:str= """CustomerID,Name,Email,Phone,Country
1,anil,anil.doe@example.com,555-1234,USA
2,sunil Smith,sunil.smith@example.com,555-5678,Canada
3,Aman gaman,aman.gaman@example.com,555-8765,UK
4,Maria d,maria.d@example.com,555-4321,Spain
5,Chen Wei,chen.wei@example.com,555-3456,China """



#headerdata
header=custdata.split("\n")[0].split(",")
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
        header[1] : value[0],
        header[2] : value[1],
        header[3] : value[2],
        header[4] : value[3]

    }

#nested dict
#print(nesteddict)
#{'key': {'name': 'Chen Wei', 'mailid': 'chen.wei@example.com', 'mobileno': '555-3456', 'country': 'China '}}

#print(nesteddict.get("1"))

#id=input("enter teh customer_id  :")
#details=input("enter what details u want  :")

#print(nesteddict.get(id).get(details))

order_data = """101,Laptop,1,1200
102,Smartphone,2,800
103,Headphones,3,150
104,Monitor,4,300
105,Keyboard,5,70"""

order=order_data.split("\n")


combinelist=[]

for x in order:
    border=x.split(",")
    combinelist.append((border[0],border[1],border[2],border[3],newdict[border[2]]))  #combine order and dict

print(combinelist)

#[('101', 'Laptop', '1', '1200', ('anil', 'anil.doe@example.com', '555-1234', 'USA'))






























