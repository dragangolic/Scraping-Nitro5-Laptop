from bs4 import BeautifulSoup
import requests

url = "https://store.acer.com/en-us/laptops/gaming/product_series-nitro_5?msclkid=" \
      "c4f8026f871c137245e4613d8c17823c&utm_source=bing&utm_medium=cpc&utm_campaign=Brand%20-%20Nitro&utm_term=" \
      "acer%20nitro%205%20gaming%20laptop&utm_content=Nitro%205%20-%20Phrase"
results = requests.get(url)
doc = BeautifulSoup(results.text, "html.parser")
prices = doc.find_all(text="$")
print(prices)