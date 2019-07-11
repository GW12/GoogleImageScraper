# GoogleImageScraper
Main Aim: Download images from google based on search. 
This module allows you to choose your search, download folder and no. of images. 

Code example using module:

import scrapeImages as scrape
query = input("Search")
foldername = input("Foldername:")
max_images = input("No. of images:")
scrape.main(query, foldername, max_images)
