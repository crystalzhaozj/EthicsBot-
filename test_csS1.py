from utils import similarity_indices as si
from utils import vectorization as vec
from utils import visualization as vz

vectorizer1 = vec.create_vectorizer("txtreports/S1")

rq_vecs, rq_labels = vec.get_tfidf_vectors("txtreports/S1/RQ", vectorizer1)
intro_vecs, intro_labels = vec.get_tfidf_vectors("txtreports/S1/Intro", vectorizer1)

print([len(v) for v in rq_vecs]) # 2 vectors in rq_vecs, each with a length of 509 
#509 means that there are 509 unique terms -> 509 dimensions

score = si.group_similarities(rq_vecs, intro_vecs)
print(score)