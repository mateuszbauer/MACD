from simulation import TradingSimulator
from MACD import MACD
import sys


assert len(sys.argv) > 2 
bot = TradingSimulator(MACD(sys.argv[1]), sys.argv[2])

if len(sys.argv) > 3:
    bot.trade(int(sys.argv[3]))

else:
    bot.trade()

