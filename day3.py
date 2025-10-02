my_dict = {"name": "philip", "age": 30, "tribe": "kenyan"}
print(my_dict)

#  my_dict.clear()
#  print(my_dict)

backup = my_dict.copy()
print(backup)

keys = [ "name", "age", "city"]
values = "unknown"
default = dict.fromkeys(keys, values)
print(default)

getting = backup.get("name")
print(getting)

key1 = backup.keys()
print(key1)

value1 = backup.values()
print(value1)

all_items = backup.items()
print(all_items)

popping = backup.pop("name")
print(popping)
print(backup)

popitem = my_dict.popitem()
print(popitem)
print(my_dict)

new_dict = {"name": "james", "country": "kenya"}
# setdefault = backup.setdefault("ethinicity", "giriama")
# print(setdefault)
setdefault = new_dict.setdefault("name", "tony")
print(setdefault)
print(new_dict)

updating = my_dict.update(new_dict)
# print(updating)
print(my_dict)
 
 
new_keys = ["school", "gender", "class"]
new_values = ["Barani", "male", "form 3"]
complete_dict = dict(zip(new_keys, new_values))
print(complete_dict)
