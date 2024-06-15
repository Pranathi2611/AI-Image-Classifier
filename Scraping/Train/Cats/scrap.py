import bs4
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import time


# -------Function for downloading image---------
def download_image(url, folder_name, Imgtype, num):

    # write image to file
    reponse = requests.get(url)
    if reponse.status_code==200:
        with open(os.path.join(folder_name, Imgtype + str(num)+".jpg"), 'wb') as file:
            file.write(reponse.content)




#-----------Startig Driver------------------
chromePath='C:/Users/shreya anand/Dropbox/PC/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe'
service = Service(executable_path=chromePath)
driver = webdriver.Chrome(service=service)



# # -------------AI images scraping---------------
AI_images_folder = 'Cats/AI_gen_cats'
if not os.path.isdir(AI_images_folder):
    os.makedirs(AI_images_folder)

search_URL = "https://www.freepik.com/free-photos-vectors/cat-ai/7#uuid=9077361a-d4ee-46a0-b5e5-86d478491e23"
driver.get(search_URL)

img_number = 1
for page in range(1,25):

    print("working on page ", page)
    print("starting with image", img_number)

    # -----Container for all the images in that page--------
    imageContainer = driver.find_elements(By.XPATH, '//*[@id="main"]/div[3]/div/div[2]/section/figure') 

    for image in imageContainer:
        imageURL = image.get_attribute('data-image')
        try:
            download_image(imageURL, AI_images_folder, "AI_", img_number)
            img_number += 1
        except:
            print("Couldn't download an image %s, continuing downloading the next one"%(img_number))

    # -------- XPath of next button: //*[@class="pagination__next button floatl pd-y-none-i"] -----------
    nxt_Button = driver.find_element(By.XPATH, '//*[@class="pagination__next button floatl pd-y-none-i"]') 
    nxt_Button.click()   







# -----------------Real images scraping----------------------

Real_images_folder = 'Cats/Real_cats'
if not os.path.isdir(Real_images_folder):
    os.makedirs(Real_images_folder)

search_URL = "https://www.pexels.com/search/cat/"
driver.get(search_URL)

i = 1
img = 1
time.sleep(10)
while i<=1500:
    # //*[@id="-"]/div[1]/div/div[2]/div[1]/article

    for j in range(1,4):

        xpath = '//*[@id="-"]/div[1]/div/div[%s]/div[%s]/article/a/img'%(j,i)

        #-------------for scrolling to load images------------
        if i%9 == 0:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight/1.2);")  
            time.sleep(3)

        try:
            container = driver.find_element(By.XPATH, xpath) 
        except:
            print("Couldn't download an image %s, continuing downloading the next one"%(i))
            i+=1
            continue

        try:
            imageURL = container.get_attribute('src')
            download_image(imageURL, Real_images_folder, "Real_", img)
            img+=1
            i += 1
        except:
            print("Couldn't download an image %s, continuing downloading the next one"%(i))

    

