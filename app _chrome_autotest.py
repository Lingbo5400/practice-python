import selenium
import time
from appium import webdriver
#from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import sys



#定義左滑封包
def swipe_left(element):
    location = element.location
    element_x=location['x']
    element_y=location['y']
    driver.swipe(element_x,element_y,element_x*0.5,element_y,200)

#create folder save screenshot pic
currentPath=os.getcwd()
A_folder=currentPath+"/image"

if not os.path.exists(A_folder):
    os.mkdir('image')
newpath=os.getcwd()+"/image"
B_folder=newpath+"/screenshot"
if not os.path.exists(B_folder):
    os.mkdir(B_folder)

des={   
    "platformName": "Android",
    "deviceName": "Pixel",
    "browserName": "Chrome",
}



driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)
driver.get("https://www.cathaybk.com.tw/cathaybk/")

# 页面加载完成，执行后续操作
#driver.implicitly_wait(10) 



try:
    element =WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/section/div[3]/div[4]/div')))
except:
    print("loading....") 
    #driver.quit()

img_path = os.path.abspath(os.path.dirname(sys.argv[0]))+"\image"
driver.get_screenshot_as_file(img_path+'\\Home img.png')
print("------screenshot Home OK!-----------")
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]").click()
driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[1]/div").click()
driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div").click()
driver.implicitly_wait(5)

driver.get_screenshot_as_file(img_path+'\\creditcard list.png')
print("------screenshot creditcard list OK!-----------")

menu_list=driver.find_elements(By.XPATH,"/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/a")
print("計算有幾項目在信用卡選單下面:",len(menu_list))
#for i in menu_list:
    #print(i.text)
time.sleep(1)
menu_list[0].click()

#定位一個元件座標做滑動定點
slider = driver.find_elements(By.XPATH,"//div[@class='swiper-wrapper']/a")[2]
swipe_left(slider)

targetElement = driver.find_element(By.XPATH,"//div[@class='swiper-wrapper']/a/p[text()='停發卡']") 
targetElement.click()

expirecard_local =driver.find_element(By.XPATH,"//div[@class='cubre-o-block__wrap']")

expire_card=driver.find_elements(By.XPATH,"//div[@class='cubre-m-compareCard__title' and contains(text(), '(停發)')]")
count = 0

swiped = True
while swiped == True:
    before_swipe=driver.page_source
    swipe_left(expirecard_local)
    time.sleep(2) #換頁等一下
    after_swipe=driver.page_source
    
    if before_swipe == after_swipe:
        swiped = False
        break
    else:   
        print("screenshot....."+f"{count}.png") 
        driver.get_screenshot_as_file(img_path+'\\screenshot'+f"\\{count}.png")
        count += 1
        #print(count)
        


# 開啟截圖資存放料夾
openfolder = img_path+'\\screenshot'
dirs = os.listdir(openfolder)

# 輸出所有檔案和資料夾
print("------read screenshot expirecard list-----------") 
for file in dirs:
    print(file)   
if len(expire_card)== len(dirs):
    print("(停發)信用卡數量與截圖數量相同!!!") 
else:
    print("(停發)信用卡數量與截圖數量不相同!!!") 
        
driver.quit()
