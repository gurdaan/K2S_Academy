# from keras.models import load_model
# import nltk
# import numpy as np
# import re
# from lexrank import STOPWORDS, LexRank
# from nltk.stem import PorterStemmer
# import re
# import string
# import nltk
# nltk.download('punkt')
# nltk.download('stopwords')
# import gensim
# from tensorflow.keras.preprocessing.sequence import pad_sequences
# import numpy as np
# from sklearn.metrics.pairwise import cosine_similarity

def summarize(text):

    # Tokenize the text into sentences
    # sentences = re.split('\. |\n', text)

    # # Remove any empty sentences
    # sentences = list(filter(lambda x: len(x.strip()) > 0, sentences))

    # # Create a list of stop words
    # stopwords = set(STOPWORDS['en'])

    # # Create a LexRank object
    # lxr = LexRank(sentences, stopwords=stopwords)

    # # Calculate sentence importance using LexRank
    # sentence_importance = lxr.rank_sentences(sentences, threshold=None)

    # # Get top 2 most important sentences as summary
    # num_sentences = 2
    # summary_sentences = np.argsort(sentence_importance)[::-1][:num_sentences]
    # summary = [sentences[i] for i in sorted(summary_sentences)]

    # # Print the summary
    # print(' '.join(summary))


    #return ' '.join(summary)
    return "Hello"

# def summarize2(text):
#     # summarizer=pipeline('summarization', model='t5-base')
#     # summary = summarizer(text, max_length=500, min_length=30,  do_sample=False)[0]['summary_text']
#     embedding_dim = 100 # replace with the correct embedding dimension of your GloVe embeddings
#     glove_path = '/content/drive/MyDrive/glove/glove.42B.300d.txt' 

#     # Create a dictionary to store the GloVe embeddings
#     glove_embeddings = {}
#     with open(glove_path) as f:
#         for line in f:
#             values = line.split()
#             word = values[0]
#             vector = np.asarray(values[1:101], dtype='float32')
#             glove_embeddings[word] = vector
        
    
#     # Preprocess Text
#     tokens=preprocess(text)

#     # Converting Preprocessed text to embedding
#     embedding_size = 100
#     text_embedding=[glove_embeddings.get(key, np.zeros(embedding_size)) for key in tokens if key in glove_embeddings]

#     # Padding each sentence 
#     max_len=100 #(Have to fetch the max value of text on which was trained)
#     padded_text_embeddings = pad_sequences([text_embedding], maxlen=max_len, padding='post', dtype='float64')

#     # Loading the saved model
#     ml_model = load_model('my_lstm_model.h5')

#     # Convert the padded vectorized text to a tensor
#     new_text_tensor = tf.convert_to_tensor(padded_text_embeddings)

#     # Making Prediction
#     prediction = ml_model.predict([new_text_tensor, np.zeros((1, max_len-1, embedding_dim))])

#     # Converting predicated embeddings again to closest word from Glove-pre trained embeddings
#     summary=' '.join(set(convert_prediction_to_summary(prediction,glove_embeddings)))
#     return summary

# def preprocess(text):
#     # Convert text to lower case
#     text = text.lower()
#     # Remove numbers
#     text = re.sub(r'\d+', '', text)
#     # Remove punctuation
#     translator = str.maketrans('', '', string.punctuation)
#     text = text.translate(translator)
#     # Remove whitespaces
#     text = text.strip()
#     # Tokenize into words
#     tokens = nltk.word_tokenize(text)
#     # Remove stopwords
#     stop_words = nltk.corpus.stopwords.words('english')
#     tokens = [token for token in tokens if token not in stop_words]
#     # Apply Porter stemming
#     stemmer = PorterStemmer()
#     tokens = [stemmer.stem(token) for token in tokens]

#     return tokens

# def convert_prediction_to_summary(prediction, embeddings):
#     # Reshape prediction
#     prediction = prediction.reshape(-1, prediction.shape[-1])

#     # Compute cosine similarity between prediction and embedding matrix
#     similarity = cosine_similarity(prediction, list(embeddings.values()))

#     # Find indices of most similar words
#     indices = np.argmax(similarity, axis=1)

#     summary = [list(embeddings.keys())[idx] for idx in indices]

#     return summary