''''l=["hii","hello","hey"]
for i in range(4):
  l.append("yelow")
  print(i,l[i])'''
 
 
'''import numpy as np
def analyze(sales, bonus_row, temps):
      sales=np.array(sales)
      bonus_row=np.array(bonus_row)
      temps=np.array(temps)
      
      quarterly_totals=sales.sum(axis=0).tolist()
      store_totals=sales.sum(axis=1).tolist()
      top_store_index=int(np.argmax(sales.sum(axis=1)))
      bonus_applied=(sales+bonus_row.tolist())  
      hot_days=temps[temps > 35].tolist()   
      
      return {
        "quarterly_total": quarterly_totals,
        "store_toal": store_totals,
        "top_store_index": top_store_index,
        "bonus_applied": bonus_applied,
        "hot_days": hot_days
      }
if __name__ == "__main__":
  sales=[[110,142,152,158],
         [98,110,105,120],
         [121,145,152,160]]
  bonus_row=[10,20,30,40]
  temps=[28,31,30,20,40,38,41]
  print(analyze(sales, bonus_row, temps))'''
  
'''a = [1, 2, 3]
b = a
b.append(4)

original = [1, 2, 3]
copy = original.copy()
copy.append(4)
print(a)
print(b)
print(original)
print(copy)'''
A = [
    {"id": 1, "name": "laptop", "price": 65000, "tags": ["tech", "sale"]},
    {"id": 2, "name": "mouse", "price": 9000, "tags": ["tech", "sale"]}
]
print(type(A[0]["name"]))


