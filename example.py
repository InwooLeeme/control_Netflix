from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
# 본인의 Chrome 사용자 데이터 경로를 입력합니다.
options.add_argument("--user-data-dir=C:/Users/[사용자 이름]/AppData/Local/Google/Chrome/User Data")
# 사용할 프로필 (예: 기본 프로필은 'Default')
options.add_argument("--profile-directory=Default")


driver = webdriver.Chrome(options=options)
driver.get("https://www.netflix.com/")

input("Press Enter to exit...")
