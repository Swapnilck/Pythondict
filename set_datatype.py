#define set
#order_set={"man","wan","man"}
#print(order_set)

#op-{'man', 'wan'} --no duplicates allowed

myset={1,2,3}
myset.add(4)
#print(myset)    #op {1, 2, 3, 4}

myset.remove(2)
#print(myset)      #opt {1, 3, 4}


op={(1,2,3),(1,2),(1,2,3)}
op.remove((1,2))
#print(op)

#(km={[1,2,3],[1,2]}
#print(km)        #TypeError: unhashable type: 'set'  ...primitive and tuples allowed in set


#print(jk)       #TypeError: unhashable type: 'set'

##realtime use case

#1.find duplicates

list1=[1,1,1,2,3,2,3,2,3,2,3]
dupli=set(list1)
print(dupli)          #{1, 2, 3}

#2.check membership
man={"10.3.4.5","21.34.5.6"}
if "10.3.4.5" in man:
    print("good")        #good

#matching elements between 2 set
a={"ab","ac","ad"}
b={"ad","ac","kb"}
common=a.intersection(b)
print(common)     #{'ac', 'ad'}






