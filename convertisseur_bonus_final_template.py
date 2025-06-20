
import streamlit as st
import pandas as pd
import base64
from io import BytesIO

# Personnalisation CSS
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: #FFFFFF;
    }}
    .main > div {{
        padding-top: 2rem;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Affichage du logo
st.image("resized_logo.png", width=200)

# Intro personnalisée
st.markdown("""
### 🎯 Bienvenue sur l'outil de conversion des fichiers bonus

Dépose ici un fichier Excel, et l'application le convertira automatiquement au format standard attendu.  
Voici les colonnes que ton fichier doit comporter, dans cet ordre :  
📧 email, ⭐ points bonus, 📅 date (NN/MM/JJ), 📝 raison du bonus.
""")

# Bouton pour télécharger le fichier modèle
with open("modele_bonus.xlsx", "rb") as f:
    modele_bytes = f.read()

st.download_button(
    label="📄 Télécharger le fichier modèle",
    data=modele_bytes,
    file_name="modele_bonus.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

# Uploader le fichier utilisateur
uploaded_file = st.file_uploader("Dépose ton fichier Excel ici", type=["xlsx"])

if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file)

        # Vérifie qu'on a au moins 4 colonnes
        if df.shape[1] < 4:
            st.error("❌ Le fichier doit contenir au moins 4 colonnes.")
        else:
            # Garde les 4 premières colonnes et renomme-les
            df = df.iloc[:, :4]
            df.columns = ['Email', 'Points bonus', 'Date', 'Raison']

            # Exporter le fichier au format CSV
            csv = df.to_csv(index=False).encode('utf-8')
            st.success("✅ Conversion réussie !")
            st.download_button(
                label="📥 Télécharger le fichier CSV converti",
                data=csv,
                file_name="bonus_converti.csv",
                mime="text/csv"
            )
    except Exception as e:
        st.error(f"Une erreur est survenue : {e}")
