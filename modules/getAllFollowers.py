import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC


def getFollowers(acc_username: str, acc_password: str):
    os.system('cls')
    browser = webdriver.Chrome(executable_path=r'../chromedriver.exe')

    browser.get("https://www.instagram.com/")

    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')))

    username = browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
    password = browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')

    username.send_keys(acc_username)
    password.send_keys(acc_password)

    loginButton = browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')

    loginButton.click()

    time.sleep(5)

    browser.get(f'https://www.instagram.com/{acc_username}/followers/')
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
    followers = browser.find_elements(By.CSS_SELECTOR, "._ab8y._ab94._ab97._ab9f._ab9k._ab9p._abcm")
    for follower in followers:
        print(f"[i] {counter} ---> " + follower.text)
        followersList.append(follower.text + "\n")
        counter += 1

    with open("../saved/followers.txt", "w", encoding="UTF-8") as file:
        for follower in followersList:
            file.write(follower)

    browser.close()
