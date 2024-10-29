class Phone:
    #Class Attributes
    brand = "Samsung"
    model = "S21 Ultra"
    price = 121000
    
    #Class Methods
    def getPrice(self):
        return self.price
    def getInfo(self):
        return {"Brand ":self.brand,
                "Model ":self.model}
    @staticmethod
    def greet():
        return "Hello, I am a phone"

obj = Phone()
print(obj.greet())