import argparse
import os
import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image

#Made by . Alejandro Cavazos Valdés
# Last update 15/10/2021

def decode_gps_info(exif):
    gpsinfo = {}
    if 'GPSInfo' in exif:
        #Parse geo references.
        print(exif['GPSInfo'])
        input("...")
        Nsec = exif['GPSInfo'][2][2]
        Nmin = exif['GPSInfo'][2][1]
        Ndeg = exif['GPSInfo'][2][0]
        Wsec = exif['GPSInfo'][4][2]
        Wmin = exif['GPSInfo'][4][1]
        Wdeg = exif['GPSInfo'][4][0]
        if exif['GPSInfo'][1] == 'N':
            Nmult = 1
        else:
            Nmult = -1
        if exif['GPSInfo'][3] == 'E':
            Wmult = 1
        else:
            Wmult = -1
        Lat = Nmult * (Ndeg + (Nmin + Nsec/60.0)/60.0)
        Lng = Wmult * (Wdeg + (Wmin + Wsec/60.0)/60.0)
        exif['GPSInfo'] = {"Lat" : Lat, "Lng" : Lng}
        
def get_exif_metadata(image_path):
    ret = {}
    image = Image.open(image_path)
    if hasattr(image, '_getexif'):
        exifinfo = image._getexif()
        if exifinfo is not None:
            for tag, value in exifinfo.items():
                decoded = TAGS.get(tag, tag)
                ret[decoded] = value
    decode_gps_info(ret)
    return ret

def printMeta():
    dir = os.getcwd()
    os.chdir(f"{dir}\Images")
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            print(os.path.join(root, name))
            print ("[+] Metadata for file: %s " %(name))
            f = open(f"{name}metadata.txt","w+")
            try:
                exifData = {}
                exif = get_exif_metadata(name)
                for metadata in exif:
                    print ("Metadata: %s - Value: %s " %(metadata, exif[metadata]))
                    x = "Metadata: %s - Value: %s " %(metadata, exif[metadata])
                    f.write(x)
                f.close()
                print ("\n")
            except:
                import sys, traceback
                traceback.print_exc(file=sys.stdout)

#Href: https://www.geeksforgeeks.org/how-to-download-all-images-from-a-web-page-in-python/
def download_images(url):
    name = "Images"
    folder_name = os.mkdir(name)
    request = requests.get(url)
    soup = bs(request.content, "html.parser")
    images = soup.findAll('img')
    count = 0
    # print total images found in URL
    print(f"Total {len(images)} Image Found!")
    # checking if images is not zero
    if len(images) != 0:
        for i, image in enumerate(images):
            # From image tag ,Fetch image Source URL

                        # 1.data-srcset
                        # 2.data-src
                        # 3.data-fallback-src
                        # 4.src

            # Here we will use exception handling

            # first we will search for "data-srcset" in img tag
            try:
                # In image tag ,searching for "data-srcset"
                image_link = image["data-srcset"]

            # then we will search for "data-src" in img
            # tag and so on..
            except:
                try:
                    # In image tag ,searching for "data-src"
                    image_link = image["data-src"]
                except:
                    try:
                        # In image tag ,searching for "data-fallback-src"
                        image_link = image["data-fallback-src"]
                    except:
                        try:
                            # In image tag ,searching for "src"
                            image_link = image["src"]

                        # if no Source URL found
                        except:
                            pass

            # After getting Image Source URL
            # We will try to get the content of image
            try:
                r = requests.get(image_link).content
                try:

                    # possibility of decode
                    r = str(r, 'utf-8')

                except UnicodeDecodeError:

                    # After checking above condition, Image Download start
                    with open(f"{name}/imagenes{i+1}.jpg", "wb+") as f:
                        f.write(r)

                    # counting number of image downloaded
                    count += 1
            except:
                pass

        # There might be possible, that all
        # images not download
        # if all images download
        if count == len(images):
            print("All Images Downloaded!")

        # if all images not download
        else:
            print(f"Total {count} Images Downloaded Out of {len(images)}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--direccion", dest = "direccion", help = "Sitio web donde se va a hacer el analisis")
    args = parser.parse_args()
    if args.direccion:
        download_images(args.direccion)
        printMeta()

if __name__ == "__main__":
    main()
