from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
website = ['http://bbs.skykiwi.com/forum.php?mod=viewthread&tid=3840473']


def post(i):
    driver = webdriver.Chrome(executable_path='/Users/anne/Documents/post_skykiwi/auto_post/chromedriver')
    driver.get(url=website[i])
    driver.maximize_window()

    denglu = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/form/div/div/table/tbody/tr[2]/td[4]/a')
    denglu.click()

    user = driver.find_element_by_class_name('login-email-input')
    user.clear()
    user.click()
    user.send_keys('econ140')

    password = driver.find_element_by_class_name('login-pwd-input')
    password.clear()
    password.click()
    password.send_keys('8875450')

    login = driver.find_element_by_class_name('button_normal')
    login.click()
    sleep(5)

    html = driver.find_element_by_tag_name('html')
    html.send_keys(Keys.END)

    content = driver.find_element_by_id('fastpostmessage')
    content.click()
    content.clear()
    content.send_keys('顶顶顶顶顶顶顶顶顶顶')

    post = driver.find_element_by_name('replysubmit')
    post.click()

    sleep(1)
    driver.close()


for i in range(len(website)):
    post(i)
