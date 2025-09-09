from bs4 import BeautifulSoup
import csv
ocie_html = "ocie.html"
ocie_csv = "ocie.csv"
with open(ocie_html, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")
table = soup.find("table", {"class": "BORDERTABLE"})
headers = [
    "MENU", "LIN", "SIZE", "CIC", "NOMENCLATURE", "PARTIAL NSN",
    "AU QTY", "OH QTY", "DO QTY", "PCS TRANS", "ETS TRANS", "ISSUING CIF"
]
rows = []
for tr in table.find_all("tr", {"class": "resultscell"}):
    cells = [td.get_text(strip=True) for td in tr.find_all("td")]
    rows.append(cells)
with open(ocie_csv, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    writer.writerows(rows)

print(f"Clothing record saved as {ocie_csv}")
