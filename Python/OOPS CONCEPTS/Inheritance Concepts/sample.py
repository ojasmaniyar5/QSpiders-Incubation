class Mobile:
    def __init__(self, model, price, model_no, color):
        self.model = model
        self.price = price
        self.model_no = model_no
        self.color = color
        
    def display(self):
        color = ['blue', 'black', 'red']
        for i in color:
            print(self.model, self.price, self.model_no, i)
        
obj1 = Mobile(1, 'iphone', 1500000)
obj2 = Mobile(2, 'Samsung', 50000)
obj3 = Mobile(3, 'OnePlus', 30000)

obj1.display()
print()
obj2.display()
print()
obj3.display()