# Import Splinter to automate browser actions
from splinter import Browser

# Import Beautiful Soup
from bs4 import BeautifulSoup

# Import the Chromedriver
from webdriver_manager.chrome import ChromeDriverManager

# Import the others
import pandas as pd
import time
import requests
import os

def scrape():
# ---------------------------------------------------------------------#
    #### 1a Mars News Site - Get latest news article and desc ####
# ---------------------------------------------------------------------#
    #Open the browswer window - set up splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    # set URL to scrape
    url = 'https://redplanetscience.com/'

    # open the page in browswer
    browser.visit(url)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    #Locate the section containing the news articles
    container = soup.find('section', class_='image_and_description_container')

    #Locate the title and descriptive paragraph for the first article and save to variables
    news = container.find('div', class_='content_title').text
    news_p = container.find('div', class_='article_teaser_body').text

    browser.quit()
# ---------------------------------------------------------------------#
    #### 1b Mars Images - Get the featured Mars image ####
# ---------------------------------------------------------------------#

    #Open the browswer window - set up splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    # set URL to scrape
    url = 'https://spaceimages-mars.com/'

    # open the page in browswer
    browser.visit(url)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    #find the image url
    image = soup.find('div', class_ = "floating_text_area").a['href']
    featured_image_url = f'{url}{image}'

    browser.quit()
# ---------------------------------------------------------------------#
    #### 1c Mars Facts - Get and convert Mars facts table to HTML ####
# ---------------------------------------------------------------------#
    #set url
    url = 'https://galaxyfacts-mars.com/'

    #use pandas to find all tables on the page
    tables = pd.read_html(url)

    #select the second table since it is in a side bar and there is one on the main page
    df = tables[1]

    #Turn the dataframe into HTML
    html_table = df.to_html(classes = 'table table-stripped', header=False, index=False)
# ---------------------------------------------------------------------#
    #### 1d Mars Hemisphere images - Get urls for hemisphere images ####
# ---------------------------------------------------------------------#
    # Stack Overflow URL to scrape
    url = 'https://marshemispheres.com/'

    # Retrieve page with the requests module
    response = requests.get(url)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(response.text, 'html.parser')

    #find section with the Hemisphere pages
    results = soup.find_all('div', class_='item')
    hemisphere_image_urls = []  
        
    #for each Hemisphere
    for result in results:
        #find the address for the hemisphere page and get hemi name
        webadd = result.a['href']
        hemi_name=result.find('h3').text
        
        #Open the browswer window - set up splinter
        executable_path = {'executable_path': ChromeDriverManager().install()}
        browser = Browser('chrome', **executable_path, headless=True)
        
        # set URL to scrape
        hemi_url = url + webadd
        
        # open the page in browswer
        browser.visit(hemi_url)
        
        # Create BeautifulSoup object; parse with 'html.parser'
        hemi_html = browser.html
        hemi_soup = BeautifulSoup(hemi_html, 'html.parser')

        #find the url
        hemi_image = hemi_soup.find('img', class_='wide-image')['src']
        hemi_image_url = url+hemi_image
        
        # Dictionary to be inserted into list
        hemi_dict = {
            'title' : hemi_name,
            'img_url' : hemi_image_url
        }
        
        #Append dictionary to list
        hemisphere_image_urls.append(hemi_dict)
            
        #Close Broswer
        browser.quit()

# ---------------------------------------------------------------------#  
    # Populate the dictionary with key-value pairs for Mars info and images
    # Create an empty dict for listings that we can save to Mongo
    MarsInfo = {}
    MarsInfo["NewsArtTitle"] = news
    MarsInfo["NewsArtDesc"] = news_p 
    MarsInfo["FeatImage"] = featured_image_url 
    MarsInfo["FactTable"] = html_table
    MarsInfo["HemiImages"] = hemisphere_image_urls 

    # Return our populated dictionary
    return MarsInfo
