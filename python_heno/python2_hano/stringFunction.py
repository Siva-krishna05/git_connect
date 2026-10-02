a={"u1","u2",'u3','u4'}
b={'u1','u2','u5','u6'}
#print("common:",a&b)
#print("all elements in the set:",a|b)
#print("unique:",a^b)
#print("it prints boolean values:",a.issubset(b))
#print("it prints boolean values:",b.issuperset(a))
a.update("u7","u9")
print(a)
a.add("u10")
print(a)