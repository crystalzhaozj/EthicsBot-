from utils import processing_txt as pr
import numpy as np

# 1. Similarity Functions
"""
Jaccard Similarity
"""


def jaccard_s(set1, set2):
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

def cosine_s(v1, v2):
    """
    Takes in 2 vectors, calculates the cosine similarity between the two vectors.
    Returns a float number that is the similarity score.
    """
    # Convert to numpy arrays
    v1 = np.array(v1)
    v2 = np.array(v2)

    dot_product = np.dot(v1, v2)

    # compute length of vector
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)

    if norm_v1 == 0 or norm_v2 == 0:
        return 0.0 # Return 0 if one or both vectors are zero vectors
    return dot_product / (norm_v1 * norm_v2)

def centroid(vlist):
    """
    Takes in a list of numpy vectors and creates a centered, averaged vector.
    Returns a numpy.array.
    """
    if not vlist:
        return np.array([]) # Return empty array if no vectors
    # Stack vectors vertically and then compute the mean along the first axis (rows)
    return np.mean(vlist, axis=0) # elemnt by element 

"""
RARE WORD DENSITY

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
"""
# 2. Calculating similarities

def pairwise_similarities(dir, similarity_function):
    """
    Reads all text files in a given group directory, preprocesses them,
    calculates pairwise similarities, and returns a similarity matrix
    along with file labels.
    For Jaccard: 1 group directory resembles 1 paper with 4 reports
    For Cosine:
    """

    strlist, labels = pr.file_to_string(dir)
    num_files = len(labels) # There should be 4
    similarity_matrix = np.zeros((num_files, num_files)) # creates a square matrix of size num_files * num_files, all filled with zeroes now

    # Calculate pairwise similarities
    for i, file1 in enumerate(labels):
        for j, file2 in enumerate(labels):
            if i == j:
                similarity_matrix[i, j] = 1.0 # A file is perfectly similar to itself
            elif i < j: # Calculate only once for each pair (matrix is symmetric)
                t1 = strlist[file1]
                t2 = strlist[file2]
                if similarity_function == jaccard_s: # convert to sets for jaccard
                    set1 = set(t1.split())
                    set2 = set(t2.split())
                    similarity = similarity_function(set1, set2)
                else:
                    similarity = similarity_function(t1, t2)
                similarity_matrix[i, j] = similarity
                similarity_matrix[j, i] = similarity # Fill the symmetric part

    return similarity_matrix, labels

def group_similarities(vecs1, vecs2):
    c1 = centroid(vecs1)
    c2 = centroid(vecs2)
    similarity = cosine_s(c1, c2)
    return similarity
                       