import streamlit as st
import pandas as pd
import random

# Tema
st.set_page_config(page_title="Tabelas de conjoint",
                   layout="wide", initial_sidebar_state="expanded",
                   page_icon=None)

# Atributos e levels do conjoint
attributes = {
    "Sexo": ["Homem", "Mulher"],
    "Cor/raça": ["Branca", "Parda", "Preta", "Amarela/Indígena"],
    "Religião": ["Católica", "Evangélica", "Sem religião", "Umbanda"],
    "Orientação sexual": ["Heterossexual", "LGBT"],
    "Experiência na política": ["Nenhuma", "Ex-vereador(a)", "Ex-deputado(a)"],
    "Apoio político": ["Nenhum", "Tem o apoio do(a) atual prefeito(a)", "Tem o apoio do governador", "Tem o apoio da comunidade"],
    "Pena de morte": ["É a favor da pena de morte", "É contra a pena de morte"],
}

# Menu lateral
st.sidebar.title("Simulação de tabelas")
st.sidebar.markdown("Cada simulação sorteia levels independentemente de cada atributo usando probabilidade uniforme de seleção.")
if st.sidebar.button("Simular"):
    candidate_1 = {attribute: random.choice(levels) for attribute, levels in attributes.items()}
    candidate_2 = {attribute: random.choice(levels) for attribute, levels in attributes.items()}
    df = pd.DataFrame([candidate_1, candidate_2], index=["Candidato 1", "Candidato 2"]).T
    df.columns.name = "Attribute"
    st.table(df)
