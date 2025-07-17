
import plotly as pl
import numpy as np

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

