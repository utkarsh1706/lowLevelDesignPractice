class WatchList:
    def __init__(self, user) -> None:
        self.user = user
        self.watchlist = []

    def addtowatchlist(self, asset):
        if asset not in self.watchlist:
            self.watchlist.append(asset)
        else:
            print("Asset already Added!")

    def removeFromWatchList(self, asset):
        if asset not in self.watchlist:
            raise ValueError("Asset not present in watchlist")
        self.watchlist.remove(asset)
        return
    
    def getWatchlistData(self):
        watchList = {}
        for w in self.watchlist:
            p = w.getPrice()
            name = w.getName()
            watchList[name] = p
        return watchList
