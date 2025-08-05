# Book Details Web Scraper

This project demonstrates how to scrape book details (Title, Rating, and Price) from [Books to Scrape](https://books.toscrape.com/) using Python, BeautifulSoup, and pandas.

## Features

- Fetches the main page of the website.
- Extracts book titles, ratings, and prices.
- Saves the HTML content locally.
- Outputs the extracted data as a pandas DataFrame.

## Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the script:

    ```bash
    python extract_book_details.py
    ```

2. The script will:
    - Download the main page HTML and save it as `books_bs4_html.txt`.
    - Print each book's details.
    - Display a DataFrame of all extracted books.

## Files

- `extract_book_details.py`: Main scraping script.
- `requirements.txt`: Python dependencies.
- `books_bs4_html.txt`: Saved HTML content from the website (generated after running the script).

## Notes

- This script scrapes only the first page of the website.
- For educational and demonstration purposes only.

---