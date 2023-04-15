from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import sys
from tkinter import *

driver = webdriver.Edge()
driver.get('https://shopee.co.id/gaminggearoutlet')

def login(driver):
    userEmail = "gigahidjrikaaa@gmail.com"
    userPassword = "gigahidjrikaaa"

    # Wait for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'shopee-button-solid')))

    # Find the login button
    login_button = driver.find_element(By.CLASS_NAME, 'shopee-button-solid')
    # Click the login button
    login_button.click()

    # Wait for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'shopee-button-solid')))

    # Find the login with email button
    login_with_email_button = driver.find_element(By.CLASS_NAME, 'shopee-button-solid')
    # Click the login with email button
    login_with_email_button.click()

    # Wait for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'shopee-button-solid')))

    # Find the email input field
    email_input = driver.find_element(By.CLASS_NAME, 'shopee-input')
    # Type the email address
    email_input.send_keys(userEmail)

    # Find the password input field
    password_input = driver.find_element(By.CLASS_NAME, 'shopee-input')
    # Type the password
    password_input.send_keys(userPassword)

    # Find the login button
    login_button = driver.find_element(By.CLASS_NAME, 'shopee-button-solid')
    # Click the login button
    login_button.click()

def getItemData(driver):
    # Wait for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, '_44qnta')))

    # Find item name. If not found, print error message
    try:
        global item_name
        item_name = driver.find_element(By.CLASS_NAME, '_44qnta')
        # find the item name inside the span tag inside the class _44qnta
        item_name = item_name.find_element(By.TAG_NAME, 'span')
    except:
        item_name = "NOT FOUND"
        sys.exit()

    # Find item price. If not found, print error message
    try:
        global item_price
        item_price = driver.find_element(By.CLASS_NAME, 'pqTWkA')
    except:
        item_name = "NOT FOUND"
        sys.exit()

    # Find item stock. If not found, print error message
    try:
        global item_stock
        # the 10th element of the class MCCLkq is the stock
        item_stock = driver.find_elements(By.CLASS_NAME, 'dR8kXc')[10]
        # only get the text inside the div tag
        item_stock = item_stock.find_element(By.TAG_NAME, 'div').text
    except:
        item_stock = "NOT FOUND"
        sys.exit()

def showData():
    # Create a new tkinter window
    window = Tk()
    # Set the window title
    window.title("Shopee Tokolaptop Sync")
    # Set the window size
    window.geometry("700x200")

    # Create a label and place it
    label = Label(window, text="Received data from Shopee", font=("Arial Bold", 15))
    label.grid(column=0, row=0)

    label = Label(window, text="Item Name: " + item_name.text, font=("Arial Bold", 10))
    label.grid(column=0, row=1)

    label = Label(window, text="Item Price: " + item_price.text, font=("Arial Bold", 10))
    label.grid(column=0, row=2)

    label = Label(window, text="Item Stock: " + item_stock, font=("Arial Bold", 10))
    label.grid(column=0, row=3)

    button = Button(window, text="Close", command=window.destroy)
    button.grid(column=0, row=5)

    # center the labels
    # for i in range(0, 5):
    #     window.grid_rowconfigure(i, weight=1)
    for i in range(0, 1):
        window.grid_columnconfigure(i, weight=1)

    # Start the tkinter window
    window.mainloop()

# Wait for the page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'shopee-searchbar-input__input')))
# Find the search bar
search_bar = driver.find_element(By.CLASS_NAME, 'shopee-searchbar-input__input')
# Type the search query
search_bar.send_keys('laptop')
# Press enter
search_bar.send_keys(Keys.RETURN)

# Wait for the page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'shopee-search-item-result__items')))
# Find the first item
first_item = driver.find_element(By.CLASS_NAME, 'shopee-search-item-result__items')
# Click the first item
first_item.click()

getItemData(driver)

showData()

# Close the browser
driver.quit()