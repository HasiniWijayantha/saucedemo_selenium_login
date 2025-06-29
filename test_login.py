from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Launch the browser
driver = webdriver.Chrome()  # You can also use Firefox or Edge if preferred

# Step 2: Open the website
driver.get("https://www.saucedemo.com/")

# Optional: Maximize the browser
driver.maximize_window()
#time.sleep(2)

# Step 3: Locate elements and interact
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Step 4: Validate login (e.g., check if we're redirected to inventory page)
time.sleep(5)  # Wait for page to load (can be replaced with WebDriverWait)
assert "inventory" in driver.current_url, "Login failed!"

# Step 5: Close the browser
driver.quit()

print("✅ Login test completed successfully!")
