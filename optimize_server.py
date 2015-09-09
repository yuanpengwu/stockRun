import itertools
from pyalgotrade.optimizer import local
import rsi2
from pyalgotrade.barfeed import yahoofeed
from pyalgotrade.optimizer import server


def parameters_generator():
    instrument = ["skyw"]
    entrySMA = range(150, 251)
    exitSMA = range(5, 16)
    rsiPeriod = range(2, 11)
    overBoughtThreshold = range(75, 96)
    overSoldThreshold = range(5, 26)
    return itertools.product(instrument, entrySMA, exitSMA, rsiPeriod, overBoughtThreshold, overSoldThreshold)

# The if __name__ == '__main__' part is necessary if running on Windows.
if __name__ == '__main__':
    # Load the feed from the CSV files.
    feed = yahoofeed.Feed()
    feed.addBarsFromCSV("skyw", "database/skyw-2009-yahoofinance.csv")
    feed.addBarsFromCSV("skyw", "database/skyw-2010-yahoofinance.csv")
    feed.addBarsFromCSV("skyw", "database/skyw-2011-yahoofinance.csv")
    feed.addBarsFromCSV("skyw", "database/skyw-2012-yahoofinance.csv") 
    feed.addBarsFromCSV("skyw", "database/skyw-2013-yahoofinance.csv")
    feed.addBarsFromCSV("skyw", "database/skyw-2014-yahoofinance.csv")

    # Run the server.
    #server.serve(feed, parameters_generator(), "localhost", 5000)
    local.run(rsi2.RSI2, feed, parameters_generator())
