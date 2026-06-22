class ExchangeRateBoard:
    def __init__(self, rates: dict):
        self.rates = dict(rates)
        
    def get_rate(self, code):
        if code not in self.rates:
            raise ValueError("Такой валюты нет")
            
        return self.rates[code]
        
    def add_rate(self, code, rate):
        self.rates[code] = rate
        

class HistoryManager:
    def __init__(self):
        self.records = []
        
    def add_record(self, transaction):
        self.records.append(transaction)
        
    def get_all(self):
        return list(self.records)

def show_menu():
    print('1.конвертировать валюту')
    print('2.показать курс валюты')
    print('3.Показать записи')
    
def get_user_input():
    convert_currency = input("Введите валюту в которую хотите конвертировать").upper()
    show_rate_currency = input("Введите валюту курс которой хотите узнать").upper()
    show_records = input("Просмотр записей").upper()
    try:
        amount = float(input("Введите сумму: "))
    except TypeError:
        raise TypeError("Сумма должна быть числом!")
    if amount <= 0:
        raise ValueError("Сумма должна быть больше 0!")

def run():
    show_menu()
    while True:
               
        choice = input("Выберите пункт меню: ")
        if choice == "1":
            try:
                from_currency = input("Введите валюту: ")
                to_currency = input("Введите валюту,в которую хотите конвер: ")
                amount = float(input("Введите сумму: "))  
                
                if amount <= 0:
                    raise ValueError("Сумма должна быть больше 0")
                result = converterengine.convert(amount, from_currency, to_currency)
                print(result)
            
            except ValueError as error:
                print(f"Ошибка: {error}")
            
        elif choice == "2":
            try:
                currency = input("Введите валюту курс которой хотите узнать: ")
                rate = board.get_rate(currency)
                print(f"Курс {currency}: {rate}")
            
            except ValueError as error:
                print(f"Ошибка: {error}")
                    
                  
            
        elif choice == "3":
            print(history.get_all())
                
              
import time

class Transaction:
    def __init__(self, timestamp, from_currency, to_currency, amount, result, fee):
        self.timestamp = timestamp
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.amount = amount
        self.result = result
        self.fee = fee
        
    def __str__(self):
        return (
            f'Время транзакции: {self.timestamp} '
            f'Начальная монета: {self.from_currency} '
            f'Результат: {self.result:.2f} '
            f'Монета:{self.to_currency}'
            )
            
class ConverterEngine:
    def __init__(self, board, history, fee_percent):
        self.board = board
        self.history = history
        self.fee_percent = fee_percent
        
    def convert(self, amount, from_code, to_code):
        ts = time.time()
        rate_from = self.board.get_rate(from_code)
        rate_to = self.board.get_rate(to_code)
        result = (amount / rate_to) * rate_from
        fee = round(result * self.fee_percent, 2)
        transaction = Transaction(ts, from_code, to_code, amount, result, fee)
        self.history.add_record(transaction)
        return transaction
board = ExchangeRateBoard({"usd": 85, "euro": 90, "lira":25, "rub": 1})
history = HistoryManager()
converterengine = ConverterEngine(board,history, 0.0015)
run()