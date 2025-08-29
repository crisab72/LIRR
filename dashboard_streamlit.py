
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Carica i dati
riepilogo_df = pd.read_excel("riepilogo_unificato_con_assenze.xlsx", sheet_name="Riepilogo", engine="openpyxl")
assenze_df = pd.read_excel("riepilogo_unificato_con_assenze.xlsx", sheet_name="Assenze", engine="openpyxl")

# Titolo
st.title("Dashboard Annuale - Ore e Assenze")

# Per ogni anno
for anno in [2023, 2024, 2025]:
    st.header(f"Anno {anno}")
    df_anno = riepilogo_df[riepilogo_df['Anno'] == anno]
    mesi = df_anno['Periodo'].dt.strftime('%b')

    # Grafico a barre 3D
    fig = go.Figure()
    fig.add_trace(go.Bar(x=mesi, y=df_anno['Assenze_ore'], name='Assenze', marker_color='red', text=df_anno['Assenze%'], textposition='outside'))
    fig.add_trace(go.Bar(x=mesi, y=df_anno['PresenzeDiv_ore'], name='Presenze Diverse', marker_color='orange', text=df_anno['PresDiv%'], textposition='outside'))
    fig.add_trace(go.Bar(x=mesi, y=df_anno['Straord_ore'], name='Straordinario', marker_color='deepskyblue', text=df_anno['Straord%'], textposition='outside'))
    fig.add_trace(go.Bar(x=mesi, y=df_anno['Ferie_ore'], name='Ferie', marker_color='green', text=df_anno['Ferie%'], textposition='outside'))

    fig.update_layout(
        title=f"Ore Mensili per Categoria - {anno}",
        barmode='group',
        hovermode='x unified'
    )

    st.plotly_chart(fig)

    # Grafico a torta delle assenze
    assenze_anno = assenze_df[assenze_df['Anno'] == anno]
    categorie = ['Psin','L104','All','Conp','Dons','Frc','Inf','Malf','Mat','Nasf','Pdec','Pele','Prls','Rci','Ros','Vmsp','Mal','Ass','Pext','Scio']
    totale_per_tipo = assenze_anno[categorie].sum()
    fig_pie = px.pie(values=totale_per_tipo.values, names=totale_per_tipo.index, title=f"Distribuzione Assenze - {anno}")
    st.plotly_chart(fig_pie)

st.success("Dashboard interattiva pronta per la pubblicazione su Streamlit Cloud.")
