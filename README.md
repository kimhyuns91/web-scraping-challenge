# Web Scraping Homework - Mission to Mars

In this project, a web application will be built that contains the scrapes of various websites for data related to the Mission to Mars and displays the information in a single HTML page.


## Step 1 - Scraping

Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter will be used for scraping.


### NASA Mars News

* Scraping [NASA Mars News Site](https://mars.nasa.gov/news/) to collect the latest News Title and Paragraph Text. 


### JPL Mars Space Images - Featured Image

* Visiting the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).

* Using splinter to navigate the site and find the image url for the current Featured Mars Image


### Mars Weather

* Visiting the Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en) to scrape the latest Mars weather tweet from the page. 

### Mars Facts

* Visiting the Mars Facts webpage [here](https://space-facts.com/mars/) and using Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.


### Mars Hemispheres

* Visiting the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.


- - -

## Step 2 - MongoDB and Flask Application

Using MongoDB with Flask templating, a new HTML that displays all of the information that was scraped from the URLs above will be created.

![](Mission_to_Mars/Screenshot/Web_Page.png)
