import yfinance as yf
from datetime import datetime
import pandas as pd

def get_info(symbol, start_date):
    
    # Obtén la fecha de hoy
    hoy = datetime.today().strftime('%Y-%m-%d')

    # Descarga los datos históricos de la acción una fecha de inicio delimitada hasta hoy
    data = yf.download(symbol, start=start_date, end=hoy)

    return data


def save_excel(stock_name, start_date):
    
    data = get_info(stock_name, start_date)

    # Escribir hoja de Excel
    writer = pd.ExcelWriter('price_evolution.xlsx', engine='openpyxl')
    data.to_excel(writer, sheet_name=stock_name, index=True)
    writer.close()

