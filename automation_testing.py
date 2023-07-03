from selenium import webdriver
from selenium.webdriver.common.by import By

# Configure the PhantomJS WebDriver
driver = webdriver.PhantomJS()

# Navigate to a web page
driver.get('https://www.lambdatest.com/selenium-playground/table-sort-search-demo')
driver.set_window_size(1440, 550)

# Getting the search bar
search_bar = driver.find_element(By.XPATH,'//*[@id="example_filter"]/label/input')
search_bar.send_keys("London")

# Getting row of the table
rows = driver.find_elements(By.TAG_NAME,"tr")

# Capturing the screenshot of the window 
driver.save_screenshot('table_data.png')

# Printing the row
for row in rows:
    data = row.text # spiliting the data 
    print(data)
driver.quit()