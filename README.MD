# Chart Scraper

Python module that scrapes tradingview charts when appropriate inputs are given.

## Installation

Install chartscraper

```bash
  pip install chartsnap
```


## Requirements

    1. Selenium Web driver for chrome
You can download the latest version from [here](https://chromedriver.chromium.org/downloads).

## Usage/Examples
```
from chartsnap import get_chart
ticker='SBIN'
time_interval = '1d'
time_period = '6M'
chart_location = 'location/of/the/folder/to/store/charts'
get_chart(ticker,time_interval,time_period,chart_location)
```
All the values are required.