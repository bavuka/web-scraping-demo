import requests
from bs4 import BeautifulSoup
import time
import csv


url_text="https://www.booking.com/searchresults.en-gb.html?ss=New+Delhi%2C+Delhi+NCR%2C+India&efdco=1&label=gen173nr-10CAEoggI46AdIM1gEaGyIAQGYATO4ARfIAQzYAQPoAQH4AQGIAgGoAgG4AvjjlMcGwAIB0gIkNjlhMzU4NWUtNzJiMi00NzZmLTk3MGMtMmQ4ZTczNjIzZjYz2AIB4AIB&sid=0c024526ed956272b4eabd992c558acc&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=-2106102&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=56a06d0d68bd0312&ac_meta=GhA1NmEwNmQwZDY4YmQwMzEyIAAoATICZW46A25ld0AASgBQAA%3D%3D&checkin=2026-04-01&checkout=2026-04-02&group_adults=2&no_rooms=1&group_children=0"
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'}
response=requests.get(url_text,headers=header)
print(response.status_code)

if response.status_code==200:
    print("successfully connected")
    html_content=response.text
    soup=BeautifulSoup(html_content,"lxml")
    print(soup.prettify())
    hotels=soup.find_all("div",attrs={"role":"listitem"})
    # print(hotels)
    # soup gives a interface to lxml to convert the entire html raw content to tree like structure(nodes)
    # so it can be parsed using methods provided by beatifulsoup

#     you don’t need to use it again to access tags that are already stored in variables like hotel.
# That’s because each tag (hotel) is itself a mini-soup, or more accurately, 
# a BeautifulSoup Tag object that can be searched independently.
    with open("hotel.csv","w") as file_csv:
        csv.writter(file_csv)
        print()



    for hotel in hotels:
        hotel_name=hotel.find("div",attrs={"data-testid":"title"}).text.strip()
        location=hotel.find("span",attrs={"class":"d823fbbeed f9b3563dd4"}).text.strip()
        price=hotel.find("span",attrs={"class":"b87c397a13 f2f358d1de ab607752a2"}).text.strip().replace("₹ ","")
        rating=hotel.find("div",attrs={"class":"f63b14ab7a f546354b44 becbee2f63"}).text.strip()

        score=hotel.find("div",attrs={"class":"f63b14ab7a dff2e52086"}).text.strip()
        reviews=hotel.find("div",attrs={"class":"fff1944c52 fb14de7f14 eaa8455879"}).text.strip()
        link=hotel.find("a",href=True).attrs.get("href")



        print(hotel_name)
        print(location)
        print(price)
        print(rating)
        print(score)
        print(reviews)
        print(link)
        print()

else:
    print("unsuccessfull")

