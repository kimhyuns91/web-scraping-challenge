#Imports
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape():
    #Opening browser
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=True)

    ### Scraping Title and Paragraphs ###

    mars_data ={}

    #NASA Website
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    #Grabbing code for the title and the paragraph
    results = soup.find_all('li', class_='slide')

    news_title=[]
    news_p=[]

    #Storing in a list
    for result in results:
        news_title.append(result.find(class_='content_title').get_text())
        news_p.append(result.find(class_='article_teaser_body').get_text())

    mars_data['news_title'] = news_title
    mars_data['news_p'] = news_p
    
    #Storing in a list
    for result in results:
        news_title.append(result.find(class_='content_title').get_text())
        news_p.append(result.find(class_='article_teaser_body').get_text())

    mars_data['news_title'] = news_title
    mars_data['news_p'] = news_p






    ### Scraping Images ###
    
    #Opening Browser    
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    
    html = browser.html
    soup = BeautifulSoup(html, "html.parser") 

    #Grabbing the code for images
    results = soup.find_all('a', class_='fancybox')
        
    featured_image_url=[]
    
    #Storing in the list
    for result in results:
        featured_image_url.append('https://www.jpl.nasa.gov'+result['data-fancybox-href'])


    mars_data['featured_image_url'] = featured_image_url



    #### Scraping temperature from twitter ###
    
    #Opening Browser            
    url ='https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    time.sleep(5)
    
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    #Grabing Code for the temperature
    results3 = soup.find_all('article', attrs ={'role':'article'})
    weather_text=results3[0].find_all('span', attrs = {'class':'css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0'})
  
    #Storing string in a variable
    weather_text_cleaned=weather_text[4].text.replace('\n', ' ')

    mars_data['mars_weather'] = weather_text_cleaned




    ### Scrapping Facts on Mars ###

    #Opening URL
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)
    
    #Selecting Table
    facts=tables[0]
    
    #Removing the colon
    facts[0]=facts[0].str.strip(":")

    #Adding column labels
    facts.columns=['Facts', 'Values']

    #Add Index
    facts_df=facts.set_index('Facts')
    facts_df

    #convert to html table format
    html_table=facts_df.to_html()

    mars_data["html_table"] = html_table




    ### Scraping Mars Hemispheres###

    #Opening Broswer
    base_url='https://astrogeology.usgs.gov'
    url ='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    time.sleep(5)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    results4 = soup.find_all('div', class_='description')

    title=[]
    links=[]

    #Saving title/initial address for image
    for result in results4:
        title.append(result.find('h3').text)
        links.append(base_url+result.find('a')['href'])

        
    img_url=[]

    #Saving full image link
    for link in links:
        url = link
        browser.visit(url)

        html = browser.html
        soup = BeautifulSoup(html, "html.parser")
        
        img_url.append(base_url + soup.find('img', class_="wide-image")['src'])


    #Creating a dictionary
    hemisphere_image_urls ={'title':title,
                        'img_url':img_url}


    mars_data["hemisphere_image_urls"] = hemisphere_image_urls


    return mars_data