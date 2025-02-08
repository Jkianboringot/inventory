#first build atext type program where you can add a productname, quantity ,price,type


class Store():
    def __init__(self,product='',quantity=0,price=0):
        self.product = product
        self.quantity = quantity
        self.price = price


    def storing(self,PN,Q,P):
        self.product=PN
        self.price=P
        self.quantity=Q
        print(self.quantity,self.product,self.price)
    def quantity_product(self):
        pass
    def product_name(self):
        print(self.quantity,self.product)


    def prices(self,k):
        return k

    def category(self):
        pass


def hub():
    op=Store()
    while True:
        try:
            product_name=str(input("Enter product name: "))
            print("invalid input make sure it the correct data type")
            quantity=int(input("Enter quantity of product: "))
            price=int(input("Enter product price: "))
            op.storing(product_name,quantity,price)
            break
        except ValueError:
            print("invalid input make sure it the correct data type")

hub()









