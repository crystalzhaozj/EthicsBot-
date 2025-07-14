
import plotly as pl

"""
JACCARD SIMILARITY: 4 reports, 4 papers 
"""

# 1. Read in reports

# 2. For each pair, calculat the Jaccard similarity

# 3. Produce the plot


"""
COSINE SIMILARITY 
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Calculating similarity
texts = ["Your first text here", "Your firstsecond text here"]
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(texts)
similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]
print(similarity)

### RQ VS INTRO ###

# 1. Read in RQ reports

# 2. Read in Intro reports

# 3. For each paper: for each pair of RQ vs. Intro (RQ minimal vs. Intro minimal, RQ extended vs. 
# Intro extended, RQ minimal vs. Intro extended, RQ extended vs. Intro minimal), calculate the cosine similarity

### MINIMAL VS EXTENDED ###

# 1. Read in Minimal reports

# 2. Report Extended reports

# 3. For each paper: for each pair of Minimal vs. Extended (RQ minimal vs. RQ extended, Intro minimal vs. 
# Intro extended), calculate the cosine similarity

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

# Example usage
protocol = "Extract DNA using the QIAamp kit, elute in 50 µL Buffer AE."
analysis_specific = "DNA was extracted with the QIAamp kit and eluted in 50 µL Buffer AE."
analysis_generic = "The samples were processed using a standard kit."

print(entity_jaccard(protocol, analysis_specific))  # ~1.0
print(entity_jaccard(protocol, analysis_generic))   # ~0.0