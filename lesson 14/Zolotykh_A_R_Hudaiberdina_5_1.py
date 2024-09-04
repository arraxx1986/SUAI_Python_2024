import datetime
class BankAccount:
    data = []
    def __init__(self, account_number, summ):
        self.summ = summ
        self.account_number = account_number
        BankAccount.data.append(f'{datetime.datetime.now()}\nСоздан счет {self.account_number} на сумму {self.summ}\n __________________')

    def add_money(self, value):
        self.summ = self.summ + value
        BankAccount.data.append(f'{datetime.datetime.now()}\nНа счет {self.account_number} добавлена сумма в размере {value}')
        BankAccount.data.append(f'Сумма на счету {self.account_number} составляет {self.summ}\n __________________')
    def take_money(self, value):
        self.summ = self.summ - value
        BankAccount.data.append(f'{datetime.datetime.now()}\nСо счета {self.account_number} снята сумма в размере {value}')
        BankAccount.data.append(f'Сумма на счету {self.account_number} составляет {self.summ}\n __________________')

    def add_percent(self, percent):
        self.summ = self.summ + (self.summ*percent/100)
        BankAccount.data.append(f'{datetime.datetime.now()}\nНа счет {self.account_number} добавлен процент в размере {percent}')
        BankAccount.data.append(f'Сумма на счету {self.account_number} составляет {self.summ}\n __________________')

    def get_info_all_operations(self):
        for i in BankAccount.data:
            print(i)

account_1 = BankAccount(5469, 1000)
account_1.add_money(500)
account_1.take_money(253)
account_1.add_percent(3)
account_1.get_info_all_operations()






