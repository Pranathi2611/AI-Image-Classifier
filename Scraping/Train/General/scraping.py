import bs4
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import time



# ---------------- For downloading images---------------------------------
def download_image(url, folder_name, imgType, num):

    # write image to file
    reponse = requests.get(url)
    if reponse.status_code==200:
        with open(os.path.join(folder_name,  imgType + str(num)+".jpg"), 'wb') as file:
            file.write(reponse.content)


chromePath='C:/Users/shreya anand/Dropbox/PC/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe'
service = Service(executable_path=chromePath)
driver = webdriver.Chrome(service=service)


#----------------For AI generated images------------------------
AI_images_folder = 'AI generated'
if not os.path.isdir(AI_images_folder):
    os.makedirs(AI_images_folder)


img = 1
for page in range (1,300):

    search_URL = "https://pixabay.com/images/search/ai/?pagi=%s" %(page)
    driver.get(search_URL)

    # print("woking on page: ", page)
    # print(img)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
    time.sleep(10)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")
    time.sleep(5)

    #---------------Scrolling all the way up-------------------
    driver.execute_script("window.scrollTo(0, 0);")  
    ImageContainers = driver.find_elements(By.XPATH, '//*[@class="container--MwyXl"]/a/img')
    
    for image in ImageContainers:

        imageURL = image.get_attribute('src')

        if imageURL == 'https://pixabay.com/static/img/blank.gif': 
            continue

        try:
            download_image(imageURL, AI_images_folder, "AI_", img)
            img += 1
        except:
            print("Couldn't download an image %s, continuing downloading the next one"%(img))