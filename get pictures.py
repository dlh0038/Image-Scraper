from bs4 import *
import requests
import os
import datetime

def process_folder_name(link):
    temp = link.split('.com')
    return temp[-1].replace('/','')
    
def folder_create(folderName):
    success = False
    try:
        # folder creation
        os.mkdir(folderName)
        # if folder exists with that name, try to create with different name
    except FileExistsError:
        try:
            folderName += str(datetime.datetime.today()).replace(":","")
            print(f"Folder Exist with that name! Attempting to create folder with name {folderName}")
            os.mkdir(folderName)
        except FileExistsError:
            raise Exception("Folder Exist with that name too!")
    except:
        raise Exception("Folder cannot be created")
    return folderName

def get_images_links(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.text, 'html.parser')
    #imgs = soup.findAll('img') #find all image tags
    imgs = soup.findAll('a', {"class":"rel-link"})
    #images = [i.get('data-src') for i in imgs if i.get('data-src') is not None]
    images = [i.get('href') for i in imgs]
    return images

def download_images(imageList, folderNamePath):
    os.chdir(folderNamePath)
    for image in imageList:
        r = requests.get(image).content
        with open(image.split('/')[-1], "wb+") as f:
            f.write(r)
            print(f"downloaded: {image}")
        

def get_and_save_images(link):
    path = os.getcwd()
    #create folder
    #folder_create(link.replace("/", "").replace(':',""))
    folderName = folder_create(process_folder_name(link))

    #get image link
    images = get_images_links(link)

    #download images
    download_images(images, folderName)

    #go back to main path
    os.chdir(path)
    
def main():
    
    while True:
        #os.chdir('C:\\Users\\User\\Desktop\\')
        link = input("enter link(s): ")

        if link == "" or link == "\n":
            break
        if " " in link:
            links = link.split(' ')
            for link in links:
                get_and_save_images(link)

        else:
            get_and_save_images(link)
main()
