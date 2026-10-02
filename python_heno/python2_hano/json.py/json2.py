'''with open("file.txt","w") as f:
    print(f.write("\nhello guru prema kosame noiiii jevitham.."))
    print(f.write("\nchiru,nag,rajni...."))
    
with open("file.txt","r") as f :
    for line in f:
        print(line)
        
f=open("file.txt","r")
print(f.tell())
f.seek(0)
f.close()

'''
'''try:
    with open("file.txt","r") as f:
        print(f.read())
except FileNotFoundError:
    print("file not found.")'''
    
'''with open("file.txt","rb") as f:
    data=f.read()
    print(f.read())'''
    
'''import csv

with open("file1.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["names", "age"])
    rows=[["dhanu",20],
    ["raghu",18],
    ["siva",21]]
    writer.writerows(rows)'''
    
    
import time
import numpy as np

# Python list approach
data_list = list(range(10**6))
start = time.time()
result_list = [x * 2 for x in data_list]
end = time.time()
print(end - start)

# NumPy array approach
data_array = np.array(data_list)
start = time.time()
result_array = data_array * 2
end = time.time()
print(end - start)

   