#%%
import pandas as pd


url = "https://www.uol.com.br/esporte/futebol/campeonatos/brasileirao/"
df=pd.read_html(url)
df

# %%
times = df[0]
pontos = df[1]
#%%
times.to_csv("brasileirao.csv",sep=";",index=False)
pontos.to_csv("pontos.csv",sep=";",index=False)


brasileirao = pd.concat([times,pontos],axis=1)

brasileirao[['Time', 'Abreviacao']] = brasileirao['classificação'].str.extract(r'(.+?)([A-Z]{3})$')
brasileirao.to_csv("brasileirao_completo.csv",sep=";",index=False)
# %%
# opcional: remover coluna antiga
brasileirao = brasileirao.drop(columns=['classificação'])
# %%
# salva novamente
brasileirao.to_csv("brasileirao_completo.csv", sep=";", index=False)

print(brasileirao.head())

