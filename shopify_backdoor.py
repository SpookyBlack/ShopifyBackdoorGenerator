import requests
from bs4 import BeautifulSoup


base_url = raw_input("Shopify Link >>  ") #Link to Shopify product page
xml_link = base_url + ".xml" #Accesses xml of product

cart_array = base_url.split(".") #Splits the url to get store name
cart_link = "www." + cart_array[1] + ".myshopify.com/cart/" #Creates basic cart link, just need to add the variants & quantity
print cart_link

quantity = raw_input("Enter Product Quantity >>  ") #Quanity for creating link

r = requests.get(xml_link)
soup = BeautifulSoup(r.text, 'html.parser')

print "PRODUCT NAME:  %r" %(soup.find("title").getText()) #Prints the name of the desired product

title_array = []

for i in soup.find_all('title'):
	title_array.append(i.getText())
	
del title_array[0]#Deleted the first title in the array as that will be a repeat of the product name and will mess with order

id_array = []

for i in soup.find_all('id'):
	id_array.append(i.getText())

del id_array[0]
	
i = 0
while (i < len(title_array)):
	print title_array[i], id_array[i]
	print str(cart_link) + str(id_array[i]) + ":" + str(quantity)
	print "------------------------------------------------------ \n"
	i = i + 1
