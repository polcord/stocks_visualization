import plotly.graph_objects as go

def plot_stocks(data, buy_date, name):
    fig = go.Figure(data=[go.Candlestick(x=data.index,
                    open=data['Open'],
                    high=data['High'],
                    low=data['Low'],
                    close=data['Close'])])

    fig.add_shape(type="line",
        x0=buy_date, y0=0, x1=buy_date, y1=1,
        yref='paper', xref='x',
        line=dict(color="Green",width=1.5))

    fig.update_layout(title='Precio histórico ' + name,
                    xaxis_title='Fecha',
                    yaxis_title='Precio de cierre ($)')

    return fig