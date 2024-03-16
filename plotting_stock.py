import plotly.graph_objects as go
from get_data import get_data

data = get_data('AAPL')

# Crea un gráfico de los precios de cierre
fig = go.Figure(data=[go.Candlestick(x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'])])

fig.add_shape(type="line",
    x0="2024-03-15", y0=0, x1="2024-03-15", y1=1,
    yref='paper', xref='x',
    line=dict(color="Blue",width=1.5))

fig.update_layout(title='Precio histórico de la acción de Apple',
                   xaxis_title='Fecha',
                   yaxis_title='Precio de cierre ($)')

fig.show()