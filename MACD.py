import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys

class MACD:
    def __init__(self, path_to_data_file):
        self.df = pd.read_csv(path_to_data_file)
        self.df.Date = pd.to_datetime(self.df.Date)
        self.stock_prices = self.df.Close.to_numpy()
        self.macd = self.calculate_ema(self.stock_prices, 12) - self.calculate_ema(self.stock_prices, 26)
        self.signal = self.calculate_ema(self.macd, 9)
        
    def calculate_ema(self, arr, period):
        alpha = 2 / (period+1)
        ema = np.zeros(len(arr))
        
        for index in range(0, len(arr)):
            prev_values = []
            i = 0
            while i <= period and index+i < len(arr):
                prev_values.append(arr[index+i])
                i += 1             
            
            ema[index] = (
                  sum([x * (1.0-alpha)**i for i, x in enumerate(prev_values)])
                / sum([(1.0-alpha)**i for i in range(0, len(prev_values))])
            )
            
        return ema
    
    def plot_data(self):
        plt.plot(self.df.Date, self.stock_prices, color='black', label='Stock value')
        plt.plot(self.df.Date, self.macd, color='blue', label='MACD')
        plt.plot(self.df.Date, self.signal, color='red', label='Signal Line')
        plt.legend(loc='upper left')
        plt.show()
 
               
def main():
    macd = MACD(sys.argv[1])
    macd.plot_data()


if __name__ == '__main__':
    main()
