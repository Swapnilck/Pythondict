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

jk={{1,3,3},{2,3,4}}
print(jk)       #TypeError: unhashable type: 'set'
