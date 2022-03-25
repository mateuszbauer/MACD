from MACD import MACD

class TradingSimulator:
    def __init__(self, macd, start_day, num_of_shares=1000):
        self.macd = macd
        self.start_day = start_day
        self.num_of_shares = num_of_shares
        self.wallet = 0
        self.current_day_index = self.get_day_index(self.start_day)
    
    def get_day_index(self, day):
        return self.macd.df.index[self.macd.df['Date'] == day].values[0]
    
    def get_current_share_value(self):
        return self.macd.stock_prices[self.current_day_index]

    def get_macd_value(self, day_index):
        return self.macd.macd[day_index]

    def get_signal_value(self, day_index):
        return self.macd.signal[day_index] 

    def print_status(self):
        print("Wallet: {}, Shares amout: {}".format(self.wallet, self.num_of_shares))

    def sell_shares(self, num_of_shares):
        if self.num_of_shares == 0:
            print("No shares left, cannot sell anymore")
        
        elif self.num_of_shares <= num_of_shares:
            self.wallet += self.num_of_shares * self.get_current_share_value() 
            print("Sold {} shares for {}".format(self.num_of_shares, self.num_of_shares * self.get_current_share_value()))
            self.num_of_shares = 0
            print("All the shares have been sold")
        
        else:
            self.wallet += num_of_shares * self.get_current_share_value()
            self.num_of_shares -= num_of_shares
            print("Sold {} shares for {}".format(num_of_shares, self.get_current_share_value()))

        self.print_status()

    def buy_shares(self, num_of_shares):
        if self.wallet == 0:
            print("No money left, cannot buy anymore")

        else:
            price = num_of_shares * self.get_current_share_value()

            if price >= self.wallet:
                amout_to_buy = int(price // self.wallet)
                self.num_of_shares += amout_to_buy
                self.wallet -= amout_to_buy * self.get_current_share_value()
                print("Bought {} shares for {}".format(amout_to_buy, amout_to_buy * self.get_current_share_value()))
        
            else:
                self.num_of_shares += num_of_shares
                self.wallet -= price
                print("Bought {} shares for {}".format(num_of_shares, price))

        self.print_status()

    # Main function of the class
    # if MACD line crosses SIGNAL line from the bottom - buy
    # if MACD line crosses SIGNAL line from the top - sell
    def trade(self, period):
        print("Starting trading")
        initial_wealth = self.wallet + self.num_of_shares * self.get_current_share_value()
        self.print_status()
        while period > 0:
            prev_macd, curr_macd = self.get_macd_value(self.current_day_index+1), self.get_macd_value(self.current_day_index) 
            prev_signal, curr_signal = self.get_signal_value(self.current_day_index+1), self.get_signal_value(self.current_day_index) 

            if prev_macd < prev_signal and curr_macd >= curr_signal:
                print("MACD crosses SIGNAL from the bottom - BUY")
                self.buy_shares(int(self.num_of_shares * 0.25))
           
            elif prev_macd > prev_signal and curr_macd <= curr_signal:
                print("MACD crosses SIGNAL from the top - SELL")
                self.sell_shares(int(self.num_of_shares * 0.25))

            period -= 1
            self.current_day_index -= 1

        self.print_status()
        wealth_after_trading = self.wallet + self.num_of_shares * self.get_current_share_value()
        print("Initial wealth = {}, Current wealth = {}".format(initial_wealth, wealth_after_trading))
        print("approximate profit = {}".format(wealth_after_trading - initial_wealth))

