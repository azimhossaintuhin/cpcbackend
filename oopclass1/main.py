class Mobile:
 
    BATTERY = 4000  
#    private and protected variables are not directly supported in Python, but we can use naming conventions to indicate that a variable is intended to be private or protected.
    _protected_variable = "This is a protected variable"
    
    __private_variable = "This is a private variable"
    
    
    def _protected_method(self):
        print("This is a protected method")
    
    def __new__(cls ,brand_name, model_name, camera_megapixels ,battery):
        print("Creating a new Mobile instance" , brand_name, model_name, camera_megapixels ,battery)
        if battery < 4000:
            raise ValueError("Battery capacity must be at least 4000 mAh")
        return super().__new__(cls)
    
    
    def __init__(self, brand_name, model_name, camera_megapixels ,battery=BATTERY):
        self.brand = brand_name
        self.model =  model_name
        self.camera = camera_megapixels
        self.battery = battery
        
    
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Camera: {self.camera} MP , Battery: {self.battery} mAh")


mob1 = Mobile("Apple", "iPhone 14 Pro", 48,4000 )
mob1.display_info()
mob2 = Mobile("Samsung", "Galaxy S23 Ultra",30,3000)
mob2.display_info()
mob3 = Mobile("Google", "Pixel 7 Pro", 50,5000)
mob3.display_info()
