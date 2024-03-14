
# Importation de la bibliothèque Streamlit
import streamlit as st

# Titre de la page
st.title('Ma première application Streamlit')

# Ajout d'un texte
st.write("Voici du texte affiché sur la page web.")

# Ajout d'un graphique simple
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(100)
plt.hist(data, bins=20)
st.pyplot()

# Ajout d'un widget de sélection
option = st.selectbox(
    'Quelle est votre couleur préférée ?',
    ['Rouge', 'Vert', 'Bleu'])

'Vous avez sélectionné :', option