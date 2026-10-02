import json
user_prefs = {"theme": "dark", "notifications": True, "language": "en"}

# json.dump() writes directly to a file
with open("prefs.json", "w") as file:
    json.dump(user_prefs, file)
    
import json

# This is what the API returns — a JSON string
json_string = '{"city": "Mumbai", "temperature": 28, "humidity": 75, "rainy": true}'

# Use json.loads() to convert it to a Python dictionary
data = json.loads(json_string)

# Now you can access values easily
print(data["temperature"])  # Output: 28
print(data["city"])        # Output: Mumbai
print(type(data))
