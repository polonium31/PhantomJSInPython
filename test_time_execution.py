from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
import time

def scrape_table_data():
    start = time.time()
    driver.get('https://www.lambdatest.com/selenium-playground/table-sort-search-demo')

    search_bar = driver.find_element(By.XPATH, '//*[@id="example_filter"]/label/input')
    search_bar.send_keys("London")

    rows = driver.find_elements(By.TAG_NAME, "tr")

    data_list = []
    for row in rows:
        data = row.text
        data_list.append(data)
    driver.quit()
    end = time.time()

    execution_time = (end - start) * 10 ** 3
    return execution_time

# PhantomJS execution
# Required selenium==3.8.0
# driver = webdriver.PhantomJS()
# execution_time = scrape_table_data()
# print(f"Time taken PhantomJS Browser: {execution_time:.03f}ms")

# Chrome execution
# Latest version of Selenium is recommended
options = ChromeOptions()
options.add_argument('--headless=new')
driver = webdriver.Chrome(options=options)
execution_time = scrape_table_data()
print(f"Time taken Chrome Browser: {execution_time:.03f}ms")

# Firefox execution
# Latest version of Selenium is recommended
# options = FirefoxOptions()
# options.add_argument('--headless')
# driver = webdriver.Firefox(options=options)
# execution_time = scrape_table_data()
# print(f"Time taken Firefox Browser: {execution_time:.03f}ms")

# Edge execution
# Latest version of Selenium is recommended
# options = EdgeOptions()
# options.add_argument('--headless')
# driver = webdriver.Edge(options=options)
# execution_time = scrape_table_data()
# print(f"Time taken Edge Browser: {execution_time:.03f}ms")