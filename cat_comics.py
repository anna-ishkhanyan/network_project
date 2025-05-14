import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
from io import BytesIO

COMICS = {
    "1": ("Garfield", "https://www.gocomics.com/garfield"),
    "2": ("Breaking Cat News", "https://www.gocomics.com/breaking-cat-news"),
    "3": ("Cat's Cafe", "https://www.gocomics.com/cats-cafe"),
    "4": ("Cattitude — Doggonit", "https://www.gocomics.com/cattitude-doggonit"),
    "5": ("Fat Cats", "https://www.gocomics.com/fat-cats"),
    "6": ("Kliban's Cats", "https://www.gocomics.com/klibans-cats")
}

def get_comic_choice():
    print("Pick a comic:")
    for key, (name, _) in COMICS.items():
        print(f"{key}. {name}")
    return input("Your choice: ").strip()

def scrape_comic_page(url):
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    page = driver.page_source
    driver.quit()
    return page

def find_comic_image_url(page_html):
    soup = BeautifulSoup(page_html, "html.parser")
    for img in soup.find_all("img"):
        classes = img.get("class", [])
        if ("Comic_comic__image__6e_Fw" in classes and
            "Comic_comic__image_isStrip__eCtT2" in classes and
            img.get("fetchpriority") == "high"):
            srcset = img.get("srcset")
            if srcset:
                return srcset.split(",")[-1].split()[0].replace("&amp;", "&")
    return None

def save_image(img_url, filename):
    try:
        response = requests.get(img_url, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code == 200:
            img = Image.open(BytesIO(response.content)).convert("RGB")
            img.save(filename, "JPEG")
            print(f"Saved to {filename}")
        else:
            print("Couldn’t fetch the image.")
    except Exception as err:
        print("Something went wrong:", err)

def main():
    choice = get_comic_choice()
    if choice not in COMICS:
        print("Not a valiid option")
        return

    date = input("Date in format  (YYYY-MM-DD): ").strip()
    name, base_url = COMICS[choice]
    url = f"{base_url}/{date.replace('-', '/')}"

    print(f"Getting   {name} for {date}...")

    html = scrape_comic_page(url)
    img_url = find_comic_image_url(html)

    if img_url:
        filename = f"{name.replace(' ', '_')}_{date}.jpg"
        save_image(img_url, filename)
    else:
        print("No comic was found for that date")

if __name__ == "__main__":
    main()
