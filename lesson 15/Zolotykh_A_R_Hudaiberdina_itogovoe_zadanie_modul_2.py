class Person:
    def __init__(self,name,phone_number, address):
        self.__name = name
        self.__phone_number = phone_number
        self.__address = address

    @property
    def phone(self):
        return self.__phone_number

    @phone.setter
    def phone(self, number):
        self.__phone_number = number

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, data_address):
        self.__address = data_address
# _______________________________________________________

class Customer(Person):
    client_id = 0                                       # создаем атрибут класса
    def __init__(self, name,phone_number, address):
        super().__init__(name,phone_number, address)
        Customer.client_id +=1                          # меняем его при каждом создании экземпляра класса
        self.client_id = Customer.client_id             # создаем атрибут экземпляра класса и присваиваем ему значение текущего экземпляра объекта
# _______________________________________________________
class ShoppingCard():
    def __init__(self):
        self.product_list = []

    def add_list_product(self,name, number, price):
        self.product_list.append((name, number, price))

    def calculate_total(self):
       product_sum = [i[1]*i[2] for i in self.product_list] #в списочном выражении считаем сумму каждой покупки и укладываем в список
       return sum(product_sum)

    def remove_product(self, product_name):
        for i in self.product_list:
            if product_name == i[0]:
                self.product_list.remove(i)
# _______________________________________________________
class Shop:
    def __init__(self):
        self.customers = {}     # создаем пустой словарь при генерации экземпляра класса

    def add_customers(self, customer:Customer, product_list:ShoppingCard):
        self.customers[customer] = product_list                           # указываем через двоеточие, к какому классу принадлежит передаваемый объект и записываем в словарь

    def get_order_shopping(self, number):
        list_of_ids = [i.client_id for i in self.customers]
        if number in list_of_ids:
            for i in self.customers:
                if i.client_id == number: #обращаемся через i к ключу словаря, т.е. покупателю. Точнее к его атрибуту id. Сравниваем с введенным номером
                    return self.customers[i].calculate_total()  # через ключ i (покупатель) обращаемся к списку продуктови далее через точку вызываем метод подсчета суммы всех продуктов
        else:
            raise FailedClientID('Введено неверный id покупателя')


customer_1 = Customer('Иван', '89187587729', 'Москва')
customer_2 = Customer('Денис', '89187459652', 'Санкт-Петербург')
customer_3 = Customer('Наталья', '89185236648','Астрахань')
print(customer_2.client_id)
print(customer_1.client_id)
print(customer_3.client_id)
products_1 = ShoppingCard()
products_1.add_list_product('колбаса', 2, 500)
products_1.add_list_product('хлеб', 1, 73)
products_2 = ShoppingCard()
products_2.add_list_product('молоко', 3, 98)
products_2.add_list_product('плавленный сыр', 1, 212)
products_3 = ShoppingCard()
products_3.add_list_product('Энергетик Flash', 5, 69)
products_3.add_list_product('Кофе Chibo', 1, 560)


data = Shop()
data.add_customers(customer_1,products_1)
data.add_customers(customer_2,products_2)
data.add_customers(customer_3, products_3)

print(data.get_order_shopping(4))










