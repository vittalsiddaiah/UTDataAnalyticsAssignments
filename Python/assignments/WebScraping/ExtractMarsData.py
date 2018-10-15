################################################################################
# Dependencies
################################################################################
import pandas as pd
import multiprocessing as mp
from bs4 import BeautifulSoup
from splinter import Browser
import requests
import pymongo
import time
import re
################################################################################

################################################################################
class Mars:
    __hemiUrls = []
    __results = ''
    def __init__(self):
        return
    def __del__(self):
        return
    def Data(self):
        return self.__results
    ################################################################################
    ################################################################################
    def __OpenSite__(self, url):
        chromeDriverPath = {"executable_path":"/usr/local/bin/chromedriver"}
        browser = Browser("chrome", **chromeDriverPath, headless = False)
        browser.visit(url)
        return browser
    ################################################################################
    ################################################################################
    def News(self, link, queDescriptor):
        print("News...")
        browser = self.__OpenSite__(link)
        soup = BeautifulSoup(browser.html, 'html.parser')
        title = soup.find('div','content_title','a').text
        browser.quit()
        print("News Completed...")
        queDescriptor.put({  "news": soup.find('div', class_ = 'article_teaser_body').text })
        return
    ################################################################################
    ################################################################################
    def Image(self, link, queDescriptor):
        print("Image...")
        browser = self.__OpenSite__(link)
        time.sleep(10)
        browser.click_link_by_partial_text('FULL IMAGE')
        time.sleep(10)
        browser.click_link_by_partial_text('more info')
        time.sleep(10)
        webData   = BeautifulSoup(browser.html, 'html.parser').find('article')
        browser.quit()
        print("Image Completed...")
        queDescriptor.put({ "image": "https://www.jpl.nasa.gov" + webData.find('figure', 'lede').a['href'] })
        return

    ################################################################################
    ################################################################################
    def Weather(self, link, queDescriptor):
        print("Weather...")
        browser = self.__OpenSite__(link)
        soup = BeautifulSoup(browser.html, "html.parser")
        marsWeather=soup.find(string=re.compile("Sol"))
        browser.quit()
        print("Weather Completed...")
        queDescriptor.put({"weather": re.sub(r'\,', ";", marsWeather)})
        return
    ################################################################################
    ################################################################################
    def Profile(self, link, queDescriptor):
        print("Profile...")
        browser = self.__OpenSite__("https://space-facts.com/mars/")
        soup = BeautifulSoup(browser.html,'html.parser')
        marsProfile = {}
        for val in soup.find('tbody').find_all('tr'):
            key = val.find('td', 'column-1').text.split(":")[0]
            value = val.find('td', 'column-2').text
            marsProfile[key] = value
        df = (pd.DataFrame([marsProfile]).T).reset_index()
        df.columns=['Attributes','Details']
        html_data = (df.to_html()).replace("\n","").replace("\\n","")
        print("Profile Completed...")
        browser.quit()
        queDescriptor.put({"profile": html_data})
        return
    ################################################################################
    ################################################################################
    def HemiLinks(self, partialText, title, keyName, queDescriptor):
        print(title + " ...")
        browser = self.__OpenSite__("https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars")
        time.sleep(5)
        browser.click_link_by_partial_text(partialText)
        time.sleep(5)
        soup = BeautifulSoup(browser.html, 'html.parser')   # Create BeautifulSoup object; parse with 'html.parser'
        link = soup.find('div', 'downloads').a['href']   # Store link
        # Create dictionary
        result = {
            "title": title,
            "img_url": link
        }
        print(title + " Completed...")
        browser.quit()
        queDescriptor.put({keyName:result})
        return
    ################################################################################
    ################################################################################
enQueue = mp.Queue()
def ExtractMarsData():
    procs = []
    procs.append(mp.Process(target=Mars().Image, args=("https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars",enQueue)))
    procs.append(mp.Process(target=Mars().News, args=("https://mars.nasa.gov/news/",enQueue,)))
    procs.append(mp.Process(target=Mars().Weather, args=("https://twitter.com/marswxreport?lang=en",enQueue,)))
    procs.append(mp.Process(target=Mars().Profile, args=("https://space-facts.com/mars/",enQueue,)))
    procs.append(mp.Process(target=Mars().HemiLinks, args=("Valles Marineris Hemisphere Enhanced","Valles Marineris Hemisphere", "velles", enQueue,)))
    procs.append(mp.Process(target=Mars().HemiLinks, args=("Cerberus Hemisphere Enhanced","Cerberus Hemisphere","cerberus",enQueue,)))
    procs.append(mp.Process(target=Mars().HemiLinks, args=("Schiaparelli Hemisphere Enhanced","Schiaparelli Hemisphere","schiaparelli",enQueue,)))
    procs.append(mp.Process(target=Mars().HemiLinks, args=("Syrtis Major Hemisphere Enhanced","Syrtis Major Hemisphere","syrtis",enQueue,)))
    print("Parallelism Start")
    print("Started Scraping")
    print("------------------------------")
    for proc in procs: proc.start()
    print("------------------------------")
    for proc in procs: proc.join()
    print("Parallelism Ended")
    data = {}
    while not enQueue.empty(): data.update(enQueue.get_nowait())
    return data
