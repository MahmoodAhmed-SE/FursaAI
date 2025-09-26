from selenium import webdriver

def main():
  driver = webdriver.Chrome()
  driver.get("https://www.selenium.dev/selenium/web/web-form.html")
  title = driver.title
  print(title)
  driver.implicitly_wait(0.5)

# Only run main if this file is executed directly
if __name__ == "__main__":
    main()
