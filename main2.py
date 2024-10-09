import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Function to log in to Instagram
def login(username, password):
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(3)

    # Enter username
    username_input = driver.find_element(By.NAME, 'username')
    username_input.send_keys(username)

    # Enter password
    password_input = driver.find_element(By.NAME, 'password')
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)
    time.sleep(5)

# Function to send a message
def send_message(user, message):
    # Go to the user's profile
    driver.get(f"https://www.instagram.com/pavanparvatalu/")
    time.sleep(3)

    # Click on the message button
    message_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[2]/div/div/div[2]/div/div[2]/div")
    message_button.click()
    time.sleep(3)

    # Find the message input box
    message_input = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/p")
    message_input.send_keys(message)
    message_input.send_keys(Keys.RETURN)
    time.sleep(2)

# Main execution
if __name__ == "__main__":
    # Start the WebDriver
    driver = webdriver.Chrome()  # Change this if you're using a different browser

    try:
        # Login credentials
        username = "pavanparvatalu@gmail.com"
        password = "pavan@1642"
        
        login(username, password)
        
        # User to message and the message text
        user_to_message = "pavanparvatalu"
        message_text = "Hello! This is an automated message."

        send_message(user_to_message, message_text)

    finally:
        # Close the browser
        time.sleep(5)  # Wait for a bit before closing
        driver.quit()
