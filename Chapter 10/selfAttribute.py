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

obj = Phone()
print(obj.getPrice())
print(obj.getInfo())

# Instance attribute
obj.brand = "Apple"
print(obj.getInfo())

#Output: 
# 121000
# {'Brand ': 'Samsung', 'Model ': 'S21 Ultra'}
# {'Brand ': 'Apple', 'Model ': 'S21 Ultra'}

