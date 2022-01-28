import datetime

def get_date(unix):
    print(datetime.datetime.utcfromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    time=datetime.datetime.utcfromtimestamp(unix)
    return [time.year,time.month,time.day]

##read file
def red_file():
    with open("Coins.txt","r") as file:
        readline = file.read().splitlines()
        return readline




