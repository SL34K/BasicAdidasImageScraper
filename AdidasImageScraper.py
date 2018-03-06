###Adidas Product Image Scraper By @Sl34k
##DM me on Twitter with questions.
import requests, shutil
url = 'https://www.adidas.co.uk/dis/dw/image/v2/aagl_prd/on/demandware.static/-/Sites-adidas-products/default/dw133db8e5/zoom/{}_{}_standard.jpg'
durl = 'https://www.adidas.co.uk/dis/dw/image/v2/aagl_prd/on/demandware.static/-/Sites-adidas-products/default/dw133db8e5/zoom/{}_{}.jpg'
def pull(pid):
    print("Saving standard images...")
    #image 1
    url1 = url.format(pid,'01')
    response = requests.get(url1, stream=True)
    fname = pid+'_01.png'
    with open(fname, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    print("Successfully Saved {}_{}.png".format(pid,'01'))
    #image 2
    url2 = url.format(pid,'02')
    response = requests.get(url2, stream=True)
    fname = pid+'_02.png'
    with open(fname, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    print("Successfully Saved {}_{}.png".format(pid,'02'))
    #image 3
    url3 = url.format(pid,'03')
    response = requests.get(url3, stream=True)
    fname = pid+'_03.png'
    with open(fname, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    print("Successfully Saved {}_{}.png".format(pid,'03'))
    #image 4
    url4 = url.format(pid,'04')
    response = requests.get(url4, stream=True)
    fname = pid+'_04.png'
    with open(fname, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    print("Successfully Saved {}_{}.png".format(pid,'04'))
    #image 5
    url5 = url.format(pid,'05')
    response = requests.get(url5, stream=True)
    fname = pid+'_05.png'
    with open(fname, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    print("Successfully Saved {}_{}.png".format(pid,'05'))
    #image 6
    url6 = url.format(pid,'06')
    response = requests.get(url6, stream=True)
    fname = pid+'_06.png'
    with open(fname, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    print("Successfully Saved {}_{}.png".format(pid,'06'))
    print("Saving detailed images...")
    #image detailed 1
    url7 = durl.format(pid,'41_detail')
    response = requests.get(url7, stream=True)
    fname = pid+'_41_detail.jpg'
    with open(fname, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    print("Successfully Saved {}_{}.jpg".format(pid,'41_detail'))
    #image detailed 2
    url8 = durl.format(pid,'42_detail')
    response = requests.get(url8, stream=True)
    fname = pid+'_42_detail.jpg'
    with open(fname, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    print("Successfully Saved {}_{}.jpg".format(pid,'42_detail'))
    #image detailed 3
    url9 = durl.format(pid,'43_detail')
    response = requests.get(url9, stream=True)
    fname = pid+'_43_detail.jpg'
    with open(fname, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    print("Successfully Saved {}_{}.jpg".format(pid,'43_detail'))
    

print("@SL34k's Adidas Image Scraper")
pid = input("Enter PID: ")
pull(pid)
input("Press enter to exit")
