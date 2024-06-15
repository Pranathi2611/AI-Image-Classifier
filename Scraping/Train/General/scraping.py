# import bs4
# import requests
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import os
# import time



# def download_image(url, folder_name, num):

#     # write image to file
#     reponse = requests.get(url)
#     # print("download called", reponse.status_code)
#     if reponse.status_code==200:
#         with open(os.path.join(folder_name, str(num)+".jpg"), 'wb') as file:
#             file.write(reponse.content)


# chromePath='C:/Users/shreya anand/Dropbox/PC/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe'
# service = Service(executable_path=chromePath)
# driver = webdriver.Chrome(service=service)


# # For AI generated images

# AI_images_folder = 'AI generated'
# if not os.path.isdir(AI_images_folder):
#     os.makedirs(AI_images_folder)

# i = 5916
# for page in range (114,300):
#     search_URL = "https://pixabay.com/images/search/ai/?pagi=%s" %(page)
#     driver.get(search_URL)
#     print("woking on page: ", page)
#     print(i)
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
#     time.sleep(10)
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")
#     time.sleep(5)
#     #Scrolling all the way up
#     driver.execute_script("window.scrollTo(0, 0);")  

#     # print("hello1")
#     # page_html = driver.page_source
#     # pageSoup = bs4.BeautifulSoup(page_html, 'html.parser')
#     containers = driver.find_elements(By.XPATH, '//*[@class="container--MwyXl"]/a/img') 
#     # print(containers.__getattribute__('src'))
#     for container in containers:
#         # time.sleep(3)
#         # print(i,container.get_attribute('src'))
#         imageURL = container.get_attribute('src')
#         if imageURL == 'https://pixabay.com/static/img/blank.gif':
#             continue
#         # print(i,imageURL)
#         try:
#             download_image(imageURL, AI_images_folder, i)
#             # print("Downloaded element %s out of %s total. URL: %s" % (i, 100, imageURL))
#         except:
#             print("Couldn't download an image %s, continuing downloading the next one"%(i))
#         i += 1


































# import bs4
# import requests
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import os
# import time



# def download_image(url, folder_name, num):

#     # write image to file
#     reponse = requests.get(url)
#     print("download called", reponse.status_code)
#     if reponse.status_code==200:
#         with open(os.path.join(folder_name, str(num)+".jpg"), 'wb') as file:
#             file.write(reponse.content)


# chromePath='C:/Users/shreya anand/Dropbox/PC/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe'
# service = Service(executable_path=chromePath)
# driver = webdriver.Chrome(service=service)


# # For AI generated images

# AI_images_folder = 'AI generated'
# if not os.path.isdir(AI_images_folder):
#     os.makedirs(AI_images_folder)


# for page in range (1,101):
#     search_URL = "https://pixabay.com/images/search/ai/?pagi=%s" %(page)
#     driver.get(search_URL)


#     #Scrolling all the way up
#     driver.execute_script("window.scrollTo(0, 0);")

#     # print("hello1")
#     # page_html = driver.page_source
#     # pageSoup = bs4.BeautifulSoup(page_html, 'html.parser')
#     containers = driver.find_elements(By.XPATH, '//*[@class="container--MwyXl"]/a/img') 
#     # print(containers.__getattribute__('src'))
#     i = 100*(page-1) + 1
#     for container in containers:
#         time.sleep(3)
#         # print(i,container.get_attribute('src'))
#         imageURL = container.get_attribute('src')
#         if imageURL == 'https://pixabay.com/static/img/blank.gif':
#             continue
#         # print(i,imageURL)
#         try:
#             download_image(imageURL, AI_images_folder, i)
#             print("Downloaded element %s out of %s total. URL: %s" % (i, 100, imageURL))
#         except:
#             print("Couldn't download an image %s, continuing downloading the next one"%(i))
#         i += 1