from time import sleep
from selenium import webdriver, common

browser = webdriver.Firefox()
browser.implicitly_wait(5)

browser.get('https://www.instagram.com/accounts/login/')

try:
    # login
    username_input = browser.find_element_by_css_selector("input[name='username']")
    password_input = browser.find_element_by_css_selector("input[name='password']")
    with open("login_info.txt") as login_info:
        username_input.send_keys(login_info.readline())
        password_input.send_keys(login_info.readline())

        login_button = browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
    sleep(2)

    # follow users
    unsuccessful = []
    with open("want_to_follow.txt") as follow_list:
        for username in follow_list:
            username = username.rstrip()
            if username != "":
                browser.get('https://www.instagram.com/' + username + '/')
                try:
                    followButton = browser.find_element_by_css_selector('button')
                    followButton.click()
                except common.exceptions.NoSuchElementException:
                    # if user not found
                    unsuccessful.append(username)

    print("These users couldn't be found: " + str(unsuccessful))

    sleep(5)
    browser.close()
except common.exceptions.ElementClickInterceptedException:
    print("Add your username and password to login_info.txt and run again!")
