import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="Convertisseur Excel → Bonus CSV", layout="centered")
st.title("🎁 Convertisseur de fichiers bonus")
st.write("Charge un fichier Excel au format Squadeasy et récupère le fichier CSV formaté.")

uploaded_file = st.file_uploader("Choisis ton fichier Excel", type=[".xlsx"])

if uploaded_file:
    try:
        excel_data = pd.read_excel(uploaded_file, sheet_name="Utilisateurs")

        df_formate = excel_data.rename(columns={
            "Email": "Email",
            "Total": "Montant",
            "Date": "Date",
            "Raison": "Raison"
        })[["Email", "Montant", "Date", "Raison"]]

        # Convertir en CSV pour téléchargement
        csv_buffer = io.StringIO()
        df_formate.to_csv(csv_buffer, index=False)
        csv_bytes = csv_buffer.getvalue().encode('utf-8')

        st.success("✅ Conversion réussie !")
        st.download_button(
            label="📁 Télécharger le CSV formaté",
            data=csv_bytes,
            file_name="bonus_format.csv",
            mime="text/csv"
        )

    except Exception as e:
        st.error(f"❌ Erreur lors du traitement du fichier : {e}")