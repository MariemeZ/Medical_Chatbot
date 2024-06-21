import spacy

# # Charger le modèle entraîné
# nlp = spacy.load("C:\\Users\\USER\\Desktop\\IDS4\\SEMESTRE 2\\NLP\\projet\\modele_ner")

# # Texte d'exemple pour tester le modèle
# text = "What is (are) Paralysis ?"

# # Appliquer le modèle au texte
# doc = nlp(text)

# # print(doc)
# # print(doc.ents)
# # Afficher les entités nommées détectées dans le texte
# for ent in doc.ents:
#     print(ent.text, ent.label_)


def detecter_entites_nommées(texte, chemin_modele="C:\\Users\\USER\\Desktop\\IDS4\\SEMESTRE 2\\NLP\\projet\\modele_ner"
):
    # Charger le modèle entraîné
    nlp = spacy.load(chemin_modele)

    # Appliquer le modèle au texte
    doc = nlp(texte)

    # Stocker les entités nommées détectées dans une liste de tuples (entité, étiquette)
    entites = [(ent.text, ent.label_) for ent in doc.ents]

    return entites

# Exemple d'utilisation de la fonction
texte = "What is (are) Paralysis ?"
chemin_modele = "C:\\Users\\USER\\Desktop\\IDS4\\SEMESTRE 2\\NLP\\projet\\modele_ner"

# entites_detectees = detecter_entites_nommées(texte, chemin_modele)
# print(entites_detectees)