##Adidas Image Scraper By @SL34K
##DM me on Twitter with any requests or ideas
import requests, os, shutil
iUrl = 'https://www.adidas.co.uk/dis/dw/image/v2/aagl_prd/on/demandware.static/-/Sites-adidas-products/default/dw133db8e5/zoom/{}_{}'
#Pull Image Code
def getImg(pid,imName):
    imUrl = iUrl.format(pid,imName)
    response = requests.get(imUrl, stream=True)
    fname = pid+imName
    with open(pid+'/'+fname, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
#Main Scraper
def main(pid):
    newpath = r'{}'.format(pid) 
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    getImg(pid,'02_hover_frv.jpg')
    getImg(pid,'01_standard.jpg')
    getImg(pid,'02_standard.jpg')
    getImg(pid,'03_standard.jpg')
    getImg(pid,'04_standard.jpg')
    getImg(pid,'05_standard.jpg')
    getImg(pid,'06_standard.jpg')
    getImg(pid,'41_detail.jpg')
    getImg(pid,'42_detail.jpg')
    getImg(pid,'43_detail.jpg')
    print("Images Saved")

print("####Adidas Image Scraper @SL34K####")
pid = input("Please enter the PID: ")
main(pid)
input("Press enter to exit")
