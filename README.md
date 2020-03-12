# ArtstationCrawler
An [Artstation](https://www.artstation.com/)  crawler made specific for downloading images, now supporting:
* Artists profile
* Search results
### Requirements
* **Python 3**
* **Selenium**: `pip install selenium`
* **Latest Chrome and [ChromeDriver](https://chromedriver.chromium.org/downloads)** : Unzip and put in the same directory as ArtstationCrawler.py.
### How to use
#### Artist mode
`python ArtstationCrawler.py -a [Artist username]` or `python ArtstationCrawler.py --artist [Artist username]`
#### Search mode
`python ArtstationCrawler.py -s [Search terms]` or `python ArtstationCrawler.py -search [Search terms]`
### Examples
#### Artist mode
```
> python ArtstationCrawler.py -a cyhsu
Fetching artworks from https://www.artstation.com/cyhsu
Fetched 4 links.
Found 4 projects with 8 images...
Download Completed.
```
#### Search Mode
```
> python ArtstationCrawler.py -s baby elephant
Fetching artworks in https://www.artstation.com/search?q=baby%20elephant&sort_by=relevance.
Fetched 81 links.
Found 81 projects with 175 images...
Download Completed.
```
