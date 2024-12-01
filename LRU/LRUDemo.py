from LRU import LRU

class LRUDemo:
    @staticmethod
    def run():
        lruCache = LRU(3)
        
        lruCache.putValue(3, "Hi")
        lruCache.putValue(2, "Bi")
        lruCache.putValue(1,"My")
        
        print(lruCache.getValue(2))
        
        lruCache.putValue(4, "Hello")
        
        print(lruCache.getValue(2))

if __name__=="__main__":
    LRUDemo.run()