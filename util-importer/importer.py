from prestapyt import PrestaShopWebServiceDict
import requests
import json
import re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

SCRAPER_OUTPUT_PATH = "../util-scraper/output/"
WEBSERVICE_KEY = "9KLBU8X113FV5RTDZF42RVPX9EFVUQ6M"


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

def read_json(filename):
	ret = None
	with open(filename, "r") as jsonfile:
		ret = json.load(jsonfile)
	return ret

def langstr(langid, value):
	return {"attrs":{"id":langid}, "value": value}

def make_url_friendly(string):
	ret = re.sub(r"\s+", '-', string)
	ret = re.sub("[^0-9a-zA-Z]+", "-", ret)
	return ret.lower()


def create_category_dict(category, category_map):
	template = read_json("template-category.json")

	template["category"]["name"]["language"] = langstr("2",category["name"])
	template["category"]["link_rewrite"]["language"] = langstr("2", make_url_friendly(category["name"]))
	# template["category"]["id"] = category["id"]
	if "parent_id" in category:
		template["category"]["id_parent"] = category_map[category["parent_id"]]
	else:
		template["category"]["id_parent"] = "2"

	return template

def create_product_dict(product, category_map):
	template = read_json("template-product.json")

	categories = [{"id": "2"}] + [{"id": category_map[cd["id"]]} for cd in product["categories"]]


	template["product"]["name"]["language"] = langstr("2",product["name"])
	template["product"]["description"]["language"] = langstr("2",product["desc"])
	template["product"]["description_short"]["language"] = langstr("2",product["short_desc"])
	template["product"]["id_category_default"] = category_map[product["main_category"]]
	template["product"]["price"] = product["price"]
	template["product"]["associations"]["categories"]["category"] = categories #product["categories"]

	return template

def create_combination_dict(prod_id, option_value_id):
	template = read_json("template-combination.json")

	template["combination"]["id_product"] = prod_id
	template["combination"]["associations"]["product_option_values"]["product_option_value"]["id"] = str(option_value_id)

	return template

def create_option_value_dict(name, position):
	template = read_json("template-product-option-value.json")

	template["product_option_value"]["position"] = str(position)
	template["product_option_value"]["name"]["language"] = langstr("2",name)

	return template


def upload_image(pws, resourceurl, imgfilename):
	with open(imgfilename, "rb") as img:
		pws.add(resourceurl, files=[("image", imgfilename, img.read())])
	pass

def upload_category(pws, category, category_map):
	return pws.add("categories", create_category_dict(category, category_map))

def upload_combination(pws, prod_id, prod_option_value):
	return pws.add("combinations", create_combination_dict(prod_id, prod_option_value))

product_option_values = ["26", "27", "28"]

def upload_product(pws, product, category_map):
	new_prod = presta.add("products", create_product_dict(product, category_map))
	new_prod_id = new_prod["prestashop"]["product"]["id"]

	for val in product_option_values:
		upload_combination(pws, new_prod_id, val)

	upload_image(presta, "images/products/"+new_prod_id, SCRAPER_OUTPUT_PATH + product["img"])


def get_list_of_ids(pws, table_name, table_name_singular):
	li = pws.get(table_name)
	if len(li[table_name]) == 0:
		return []
	li1 = li[table_name][table_name_singular]
	#print(json.dumps(li))
	#print(li1)
	if isinstance(li1, list):
		return [r["attrs"]["id"] for r in li[table_name][table_name_singular]]
	return [li1["attrs"]["id"]]

def purge_products(pws):
	ids = get_list_of_ids(pws, "products", "product")
	if len(ids):
		pws.delete("products", resource_ids=ids)

def purge_categories(pws):
	ids = get_list_of_ids(pws, "categories", "category")
	ids = [i for i in ids if int(i)>=3]
	if len(ids):
		pws.delete("categories", resource_ids=ids)

ses = requests.Session()
ses.verify = False
presta = PrestaShopWebServiceDict('https://localhost:443/api', WEBSERVICE_KEY, session=ses)
#presta.debug = True


presta.get("products")

print("Purging products...")
purge_products(presta)

print("Purging categories...")
purge_categories(presta)
#exit()

#print(presta.add("products", read_json("template-product.json")))
#exit()
p_category_map = dict()
s_products = read_json(SCRAPER_OUTPUT_PATH + "items.json")
s_categories = read_json(SCRAPER_OUTPUT_PATH + "categories.json")

print("Uploading categories...")
progCounter = ProgressCounter(len(s_categories))
for category in s_categories:
	progCounter.print_progress()
	resp = upload_category(presta, category, p_category_map)
	#print("XDDDDDDDDD")
	#print(json.dumps(resp,indent=4))
	#print("XDDDDDDDD")
	p_category_map[category["id"]] = resp["prestashop"]["category"]["id"]
progCounter.end()


#print(json.dumps(presta.get("combinations/10"), indent=4))
#exit()


print("Uploading products...", end='')
progCounter = ProgressCounter(len(s_products))
for product in s_products:
	progCounter.print_progress()
	upload_product(presta, product, p_category_map)
	#exit()
progCounter.end()

print("")