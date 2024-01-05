import datetime

import requests


class BankTerminal:
    def __init__(self, balance, pin):
        self.__user_balance = balance
        self.__system_balance = balance
        self.__pin = pin
        self.__logged_in = False

    def __check_pin(self, entered_pin):
        if entered_pin == self.__pin:
            self.__logged_in = True
            return True
        else:
            return False

    def __update_balances(self):
        with open("user_balance.txt", "w") as user_file:
            user_file.write(str(self.__user_balance))

        with open("system_balance.txt", "w") as system_file:
            system_file.write(str(self.__system_balance))

    def withdraw_funds(self, amount):
        if self.__logged_in and amount <= self.__user_balance and amount <= self.__system_balance:
            self.__user_balance -= amount
            self.__system_balance -= amount
            self.__update_balances()
            self.__log_activity("Withdraw", amount)
            return f"Withdrawn {amount} from your account."
        else:
            return "Withdrawal unsuccessful. Insufficient balance or not logged in."

    def deposit_funds(self, amount):
        if self.__logged_in:
            self.__user_balance += amount
            self.__system_balance += amount
            self.__update_balances()
            self.__log_activity("Deposit", amount)
            return f"Deposited {amount} to your account."
        else:
            return "Deposit unsuccessful. Not logged in."

    def get_exchange_rate(self, base_currency, target_currency):
        response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{base_currency}")
        data = response.json()
        rate = data["rates"][target_currency]
        return rate

    def convert_currency(self, amount, from_currency, to_currency):
        if self.__logged_in:
            exchange_rate = self.get_exchange_rate(from_currency, to_currency)
            converted_amount = amount * exchange_rate
            with open("converted_currency.txt", "w") as converted_file:
                converted_file.write(f"Converted amount: {converted_amount} {to_currency}")
            self.__log_activity("Currency Conversion", amount, from_currency, to_currency)
            return f"Converted {amount} {from_currency} to {converted_amount} {to_currency}."
        else:
            return "Conversion unsuccessful. Not logged in."

    def __log_activity(self, action, amount, from_currency=None, to_currency=None):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = {
            "Timestamp": timestamp,
            "Action": action,
            "Amount": amount,
            "From Currency": from_currency,
            "To Currency": to_currency
        }
        with open("activity_log.txt", "a") as log_file:
            log_file.write(str(log_entry) + "\n")


# Приклад використання класу BankTerminal:
user_pin = 1234  # Пін користувача
user_balance = 1000  # Початковий баланс користувача

# Створення об'єкту терміналу
terminal = BankTerminal(user_balance, user_pin)

# Перевірка пін-коду (викличеться автоматично при створенні об'єкту)
entered_pin = 1234  # Введений пін
if terminal._BankTerminal__check_pin(entered_pin):
    print("Logged in successfully")
else:
    print("Login failed")

# Приклад використання методів терміналу:
print(terminal.withdraw_funds(500))  # Зняття коштів
print(terminal.deposit_funds(200))  # Поповнення балансу
print(terminal.get_exchange_rate("USD", "EUR"))  # Отримання курсу валют
print(terminal.convert_currency(100, "USD", "EUR"))  # Конвертація валюти
