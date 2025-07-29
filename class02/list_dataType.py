# list = [1,2,3,4,5,"Tuhin",1.2,True,False]
# List Methods
list.append(6)
list.remove(1.2)
list.pop()
list.insert(0,0)


unsorted_list = [4,3,2,6,1,0]
# for sort and reverse the list
unsorted_list.sort(reverse=True)

# for sort the list
print(sorted(unsorted_list))

# print the first element of the list
print(list[0])

print("Print the list using for loop")
for  i in list:
    print(i)
    


for index,value in enumerate(list):
    print(f"Index: {index} Value: {value}")


list_length = int(input("Enter a the length of the list: "))
lst = list() or []

for i in range(list_length):
    element = input(f"Enter the element {i+1}: ")
    list.append(int(element))

print(list)






    
    
    
    
    
    




