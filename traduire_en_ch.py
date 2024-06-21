# Importation des modules nécessaires
from transformers import MarianMTModel, MarianTokenizer
import torch

# Initialisation du modèle et du tokenizer

token = "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"
model_name = "Helsinki-NLP/opus-mt-en-ZH"
tokenizer = MarianTokenizer.from_pretrained(model_name,  use_auth_token=token)
model = MarianMTModel.from_pretrained(model_name,  use_auth_token=token)

# Fonction de traduction
def traduire(texte, langue_source="en", langue_cible="zh-CN"):
    texte_tokenise = tokenizer.prepare_seq2seq_batch(src_texts=[texte], src_langs=[langue_source], tgt_langs=[langue_cible], return_tensors="pt")
    with torch.no_grad():
        traduction = model.generate(**texte_tokenise)
    texte_traduit = tokenizer.decode(traduction[0], skip_special_tokens=True)
    return texte_traduit

# Texte en anglais à traduire
# texte_en_anglais = "What is (are) Precocious puberty ?"

# # Traduction du texte en chinois simplifié
# texte_traduit = traduire(texte_en_anglais)

# # Affichage du résultat
# print("Texte en anglais:", texte_en_anglais)
# print("Texte traduit en chinois simplifié:", texte_traduit)




import torch
from transformers import MarianMTModel, MarianTokenizer

# Charger le modèle et le tokenizer pour la traduction chinois-anglais
model_name1 = "Helsinki-NLP/opus-mt-zh-en"
tokenizer1 = MarianTokenizer.from_pretrained(model_name1)
model1 = MarianMTModel.from_pretrained(model_name1)

# Définir la fonction traduire_zh_en
# def traduire_zh_en(texte, langue_source="zh-CN", langue_cible="en"):
#     texte_tokenise = tokenizer1.prepare_seq2seq_batch(src_texts=[texte], src_langs=[langue_source], tgt_langs=[langue_cible], return_tensors="pt")
#     with torch.no_grad():
#         traduction = model1.generate(**texte_tokenise)
#     texte_traduit = tokenizer1.decode(traduction[0], skip_special_tokens=True)
#     return texte_traduit

from googletrans import Translator

def traduire_zh_en(texte, langue_source="zh-CN", langue_cible="en"):
    # Créer une instance de traducteur
    translator = Translator()

    # Traduire le texte
    traduction = translator.translate(texte, src=langue_source, dest=langue_cible)

    # Récupérer le texte traduit
    texte_traduit = traduction.text

    return texte_traduit
