import bs4
from urllib import request
import pandas as pd

dico_auchan = {}

for i in range(0,10):
    req = request.Request('https://www.auchan.fr/enfant/vetement-garcon-2-14-ans/tee-shirt-polo-chemise/c-8625363?sort=position-asc&engine=fh&show=FORTY_EIGHT&page=' + str(i),
                                         headers={'User-Agent': 'Mozilla/5.0'})

    request_text = request.urlopen(req).read()


    page = bs4.BeautifulSoup(request_text, 'lxml') #transformation en page html

    page_clothes = page.findAll('article', attrs = {})



    for clothe in page_clothes[10:11]:
        name_tag = clothe.find(['meta', 'alt'])
        name_clothe = name_tag['alt']
        image_tag = clothe.find(['img', 'alt'])
        image_clothe = image_tag['data-srcset'].split('//')
        image_clothe = image_clothe[-1]
        image_clothe = image_clothe[:len(image_clothe)-5]
        dico_auchan[name_clothe] = image_clothe

    data_auchan = pd.DataFrame.from_dict(dico_auchan, orient='index')

data_auchan.columns = ['Image']
data_auchan.rename_axis('Name')
