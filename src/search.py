from vdb import find_most_similar_embeddings
from embed import encode_string

q = r'A black jersey'

qe = encode_string(q)
r = find_most_similar_embeddings(qe, n_results=3)

print(r)
