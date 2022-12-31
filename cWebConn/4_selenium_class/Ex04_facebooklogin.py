from selenium import webdriver

email = 'cgtcsg@naver.com'
pw = 'tae@hin%4522912'

driver = webdriver.Chrome('./webdriver/chromedriver.exe')
driver.implicitly_wait(3)

driver.get('https://ko-kr.facebook.com/')

email = driver.find_element_by_id('email')
pw = driver.find_element_by_id('pass')
login_btn = driver.find_element_by_name('login')

email.send_keys(email)
pw.send_keys(pw)
login_btn.click()
