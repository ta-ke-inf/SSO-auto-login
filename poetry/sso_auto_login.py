"""
SSO認証自動化
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from typing import List
import time
import schedule
import datetime
import sys

def task(args: List[str]) -> None:
    print("task start!!")
    driver = webdriver.Chrome()

    # Open Ghrome Tab 
    driver.get("https://www.google.com/")
    time.sleep(1)
    #river.implicitly_wait(10)
    print("Current url is ", driver.current_url)
    
    try:
        # タブの移動
        driver.switch_to.window(driver.window_handles[1])
        print(driver.current_url)

    # 移動できない場合既にログインされているため終了
    except:
        dt_now = datetime.datetime.now()
        print("Now already logined!! ", dt_now)
        return

    # Type username 
    form_username = driver.find_element(By.XPATH,'//*[@id="login-username"]')
    form_username.send_keys(args[1])

    # Type passward 
    form_pass = driver.find_element(By.XPATH, '//*[@id="login-password"]')
    form_pass.send_keys(args[2])

    # Click login button
    driver.find_element(By.XPATH, '//*[@id="btn-login"]').click()

    dt_now = datetime.datetime.now()
    print("Connected!! ", dt_now)

    # Close Chrome Tab 
    driver.quit()

# 一定の時間で task を実行
if __name__ == "__main__":
    """
    Args: 
    ----------------------
    args[1]: "your username"
    args[2]: "your passward"
    args[3]: "Time" to decide how many you want to monitor

    """
    args = sys.argv
    if len(args) == 4:
        print("Start!!")
        schedule.every(int(args[3])).minutes.do(task, args[:3])

        while True:
            schedule.run_pending()
            time.sleep(1)

    else :
        print("Argments do not match.\nThe number of argments must be 3 !!")
    