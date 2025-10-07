#%%
import pandas as pd
import streamlit as st

df = pd.read_csv("brasileirao_completo.csv",sep=";")
df['Time'] = df['Time'].apply(lambda x: ' '.join(x.split()[1:]))
#título da pag
st.title("Consulta de Pontos Brasileirão")
#input do usuário
time = st.text_input("Digite o nome do time:").strip()
#quando o usuário digitar
if time:
    #busca o time na tabela
    resultado = df[df['Time'].str.lower() == time.lower()]

    if not resultado.empty:
        abv = resultado["Abreviacao"].values[0]
        pontos = resultado['PG'].values[0]  # coluna de pontos
        vitorias = resultado['V'].values[0]  # coluna de vitórias
        empates = resultado['E'].values[0]   # coluna de empates
        derrotas = resultado['D'].values[0]  # coluna de derrotas
        if time.lower() == "sport":
            st.warning("🔦 O Sport está segurando a lanterna do campeonato! 🔦")
        st.success(f"O pontos do {time} é:")
        st.write(f"Pontos: {pontos}")
        st.write(f"Vitórias: {vitorias}")
        st.write(f"Empates: {empates}")
        st.write(f"Derrotas: {derrotas}")
    else:
        st.error("Time não encontrado na Série A")
