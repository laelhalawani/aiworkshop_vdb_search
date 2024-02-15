from vdb import current_collection, add_embeddings, find_most_similar_embeddings
from embed import encode_string, encode_image, encode_image_from_path
from pathlib import Path
import json

data_file = "data.json"
products_dir = Path("products")
# Iterate through the dirs to get each product data
# Extract the pid, title, category, url, and image
# Create embeddings for images and add to the collection with the product data as metadata