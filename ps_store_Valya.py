import requests
from bs4 import BeautifulSoup as bs 

for i in range(1, 6):
	html_code = requests.get('https://store.playstation.com/ru-ru/grid/STORE-MSF75508-PRICEDROPSCHI/1')

	soup = bs(html_code, 'lxml')

	for product in soup.findAll('div', {'class':'grid-cell grid-cell--game'}):
		product_name = product.find('div', {'class':'grid-cell__tite'}).span.text
		product_not_sale_price = product.find('div', {'class':'price'}).text
		product_sale_price = product.find('h3', {'class':'price-display__price'}).text
		product_image = product.find('div', {'class':'product-image__img product-image__img--main'}).img.get('src')
		print(product_name)
		print(product_name)
		print('Цена без скидки '+product_not_sale_price)
		print('Цена со скидкой '+product_sale_price)
		print('https://store.playstation.com' + product.a.get('href'))

