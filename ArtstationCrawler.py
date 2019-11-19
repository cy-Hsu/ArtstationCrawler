"""
An Selenium based Artstation crawler made by CY Hsu
"""
import os
import selenium
from selenium import webdriver
from selenium import common
from selenium.webdriver.support.ui import WebDriverWait
import requests
import re

#Webdriver setting
opt = webdriver.ChromeOptions()
opt.add_argument("disable-extensions")
driver = webdriver.Chrome(chrome_options=opt)
#crawler setting
ARTSTATION = 'https://www.artstation.com/'
ARTIST = 'eventrue'
mode = 'artist'
#page setting
total_scrolls = 5000
current_scrolls = 0
scroll_time = 3
    
def UrlGenerator(mode):
    if mode is 'artist':
        return ARTSTATION + ARTIST, ARTIST
    elif mode is 'trending':
        return ARTSTATION + 'artwork?sorting=trending', 'Trending'

def check_height():
    new_height = driver.execute_script("return document.body.scrollHeight")
    return new_height != old_height

def scroll():
    global old_height
    current_scrolls = 0

    while (True):
        try:
            if current_scrolls == total_scrolls:
                return

            old_height = driver.execute_script("return document.body.scrollHeight")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            WebDriverWait(driver, scroll_time, 0.05).until(lambda driver: check_height())
            current_scrolls += 1
        except selenium.common.exceptions.TimeoutException:
            break

    return

def getlinks():
    scroll()
    try:
        links = driver.find_elements_by_xpath('//a[@class="project-image"]')
        links = links[int(len(links) / 2):]
        print('fetched %d links' % len(links))
    except selenium.common.exceptions.NoSuchElementException:
        print('no links fetched')
    return links

def grabber(links):
    titles = []
    images = []
    nImg = 0
    urls = []
    for link in links:
        url = link.get_attribute('href')
        urls.append(url)
    for projectUrl in urls:
        #navigate to each project
        driver.get(projectUrl)
        #grabbing
        try:
            text = driver.find_element_by_xpath('//h1[@ng-bind-html="project.title"]').text
            imgs = driver.find_elements_by_xpath('//img[@class="img"]')
            if len(imgs) < 1: 
                print('no images found in: %s' % projectUrl)
            imgSrcs = []
            for img in imgs:
                src = img.get_attribute('src')
                imgSrcs.append(src)
            titles.append(text)
            images.append(imgSrcs)
            nImg += len(imgSrcs)
        except  selenium.common.exceptions.NoSuchElementException:
            print('no title/images fetched')
        driver.back()
    assert len(titles) == len(images), 'unmatched projects and titles'
    #downloading
    print('downloading %d projects with %d images...' % (len(titles), nImg))
    for idx in range(len(images)):
        titles[idx] = re.sub('[^A-Za-z0-9]+', ' ', titles[idx])
        project = images[idx]
        if len(project) is 1:
            imgName = titles[idx] + '.jpg'
        else:
            if os.path.exists(titles[idx]) is not True:
                os.mkdir(titles[idx])
            os.chdir(titles[idx])
        for img in project:
            try:
                r = requests.get(img)
                if len(project) is not 1:
                    imgName = img.split('/')[-1].split('.jpg')[0] + '.jpg'
                with open(imgName, 'wb') as outfile:
                    outfile.write(r.content)
            except Exception as e:
                print(str(e))
                print('skipped %s' % imgName)
        if len(project) is not 1:
            os.chdir('..')
    print('finish')

def main():
    url, dir = UrlGenerator(mode)
    if os.path.exists(dir) is not True:
        os.mkdir(dir)
    os.chdir(dir)
    driver.get(url)
    projects = getlinks()
    grabber(projects)

if __name__ == '__main__':
    main()