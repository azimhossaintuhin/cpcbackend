# inheritance and polymorphism
class  GrandParent:
    def __init__(self):
        self.grandparent_var = "This is a grandparent variable"
        print("this is a constructor from  the grandparent")

class  Parent(GrandParent):
    BASE = "This is the base class"

    def __init__(self):
        self.instance_var = "This is an instance variable"
        print("this is a constructor from  the parent")

    def mobile(self):
        return "This is a mobile method from  parent class"
    


# MRO (Method Resolution Order)
class Child(Parent,GrandParent):
    
    def __init__(self):
        self.class_instance_var_from_child = "This is a class instance variable"
        print("this is a constructor from  the child")

# Polymorphism
# A  bird which  can  walk like a duck swim like a duck  and  quack like a duck the bird is duck

class Vscode:
    def code(self):
        return "Coding in Visual Studio Code"
    def error_detection(self):
        return "Detecting errors in Visual Studio Code"
    def run_code(self):
        return "Running code in Visual Studio Code"


class VsyCode(Vscode):
    def code(self):
        return "Coding in Vsy Studio Code"
    def error_detection(self):
        return "Detecting errors in Vsy Studio Code"
    def run_code(self):
        return "Running code in Vsy Studio Code"
    def ai_gen(self):
        return "Generating AI code in Vsy Studio Code"


baseobj = Vscode()
obj1 = VsyCode()
print(obj1.code())
print(obj1.code())


# for creating virtual environment
# python -m venv env
# for windows
# .\env\Scripts\activate
# for linux or  mac
# source env/bin/activate