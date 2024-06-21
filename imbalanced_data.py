from imblearn.over_sampling import SMOTE
import pandas as pd
import numpy as np
import tensorflow as tf
import torch
from data_balanced import data_list
from textattack.transformations import WordSwap
from textattack.augmentation import CheckListAugmenter

from traduire_en_ch import traduire
from textattack.augmentation import EasyDataAugmenter

# Function to augment data using CheckListAugmenter

def augmenter_donnees(phrases, num_replacements=2, transformations_per_example=1):  # Adjust num_replacements as needed
    augmenter = EasyDataAugmenter(pct_words_to_swap=0.2, transformations_per_example=transformations_per_example)
    phrases_augmentees = []
    for phrase in phrases:
        phrases_augmentees.append(augmenter.augment(phrase))
        print('la phrase originale est:')
        print(phrase)
    print(len(phrases_augmentees))
    return phrases_augmentees

df = pd.DataFrame(data_list, columns=["sentence_en", "sentence_zh", "label"])

# Calculer le nombre d'échantillons de chaque classe
class_counts = df['label'].value_counts()
print(class_counts)




majority_class = 'prevention'
majority_count = class_counts[majority_class]
desired_majority_samples = 2700  

if majority_count > desired_majority_samples:
    indices_to_remove = df[df['label'] == majority_class].sample(n=majority_count - desired_majority_samples, random_state=42).index
    df = df.drop(indices_to_remove)



# # 3. Identify all intentions and define minimum sample threshold
# all_intentions = df['label'].unique().tolist()
# minority_threshold = 6  # Adjust this threshold as needed

# minority_intentions = []
# for intention in all_intentions:
#   intention_count = df[df['label'] == intention].shape[0]
#   if intention_count < minority_threshold:
#     minority_intentions.append(intention)


# # minority_intentions=[  'susceptibility',   'dietary', 'usage', 'precautions', 'other information']
# minority_intentions=[   'prevention']
# print(minority_intentions)
# # 4. Find minority intentions
# minority_data = []
# for intention in minority_intentions:
#     minority_data.extend(zip(df[df['label'] == intention]['sentence_en'].tolist(), [intention] * df[df['label'] == intention].shape[0]))


# minority_sentences, y_minority = zip(*minority_data)

# data_par_intention = {}
# for intention in df['label'].unique():
#     data_par_intention[intention] = df[df['label'] == intention]['sentence_en'].tolist()

# # Augment data for minority classes
# augmented_data = []
# for intention, data in data_par_intention.items():
#     if intention in minority_intentions:  # Augmenter uniquement les classes non majoritaires
#         augmented_data_en = augmenter_donnees(data)  # Phrases anglaises augmentées
#         augmented_data_en = [sentence for sublist in augmented_data_en for sentence in sublist]
#         augmented_data.extend([(en_sentence,intention, traduire(en_sentence)) for en_sentence in augmented_data_en])

# # Créer un nouveau DataFrame à partir du dictionnaire

# new_data = {
#     "sentence_en": [sentence[0] for sentence in augmented_data],  # Extraire la première phrase pour l'anglais
#     "label": [sentence[1] for sentence in augmented_data],
#     "sentence_zh": [sentence[2] for sentence in augmented_data]  # Phrases traduites
# }

# print(new_data)

# # Create a DataFrame from the dictionary
# new_df = pd.DataFrame(new_data)


# # Concatenate the original DataFrame with the new DataFrame
# df_augmented = pd.concat([df, new_df], ignore_index=True)
# # 6. Calculate class distribution after balancing

# class_counts = df_augmented['label'].value_counts()
# print(class_counts)



# 7. Save balanced data (adapt saving logic as needed)
balanced_data = [(row['sentence_en'], row['sentence_zh'], row['label']) for _, row in df.iterrows()]
class_counts = df['label'].value_counts()
print(class_counts)

with open("data_balanced.py", 'w', encoding='utf-8') as f:
  f.write("data_list = [\n")
  for item in balanced_data:
    f.write(f"    ({repr(item[0])}, {repr(item[1])}, {repr(item[2])}),\n")
  f.write("]\n")
