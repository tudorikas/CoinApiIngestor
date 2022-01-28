import datetime
import cryptocompare

class CryptoCompare:
    def __init__(self):
        cryptocompare.cryptocompare._set_api_key_parameter(
            "bbbba9d00f44ca207ddac90c6f8370413b2572e2ddedff28fc5a72c4a3c6af34")
        self.count_file = open("coinList.txt", "a")

    def register_call(self,text):
        self.count_file.write(text + "\n")

    def get_historical_price_day(self,coin,currency,limit,exchange):
        self.register_call("get_historical_price_day "+coin+" "+currency+" "+str(limit)+" "+str(datetime.datetime.now))
        return cryptocompare.get_historical_price_day(coin, currency, limit, exchange)

    def get_historical_price_day_toTs(self, coin, currency, limit, exchange, toTs):
        self.register_call("get_historical_price_day_toTs "+coin + " " + currency + " " + str(limit) + " " + str(toTs))
        return cryptocompare.get_historical_price_day(coin, currency, limit, exchange,toTs)

    def get_coin_list(self,format):
        self.register_call("get_coin_list "+str(datetime.datetime.now))
        return cryptocompare.get_coin_list(format)

    def get_historical_price(self,coin,currency,timestamp):
        self.register_call("get_historical_price " + str(datetime.datetime.now) +" "+coin)
        return cryptocompare.get_historical_price(coin, currency, timestamp)