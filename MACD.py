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
            values = np.array([arr[index:index+n+1]])    
            
            # (n+1, 1) matrix with weights
            # w[i] = (1-alpha)^i, i <- 0..n+1
            weights = np.array([[(1.0-alpha)**i] for i in range(values.size)])
            
            ema[index] = (np.matmul(values, weights).item() / weights.sum())
            
        return ema
    
    def plot_data(self, period):
        fig, axs = plt.subplots(2)
        axs[0].plot(self.df.Date[0:period], self.stock_prices[0:period], color='black', label='Stock value')
        axs[1].plot(self.df.Date[0:period], self.macd[0:period], color='blue', label='MACD')
        axs[1].plot(self.df.Date[0:period], self.signal[0:period], color='red', label='Signal Line')
        axs[0].legend(loc='upper left')
        axs[1].legend(loc='upper left')
        plt.show()
 
               
def main():
    assert len(sys.argv) > 1, 'Path to data file was not provided'
    
    macd = MACD(sys.argv[1])

    if len(sys.argv) > 2:    
        macd.plot_data(int(sys.argv[2]))

    else:
        macd.plot_data(len(macd.df))




if __name__ == '__main__':
    main()
