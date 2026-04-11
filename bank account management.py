class BankAccount:
    def __init__(self, name, account_no, initial_balance=0):
        self.name = name
        self.account_no = account_no
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New Balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        try:
            if amount > self.balance:
                raise Exception("Insufficient Balance")
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive")
            
            self.balance -= amount
            print(f"Withdrew {amount}. New Balance: {self.balance}")
        except Exception as e:
            print(f"Error: {e}")

    def save_to_file(self):
        try:
            f = open("bank_records.txt", "a")
            f.write(f"Account: {self.account_no} | Name: {self.name} | Balance: {self.balance}\n")
            print("Record saved to file.")
        except Exception:
            print("Error while writing to file")
        finally:
            try:
                f.close()
            except:
                pass

def main():
    print("--- Welcome to the Bank Management System ---")
    name = input("Enter Account Holder Name: ")
    acc_no = input("Enter Account Number: ")
    
    user_acc = BankAccount(name, acc_no, 1000)

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Save and Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            try:
                amt = float(input("Enter amount to deposit: "))
                user_acc.deposit(amt)
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        elif choice == "2":
            try:
                amt = float(input("Enter amount to withdraw: "))
                user_acc.withdraw(amt)
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        elif choice == "3":
            user_acc.save_to_file()
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

main()