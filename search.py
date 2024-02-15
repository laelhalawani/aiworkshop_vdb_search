from vdb import find_most_similar_embeddings
from embed import encode_string, encode_image_from_path
import json

search_query = input("Enter search query: ")
search_embeddings = encode_string(search_query)

r = find_most_similar_embeddings(search_embeddings, n_results=3)
#print(r)

ids = r['ids'][0]
distances = r['distances'][0]
metadatas = r['metadatas'][0]
print(f"Found the following results")
for i, (id, distance, metadata) in enumerate(zip(ids, distances, metadatas)):
    category = metadata['category']
    title = metadata['title']
    url = metadata['url']
    image = metadata['image']
    print(f"Result {i+1}: \ndistance: {distance:.2f} \ncategory: {category} \ntitle: {title} \nurl: {url} \nimage: {image} \n\n")