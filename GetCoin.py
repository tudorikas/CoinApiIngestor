import datetime

from CryptoCompare import CryptoCompare


class GetCoin:
    def __init__(self):
        self.cryptocompare = CryptoCompare()

    def get_date(self,unix):
        print(datetime.datetime.utcfromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
        time = datetime.datetime.utcfromtimestamp(unix)
        return [time.year, time.month, time.day]

    def get_disponible_coin(self):
        coin_list = self.cryptocompare.get_coin_list(format=True)
        textfile = open("coinList.txt", "w")
        for element in coin_list:
            textfile.write(element + "\n")
        textfile.close()

    def get_coin_all_data(self,coin):
        listCoin = self.cryptocompare.get_historical_price_day(coin, 'USD', limit=2000, exchange='CCCAGG')
        lastdate = listCoin[0]['time']

        while True:
            [year, month, day] = self.get_date(lastdate)

            resp = self.cryptocompare.get_historical_price_day_toTs('BTC', 'USD', limit=2000, exchange='CCCAGG',
                                                          toTs=datetime.datetime(year, month, day, 12))
            listCoin.extend(resp)

            if len(resp) == 0:
                break
            if year < 2009:
                break
            lastdate = resp[0]['time']


        return listCoin

    def get_historical_price(self,coin):
        return self.cryptocompare.get_historical_price(coin, 'USD', datetime.datetime(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day))

