import pandas as pd
import numpy as np

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler


url = "https://www.google.com/flights/explore/#explore;f=JFK,EWR,LGA;t=HND,NRT,TPE,HKG;s=1;li=8;lx=12;d=2018-06-14"
driver = webdriver.PhantomJS()
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap['phantomjs.page.settings.userAgent'] = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 "
                                             "(KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36")

driver = webdriver.PhantomJS(desired_capabilities=dcap, service_args=['--ignore-ssl-errors=true'])
driver.implicitly_wait(20)
driver.get(url)
driver.save_screenshot(r'flight_explorer.png')

s = BeautifulSoup(driver.page_source, "lxml")

best_price_tags = s.findAll('div', 'FTWFGDB-w-e')
best_prices = []
for tag in best_price_tags:
    best_prices.append(int(tag.text.replace('$','')))
best_price = best_prices[0]
best_height_tags = s.findAll('div', 'FTWFGDB-w-f')
best_heights = []
for t in best_height_tags:
    best_heights.append(float(t.attrs['style'].split('height:')[1].replace('px','')))
best_height = best_heights[0]

pph = np.array(best_price)/np.array(best_height)

cities = s.findAll('div', 'FTWFGDB-w-o')

hlist = []
for bar in cities[0].findAll('div', 'FTWFGDB-w-x'):
    hlist.append(float(bar['style'].split('height: ')[1].replace('px;','')) *pph)
fares = pd.DataFrame(hlist, columns=['price'])
print(fares.min())

DBSCAN(esp=.5, min_samples=1)