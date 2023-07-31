import sys

import requests
from bs4 import BeautifulSoup

sys.path.append(
    r"C:\Users\Storm1050\Desktop\Dossier\ProjetPerso\Python\WikiPython\FlaskBackend"
)
from src.database.simple_database import WikiPythonDB
from src.utils.terminal import clean_terminal

# from database import SimpleSQLiteDB


def extract_hrefs_from_url(url):
    try:
        # Send an HTTP request to the URL and get the HTML content
        response = requests.get(url, timeout=5000)
        response.raise_for_status()  # Check if the request was successful
        html_content = response.text

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, "html.parser")
        div_element = soup.find("div", {"role": "main"})
        # Find all elements with 'href' attribute
        hrefs = [link["href"] for link in div_element.find_all("a", href=True)]

        return hrefs
    except requests.exceptions.RequestException as e:
        print("Error occurred while fetching the URL:", e)
        return []


def main():
    # db = SimpleSQLiteDB()
    # Replace 'your_url_here' with the URL you want to extract hrefs from
    # list_of_version = [f"3.{i}" for i in range(5, 14)]
    version = "3.13"
    url_with_all_links = f"https://docs.python.org/{version}/genindex-all.html"
    hrefs = extract_hrefs_from_url(url_with_all_links)
    # Print the extracted hrefs
    # {'howto', 'whatsnew', 'distributing', 'c-api', 'faq', 'tutorial', 'using', 'extending', 'library', 'reference', 'install'}
    db = WikiPythonDB("WikiPython.db")
    with db:
        db.init_db()
        for href in hrefs:
            full_url = f"https://docs.python.org/3.13/{href}"
            val = href.split("/")
            if len(val) > 1:
                category = val[0]
                db.insert_data_python_wiki_db(
                    python_version=version,
                    category_name=category,
                    reference_url=full_url,
                )
            else:
                # glossary.html#term-triple-quoted-string
                if "glossary.html" in href:
                    category = "glossary"
                    db.insert_data_python_wiki_db(
                        python_version=version,
                        category_name=category,
                        reference_url=full_url,
                    )


if __name__ == "__main__":
    clean_terminal()
    main()
