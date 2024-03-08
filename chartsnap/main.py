from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time

def get_chart(
        ticker,
        time_interval,
        time_period,
        store_location
):
    flag = 0
    if time_interval and time_period is None:
        time_interval = '1d'
        flag = 1

    options = Options()
    options.add_argument("--headless")  
    options.add_argument("--window-size=1920,1080")   
    options.add_argument("--ignore-certificate-errors")  
    options.add_argument("--disable-extensions")    
    options.add_argument("--no-sandbox")   
    options.add_argument("--disable-dev-shm-usage")

    options.add_experimental_option("prefs", {
    "download.default_directory": store_location,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
    })

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    if ticker is None:
        return

    try:
        tradingview_url = 'https://www.tradingview.com/chart/?symbol=NSE%3A{}'.format(ticker)
        driver.get(tradingview_url)
        wait = WebDriverWait(driver, 100)
        chart_body = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='header-toolbar-screenshot']")))

        chart_body.click()

        if flag == 0:
            time_date = {'1D':1,'5D':2,'1M':3,'3M':4,'6M':5,'YTD':6,'1Y':7,'5Y':8,'ALL':9}

            time_period = '1Y' 
            if time_period in time_date:
                value = int(time_date[time_period])
            else:
                print("Time period entered is incorrect")

            try:
                time_period_button = wait.until(EC.presence_of_element_located((By.XPATH,  "/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div/button[{}]".format(value))))
                time_period_button.click()
                print("time period button found")
            except Exception as e:
                print(f"Error clicking download button: {str(e)}")

        time_interval = '1d'
        driver.switch_to.active_element.send_keys(time_interval)
        driver.switch_to.active_element.send_keys(Keys.ENTER)

        image_download_selector = 'header-toolbar-screenshot'

        try:
            download_button = wait.until(EC.presence_of_element_located((By.ID, image_download_selector)))
            download_button.click()
        except Exception as e:
            print(f"Error clicking download button: {str(e)}")

        time.sleep(3)
        download_button_selector = 'span.label-jFqVJoPk'
        try:
            download_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, download_button_selector)))
            download_button.click()
            now = datetime.now()
            print(now)
            
        except Exception as e:
            print(f"Error clicking download button: {str(e)}")

    finally:
        time.sleep(100) 
        driver.quit()



