0. Setup

   just venv, activate it and
   `python -m playwright install`

1. Run scrape.py -> this will create a file called products.json with all the products and following structure:

```
    {
        "pid": "PM-4905041",
        "url": "https://...product/airoh-twist-20-mx-helmet-white_pid-PM-4905041",
        "category": "helmets",
        "title": "Airoh Twist 2.0 MX Helmet White",
        "image_links": [
            "https://pierce-images.imgix.net/images/7/0/b/b/70bb75abdda229770a6dfa30d422811768a29bd2_2_PIA_133951_0_140.png"
        ]
    },
```

2. Run prepare_products.py -> this will create a direcotry 'products'
and inside there will be a directory for each 'product id' (PM or PIA). Each of the product dirs will include two files:

- data.json -> with the following structure:

```
{
    "title": "24MX Sweat Beanie",
    "category": "helmets",
    "image": "products\\GBBEANIE\\0.png",
    "pid": "GBBEANIE",
    "url": "https://...product/24mx-sweat-beanie_pid-GBBEANIE",
}
```
- 0.png -> the image of the product

3. Create logic for adding products to the vectordb with product data as metadata

See: `vdb_add_products.py`

4. Create search engine logics

See: `search.py`
