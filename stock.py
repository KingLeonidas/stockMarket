class Stock:
    def __init__(self, name,ticker,sector,originalPrice,numOfShares):
        self.name =name
        self.ticker=ticker
        self.sector =sector
        self.originalPrice = float(originalPrice)
        self.numOfShares =numOfShares
        self.currentPrice =float(originalPrice)
        self.gain=0

    def updatePrice(self,updatedValue):
        self.currentPrice =updatedValue
        self.gain = self.currentPrice - self.originalPrice