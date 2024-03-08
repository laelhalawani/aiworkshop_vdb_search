from vdb import current_collection, add_embeddings, find_most_similar_embeddings
from embed import encode_string, encode_image, encode_image_from_path
from pathlib import Path
import json

data_file = "data.json"
products_dir = Path("products")
# Iterate through the dirs to get each product data
# Extract the pid, title, category, url, and image
# Create embeddings for images and add to the collection with the product data as metadata

for product_dir in products_dir.iterdir():
    if product_dir.is_dir():
        pid = product_dir.name
        product_data = json.loads((product_dir / data_file).read_text())
        product_pid = product_data["pid"]
        product_image_path = product_data["image"]
        # validation
        if product_pid != pid:
            raise ValueError(f"Product ID mismatch: {product_pid} != {pid}")
        image_path = Path(product_image_path)
        if not image_path.exists():
            raise FileNotFoundError(f"Image not found: {image_path}")

        image_embeddings = encode_image_from_path(product_image_path)
        add_embeddings(embeddings=image_embeddings, metadatas=product_data)
