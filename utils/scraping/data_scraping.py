from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from bs4 import BeautifulSoup
import urllib
import os
import time



def scrap_garments(garment_classes,save_path,chromedriver_path):

    """
        Constructs all the necessary attributes for the person object.
        Performs the data scraping for inputed garment classes.
        Saves the data in specified path with a specific folder structure : each class data points in an eponym repertory.

        Parameters
        ----------
            garment_classes : arr
                array containing garment classes to be web-scraped
            save_path : str
                save path for the web-scraped data
            chromedriver_path : str
                path for the local chromedriver/firefox executable
        
    """

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')


    driver = webdriver.Chrome(executable_path=chromedriver_path,options=chrome_options)


    t1 = time.time()

    print ('*'* 10 + ' DATASET ACQUISITION ' + '*'* 10)
    for garment in garment_classes:
        
        print('*'* 5 + ' {} Images Scraping '.format(garment) + '*'* 5)
 
        os.makedirs('{}/{}/'.format(save_path,garment))
        
        # Initializing the first target page for the selected garment
        driver.get('https://www.auchan.fr/recherche?text={}&engine=fh&categorylevel1=categorylevel120160914933'.format(garment))
        # Making sure Chrome has the time to catch all the page source code
        time.sleep(1)
        # Grabing source code and transforming it into convenient soup
        source = driver.page_source
        soup = BeautifulSoup(source)
       
        while True:
            try:

                for img in soup.select('#wrapper > div.product-list--container.grid > article > div > a > span.product-item--imgFlapContainer > img'):
                    print('*'* 5)
                    
                    print('Product : {}'.format(img['alt'][:50]))

                    try:
                        img_link = img['data-src']

                    except KeyError:
                        img_link = img['src']

                    img_path = '{}/{}/{}'.format(save_path,garment,img_link[-22:-19]+img_link[-18:])

                    urllib.request.urlretrieve(img_link,img_path)
                    print('Article Ddl Done !')
                    
                
                WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#wrapper > nav > div > a.ui-pagination--next"))).click()

                
                time.sleep(1)

                source = driver.page_source
                soup = BeautifulSoup(source)
                    
                    
                    
                    
            except (NoSuchElementException,TimeoutException):
                t2 = time.time()
                
                print('\n' + '*'* 5 + 'Scraping Sucessful!' + '*'* 5)
                print('Done in {} mins !'.format((t2-t1)/60))
                
                break

if __name__ == '__main__':

    save_path = 'yourpath'
    chromedriver_path = 'yourpath'

    scrap_garments(['tshirt','pantalon','pull','short'],save_path,chromedriver_path)
