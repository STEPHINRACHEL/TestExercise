# Go to your favorite e-shop,
# navigate to some category and add the two most expensive items to the shopping cart from this category.
import time

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Extract price value part from item price string
def getPrice(price):
    return price.strip('$').split('.')[0]

def test_add_most_expensive_item_to_cart():
    # Set browser value to desired one, the default value is set to Chrome
    browser = (os.getenv("BROWSER", "firefox")).lower()
    # Set url of e-shop site
    url = "https://www.amazon.com/"

    # Instantiate Webdriver object based on browser specified
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    # elif browser == 'edge': # Not tested the code in Edge
    #     driver = webdriver.Edge()
    # elif browser == 'safari': # Not tested the code in Safari
    #     driver = webdriver.Safari()

    # Open the url in the browser window
    driver.get(url)
    # maximise the browser window
    driver.maximize_window()

    # search for Backpack in the search box
    search_box = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
    # if search_box == '':
    #
    # //*[@id="nav-bb-searchbar"]/form/input
    search_box.send_keys("backpack")
    driver.find_element(By.ID, "nav-search-submit-button").submit()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
         '//div[@id="search"]/descendant::div[@class="a-section a-spacing-none s-messaging-widget-results-header"]/div/span[text()="Results"]')))

    time.sleep(1)  # Wait for dropdown to load

    # Click on dropdown button for selecting filter
    driver.find_element(By.ID, "a-autoid-0-announce").click()

    time.sleep(1)  # wait for menu to load

    # Click on Price:High to Low filter menu
    sort_high_to_low = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "s-result-sort-select_2")))
    sort_high_to_low.click()

    search_result = WebDriverWait(driver, 10).until((EC.presence_of_all_elements_located((By.XPATH,
        '//div[@id="s-skipLinkTargetForMainSearchResults"]/following-sibling::span[@data-component-type="s-search-results"]/div/div[@data-component-type="s-search-result"]'))))
    assert (len(search_result)) != 0
    item_price_elements = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, '//span[@class="a-price"]/child::span/span[@class="a-price-whole"]')))
    # List of item prices
    item_prices = [price.text for price in item_price_elements if price.text != '']

    # Add 2 most expensive item to cart
    for i in range(2):
        try:
            # Click on the most expensive item link from the top of the list
            search_result[i].find_element(By.XPATH,
                './/descendant::div[@class="a-section a-spacing-none puis-padding-right-small s-title-instructions-style"]/h2/a').click()

            add_to_cart_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'add-to-cart-button')))
            add_to_cart_button.click()
            time.sleep(1)  # Wait for the cart to update

            # Navigate back to results page
            driver.execute_script("window.history.go(-2)")

            # Locate the elements again to avid StaleElementReferenceException
            search_result = WebDriverWait(driver, 10).until((EC.presence_of_all_elements_located((By.XPATH,
                                                                                                  '//div[@id="s-skipLinkTargetForMainSearchResults"]/following-sibling::span[@data-component-type="s-search-results"]/div/div[@data-component-type="s-search-result"]'))))

        except:
            print(f"Could not add item {i+1} to the cart")

    cart_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "nav-cart-count-container")))
    cart_link.click()
    cart_title = driver.find_element(By.XPATH, '//div[@id="sc-active-cart"]/descendant::div[@class="a-row"]/h1').text
    assert cart_title == "Shopping Cart"
    cart_item_price_elements = driver.find_elements(By.XPATH, '//form[@id="activeCartViewForm"]/descendant::p[@class="a-spacing-mini"]/span')
    assert len(cart_item_price_elements) == 2
    cart_item_prices = [price.text for price in cart_item_price_elements]

    cart_price = list(map(getPrice, cart_item_prices))
    cart_price.sort()
    item_price = item_prices[:2]
    item_price.sort()
    assert cart_price == item_price

    driver.quit()