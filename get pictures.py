from bs4 import *
import requests
import os

def folder_create(folderName):
    success = False
    try:
        # folder creation
        os.mkdir(folderName)
        success = True
        # if folder exists with that name, ask another name
    except:
        raise Exception("Folder Exist with that name!")

    return success

def get_images_links(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.text, 'html.parser')
    imgs = soup.findAll('img') #find all image tags
    images = [i.get('data-src') for i in imgs if i.get('data-src') is not None]
    return images

def download_image(images, folder_name):
    os.chdir(folder_name)
    for image in images:
        r = requests.get(image).content
        with open(image.replace("/", "").replace(':',""), "wb+") as f:
            f.write(r)
            print(f"downloaded: {image}")
        


def main():
    os.chdir('C:\\Users\\User\\Desktop\\')
    link = input("enter link: ")
    
    #create folder
    #folder_create(link.replace("/", "").replace(':',""))
    folder_create("test")

    #get image link
    images = get_images_links(link)

    #download images
    download_image(images, link)
