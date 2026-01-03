import tkinter as tk
import requests, csv
from bs4 import BeautifulSoup

def scrape():
    url = entry_url.get()   # USER INPUT
    soup = BeautifulSoup(requests.get(url).text, "html.parser")

    with open("products.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Price", "Rating"])

        for p in soup.find_all("article", class_="product_pod"):
            name = p.h3.a["title"]
            price = p.find("p", class_="price_color").text
            rating = p.p["class"][1]
            writer.writerow([name, price, rating])

    status.set("Saved to products.csv")

root = tk.Tk()
root.title("Web Scraper")

tk.Label(root, text="Enter Website URL").pack()
entry_url = tk.Entry(root, width=40)
entry_url.pack()
entry_url.insert(0, "https://books.toscrape.com/")

tk.Button(root, text="Scrape Products", command=scrape).pack()

status = tk.StringVar()
tk.Label(root, textvariable=status).pack()

root.mainloop()
