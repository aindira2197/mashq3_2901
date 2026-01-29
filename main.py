class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __add__(self, amount):
        return BankAccount(self.balance + amount)

    def __sub__(self, amount):
        if amount > self.balance:
            print("Pul yetarli emas ❌")
            return self
        return BankAccount(self.balance - amount)

    def __str__(self):
        return f"Balans: {self.balance} so‘m"


acc = BankAccount(1000)
acc = acc + 500
acc = acc - 300
print(acc)
