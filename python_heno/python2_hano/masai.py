'''import json
from pathlib import Path
def export_products(products, date_dir="data"):
    data_path=Path('data_dir')
    data_path.mkdir(exist_ok=True)
    
    csv_path=data_path/"products.csv"
    json_path=data_path/"summary.json"
    lines=["id,name,price,category\n"]
    for product in products:
        line=f"{product['id']},{product['name']},{product['price']},{product['category']}\n"
        lines.append(line)
        
    with open(csv_path, "w") as f:
        f.writelines(lines)
        
    total_products=len(products)
    totla_value=sum(product['price'] for product in products)
    summary={
        "total_products": total_products,
        "total_value": totla_value
    }
    
    with open(json_path, "w") as f:
        json.dump(summary, f)
    return str(csv_path), str(json_path)
if __name__ == "__main__":
    products=[
        {"id":1,"name":"laptop","price":65000,"category":"tech"},
        {"id":2,"name":"mouse","price":9000,"category":"tech"},
        {"id":3,"name":"desk","price":5000,"category":"furniture"},
    ]
    print(export_products(products))'''
    
import json
from pathlib import Path

def export_products(products, data_dir="data"):
    # Create directory
    data_path = Path(data_dir)
    data_path.mkdir(exist_ok=True)

    # File paths
    csv_path = data_path / "products.csv"
    json_path = data_path / "summary.json"

    # CSV lines
    lines = ["id,name,price,category\n"]

    for product in products:
        line = f"{product['id']},{product['name']},{product['price']},{product['category']}\n"
        lines.append(line)

    # Write CSV
    with open(csv_path, "w") as f:
        f.writelines(lines)

    # Summary
    total_products = len(products)
    total_value = sum(product["price"] for product in products)

    summary = {
        "total_products": total_products,
        "total_value": total_value
    }

    # Write JSON
    with open(json_path, "w") as f:
        json.dump(summary, f)

    return str(csv_path), str(json_path)


if __name__ == "__main__":
    products = [
        {"id": 1, "name": "laptop", "price": 65000, "category": "tech"},
        {"id": 2, "name": "mouse", "price": 900, "category": "tech"},
        {"id": 3, "name": "desk", "price": 5000, "category": "furniture"},
    ]

    print(export_products(products))