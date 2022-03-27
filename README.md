# MACD

**MACD** (Moving Average Convergence/Divergence) is a trading indicator used in analysis of stock prices. It is designed to reveal changes in the strength, direction, momentum and duration of a trend in a stock's price.


## Usage
__MACD.py__
```sh
python3 MACD.py <path-to-csv-file> <period>
```
__path-to-csv-file__ is mandatory. Examples of a .csv file contaning data are inside **sample_data** directory.
__period__ is optional. By default it will display all data, but it is possible to specify number of days that should be displayed on a chart.
**Example**:
```sh
python3 MACD.py my-data-file.csv 30
```
will display stock value, MACD and SIGNAL line for the last 30 days.

__simulation.py__
Contains an implementation of a simple bot that buys/sells stocks according to MACD and SIGNAL line.

__main.py__

```sh
python3 main.py <path-to-csv-file> <starting-date> <period>
```
**path-to-csv-file** is mandatory. Examples of a .csv file contaning data are inside **sample_data** directory.
**starting-date** is mandatory. Its format is MM/DD/YYYY.
**period** is optional. By default it will do its job for 1000 days.
**Example**:
```sh
python3 main.py my-data-file.csv 08/01/2017 50
```
Will place the bot on 1 Aug 2017 and it's going to trade for the next 50 days.
It will display output to stdout.
