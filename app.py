"""
AI Invoices - Streamlit aplikacija
Glavna ulazna tocka aplikacije.
"""

import streamlit as st

st.set_page_config(
    page_title="AI Invoices",
    page_icon="receipt",
    layout="wide",
    initial_sidebar_state="expanded",
)


def main():
    st.title("AI Invoices")
    st.markdown("Automatsko prepoznavanje racuna i izvoz u Excel tablicu")

    # TODO: Inicijaliziraj session state (popis racuna, postavke)
    # TODO: Postavi sidebar navigaciju (Upload, Tablica, Postavke)
    # TODO: Usmjeri na stranicu prema odabiru u sidebaru

    st.info("Aplikacija je u izradi. Odaberi stranicu iz izbornika.")


if __name__ == "__main__":
    main()
