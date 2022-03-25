from simulation import TradingSimulator
from MACD import MACD
import sys


bot = TradingSimulator(MACD(sys.argv[1]), "10/09/2020")


bot.trade(365)
