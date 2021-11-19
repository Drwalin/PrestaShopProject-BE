import urllib.request
import lxml.html as lh
import lxml.etree as et
import xml.dom.minidom as md
import hashlib
import os.path
import gzip
import json
import time
import sys

def url_cache_path(url):
    urlHash = hashlib.sha1(url.encode('utf-8')).hexdigest()
    return "htmlcache/"+urlHash+".html.gz"

def is_url_cached(url):
    return os.path.exists(url_cache_path(url))

def get_webpage_from_cache(url):
    if is_url_cached(url):
        with gzip.open(url_cache_path(url), "r") as file:
            return file.read()
    return None

def cache_webpage_content(url, content):
    try:
        os.mkdir("htmlcache")
    except FileExistsError:
        pass

    with gzip.open(url_cache_path(url), "w") as file:
        file.write(content.encode('utf-8'))
    pass        

def get_webpage(url):
    if is_url_cached(url):
        return get_webpage_from_cache(url)

    response = urllib.request.urlopen(url)
    content = response.read().decode('utf-8')
    cache_webpage_content(url, content)
    return content

def get_webpage_tree(url):
    content = get_webpage(url)
    return lh.fromstring(content)

class ProgressCounter:
    def __init__(self, numTasks):
        self.counter = 0
        self.numTasks = numTasks
        self.progressStr = ""

    def print_progress(self):
        print("\b" * len(self.progressStr), end='', flush=True)
        self.progressStr = "(%d/%d)" % (self.counter, self.numTasks)
        print(self.progressStr, end='', flush=True)
        self.counter += 1

    def end(self):
        self.print_progress()
        print("")




MAIN_URL = "https://etrapez.pl/kursy"

print("Fetching " + MAIN_URL + "...")
tree0 = get_webpage_tree(MAIN_URL)

pageLinks = tree0.xpath("//a[contains(@class, 'page-numbers')]")
pageURLs = set([a.get("href") for a in pageLinks])
pageURLs.add(MAIN_URL)
productURLs = []
products = []
fetchResult = dict()

progCounter = ProgressCounter(len(pageURLs))
print("Processing pages... ", end='')
for url in pageURLs:
    progCounter.print_progress()
    pageTree = get_webpage_tree(url)
    productLinks = pageTree.xpath("//a[contains(@class,'woocommerce-LoopProduct-link')]")
    productURLs.extend([a.get("href") for a in productLinks])
progCounter.end()


progCounter = ProgressCounter(len(productURLs))
print("Processing product pages... ", end='')
for url in productURLs:
    progCounter.print_progress()
    pageTree = get_webpage_tree(url)

    product = dict()

    titleNode = pageTree.xpath("//h1[contains(@class,'product_title entry-title')]")
    product["name"] = titleNode[0].text

    descNode = pageTree.xpath("//div[contains(@class,'woocommerce-product-details__short-description')]")
    product["description"] = lh.tostring(descNode[0]).decode('utf-8')

    priceNode = pageTree.xpath("//div[contains(@class,'summary')]//bdi")
    product["price"] = priceNode[0].text[:-1] + " PLN"

    imgNode = pageTree.xpath("//div[contains(@class,'feat_image')]/a[1]")
    product["imageURL"] = imgNode[0].get("href")

    fetchResult[hashlib.sha1(url.encode('utf-8')).hexdigest()] = product
progCounter.end()

print("Saving JSON...")
with open("shop.json", "w") as outFile:
    outFile.write(json.dumps(fetchResult, indent=4))

print("done")
