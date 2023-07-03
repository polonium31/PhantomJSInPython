from selenium import webdriver
from selenium.webdriver.common.by import By

# Configure the PhantomJS WebDriver
driver = webdriver.PhantomJS()

# Navigate to a web page
driver.get('https://www.worldometers.info/geography/alphabetical-list-of-countries/')

rows = driver.find_elements(By.TAG_NAME,"tr")

# Initialize a list to store the countries and populations
countries_populations = []

# Iterate over the rows of the table
for row in rows:
    data = row.text.split(" ") # spiliting the data 

    # Add the country and population to the list
    countries_populations.append((data))

for countries_population in countries_populations:
    if len(countries_population) == 5:
        print(f"{countries_population[1]}: {countries_population[2]}")

# Close the WebDriver
driver.quit()
