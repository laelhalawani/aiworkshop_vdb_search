import json
import requests
from pathlib import Path

products_dir_name = 'products'
scrape_file = 'scrape.json'
product_data_file_name = 'data.json'

products = {}
# Load the JSON file
with open(scrape_file) as f:
    products = json.load(f)

def download_image(image_url, save_path):
    # Send a GET request to the image URL
    response = requests.get(image_url, stream=True)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Ensure the save_path directory exists
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        
        # Open the file at save_path in binary write mode and write the contents of the response
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192): 
                file.write(chunk)
        print(f"Image saved at {save_path}")
    else:
        print(f"Failed to download image. Status code: {response.status_code}")

# Iterate through the products
for product in products:
    # Get the category and title of the product
    product_id:str = product['pid']
    product_category = product['category']
    product_title = product['title']
    product_url = product['url']
    save_dir = Path(products_dir_name) / product_id.replace('/', '')
    save_dir.mkdir(parents=True, exist_ok=True)
    # Download the images
    local_image_paths = []
    for i, image_link in enumerate(product['image_links']):
        file_name = str(i) + '.png'
        image_save_path = save_dir / file_name
        download_image(image_link, image_save_path)
        local_image_paths.append(str(image_save_path))
    #save json file
    product_data = {
        'title': product_title,
        'category': product_category,
        'image': local_image_paths[0],
        'pid': product_id,
        'url': product_url,
    }
    with open(save_dir / product_data_file_name, 'w') as f:
        json.dump(product_data, f, indent=4)

        
    