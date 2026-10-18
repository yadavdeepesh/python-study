import json 
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

print(x)
# parse x:
y = json.loads(x)

print(y)
# the result is a Python dictionary:
print(y["age"])

# There are two important methods:
# - json.dumps() — Python data → JSON string.
# - json.loads() — JSON string → Python data.

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))