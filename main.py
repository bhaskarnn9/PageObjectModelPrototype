from selenium import webdriver

base_url = 'https://exchange.sandbox.gemini.com/register/institution/thanks'
#  +ve
#  Step:1 --> Create instance of browser
#  Step:2 --> Launch url
#  Step:3 --> Launch validation --> Check for Gemini sandbox and Logo
#  -ve
# '//*[@class='css-1vvp637 e5i1odf3']//a[1]'
driver = webdriver.Chrome('/Users/bhaskarneel/Development/Selenium_Dependencies/chromedriver')
driver.get(base_url)
title = driver.title
print(title)
driver.close()
driver.quit()
# title = driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/section[2]/div/div/h2').text

# assert title == 'Gemini sandbox', 'Title not found'
# x1 = driver.title
# print(x1)
