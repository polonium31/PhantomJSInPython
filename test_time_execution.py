from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time

def scrape_table_data(browser):
    start = time.time()
    if browser == "phantomjs":
        driver = webdriver.PhantomJS()
    elif browser == "chrome":
        options = ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        options.set_headless()
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError("Invalid browser specified.")

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

phantomjs_execution_time = scrape_table_data("phantomjs")
chrome_execution_time = scrape_table_data("chrome")
firefox_execution_time = scrape_table_data("firefox")

print(f"Time taken PhantomJS Browser: {phantomjs_execution_time:.03f}ms")
print(f"Time taken Chrome Browser: {chrome_execution_time:.03f}ms")
print(f"Time taken Firefox Browser: {firefox_execution_time:.03f}ms")

if (phantomjs_execution_time < chrome_execution_time) and (phantomjs_execution_time < firefox_execution_time):
    print("PhantomJS has better time execution")
elif (firefox_execution_time < chrome_execution_time) and (firefox_execution_time < phantomjs_execution_time):
    print("Firefox has better time execution")
else:
    print("Chrome has better time execution")
