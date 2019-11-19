"""
An Selenium based Artstation crawler made by CY Hsu
"""
import selenium
from selenium import webdriver
from selenium import common
from selenium.webdriver.support.ui import WebDriverWait

ARTSTATION = 'https://www.artstation.com/'
ARTIST = 'funkysoul'

def UrlGenerator(mode):
    if mode is 'artist':
        return ARTSTATION + ARTIST, ARTIST
    elif mode is 'trending':
        return ARTSTATION + 'artwork?sorting=trending', 'Trending'
def main():
    #crawler setting
    folder_name = ARTIST
    url, dir = UrlGenerator(mode='artist')

if __name__ == '__main__':
    main()