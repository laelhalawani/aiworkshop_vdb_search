import json
import re
from playwright.sync_api import sync_playwright

SCRAPE_FILE_NAME = r'scrape.json'
__BASE_URL = r'https://24mx-ie-inttest01.pierce-ecom.com'
URLS = {
    r'helmets': __BASE_URL + r'/helmets',
    r'jerseys': __BASE_URL + r'/motocross-gear/motocross--enduro-clothing_c10013/jerseys_c10074',
    r'pants':   __BASE_URL + r'/motocross-gear/motocross--enduro-clothing_c10013/pants_c10076',
    r'gloves':  __BASE_URL + r'/motocross-gear/motocross--enduro-clothing_c10013/gloves_c10077',
    r'jackets': __BASE_URL + r'/motocross-gear/motocross--enduro-clothing_c10013/jackets--vests_c10073'
}

products_info = []


def slow_scroll(page, scroll_step=100, timeout=100):
    """Scrolls the page down in increments, waiting for a short period between each scroll."""
    last_position = page.evaluate("window.pageYOffset")
    while True:
        # Scroll down the page by the specified scroll step
        page.evaluate(f"window.scrollBy(0, {scroll_step})")
        # Wait for the specified timeout to allow the page to load
        page.wait_for_timeout(timeout)
        # Check the scroll position after waiting
        new_position = page.evaluate("window.pageYOffset")
        if new_position <= last_position:
            # If the scroll position hasn't changed, we are at the bottom of the page
            break
        last_position = new_position


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    for cat, cat_url in URLS.items():
        # Navigate to the category URL
        #page.goto(cat_url, wait_until='networkidle') # <-- does not work in codespace?
        page.goto(cat_url)
        # Scroll down the page to load all products
        slow_scroll(page, 50, 50)
        # Makesure the selector is loaded
        img_selector = 'img[pproductimg]'
        page.wait_for_selector(img_selector, timeout=10000)
        # Find all p-productcard elements
        product_cards = page.query_selector_all('p-productcard')


        # Iterate through the product cards
        for product_card in product_cards:

            # Select the first <a> tag inside the product card
            product_link = product_card.query_selector('a.o-product-card__blocklink')
            if product_link:
                # Extract the URL and title from the <a> tag
                product_url = __BASE_URL + product_link.get_attribute('href')
                product_title = product_link.get_attribute('title')
                #print(f"Title: {product_title} \nURL: {product_url}\n")
                match = re.search(r'_pid-(.+)', product_url)
                product_id = match.group(1)

                # Find all img elements with the pproductimg attribute within this product card
                product_images = product_card.query_selector_all('img[pproductimg]')
                # Process each image
                for img in product_images:
                    img_html = page.evaluate('(element) => element.outerHTML', img)
                    srcset = img.get_attribute('srcset')
                    alt = img.get_attribute('alt')

                    image_links = []
                    for src in srcset.split(","):

                        parts = src.split(" ")
                        for part in parts:
                            if "http" in part:
                                img_link = part.split("?")[0] if "?" in part else part
                                if img_link.strip() not in image_links:
                                    image_links.append(img_link.strip())

                products_info.append({
                    'pid': product_id,
                    'url': product_url,
                    'category': cat,
                    'title': product_title,
                    'image_links': image_links
                })

    browser.close()

    #save to json
    with open(SCRAPE_FILE_NAME, 'w') as f:
        json.dump(products_info, f, indent=4)

    print(f"Scraped {len(products_info)} products from {len(URLS)} categories")
