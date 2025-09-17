from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import selenium.webdriver.chrome.service 
import csv

#fetch the webpage content
url = 'https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810000401';
response = requests.get(url)
html_content = response.content

#parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content,'html.parser')

#extract specific data
table = soup.find(id='simpleTable')



