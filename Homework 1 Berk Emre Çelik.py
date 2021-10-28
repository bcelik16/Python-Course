import random

class stock(object):
    def __init__(self, price, stock_name):
        self.price = price
        self.stock_name = stock_name
        self.number_buy = 0.0

class mf(object):
    def __init__(self, price, mfund_name):
        self.price = price
        self.price = 1.0
        self.mfund_name = mfund_name
        self.number_buy = 0.0

class Portfolio(object):
    def __init__(self):
        self.cash = 0.0
        self.stocks = []
        self.mutual_funds = []
        self.transaction = ["History of Transactions:"]

    def addCash(self, amount):
        self.cash += amount
        self.transaction.append(f"\t*You have added $ {} of dollars to your account.".format(amount))

    def withdrawCash(self, amount):
        if amount > self.cash:
            print("You don't have enough cash in your account.")
        else:
            self.cash -= amount
            self.transaction.append(f'\t*You withdrew {} of dollars from your account.'.format(amount))

    def buyStock(self, number, stock):
        if self.cash > stock.price * int(number):
            stock.number_buy += int(number)
            self.stocks.append(stock)
            self.cash -= int(number) * stock.price
            self.transaction.append(f"\t*You buy {} {} stocks.".format(number,stock.stock_name))
        else:
            print("You don't have enough cash to buy this stock.")

    def sellStock(self, number, stock_name):
        price = random.uniform(0.5, 1.5)
        for stock in self.stocks:
            stock.number_buy -= int(number)
            self.cash += int(number) * price
            self.transaction.append(f"\t*You sell {} {} stock.".format(number, stock_name))

    def buyMutualFund(self, number, mf):
        if self.cash >= number * 1.0:
            mf.number_buy += number
            self.mutual_funds.append(mf)
            self.cash -= number * 1.0
            self.transaction.append(f"\t*You buy {} {} mutual funds.".format(number, mf.mfund_name))
        else:
            print("You don't have enough cash to buy this mutual fund")

    def sellMutualFund(self, number, mf):
        price = random.uniform(0.9, 1.2)
        for mf in self.mutual_funds:
            mf.number_buy -= number
            self.cash += number * price
            self.transaction.append(f"\t*You sell {} {} for {} dollars.".format(number, mf.mfund_name, number * price))

    def __str__(self):
        s = ""
        m = ""
        for stock in self.stocks:
            s += (f"{stock.number_buy} {stock.stock_name}")
        for mf in self.mutual_funds:
            m += (f"{mf.number_buy} {mf.mf_name}")
        return str(f"You have:\n\t *Cash: {self.cash} dollars\n\t *Stocks: {s} \n\t *Mutual Funds: {m}")

    def history(self):
        for hist_transaction in self.transaction:
            print(hist_transaction)

portfolio = Portfolio() #Creates a new portfolio
portfolio.addCash(300.50) #Adds cash to the portfolio
s = stock(20, "HFH") #Create Stock with price 20 and symbol "HFH"
portfolio.buyStock(5, s) #Buys 5 shares of stock s
mf1 = mf(0, "BRT") #Create MF with symbol "BRT"
mf2 = mf(0, "GHT") #Create MF with symbol "GHT"
portfolio.buyMutualFund(10.3, mf1) #Buys 10.3 shares of "BRT"
portfolio.buyMutualFund(2, mf2) #Buys 2 shares of "GHT"
print(portfolio) #Prints portfolio
portfolio.sellMutualFund(3, "BRT") #Sells 3 shares of BRT
portfolio.sellStock(1, "HFH") #Sells 1 share of HFH
portfolio.withdrawCash(50) #Removes $50
portfolio.history() #Prints a list of all transactions ordered by time

