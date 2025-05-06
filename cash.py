class BankAccount():
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(amount):
        print(f'Ваш счет пополнен на:{amount.balance}')

    def withdraw(amount):
        print(f'У вас недостаточно средств:{amount.balance}')

    def get_balance(amount):
        return f'{amount.balance}'

account = BankAccount('Gulzina',1500)
account.deposit()
account.withdraw()
print(f'Ваш баланс состовляет:{account.get_balance()}')
account.get_balance()