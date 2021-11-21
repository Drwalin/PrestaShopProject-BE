from prestapyt import PrestaShopWebServiceDict

WEBSERVICE_KEY = "9KLBU8X113FV5RTDZF42RVPX9EFVUQ6M"
presta = PrestaShopWebServiceDict('https://localhost:80/api', WEBSERVICE_KEY)

print(presta.get("products"))