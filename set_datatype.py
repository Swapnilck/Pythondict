#define set
#order_set={"man","wan","man"}
#print(order_set)

#op-{'man', 'wan'} --no duplicates allowed

myset={1,2,3}
myset.add(4)
print(myset)    #op {1, 2, 3, 4}

myset.remove(2)
print(myset)      #op {1, 3, 4}