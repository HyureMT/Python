import pandas as pd
import matplotlib.pyplot as plt

# Dados reais de mortes por COVID-19 por país
mortes_covid = {
    'País': ['EUA', 'Brasil', 'Índia', 'Rússia', 'México'],
    'Mortes': [1012833, 672033, 525242, 373595, 325793]
}

# Gráfico de linhas para mortes por COVID-19 por país
plt.figure(figsize=(8, 6))
plt.plot(mortes_covid['País'], mortes_covid['Mortes'], marker='o')
plt.xlabel('País')
plt.ylabel('Número de Mortes')
plt.title('Mortes por COVID-19 por País (Gráfico de Linhas)')
plt.grid(True)
plt.show()
