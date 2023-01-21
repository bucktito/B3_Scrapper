# WebS 
import requests
from bs4 import BeautifulSoup
import pandas as pd

start_date = 2013
end_date = 2014
base = "USD"

fx = pd.DataFrame()

# https://freecurrencyrates.com/en/exchange-rate-history/

months = {"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5, "Jun":6, "Jul":7, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12}
country_list_usd = [["Country", "USD"],["Brazil","BRL"],["South Africa", "ZAR"],["Australia", "AUD"], ["Argentina","ARS"], ["Canada", "CAD"], ["Chile", "CLP"], ["China", "CNY"], ["Euro", "EUR"], ["Great-Britain", "GBP"] ,["Japan", "JPY"], ["Mexico", "MXN"], ["Norway", "NOK"], ["New Zealand", "NZD"], ["Russia", "RUB"], ["Sweden" ,"SEK"], ["Swiss", "CHF"], ["Turkey", "TRY"]] # Lista de moedas por ticker (base: USD)
tickers_list = [l[1] for l in country_list_usd]

for currency in tickers_list:
    fx_r = []
    fx_d = []
    for anos_count in range(0, end_date-start_date+1):
        data_ano = str(end_date - anos_count)
        url_c = "https://freecurrencyrates.com/en/exchange-rate-history/"+base+"-"+currency+"/"+data_ano +"/yahoo" # "/cbr" ou "/yahoo"
        page = requests.get(url_c)
        soup_c = BeautifulSoup(page.content, 'html.parser')

        layer_r= soup_c.find_all(class_="one-month-data-rate")
        layer_d = soup_c.find_all(class_="one-month-data-date")
        ll = [layer_r, layer_d]

        for i in range(len(ll[:][0])):
            d_d = layer_d[i].get_text()
            month = str(months[d_d[0:3]])
            data_date_fltr = str(int(d_d[-2:])) +"/" + month + "/" + data_ano
            fx_r += [float(layer_r[i].get_text())]
            fx_d += [data_date_fltr]

    forex = pd.DataFrame([fx_d[::-1], fx_r[::-1]]).T
    forex.columns = ["Data", base+"/"+currency]
    forex.set_index("Data", inplace = True)
    fx = pd.concat([fx, forex], axis=1)






