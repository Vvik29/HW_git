pricesUSD=[100.34,35,67.99,25.5, 99.99]

def toPriceNew(priceList) :
    return list(map(lambda x: x * 37.45, priceList))
print("Prices without discount:")
print(toPriceNew(pricesUSD))

def decoratorWrapper(valueForDec):

    def Decorator (myFunction):

        def Wrapper (*args, **kwargs):
            result = myFunction(*args, **kwargs)
            discount = list(map((lambda x: x-(x*valueForDec)), result))
            return discount

        return Wrapper

    return Decorator

decoratorWithValue = decoratorWrapper(0.15)

toPriceNew = decoratorWithValue(toPriceNew)
print("Prices after discount of 15%:")
print(toPriceNew(pricesUSD))