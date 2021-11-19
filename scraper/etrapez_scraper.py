import urllib.request
import lxml.html as lh
import lxml.etree as et
import xml.dom.minidom as md
import hashlib
import os.path
import gzip
import json
import csv
import time
import sys

def url_cache_path(url):
    urlHash = hashlib.sha1(url.encode('utf-8')).hexdigest()
    return "httpcache/"+urlHash+".gz"

def is_url_cached(url):
    return os.path.exists(url_cache_path(url))

def get_resource_from_cache(url):
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

def get_resource(url):
    if is_url_cached(url):
        return get_resource_from_cache(url)

    response = urllib.request.urlopen(url)
    content = response.read().decode('utf-8')
    cache_webpage_content(url, content)
    return content

def get_webpage_tree(url):
    content = get_resource(url)
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
fetchResult = []

progCounter = ProgressCounter(len(pageURLs))
print("Processing pages... ", end='')
for url in pageURLs:
    progCounter.print_progress()
    pageTree = get_webpage_tree(url)
    productLinks = pageTree.xpath("//a[contains(@class,'woocommerce-LoopProduct-link')]")
    productURLs.extend([a.get("href") for a in productLinks])
progCounter.end()

categories = dict()

progCounter = ProgressCounter(len(productURLs))
print("Processing product pages... ", end='')
for url in productURLs:
    progCounter.print_progress()
    pageTree = get_webpage_tree(url)

    product = dict()
    product["Enabled"] = 1

    titleNode = pageTree.xpath("//h1[contains(@class,'product_title entry-title')]")
    product["Name"] = titleNode[0].text

    descNodes = pageTree.xpath("//div[contains(@class,'woocommerce-product-details__short-description')]/descendant-or-self::*/text()")
    product["Short desc."] = ''.join(descNodes).replace(u"\u00a0", " ")
    catNodes = pageTree.xpath("//nav[contains(@class, 'woocommerce-breadcrumb')]//a")
    catstr = ""
    for i in range(1, len(catNodes)):
        catName = catNodes[i].text
        if catName not in categories:
            categories[catName] = str(len(categories)+3)

        catstr += categories[catName]
        if i < len(catNodes)-1:
            catstr += ","
    product["Categories"] = catstr
    #product["Categories"] = catNodes[1].text + ", " + catNodes[2].text

    priceNode = pageTree.xpath("//div[contains(@class,'summary')]//bdi")
    product["Price"] = priceNode[0].text[:-1] + " PLN"

    imgNode = pageTree.xpath("//div[contains(@class,'feat_image')]/a[1]")
    product["Images URL"] = imgNode[0].get("href")

    fetchResult.append(product)
progCounter.end()

with open("items.csv", "w") as fcsv:
    fieldnames = fetchResult[0].keys()
    writer = csv.DictWriter(fcsv, delimiter=';', fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(fetchResult)

categoriescsv = [{"ID": categories[key], "Name": key} for key in categories]

with open("categories.csv", "w") as fcsv:
    fieldnames = categoriescsv[0].keys()
    writer = csv.DictWriter(fcsv, delimiter=';', fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(categoriescsv)

'''
print("Saving JSON...")
with open("shop.csv", "w") as csvFile:
    outFile.write(json.dumps(fetchResult, indent=4))
'''
print("done")
