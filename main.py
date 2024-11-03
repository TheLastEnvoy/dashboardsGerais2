import streamlit as st
from dashboard_documentos import show_dashboard as show_dashboard_documentos
from dashboard_planilhas import show_dashboard as show_dashboard_planilhas
from dashboard_pareceres import show_dashboard as show_dashboard_pareceres
from dashboard_laudos import show_dashboard as show_dashboard_laudos

def main():
    st.title("Dashboard Supervisão Ocupacional - TED INCRA/UFPR")
    tab1, tab2, tab3, tab4 = st.tabs([
        "Documentação da PGT",
        "Planilhas de monitoramento",
        "Pareceres para att. cadastral",
        "Laudos de Superv. Ocupacional"
    ])

    with tab1:
        show_dashboard_documentos()

    with tab2:
        show_dashboard_planilhas()

    with tab3:
        show_dashboard_pareceres()

    with tab4:
        show_dashboard_laudos()

if __name__ == "__main__":
    main()
