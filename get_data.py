import yfinance as yf
from datetime import datetime
import pandas as pd

def get_data(symbol):
    
    # Obtén la fecha de hoy
    hoy = datetime.today().strftime('%Y-%m-%d')

    # Descarga los datos históricos de la acción desde el 1 de enero de 2020 hasta hoy
    data = yf.download(symbol, start='2020-01-01', end=hoy)

    return data

def save_excel(stock_name):
    
    data = get_data(stock_name)

    # Escribir hoja de Excel
    writer = pd.ExcelWriter('price_evolution.xlsx', engine='openpyxl')
    data.to_excel(writer, sheet_name=stock_name, index=True)
    writer.close()

