
class Money():
    '''Совершает операции и вычисления с купюрами'''

    def __init__(self, amount_banknotes, amount_coins = [], total_money = 0, min_sum = 0, max_sum = 0): s
        '''общее количество купюр и общую сумму денег.
Количество купюры и монеты задаются при создании экземпляра класса в виде списков'''
        self.amount_banknotes = amount_banknotes
        self.amount_coins = amount_coins
        self.total_money = total_money
        self.denomination_banknotes = [100,200,500,1000,2000,5000]
        self.min_sum = 100
        self.max_sum = 45000

    def consider_amount_money(self):
        '''Метод подсчитывает все купюры и присвает одноименной переменной общую сумму на текущий момент'''
        num = 0
        k = 0
        for i in self.amount_banknotes:
            num += (self.denomination_banknotes)[k] * i
            k += 1
        self.total_money = num

    def translate(self):
        pass


den_bank = [50 for x in range(6)]
money = Money(den_bank)

money.consider_amount_money()
#print(money.total_money)
print(NEKO ONE LOVE)
