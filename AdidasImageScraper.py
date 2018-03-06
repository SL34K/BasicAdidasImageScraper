###Adidas Product Image Scraper By @Sl34k
##DM me on Twitter with questions.
import requests, shutil
url = 'https://www.adidas.co.uk/dis/dw/image/v2/aagl_prd/on/demandware.static/-/Sites-adidas-products/default/dw133db8e5/zoom/{}_{}_standard.jpg'
def pull(pid):
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

print("@SL34k's Adidas Image Scraper")
pid = input("Enter PID: ")
pull(pid)
