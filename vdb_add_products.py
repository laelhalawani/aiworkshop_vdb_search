from vdb import current_collection, add_embeddings, find_most_similar_embeddings
from embed import encode_string, encode_image, encode_image_from_path
from pathlib import Path
import json

image_file = "0.png"
data_file = "data.json"

products_dir = Path("products")
for product_dir in products_dir.iterdir():
    if product_dir.is_dir():
        dir_pid = product_dir.name
        print(f"Processing product dir {dir_pid}")
        product_data = json.loads((product_dir / data_file).read_text())
        product_title = product_data["title"]
        product_category = product_data["category"]
        product_pid = product_data["pid"]
        product_url = product_data["url"]
        if dir_pid != product_pid:
            print(f"Warning: dir name {dir_pid} does not match product id {product_pid}")
        image_path = Path(product_data["image"])
        img_embs = encode_image_from_path(str(image_path))
        add_embeddings(img_embs, metadatas=product_data, uris=[str(product_dir)])
        #print(f"""Adding {product_category} product {product_title} with pid {product_pid}""")
