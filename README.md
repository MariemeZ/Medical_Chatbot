
# Medical Chatbot Report

The project involves creating a medical chatbot that assists users by providing information about various diseases based on user queries.

<img src="https://github.com/MariemeZ/Medical_Chatbot/assets/113024831/4ac7fe9b-ee10-48f7-a7f2-d232b352d324" width="400" height="auto">


![image](https://github.com/MariemeZ/Medical_Chatbot/assets/113024831/1937b184-a980-43b6-8f87-b5a2ef2684b1)

![image](https://github.com/MariemeZ/Medical_Chatbot/assets/113024831/dda1c9ca-ae04-4d9f-b568-be0ec1ed1de7)




## Data Collection

 - In developing a medical question-answering (Q&A) chatbot, the initial crucial step is to collect relevant and accurate data. This stage plays a vital role in constructing a robust knowledge base for the chatbot, ensuring reliable and informative responses to users.

As there was no ready-made database available, we decided to construct our own:

- We traversed an organized file structure where each sub-folder contained XML files.
- Each XML file was analyzed to extract questions and their associated types.
- We focused on questions related to specific types such as treatment, symptoms, susceptibility, usage, prevention, information, causes, dietary aspects, precautions, and other relevant information. These types were selected based on their importance in understanding diseases.
  
  ![image](https://github.com/MariemeZ/Medical_Chatbot/assets/113024831/2c5ab8f8-430d-4449-9937-5594496e0d65)


### Automatic Translation:

Once questions were extracted, we utilized the Hugging Face Transformers library with the MarianMT model to automatically translate these questions from English to Simplified Chinese. Each extracted question underwent translation using MarianMT, specifying English as the source language and Simplified Chinese as the target. Neural machine translation models based on Transformer architecture, like MarianMT, were used to ensure accurate and high-quality translations. This process generated a set of translated questions ready for further analysis.

### Intentions:
The different intentions identified are: ['information', 'symptoms', 'susceptibility', 'treatment', 'prevention', 'causes', 'dietary', 'usage', 'precautions', 'other information']

### Problem: Imbalanced Data

        - Information: 8700
        - Symptoms: 2792
        - Treatment: 2756
        - Causes: 2057
        - Prevention: 1092
        - Other Information: 682
        - Dietary: 651
        - Precautions: 544
        - Usage: 487
        - Susceptibility: 419

### Solution: Data Augmentation
We addressed the imbalanced data using text data augmentation techniques available in the TextAttack library, particularly EasyDataAugmenter and translation to create new data instances.

### Methodology:

#### 1) Identifying Minority Classes:
We first identified the minority classes in our dataset—those with insufficient examples for adequate representation during model training.

#### 2) Determining Desired Sample Count: 
Our goal was to achieve 3000 examples for each minority class while maintaining balance across all classes.

#### 3) Data Augmentation: 
For each minority class, we applied data augmentation strategies. This involved modifying existing examples using EasyDataAugmenter, which substitutes a percentage of words in each sentence with synonyms or random words, creating new variants while preserving the general meaning. Additionally, these variants were translated into another language to further increase data diversity.

After augmentation, the class distribution is as follows:

        - Dietary: 3255
        - Information: 3000
        - Causes: 2800
        - Symptoms: 2792
        - Treatment: 2756
        - Other Information: 2750
        - Precautions: 2720
        - Prevention: 2700
        - Susceptibility: 2600
        - Usage: 2435

## Text Classification

In this section, we explore the use of a pre-trained model for text classification, specifically the "hfl/chinese-bert-wwm" model.

### Pre-trained Model "hfl/chinese-bert-wwm":

The "hfl/chinese-bert-wwm" model is a sequence classification model based on the Transformer architecture. It was pre-trained on a massive dataset of Chinese text and can be used for various text classification tasks, including intention classification, sentiment analysis, and topic classification.

    1) Loading the Model and Tokenizer
    2) Data Preparation
    3) Model Training
    4) Model Evaluation

### Named Entity Recognition (NER) Model with SpaCy:

Training data for the NER model was provided as manually annotated texts, where each entity was labeled with a corresponding tag. We used the pre-trained English language model "en_core_web_sm" from SpaCy as a starting point. We added an NER component to the SpaCy pipeline and defined a new label for named entities ("disease_name") that we aimed to extract from our data. After training, the trained NER model was saved to disk for future use, enabling deployment in NLP applications for automatic extraction of named entities from new texts.


### Next Steps: Calculating Similarity for Response Generation

The next step involves calculating similarity between the disease name entered by the user and the disease name existing in the knowledge base to generate the response.

### Generate the response

The generate_response function formats and presents detailed information about the disease, including description, symptoms, treatments, and other pertinent data.

### Conclusion

The development of the medical chatbot has resulted in a functional system capable of retrieving comprehensive medical information based on user queries. By leveraging structured data from the medical.json file and employing NLP techniques for query processing, the chatbot effectively assists users in accessing relevant medical knowledge.
