# python function example
def my_function(name, batch , email):
    print("Hello  my name is", name)
    print("I am from", batch)
    print("My email is", email)

my_function(batch="d-75" ,email="d-75@example.com", name="Tuhin")

# meme reference funtion
def hello_world(params):
    if params == "print":
        print("Hello, World!")
    else:
        print("Unknown command")
    
hello_world("print")




def add_numbers(*args):
    
    total = 0
    for  num in args:
        total += num
    print(total)

add_numbers(1, 2, 3, 4, 5,6,7,8,9,10,11,12)  


def  user_info(*info):
    print(type(info))
    print("User Information:")
    print("Name:", info[0])
    print("Batch:", info[1])
    print("Email:", info[2])


user_info("Tuhin", 75 ,"d-75@example.com")






def user_info(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key}: {value}")


user_info(name="Tuhin", batch="d-75", email="d-75@example.com",address="Dhaka, Bangladesh")


def add_numbers(*args):
    try:
        total = 0
        for num in args:
            total += num
            
            
            
            
            
        return total
    except Exception as e :
        print(str(e))
        print("An error occurred while adding numbers.")


add_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,"Tuhin")
