import time
import os
import requests
from bs4 import BeautifulSoup #需安裝bs4
from selenium import webdriver #需安裝selenium

#先到webdriver官網下載Win32的執行檔(符合自己Chrome的大版本)，再放到與此程式碼同一個資料夾中
#如果第12行出錯，開啟該執行檔後再接著run此程式碼試試

id='410410054' #必須修改成自己的帳號
password='!Jason0904' #必須修改成自己的密碼

def Login_User_Page():
    driver.get('https://kiki.ccu.edu.tw/~ccmisp06/cgi-bin/class_new/login.php?m=0')#登入所需的輸入框網址
    try:
        time.sleep(2) #為了避免造成伺服器負擔，隨時休息一下
        driver.find_element_by_name('id').send_keys(id)#送出學號
        time.sleep(2)
        driver.find_element_by_name('password').send_keys(password)#送出密碼
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/font/center/form/table/tbody/tr[6]/td/input[1]').submit() #送出表單
    except:
        print("error001") #可能是學號密碼打錯，網路環境不佳，網站介面被修改等等
        os._exit() #強制結束程式

def Login_Pre_Main_Page(driver):
    driver.get('https://kiki.ccu.edu.tw/~ccmisp06/cgi-bin/class_new/')#登入前主頁面網址

def Get_Sourse_Code_And_Print():
    soup = BeautifulSoup(driver.page_source, 'html.parser') #使用bs4解析網頁原始碼
    print("The original code is: ") 
    print("")
    print(soup) #印出當前網頁原始碼
    time.sleep(3)

options=webdriver.ChromeOptions() #設定瀏覽器的選項
options.add_argument("--start-maximized") #將放大視窗加入選項

driver = webdriver.Chrome('E:\progremmingFile\Html\LessonBot\code\chromedriver.exe',options=options) #開啟Win32的執行檔，此行必須依Win32執行檔的絕對路徑而修改

Login_User_Page()
Get_Sourse_Code_And_Print()
driver.quit()


