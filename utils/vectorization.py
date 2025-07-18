import numpy as np 
from sklearn.feature_extraction.text import TfidfVectorizer
from utils import processing_txt as pr

def create_vectorizer(dir):
    """
    Creates a TfidVectorizer and fits it to the given list of cleaned strings.
    Internal processes: build a global vocabulary for one study, compute Term Frequency,
    compute Inverse Document Frequency (IDF) for each word in a vocabulary. FInally,
    vectorize by converting a list of words from one document into one vector.
    """
    vectorizer = TfidfVectorizer() # instantiate 
    # Fit the vectorizer on all documents to build the vocabulary and learn IDF values
    strlist, labels = pr.file_to_string(dir)
    vectorizer = vectorizer.fit(strlist)
    return vectorizer

def get_tfidf_vectors(dir, vectorizer):
    """
    Loads cleaned files from a group directory and converts them to TF-IDF vectors
    using an already fitted TfidfVectorizer.
    Returns a list of vectors and a list o file labels.
    Run for each study.
    """
    strlist, labels = pr.file_to_string(dir)
    
    tfidf_matrix = vectorizer.transform(strlist) # Converts cleaned strings into a TF-IDF matrix
    vectors = tfidf_matrix.toarray() # Convert sparse matrix to dense  array

    return vectors.tolist(), labels 

