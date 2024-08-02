from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import sys


options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_experimental_option("detach", True)
# specify path location of chrome driver and profile according to your computer which can be accessed by using chrome://version
options.add_argument(r"--user-data-dir=C:\Users\saksh\AppData\Local\Google\Chrome\User Data")

options.add_argument(r'--profile-directory=Profile 10')

static = "message-actions"
break_error = "https://gemini.google.com/unavailable"
box = "/html/body/chat-app/main/side-navigation-v2/bard-sidenav-container/bard-sidenav-content/div/div/div[2]/chat-window/div[1]/div[2]/div[1]/input-area-v2/div/div/div[1]/div/div/rich-textarea/div[1]/p"

my_file = open("Youtube_links.txt", "r")
data = my_file.read()
my_file.close()
data_list = data.splitlines()
g = len(data_list)
a=0
def run(a):
    while a<g:
        driver = webdriver.Chrome(options=options)

        def check(c):
            try:
                driver.find_element(By.TAG_NAME, c)
            except NoSuchElementException:
                return False
            return True

        def check_box(c):
            try:
                driver.find_element(By.XPATH, c)
            except NoSuchElementException:
                return False
            return True

        driver.get("https://gemini.google.com/app")
        gem_load = check_box(box)


        if gem_load:
            input_box = driver.find_element(By.XPATH,"/html/body/chat-app/main/side-navigation-v2/bard-sidenav-container/bard-sidenav-content/div/div/div[2]/chat-window/div[1]/div[2]/div[1]/input-area-v2/div/div/div[1]/div/div/rich-textarea/div[1]/p")
            input_box.send_keys(f"{data_list[a]} generate 22 keywords in bullets",Keys.ENTER)
            time.sleep(7)
            gem_break = driver.current_url
            if gem_break == break_error:
                a=a-1
                driver.quit()
                run(a)
            while check(static) is False:
                time.sleep(1)
            elements = driver.find_elements(By.TAG_NAME, "li")
            with open('output1KW.txt', 'a') as f:
                sys.stdout = f
                j = 1
                for i in elements:
                    if j <= 20:
                        print(i.text)
                        j = j + 1

            driver.quit()
            a=a+1
            time.sleep(10)
        else:
            driver.quit()
            run(a)

run(a)




