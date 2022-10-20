from selenium import webdriver
from time import sleep
import chromedriver_binary


def jobcan_automation(method, login_id, password):
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)

        driver.get("https://id.jobcan.jp/users/sign_in")
        sleep(1)

        login_id = driver.execute_script("return document.querySelector('#user_email')").send_keys(login_id)
        sleep(1)
        password = driver.execute_script("return document.querySelector('#user_password')").send_keys(
            password)
        sleep(1)

        submit = driver.execute_script("return document.querySelector('#login_button')").click()
        sleep(1)

        driver.execute_script("return document.querySelector('#jbc-app-links > ul > li:nth-child(3) > a')").click()
        sleep(5)
        handle_array = driver.window_handles
        driver.switch_to.window(handle_array[1])
        if method == 0:
            driver.execute_script("return document.querySelector('#adit-button-work-start')").click()
            sleep(1)
        if method == 1:
            driver.execute_script("return document.querySelector('#adit-button-work-end')").click()
            sleep(1)
        driver.close()
        return 1

    except:
        return 0
