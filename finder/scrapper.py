from bs4 import BeautifulSoup
import requests

def search_articles(brand, g_model, db_model):
    source = requests.get("https://instrumentos.mercadolibre.com.ar/instrumentos-cuerdas-guitarras-electricas/" + brand + "/usado/" + g_model).text

    soup = BeautifulSoup(source, "lxml")
    new_list = []
    for article in soup.find_all(class_="ui-search-layout__item"):
        instance = db_model(brand=brand, g_model=g_model)
        #disponible = True
        instance.title = article.h2.text
        instance.price = articulo.find(class_="price-tag").text
        instance.link = articulo.find("a")["href"]

        new_list.append(instance)
    
    return new_list