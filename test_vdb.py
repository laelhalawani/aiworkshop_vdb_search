from vdb import current_collection, add_embeddings, find_most_similar_embeddings
from embed import encode_string, encode_image

# from chromadb.utils import embedding_functions
# default_ef = embedding_functions.DefaultEmbeddingFunction()
# sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

blonde_female = str("a blonde female")
blonde_female_embeddings = encode_string(blonde_female)
add_embeddings(blonde_female_embeddings, metadatas={"text": blonde_female})

brunette_female = str("a brunette female")
brunette_female_embeddings = encode_string(brunette_female)
add_embeddings(brunette_female_embeddings, metadatas={"text": brunette_female})

blonde_male = str("a blonde male")
blonde_male_embeddings = encode_string(blonde_male)
add_embeddings(blonde_male_embeddings, metadatas={"text": blonde_male})

brunette_male = str("a brunette male")
brunette_male_embeddings = encode_string(brunette_male)
add_embeddings(brunette_male_embeddings, metadatas={"text": brunette_male})


intelligent = str("a genius")
intelligence_embeddings = encode_string(intelligent)

r = find_most_similar_embeddings(intelligence_embeddings, n_results=10)
print(r)

