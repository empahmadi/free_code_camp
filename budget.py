class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": amount * -1, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        t = 0
        for j in self.ledger:
            t += j['amount']
        return t

    def transfer(self, amount, budget):
        if self.check_funds(amount):
            self.withdraw(amount, 'Transfer to ' + budget.name)
            budget.deposit(amount, 'Transfer from ' + self.name)
            return True
        else:
            return False

    def check_funds(self, amount):
        s = 0
        for i in self.ledger:
            s += i['amount']
        if amount > s:
            return False
        else:
            return True

    def __str__(self):
        first = '{num:*^{width}}'.format(num=self.name, width=30)
        second = ''
        s = 0
        for i in self.ledger:
            s += i['amount'] + 0.00
            data = i['description']
            second += '{value:<{width}}'.format(value=(data[:23]) if len(data) > 23 else data, width=23)
            second += '{num:>{width}.2f}\n'.format(num=i['amount'], width=7)
        third = 'Total: ' + str(s)
        return first + '\n' + second + third


def create_spend_chart(categories):
    withdrawals = []
    result = 'Percentage spent by category\n'
    for i in categories:
        t = 0
        for j in i.ledger:
            if j['amount'] < 0:
                t += (j['amount'] * -1)
        withdrawals.append(t)
    s = 0
    for i in withdrawals:
        s += i
    for i in range(len(withdrawals)):
        withdrawals[i] = int((withdrawals[i]/s) * 10) * 10
    for i in range(10, -1, -1):
        result += '{num:>{width}}| '.format(num=str(i * 10), width=3)
        for j in range(len(withdrawals)):
            if withdrawals[j] >= i * 10:
                result += 'o  '
            else:
                result += '   '
        result += '\n'
    result += '    {num:->{width}}-\n'.format(num='-', width=len(withdrawals)*3)
    names = []
    ml = 0
    for i in categories:
        names.append(i.name)
        if len(i.name) > ml:
            ml = len(i.name)
    for i in range(ml):
        result += '    '
        for j in names:
            if len(j) > i:
                result += '{value:^{width}}'.format(value=j[i], width=3)
            else:
                result += '   '
        if i != ml - 1:
            result += ' \n'
        else:
            result += ' '

    return result


def main():
    food = Category("Food")
    clothes = Category("Clothes")
    food.deposit(1000.00, 'initial deposit')
    food.withdraw(10.15, 'groceries')
    food.withdraw(15.89, 'restaurant and more foo')
    food.transfer(50, clothes)
    print(food)
    print(clothes)


if __name__ == '__main__':
    main()
