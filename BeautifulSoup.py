from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import selenium.webdriver.chrome.service 
import csv



#set up the webdriver
driver = webdriver.Chrome()

#fetch the webpage content
page_url = 'https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810000401'

#get the webpage
driver.get(page_url)

#tell the driver to wait to retrieve the content
driver.implicitly_wait(10)

#get the page source after JS execution
page_source = driver.page_source

#parse the HTML using BeautifulSoup
soup = BeautifulSoup(page_source,'html.parser')

#extract specific data
table = soup.find(id='simpleTable')

if table:
    #extract column headers
    headers = [th.get_text().strip() for th in table.find_all('th')] 
    
    #extract the row data
    rows = []
    for tr in table.find_all('tr'):
        row = [td.get_text().strip() for td in tr.find_all('td')]
        if row:
            rows.append(row)
            
            
    print('Column headers:')
    print(headers)

    print('\nRow data:')
    print(rows)

    #create a tuple for the headers
    header_tuple = (
        'All items',
        'Food',
        'Shelter',
        'Household operations, furnishings and equipment',
        'Clothing and footwear',
        'Transportation',
        'Gasoline',
        'Health & Personal Care',
        'Recreation, education, and reading',
        'Alcoholic beverages, tabacco products, & recreational cannabis',
        'All-items excluding food and energy',
        'All-items excluding energy',
        'Energy',
        'Goods',
        'Services'
    )

    #write the data to csv (comma separated value file)
    with open('table_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        #insert a new column as the first column in each row
        for i, row in enumerate(rows):
            rows[i] = [header_tuple[i]] + row

        #write the headers
        writer.writerow(headers[2:8])
        
        writer.writerows(rows)
        print('\nData is successsfully saved to csv file!')
else:
    print('Table not found on the webpage.')
    
            
#close the driver from selenium
driver.quit()


