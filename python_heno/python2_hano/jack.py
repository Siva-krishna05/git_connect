'''f=open("data.txt","r")
print(f.read())
f.close()
f=open("data.txt","w")
f.write("hello student\n")
f.write("hellooo studentt")
f.close()'''

'''try:
    file=open('sata.txt')
except FileNotFoundError:
    print("file not found")
finally:
    print("program finished")
'''

'''try:
    balance=5000
    withdraw=int(input("enter withdraw amount:"))
    if withdraw > balance:
        raise Exception("insufficient balance.")
    else:
        print("successful.")
except Exception as e:
    print("Error:",e)
finally:
    print("visit again...")'''
    
'''import os
for file in os.listdir():
    print(file)'''
    
'''from sklearn.tree import DecisionTreeClassifier
# Hours studied
X = [[1], [2], [3], [4], [5], [6]]
# 0 = Fail, 1 = Pass
y = [0, 0, 0, 1, 1, 1]
model = DecisionTreeClassifier()
model.fit(X, y)
result = model.predict([[5]])
if result[0] == 1:
    print("Pass")
else:
    print("Fail")'''



