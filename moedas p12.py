import requests
import datetime as dt
import pandas as pd

country_list_usd = [["Country", "USD"],["Brazil",""],["South Africa", "ZAR"],["Australia", "AUD"], ["Argentina","ARS"], ["Canada", "CAD"], ["Chile", "CLP"], ["China", "CNY"], ["Euro", "EUR"], ["Great-Britain", "GBP"] ,["Japan", "JPY"], ["Mexico", "MXN"], ["Norway", "NOK"], ["New Zealand", "NZD"], ["Russia", "RUB"], ["Sweden" ,"SEK"], ["Swiss", "CHF"], ["Turkey", "TRY"]] # Lista de moedas por ticker (base: BRL)
country_list_brl = [["Country", "BRL"],["USA",""],["South Africa", "ZAR"],["Australia", "AUD"], ["Argentina","ARB"], ["Canada", "CAD"], ["Chile", "CLP"], ["China", "CNH"], ["Euro", "EUR"], ["Great-Britain", "GBP"] ,["Japan", "JPY"], ["Mexico", "MXN"], ["Norway", "NOK"], ["New Zealand", "NZL"], ["Russia", "RUB"], ["Sweden" ,"SEK"], ["Swiss", "CHF"], ["Turkey", "TRY"]]  # Lista de moedas por ticker (base: USD)

#) 
start_d = "2005-01-01"      # Start Date
end_d = "2005-12-31"        # End Date
base = "USD"                # Moeda Base
#)

period_y = int((end_d.split("-")[0])) - int((start_d.split("-")[0]))    # Período em anos
tickers_list = [x for l in country_list_usd for x in l if len(x)==3]    # Lista de Tickers
hist_data = pd.DataFrame()

for tick in tickers_list:   # [Loop tickers]
    data_c = {}
    col = 0
    for t in range(0,period_y+1):   # [Loop anos]
        strt = start_d.split("-")   # Separar da string da data o ano e assim aumentar o ano à cada loop

        if t == period_y:   # Faltando menos de um ano
            s_data = "-".join([str(int(strt[0]) + t), strt[1], strt[2]])    # Data inicio loop (quando tem menos de um ano faltando)
            e_data = end_d                                                  # Data final loop (quando tem menos de um ano faltando)
        else:               # Faltando mais de um ano
            s_data = "-".join([str(int(strt[0]) + t), strt[1], strt[2]])    # Data inicio loop (quando tem mais de um ano faltando)
            e_data = "-".join([str(int(strt[0]) + t+1), strt[1], strt[2]])  # Data final loop (quando tem mais de um ano faltando)

        url = 'https://api.exchangerate.host/timeseries?start_date=' + s_data + "&end_date="+e_data+"&base="+base+"&symbols="+tick # URL
        response = requests.get(url)
        data = response.json()
        data_c = data_c|data['rates']                           # Extrair apenas as taxas
    hist_data.insert(col, column = tick,  value = [list(x.values())[0] if list(x.values())[0]!=1 else pd.NA for x in list(data_c.values())]) # Agregar com as outras datas rodadas (anos)
    col+=1
    
tab = pd.DataFrame(hist_data)   # Tornar um DataFrame
tab.index = data_c.keys()       # Definir Datas como Índices








