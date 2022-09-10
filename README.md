# Mission_to_Mars
I created a website that renders Mars data scraped from four different informational websites about Mars.

## Step 1: Scraping the information from

* Mars New Site: https://redplanetscience.com/
* Mars Images site: https://spaceimages-mars.com/
* Mars Facts page: https://galaxyfacts-mars.com/
* Mars Hemispheres images: https://marshemispheres.com/

#### 1a: Mars New Site: https://redplanetscience.com/
* Get the latest article title
* Get the latest article description paragraph

#### 1b: Mars Images site: https://spaceimages-mars.com/
* Get the URL for the featured Mars image (full sized)

#### 1c: Mars Facts page: https://galaxyfacts-mars.com/
* Get the table comtaining Mars facts (diamter, mass, etc)*
* Use Pandas to convert to and HTML table string

###### *Note: I selected the table with just Mars facts, not the one with earth and Mars since this project is on Mars

####  1d: Mars Hemispheres images: https://marshemispheres.com/
* Get the urls for each of the hemispheres (full resolution image)
* Store the hemisphere title and URL string to a list with one dictionary for each hemisphere

## Step 2:
* Create python file with the scrape function (scrape_mars.py) which completes all of the sub-steps for step 1.
* Put the gathered data in to a mongo db collection to be retrieved by the Flask app

## Step 3:
* Created the Flask app (app.py) with 2 routes
    * Index Route:  Main page rendering the data in the mongo db and containing button to call the Scrape Route
    * Scrape Route: Runs the python scrape function and then sends the dictionary returned to a mongo db and reroutes to the Index Route for display

    