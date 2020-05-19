import requests
import bs4
import csv

# banks will come #
res = requests.get('https://banksifsccode.com/all-banks.php')

soup = bs4.BeautifulSoup(res.text,'lxml')
links = soup.select('.bLists a')
file = open("d:/scrapbank/banks.csv","w")
for link in links:
    banks = link.get('href')
    writer = csv.writer(file)
    writer.writerow(banks)
file.close()
