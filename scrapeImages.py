from bs4 import BeautifulSoup
import requests
import os
import sys


# adapted from http://stackoverflow.com/questions/20716842/python-download-images-from-google-image-search

def get_soup(url):
    return BeautifulSoup(requests.get(url).text, 'lxml')

def main(query, originalname, max_images):
    
    query1 = query.split()
    query2 ='+'.join(query1)
    queryfile = ''.join(query1)
    url="https://www.google.co.in/search?q="+query2+"&source=lnms&tbm=isch"
    print(url)
    
    soup = get_soup(url)
    ImageSources=[]
    listimg = []
    listfilename = []
    count = 1
    for img in soup.find_all('img', alt = "Image result for {}".format(query)):
        listimg.append(img)   
    for i in listimg:
        if count<= int(max_images):
            src = listimg[count-1].get('src')
            ImageSources.append(src)
            filename = "{}/{}{}.jpg".format(originalname, originalname, str(count))
            if not os.path.exists(os.path.dirname(filename)):
                os.makedirs(os.path.dirname(filename))

            output = open(filename, "wb")
            output.write(requests.get(src).content)
            output.close()
            listfilename.append(filename)
            with open("Facenames.txt", "r") as f:
                text = f.read()
                if originalname not in text:
                    print("Adding to text file")
                    register = open("Facenames.txt", "a")
                    register.write(originalname + "\n")
                    register.close()
                        
                
                
            count+=1
    
def user():
    query = input("Search:")
    originalname = input("Foldername:")
    max_images = input("No. of images")
    main(query, max_images, originalname)
