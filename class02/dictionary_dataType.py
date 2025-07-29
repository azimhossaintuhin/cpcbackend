dictionary = {
    "name":"Tuhin",
    "age":20,
    "city":"Dhaka",
    "country":"Bangladesh",
    "is_student":True,
    "is_teacher":False,
    "is_admin":True,
}

# dictionary2=dict(
#     name = "Tuhin",
#     age = 20,
#     city = "Dhaka",
#     country = "Bangladesh",
#     is_student = True,
#     is_teacher = False,
#     is_admin = True,
# )

# print(dictionary)
# print(type(dictionary))

# # Dictionary Methods
# print(dictionary["name"])
# print(dictionary.get("name"))
# print(dictionary.keys())
# print(dictionary.values())
# print(dictionary.items())
# # update the key value 
# # dictionary["name"] = "Azim"
# # # the 2nd way
# # dictionary.update({"name":"Azim"})
# # # remove the key value
# # dictionary.pop("name")
# # print(dictionary)
# # # remove the last key value
# # dictionary.popitem()
# # print(dictionary)
# # # # clear the dictionary
# # dictionary.clear()
# # print(dictionary)
# # # # delete the dictionary
# # del dictionary
# # print(id(dictionary))
# # print(dictionary)

# return only the keys
for i in dictionary.keys():
    print(i)

# return only the values
for i in dictionary.values():
    print(i)
    
# return the keys and values
for key,value in dictionary.items():
    print(f"Key: {key} Value: {value}")










