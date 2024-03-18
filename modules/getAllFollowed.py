import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC


os.system('cls')


def getFollowed(acc_username: str, acc_password: str):
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=Options())
    
    browser.get("https://www.instagram.com/")

    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')))

    username = browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
    password = browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')

    username.send_keys(acc_username)
    password.send_keys(acc_password)

    loginButton = browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')

    loginButton.click()

    time.sleep(5)

    browser.get(f'https://www.instagram.com/{acc_username}/following/')
    time.sleep(5)
    os.system('cls')
    followersList = []

    jscommand = """
    followers = document.querySelector("._aano");
    followers.scrollTo(0, followers.scrollHeight);
    var lenOfPage=followers.scrollHeight;
    return lenOfPage;
    
    """
    lenOfPage = browser.execute_script(jscommand)
    match = False
    while not match:
        lastCount = lenOfPage
        time.sleep(1)
        lenOfPage = browser.execute_script(jscommand)
        if lastCount == lenOfPage:
            match = True
    time.sleep(5)

    os.system('cls')
    counter = 1

    followers = browser.find_elements(By.CSS_SELECTOR, "._ap3a._aaco._aacw._aacx._aad7._aade")
    for follower in followers:
        print(f"[i] {counter} ---> " + follower.text)
        followersList.append(follower.text + "\n")
        counter += 1

    with open("saved/followed.txt", "w", encoding="utf-8") as file:
        for follower in followersList:
            file.write(follower)

    browser.close()
