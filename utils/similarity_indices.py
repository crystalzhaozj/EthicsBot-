# 1. Similarity Functions
"""
Jaccard Similarity
"""
import os
import processing_txt as pr
import numpy as np

def jaccard_similarity(set1, set2):
    """
    Calculates the Jaccard similarity between two sets.
    Jaccard Similarity = |Intersection(set1, set2)| / |Union(set1, set2)|
    Closer to 1, more similar.
    """
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    if union == 0:
        return 0.0 # Avoid division by zero if both sets are empty
    return intersection / union

"""
Cosine Similarity
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Calculating similarity
def cosine_similarity(txt1, txt2):
    texts = [txt1, txt2]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(texts)
    similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]
    return similarity

"""
RARE WORD DENSITY
"""

# Word frequency
from wordfreq import zipf_frequency  # Lower zipf = rarer word
# specificity_score = sum([1 for word in text.split() if zipf_frequency(word, 'en') < 3.0]) / len(text.split())

# NER
import spacy
from sklearn.metrics import jaccard_score

nlp = spacy.load("en_core_sci_sm")  # Biomed-specialized model

def get_entities(text):
    doc = nlp(text)
    return set([ent.text.lower() for ent in doc.ents if ent.label_ in ["CHEMICAL", "METHOD", "EQUIPMENT"]])

def entity_jaccard(text1, text2):
    ents1 = get_entities(text1)
    ents2 = get_entities(text2)
    if not ents1 or not ents2:
        return 0.0  # Avoid division by zero
    intersection = len(ents1 & ents2)
    union = len(ents1 | ents2)
    return intersection / union

# 2. Calculating similarities

def group_similarities(group_path, similarity_function):
    """
    Reads all text files in a given group directory, preprocesses them,
    calculates pairwise similarities, and returns a similarity matrix
    along with file labels.
    For Jaccard: 1 group directory resembles 1 paper with 4 reports
    For Cosine:
    """
    file_contents = {}
    file_labels = []

    # Read and preprocess files
    for filename in sorted(os.listdir(group_path)): # Sort for consistent order
        if filename.endswith(".txt"):
            filepath = os.path.join(group_path, filename)
            with open(filepath, "r") as f:
                content = f.read()
            file_contents[filename] = pr.preprocess_report(content)
            file_labels.append(filename)

    num_files = len(file_labels) # There should be 4
    similarity_matrix = np.zeros((num_files, num_files)) # creates a square matrix of size num_files * num_files, all filled with zeroes now

    # Calculate pairwise similarities
    for i, file1 in enumerate(file_labels):
        for j, file2 in enumerate(file_labels):
            if i == j:
                similarity_matrix[i, j] = 1.0 # A file is perfectly similar to itself
            elif i < j: # Calculate only once for each pair (matrix is symmetric)
                set1 = file_contents[file1]
                set2 = file_contents[file2]
                similarity = similarity_function(set1, set2)
                similarity_matrix[i, j] = similarity
                similarity_matrix[j, i] = similarity # Fill the symmetric part

    return similarity_matrix, file_labels

