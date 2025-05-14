# create a class called Mobile.
# class member: model, price, model_no
# object member: color - blue, black, red.
# solve the above problem using class and object.


# class mobile:
#     model_no = 1
#     model = 'A14 5G'
#     price = 16999
#     def __init__(self, color):
#         self.color = color
# obj = eval(input('Enter the color : '))
# print(obj.model_no, obj.model, obj.price, obj.color)



class Mobile:
    def __init__(self, model, price, model_no, color):
        self.model = model
        self.price = price
        self.model_no = model_no
        self.color = color
        
        color = input('Enter the color: ')
obj1 = Mobile('A14 5G', 16999, 1, 'blue')
obj2 = Mobile('A14 5G', 16999, 1, 'black')
obj3 = Mobile('A14 5G', 16999, 1, 'red')
print(obj1.model, obj1.price, obj1.model_no, obj1.color)
print(obj2.model, obj2.price, obj2.model_no, obj2.color)
print(obj3.model, obj3.price, obj3.model_no, obj3.color)