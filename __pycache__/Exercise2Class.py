from pyexpat import model


class CellPhone:
    def __init__(self,manufact,model,price):
        self.__manufact = manufact
        self.__model = model
        self.__retail_price = price

    def set_manufact(self, m):
        self.__manufact = m

    def set_model(self, mo):
        self__model = mo

    def set_retail_price(self, p):
        self.__retail_price = p

    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__retail_price