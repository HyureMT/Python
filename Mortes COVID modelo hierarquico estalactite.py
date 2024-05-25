import pandas as pd
import matplotlib.pyplot as plt

# Dados reais de mortes por COVID-19 por país
mortes_covid = {
    'País': ['EUA', 'Brasil', 'Índia', 'Rússia', 'México'],
    'Mortes': [1012833, 672033, 525242, 373595, 325793]
}

# Gráfico de estalactite para mortes por COVID-19 por país
plt.figure(figsize=(8, 6))
plt.barh(mortes_covid['País'], mortes_covid['Mortes'])
plt.xlabel('Número de Mortes')
plt.ylabel('País')
plt.title('Mortes por COVID-19 por País (Gráfico de Estalactite)')
plt.show()
