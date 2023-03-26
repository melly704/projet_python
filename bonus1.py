import streamlit as st
import requests


def create():
    st.title("Créer une nouvelle entrée")

    title = st.text_input("Titre")
    price = st.text_input("Prix")
    category = st.text_input("Catégorie")
    advantages_clubR = st.text_input("Avantages ClubR")

    if st.button("Enregistrer"):
        response = requests.post("http://localhost:5000/nouvelle_entree",
                                json={"title": title,
                                    "price": price,
                                    "category": category,
                                    "advantages_clubR": advantages_clubR})
        if response.status_code == 201:
            st.success("Nouvelle entrée enregistrée avec succès !")
        else:
            st.error("Une erreur s'est produite lors de l'enregistrement de la nouvelle entrée.")

url = 'http://localhost:5000/mettre_a_jour_donnee/'

def maj():
    st.write('## Mettre à jour une donnée')
    id = st.text_input("ID de l'entrée à mettre à jour")
    title = st.text_input('Titre')
    price = st.text_input('Prix')
    category = st.text_input('Catégorie')
    advantages_clubR = st.text_input('Avantages ClubR')
    if st.button('Mettre à jour'):
        data = {}
        if title:
            data['title'] = title
        if price:
            data['price'] = price
        if category:
            data['category'] = category
        if advantages_clubR:
            data['advantages_clubR'] = advantages_clubR
        response = requests.patch(url + id, json=data)
        if response.status_code == 200:
            st.write('Donnée mise à jour avec succès')
        else:
            st.write('Erreur lors de la mise à jour de la donnée')

def delete():
    st.header("Supprimer une entrée")
    id = st.text_input("ID de l'entrée à supprimer")
    if st.button("Supprimer"):
        response = requests.delete(f'http://localhost:5000/supprimer_entree/{id}')
        if response.status_code == 200:
            st.success("Données supprimées avec succès")
        else:
            st.error("Une erreur s'est produite lors de la suppression des données")

def update():
    id = st.text_input("ID de l'entrée à modifier")
    title = st.text_input("Nouveau titre")
    price = st.number_input("Nouveau prix")
    category = st.text_input("Nouvelle catégorie")
    advantages_clubR = st.text_input("Nouveaux avantages Club R")
    if st.button("Mettre à jour"):
        url = f'http://localhost:5000/mettre_a_jour_donnee/{id}'
        data = {
            'title': title,
            'price': price,
            'category': category,
            'advantages_clubR': advantages_clubR
        }
        response = requests.patch(url, json=data)

        if response.status_code == 200:
            st.success("L'entrée a été mise à jour avec succès.")
        else:
            st.error("Une erreur s'est produite lors de la mise à jour.")


