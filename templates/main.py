import pandas as pd
import requests
from matplotlib import pyplot as plt


def main():
    # j = requests.get('https://iss.moex.com/iss/securities.json').json()
    # data = [{k : r[i] for i, k in enumerate(j['securities']['columns'])} for r in j['securities']['data']]
    # print(pd.DataFrame(data))

    # j = requests.get('https://iss.moex.com/iss/securities/YNDX/aggregates.json?date=2022-09-21').json()
    # data = [{k : r[i] for i, k in enumerate(j['aggregates']['columns'])} for r in j['aggregates']['data']]
    # print(pd.DataFrame(data))

    j = requests.get('http://iss.moex.com/iss/engines/stock/markets/shares/securities/YNDX/candles.json?from=2023-05-25&till=2023-09-01&interval=24').json()
    data = [{k : r[i] for i, k in enumerate(j['candles']['columns'])} for r in j['candles']['data']]
    frame = pd.DataFrame(data)
    plt.plot(list(frame['close']))
    plt.savefig("shares.png")

if __name__ == '__main__':
    # try:
    main()
    # except:
        # print "Sorry:", sys.exc_type, ":", sys.exc_value