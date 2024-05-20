
from sktime.forecasting.model_selection import temporal_train_test_split
from sktime.forecasting.naive import NaiveForecaster
from sktime.performance_metrics.forecasting import mean_absolute_percentage_error as smape_loss
from get_data import get_info
import pandas as pd

fecha_inicio = '2021-01-01'
df = get_info('BTC-USD', fecha_inicio)
df_serie = df.loc[:, 'Close']
# print(df_serie)
# Cargar los datos

# Asegúrate de tener un archivo CSV con los datos históricos del precio de Bitcoin
# df = pd.read_csv('bitcoin_price.csv', index_col=0, parse_dates=True)

# Dividir los datos en conjuntos de entrenamiento y prueba
y_train, y_test = temporal_train_test_split(df_serie, test_size=0.70)
# print(y_train)


# Crear y ajustar el modelo de pronóstico
forecaster = NaiveForecaster(strategy="last")
forecaster.fit(y_train)

# Realizar el pronóstico
y_pred = forecaster.predict(fh=range(1, len(y_test) + 1))
# print(y_pred)


# Calcular el error de pronóstico
error = smape_loss(y_test, y_pred)
print(f'Error de pronóstico: {error}')




import matplotlib.pyplot as plt

# Crear un DataFrame para las predicciones
y_pred = y_pred.rename('Prediction')
print(y_pred)
# Concatenar las series original y de predicciones
df_total = pd.concat([df, y_pred], axis=1)
print(df_total)
# Graficar las series
plt.figure(figsize=(10,6))
plt.plot(df_total.index, df_total['Close'], label='Original')
plt.plot(df_total.index, df_total['Prediction'], label='Predicciones')
plt.title('Precio de Bitcoin: Original vs Predicciones')
plt.xlabel('Fecha')
plt.ylabel('Precio')
plt.legend()
plt.show()
