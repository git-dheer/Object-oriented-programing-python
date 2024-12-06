# item1 = "phone"
# item1_price = 100
# item1_quantity = 5
import csv

class item :
    pay_rate = 0.8 # wthe pay rate after 20% discount 

    all  = []

    def __init__(self, name:str,price:int,quantity:int=0):
        assert price>=0 , f"price {price} is not greater than or equal to zero !"
        assert quantity>=0, f"quantity  {quantity} is not greater than or equal to zero !"

        print(f"An instance created : {name}")
        self.name = name 
        self.price = price
        self.quantity = quantity

        # actions to execute 
        item.all.append(self)

    # def calculate_total_price (self,x,y) : 
    #     return x*y
    def calculate_total_price (self) : 
        return self.price * self.quantity
    
    def apply_discount (self) :
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"item('{self.name}', {self.price}, {self.quantity})"

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv","r") as f :
            reader =  csv.DictReader(f)
            items = list (reader)
        
        for item in items :
            item(
                name = item.get("name"),
                price =int(item.get("price")),
                quantity = int(item.get ("quantity")),
            )
    pass

# item1 = item("phone",100,5)
# item1.name = "phone"
# item1.price = 100
# item1.quantity = 5
# print(item1.calculate_total_price(item1.price , item1.quantity))

# item2 = item("laptop",1000,3)
# item2.name = "laptop"
# item2.price = 1000
# item2.quantity = 3
# print(item2.calculate_total_price(item2.price , item2.quantity))

# print(item1.name,"  $",item1.price," ",item1.quantity)
# print(item2.name,"  $",item2.price," ",item2.quantity)

# print(item1.calculate_total_price())
# print(item2.calculate_total_price())
# print(item.pay_rate)
# print(item1.pay_rate)
# print(item2.pay_rate)
# print(item.__dict__) # all atributes for class level 
# print(item1.__dict__) # all atributes of instance level 

# item1.apply_discount()
# print(item1.price)

# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)


# item1 = item("Phone", 100, 1)
# item2 = item("Laptop", 1000, 3)
# item3 = item("Cable", 10, 5)
# item4 = item("Mouse", 50, 5)
# item5 = item("Keyboard", 75, 5)

# for instance in item.all :
#     print(instance.name)

#  csv file can be used to store values 
item.instantiate_from_csv()
print(item.all)