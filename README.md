### MACD
Short for moving average convergence/divergence - a trading indicator used in analysis of stock prices



$$ EMA _N = \frac{p_0 + (1-\alpha)p_1 + (1-\alpha)^2p_2 + \... +(1-\alpha)^Np_N}
{1 + (1-\alpha) + (1-\alpha)^2 + \... + (1-\alpha)^N} $$

where:
$$ p_0 $$  - today's price
$$ p_i $$  - price from i-th day
$$ p_N $$- price N days ago
$$ \alpha  = \frac{2}{N+1}$$
$$ N $$ - time period [days]

***MACD = EMA<sub>12</sub> - EMA<sub>26</sub>***
***SIGNAL = EMA<sub>9</sub> of the MACD series***

Cross points of MACD and SIGNAL determine best moments to buy/sell shares (with a profit in mind)

### Usage
run MACD.py from the command line
~$ python3 MACD.py [path_to_csv_file]
Note: matplotlib, pandas and numpy modules are required

in the 'sample_data' directory you can find \*.csv file containing data