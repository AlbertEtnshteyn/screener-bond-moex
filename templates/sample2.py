import requests

import apimoex
import pandas as pd


request_url = ('https://iss.moex.com/iss/engines/stock/'
               'markets/shares/boards/TQBR/securities.json')
arguments = {'securities.columns': ('SECID,'
                                    'REGNUMBER,'
                                    'LOTSIZE,'
                                    'SHORTNAME')}
with requests.Session() as session:
    iss = apimoex.ISSClient(session, request_url, arguments)
    data = iss.get()
    df = pd.DataFrame(data['securities'])
    df.set_index('SECID', inplace=True)
    print(df.head(), '\n')
    print(df.tail(), '\n')
    df.info()