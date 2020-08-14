import requests
from bs4 import BeautifulSoup
from csv import writer

source = requests.get('https://www.newegg.ca/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=7708').text

soup = BeautifulSoup(source, 'html.parser')

items = soup.find_all('div', class_='item-cell')

with open('graphicsCards.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Title', 'Price Was', 'Price Now', 'Rating', 'Amount of Ratings', 'Link']
    csv_writer.writerow(headers)

    for item in items:
        title = item.find('img')['title']
        link = item.find('a')['href']
        priceWas = item.select('.price-was')[0].get_text()
        priceCurrent = item.select('.price-current')[0].get_text()
        rating = item.find(class_='item-branding').contents[1]['title']
        amountOfRatings = item.select('.item-rating')[0].get_text()
        csv_writer.writerow([title, priceWas, priceCurrent, rating, amountOfRatings, link])
