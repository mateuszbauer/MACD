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
        
    def calculate_ema(self, arr, n):
        alpha = 2 / (n+1)
        ema = np.zeros(len(arr))
        
        for index in range(0, len(arr)):
            # (1, n+1) matrix with values from current and n previous days
            # if there's no data from previous days, fill with zeros
            values = np.array([arr[index:index+n+1]])    
            values = np.array([np.append(values, [[0] * (n-values.size+1)])])
            
            # (n+1, 1) matrix with weights
            # w[i] = (1-alpha)^i, i <- 0..n+1
            weights = np.array([[(1.0-alpha)**i] for i in range(n+1)])
            
            ema[index] = (np.matmul(values, weights).item() / weights.sum())
            
        return ema
    
    def plot_data(self):
        plt.plot(self.df.Date, self.stock_prices, color='black', label='Stock value')
        plt.plot(self.df.Date, self.macd, color='blue', label='MACD')
        plt.plot(self.df.Date, self.signal, color='red', label='Signal Line')
        plt.legend(loc='upper left')
        plt.show()
 
               
def main():
    assert len(sys.argv) > 1, 'Path to data file was not provided'
    
    macd = MACD(sys.argv[1])
    macd.plot_data()


if __name__ == '__main__':
    main()
