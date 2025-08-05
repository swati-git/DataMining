import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"
# Step 1: Send a GET request to the specified URL
response = requests.get(url)

#print(f"Response: {response.text[:1000]}...")  # Print the first 100 characters of the response for debugging
soup = BeautifulSoup(response.text, 'html.parser')

with open("books_bs4_html.txt", "w", encoding="utf-8") as file:
     file.write(str(soup))
print("Page content has been saved to books_bs4_html.txt")

books_data = []
for book in soup.find_all("article", class_="product_pod"):
    title = book.h3.a["title"]
    rating = book.find("p", class_="star-rating")["class"][1]
    price = book.find("p", class_="price_color").text.strip()
    books_data.append({"Title": title, "Rating": rating, "Price": price})

for book in books_data:
    print(book)

df = pd.DataFrame(books_data)

# # Display the resulting DataFrame
print(df)