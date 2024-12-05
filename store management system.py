# item1 = "phone"
# item1_price = 100
# item1_quantity = 5

class item :
    def __init__(self, name:str,price:int,quantity:int=0):
        assert price>=0 , f"price {price} is not greater than or equal to zero !"
        assert quantity>=0, f"quantity  {quantity} is not greater than or equal to zero !"

        print(f"An instance created : {name}")
        self.name = name 
        self.price = price
        self.quantity = quantity
    # def calculate_total_price (self,x,y) : 
    #     return x*y
    def calculate_total_price (self) : 
        return self.price * self.quantity


    pass

item1 = item("phone",100,5)
# item1.name = "phone"
# item1.price = 100
# item1.quantity = 5
# print(item1.calculate_total_price(item1.price , item1.quantity))

item2 = item("laptop",1000,3)
# item2.name = "laptop"
# item2.price = 1000
# item2.quantity = 3
# print(item2.calculate_total_price(item2.price , item2.quantity))

print(item1.name,"  $",item1.price," ",item1.quantity)
print(item2.name,"  $",item2.price," ",item2.quantity)

print(item1.calculate_total_price())
print(item2.calculate_total_price())