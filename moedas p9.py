import requests
import datetime as dt
import pandas as pd

country_list_usd = [["Country", "USD"],["Brazil",""],["South Africa", "ZAR"],["Australia", "AUD"], ["Argentina","ARS"], ["Canada", "CAD"], ["Chile", "CLP"], ["China", "CNY"], ["Euro", "EUR"], ["Great-Britain", "GBP"] ,["Japan", "JPY"], ["Mexico", "MXN"], ["Norway", "NOK"], ["New Zealand", "NZD"], ["Russia", "RUB"], ["Sweden" ,"SEK"], ["Swiss", "CHF"], ["Turkey", "TRY"]] #YF
country_list_brl = [["Country", "BRL"],["USA",""],["South Africa", "ZAR"],["Australia", "AUD"], ["Argentina","ARB"], ["Canada", "CAD"], ["Chile", "CLP"], ["China", "CNH"], ["Euro", "EUR"], ["Great-Britain", "GBP"] ,["Japan", "JPY"], ["Mexico", "MXN"], ["Norway", "NOK"], ["New Zealand", "NZL"], ["Russia", "RUB"], ["Sweden" ,"SEK"], ["Swiss", "CHF"], ["Turkey", "TRY"]] #YF
hist_m = [[]]

start_d = "2018-01-01"
end_d = "2022-12-31"
base = "USD"
#
period_y = int((end_d.split("-")[0])) - int((start_d.split("-")[0]))
tickers_list = [x for l in country_list_usd for x in l if len(x)==3]

for tick in tickers_list:
    hist_data = {x: None for x in tickers_list}
    data_c = {}
    for t in range(0,period_y+1):
        strt = start_d.split("-")

        if t == period_y:
            s_data = "-".join([str(int(strt[0]) + t), strt[1], strt[2]])
            e_data = end_d
        else:
            s_data = "-".join([str(int(strt[0]) + t), strt[1], strt[2]])
            e_data = "-".join([str(int(strt[0]) + t+1), strt[1], strt[2]])

        url = 'https://api.exchangerate.host/timeseries?start_date=' + s_data + "&end_date="+e_data+"&base="+base+"&symbols="+tick
        response = requests.get(url)
        data = response.json()
        data_c = data_c|data['rates']
    hist_data[str(tick)] = data_c
tab=pd.DataFrame(hist_data)



