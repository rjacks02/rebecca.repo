from bank_account import BankAccount

acc1 = BankAccount("123")
acc2 = BankAccount("0", 234)
acc3 = BankAccount("43", 1000000)

print(acc1)
print(acc2)
print(acc3)

acc1.deposit(300)
acc2.deposit(20)

acc3.withdraw(1)


