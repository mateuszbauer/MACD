from simulation import TradingSimulator
from MACD import MACD
import sys


assert len(sys.argv) > 1, 'Path to data file was not provided'
bot = TradingSimulator(MACD(sys.argv[1]), '08/16/2017')


bot.trade(1000)

