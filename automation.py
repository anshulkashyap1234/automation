# %%
from selenium import webdriver

from selenium.webdriver.common.by import By
import time 

"""
    This function creates and logs in to an account on the food-order-website using the given credentials.

    Parameters:
    name (str): The username for the account.
    password (str): The password for the account.
    gmail (str): The email address for the account.
    phone_no (str): The contact number for the account.

    Returns:
    None

    Example:
    >>> get_account("John", "1234", "john@gmail.com", "9876543210")
"""

def get_account(name,pasword,gmail,phone_no):
    try:
        """ this website 'https://food-order-website.onrender.com/' is my project for self learning
        I also make some project you can find it on my portfolio 'https://anshulkumarportfolio.netlify.app' 
        """
        # Load the website
        driver.get("https://food-order-website.onrender.com/")
        time.sleep(5)

        # Click on the Login link
        heading1 = driver.find_element(By.LINK_TEXT, 'Login')
        heading1.click()
        time.sleep(2)

        # Click on the create account button
        create_account = driver.find_element(By.CLASS_NAME, 'create_account')
        create_account.click()
        time.sleep(5)

        # Enter the username, password, email, and contact number
        username = driver.find_element(By.ID, 'username')
        password = driver.find_element(By.ID, 'password')
        email = driver.find_element(By.ID, 'email')
        contact_no = driver.find_element(By.ID, 'contact no')
        username.send_keys(name)
        password.send_keys(pasword)
        email.send_keys(gmail)
        contact_no.send_keys(phone_no)

        # Click on the create account submit button
        create_account_submit = driver.find_element(By.CLASS_NAME, 'button')
        create_account_submit.click()
        time.sleep(3)

        # Click on the Login link again
        heading1 = driver.find_element(By.LINK_TEXT, 'Login')
        heading1.click()

        # Enter the username and password
        username = driver.find_element(By.ID, 'account_no')
        password = driver.find_element(By.ID, 'password')
        username.send_keys(name)
        password.send_keys(pasword)

        # Click on the login account submit button
        login_account_submit = driver.find_element(By.CLASS_NAME, 'button')
        login_account_submit.click()
        
        # Print a message to indicate successful login
        return True
    
    except:
      
       return False
    


"""This code snippet launches the Edge browser, maximizes the window, and loads the settings page. It also sets the default zoom level to 0.7 using a JavaScript command."""

driver = webdriver.Edge()
driver.maximize_window()
driver.get('chrome://settings/')
driver.execute_script('chrome.settingsPrivate.setDefaultZoom(.7);')

#This function creates and logs in to an account on the food-order-website using the given credentials
# Example:
# >>> get_account("John", "1234", "john@gmail.com", "9876543210")

value=get_account("mohn", "1234", "john@gmail.com", "9876543210")
if value==True:
    print("you are login")
else:
    print("you are not login")


# %%



