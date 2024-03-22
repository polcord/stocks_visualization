import streamlit as st
from get_data import get_info
from get_data import save_excel
from plotting_stock import plot_stocks

# Definir fecha de inicio histórico
fecha_inicio = '2021-01-01'

# Acciones y fechas de compras que quieres graficar
stock_dict = {'BTC-USD': '2024-03-14', 'SMH': '2024-03-14', 'AAPL': '2024-03-15'}

def main():
    st.title('Gráficos de activos financieros')

    for activo, fecha_compra in stock_dict.items():
        
        # Descargar los datos de la acción
        data = get_info(activo, fecha_inicio)
        
        # Mostrar precios de compra y reciente
        col1, col2 = st.columns(2)
        with col1:
            buying_price = data.loc[fecha_compra, 'Close'].round(2).item()
            st.metric(label=f"Buying Price ({fecha_compra})", value=f"${buying_price}")

        with col2:
            last_date = data.index[-1].strftime('%Y-%m-%d')
            last_value = data["Close"].iloc[-1].round(2).item()
            variation = round((last_value - buying_price) / buying_price * 100, 2)
            st.metric(label=f"Recent Price ({last_date})", value=f"${last_value}", delta=f"{variation} %")

        # Crear el gráfico
        figura = plot_stocks(data, fecha_compra, activo)

        # Mostrar el gráfico en Streamlit
        st.plotly_chart(figura)

if __name__ == "__main__":
    main()
