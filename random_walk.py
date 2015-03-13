import pylab, random

class Stock(object):
    def __init__(self, price, distribution, vol):
        self.price = price
        self.history = [price]
        self.distribution = distribution
        self.vol = vol
        self.lastChangeInfluence = 0.0

    def setPrice(self, price):
        self.price = price
        self.history.append(price)

    def getPrice(self):
        return self.price
        
    def makeMove(self, bias, mo):
        oldPrice = self.price
        baseMove = self.distribution(self.vol) + bias
        self.price = self.price * (1.0 + baseMove)
        self.price += mo*random.choice([0.0, 1.0])*self.lastChangeInfluence
        self.history.append(self.price)
        change = self.price - oldPrice
        if change >= 0:
            self.lastChangeInfluence = min(change, oldPrice*0.01)
        else:
            self.lastChangeInfluence = max(change, -oldPrice*0.01)
    def showHistory(self, fig, test):
        pylab.figure(fig)
        pylab.plot(self.history)
        pylab.title('Closing Prices, Test ' + test)
        pylab.xlabel('Day')
        pylab.ylabel('Price')

class SimpleMarket(object):
    def __init__(self, numStks, volUB, price):
        self.stks = []
        self.bias = 0.0
        for n in range(numStks):
            volatility = random.uniform(0, volUB)
            distribution = lambda vol: random.gauss(0.0, vol)
            stk = Stock(price, distribution, volatility)
            self.addStock(stk)
    def addStock(self, stk):
        self.stks.append(stk)
    def setBias(self, bias):
        self.bias = bias
    def getBias(self):
        return self.bias
    def getStocks(self):
        return self.stks[:]
    def move(self, mo):
        prices = []
        for s in self.stks:
            s.makeMove(self.bias, mo)
            prices.append(s.getPrice())
        return prices

class Market(SimpleMarket):
    def __init__(self, numStks, volUB, dailyBiasRange, price):
        SimpleMarket.__init__(self, numStks, volUB, price)
        self.dailyBiasRange = dailyBiasRange
    def move(self, mo):
        prices = []
        dailyBias = random.gauss(self.dailyBiasRange[0], self.dailyBiasRange[1])
        for s in self.stks:
            s.makeMove(self.bias + dailyBias, mo)
            prices.append(s.getPrice())
        return prices

def simMkt(mkt, numDays, mo):
    endPrices = []
    for i in range(numDays):
        vals = mkt.move(mo)
        vals = pylab.array(vals)
        mean = vals.sum()/float(len(vals))
        endPrices.append(mean)
    return endPrices

def plotAverageOverTime(endPrices, title):
    pylab.plot(endPrices)
    pylab.title(title)
    pylab.xlabel('Days')
    pylab.ylabel('Price')

def plotDistributionAtEnd(mkt, title, color):
    prices = []
    sumSoFar = 0
    for s in mkt.getStocks():
        prices.append(s.getPrice())
        sumSoFar += s.getPrice()
    mean = sumSoFar/float(len(prices))
    prices.sort()
    pylab.plot(prices, color)
    pylab.axhline(mean, color = color)
    pylab.title(title)
    pylab.xlabel('Stock')
    pylab.ylabel('Last Sale')
    pylab.semilogy()

def runTrial(showHistory, test, p):
    colors = ['b','g','r','c','m','y','k']

    mkt = Market(p['numStocks'], p['volUB'], p['dailyBiasRange'], p['price'])
    mkt.setBias(p['bias'])
    endPrices = simMkt(mkt, p['numDays'], p['mo'])
    pylab.figure(1)
    plotAverageOverTime(endPrices, 'Average Closing Prices')
    pylab.figure(2)
    plotDistributionAtEnd(mkt, 'Distribution of Prices', colors[test%len(colors)])
    if showHistory:
        for s in mkt.getStocks():
            s.showHistory(test+2, str(test))

def runTest(numTrials, numDaysPerYear, numDays, numStocks, price, genMktBias=0.1):

    #Constants used in testing
    if numTrials <= 0:
        raise ValueError("Number of trials cannot be zero or negative")
    elif numStocks <= 0:
        raise ValueError("Stocks cannot be zero or negative")
    elif price <= 0:
        raise ValueError("Price cannot be zero or negative")
    elif not (0.0 < numDaysPerYear <= 365.0):
        raise ValueError("Number of days per year should be more than zero and less than 366")
    elif numDays <= 0:
        raise ValueError("Number of days cannot be zero or negative")
    elif not (0.0 < genMktBias < 1.0):
        raise ValueError("Bias should be greater than 0.0 and less than 1.0")

    elif type(numTrials) == str:
        raise TypeError("Trials cannot be string")
    elif type(numStocks) == str:
        raise TypeError("Stocks cannot be string")
    elif type(price) == str:
        raise TypeError("Prices cannot be string")
    elif type(numDaysPerYear) == str:
        raise TypeError("Number of days per year cannot be string")
    elif type(numDays) == str:
        raise TypeError("Number of days cannot be string")
    elif type(genMktBias) == str:
        raise TypeError("Bias cannot be string")

    elif type(numTrials) == float:
        raise TypeError("Number of trials should be an integer, float given")
    elif type(numDays) == float:
        raise TypeError("Number of days should be an integer, float given")
    elif type(numStocks) == float:
        raise TypeError("Number of stocks should be an integer, float given")


    elif type(numTrials) == dict:
        raise TypeError("Number of trials should be an integer, dictionary given")
    elif type(price) == dict:
        raise TypeError("Number of trials should be an integer, dictionary given")
    elif type(numDaysPerYear) == dict:
        raise TypeError("Number of trials should be an integer, dictionary given")
    elif type(numDays) == dict:
        raise TypeError("Number of trials should be an integer, dictionary given")
    elif type(numStocks) == dict:
        raise TypeError("Number of trials should be an integer, dictionary given")
    elif type(genMktBias) == dict:
        raise TypeError("Bias should be a float, dictionary given")

    elif type(numTrials) == list:
        raise TypeError("Number of trials should be an integer, list given")
    elif type(price) == list:
        raise TypeError("Number of trials should be an integer, list given")
    elif type(numDaysPerYear) == list:
        raise TypeError("Number of trials should be an integer, list given")
    elif type(numDays) == list:
        raise TypeError("Number of trials should be an integer, list given")
    elif type(numStocks) == list:
        raise TypeError("Number of trials should be an integer, list given")
    elif type(genMktBias) == list:
        raise TypeError("Bias should be a float, list given")

    elif type(numTrials) == tuple:
        raise TypeError("Number of trials should be an integer, tuple given")
    elif type(price) == tuple:
        raise TypeError("Number of trials should be an integer, tuple given")
    elif type(numDaysPerYear) == tuple:
        raise TypeError("Number of trials should be an integer, tuple given")
    elif type(numDays) == tuple:
        raise TypeError("Number of trials should be an integer, tuple given")
    elif type(numStocks) == tuple:
        raise TypeError("Number of trials should be an integer, tuple given")
    elif type(genMktBias) == tuple:
        raise TypeError("Bias should be a float, tuple given")
    else:
        params = {}
        params['price'] = price
        params['numDays'] = numDays
        params['numStocks'] = numStocks
        params['bias'] = genMktBias/numDaysPerYear #General market bias
        params['volUB'] = 12.0/numDaysPerYear #Upper bound on volatility for a stock
        params['mo'] = 1.1/numDaysPerYear #Momentum factor
        params['dailyBiasRange'] = (0.0, 4.0/numDaysPerYear)

        for t in range(1, numTrials+1):
            runTrial(True, t, params)
        return True

# runTest(3)
# pylab.show()