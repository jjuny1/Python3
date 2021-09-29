import requests
from bs4 import BeautifulSoup
import time

def scrape_weather_seoul():
    print()
    print("{------------------------------------o0o-----------------------------------}")
    print(" :::[오늘 서울의 날씨]:::")
    url1 = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8"
    res1 = requests.get(url1)
    res1.raise_for_status()
    soup1 = BeautifulSoup(res1.text, "lxml")
    cast = soup1.find("p", attrs={"class":"summary"}).get_text().replace("° ","°").replace("요 ","요 |")
    lowest_temp = soup1.find("span", attrs={"class":"lowest"}).get_text().replace("최저기온","")
    highest_temp = soup1.find("span", attrs={"class":"highest"}).get_text().replace("최고기온","")
    rain_chance = soup1.find("dl", attrs={"class":"summary_list"}).find("dd", attrs={"class":"desc"}).get_text()
    sunset =  soup1.find("li", attrs={"class":"item_today type_sun"}).find("span", attrs={"class":"txt"}).get_text()
    

    url2 = "https://weather.naver.com/today/09140104?targetId=compare"
    res2 = requests.get(url2)
    res2.raise_for_status()
    soup2 = BeautifulSoup(res2.text, "lxml")
    curr_temp = soup2.find("strong", attrs={"class":"current"}).get_text().replace("현재 온도","")
    dust1 = soup2.find("a", attrs={"onclick":"nclk_v2(this, 'wtk.pm10cd', '', '')"}).find("em", attrs={"class":"level_text"}).get_text()
    dust2 = soup2.find("a", attrs={"onclick":"nclk_v2(this, 'wtk.pm25cd', '', '')"}).find("em", attrs={"class":"level_text"}).get_text()
    summary_list2 = soup2.find("dl", attrs={"class":"summary_list"}).get_text().replace("\n"," ").replace("체감","체감온도 :").replace(" 습도"," | 습도 :").replace("% ","% | ").replace("s ","s | ").replace("강수","강수 :")
    ultraviolet = soup2.find("a", attrs={"onclick":"nclk_v2(this, 'wtk.uvictcd', '', '')"}).find("em", attrs={"class":"level_text"}).get_text()

    print()
    print(" {}".format(cast))
    print()
    print(" 현재 기온 : {}".format(curr_temp))
    print()
    print(" 최저기온 : {}| 최고기온 : {}".format(lowest_temp, highest_temp))
    print()
    print("{}".format(summary_list2))
    print()
    print(" 미세먼지 : {} | 초미세먼지 : {} | 자외선 : {} | 일몰시각 {}".format(dust1, dust2, ultraviolet, sunset))
    print("{------------------------------------o0o-----------------------------------}")

def scrape_weather_busan():
    print()
    print("{------------------------------------o0o-----------------------------------}")
    print(" :::[오늘 부산의 날씨]:::")
    url1 = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%B6%80%EC%82%B0+%EB%82%A0%EC%94%A8&oquery=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&tqi=hSersdprvmZssAEGPXGssssssuw-483780"
    res1 = requests.get(url1)
    res1.raise_for_status()
    soup1 = BeautifulSoup(res1.text, "lxml")
    cast = soup1.find("p", attrs={"class":"summary"}).get_text().replace("° ","°").replace("요 ","요 |")
    lowest_temp = soup1.find("span", attrs={"class":"lowest"}).get_text().replace("최저기온","")
    highest_temp = soup1.find("span", attrs={"class":"highest"}).get_text().replace("최고기온","")
    rain_chance = soup1.find("dl", attrs={"class":"summary_list"}).find("dd", attrs={"class":"desc"}).get_text()
    sunset =  soup1.find("li", attrs={"class":"item_today type_sun"}).find("span", attrs={"class":"txt"}).get_text()
    

    url2 = "https://weather.naver.com/today/08110580?targetId=compare"
    res2 = requests.get(url2)
    res2.raise_for_status()
    soup2 = BeautifulSoup(res2.text, "lxml")
    curr_temp = soup2.find("strong", attrs={"class":"current"}).get_text().replace("현재 온도","")
    dust1 = soup2.find("a", attrs={"onclick":"nclk_v2(this, 'wtk.pm10cd', '', '')"}).find("em", attrs={"class":"level_text"}).get_text()
    dust2 = soup2.find("a", attrs={"onclick":"nclk_v2(this, 'wtk.pm25cd', '', '')"}).find("em", attrs={"class":"level_text"}).get_text()
    summary_list2 = soup2.find("dl", attrs={"class":"summary_list"}).get_text().replace("\n"," ").replace("체감","체감온도 :").replace(" 습도"," | 습도 :").replace("% ","% | ").replace("s ","s | ")
    ultraviolet = soup2.find("a", attrs={"onclick":"nclk_v2(this, 'wtk.uvictcd', '', '')"}).find("em", attrs={"class":"level_text"}).get_text()

    print()
    print(" {}".format(cast))
    print()
    print(" 현재 기온 : {}".format(curr_temp))
    print()
    print(" 최저기온 : {}| 최고기온 : {}".format(lowest_temp, highest_temp))
    print()
    print(" 강수 확률 : {}{}".format(rain_chance, summary_list2))
    print()
    print(" 미세먼지 : {} | 초미세먼지 : {} | 자외선 : {} | 일몰시각 {}".format(dust1, dust2, ultraviolet, sunset))
    print("{------------------------------------o0o-----------------------------------}")

def scrape_weather_daejeon():
    print()
    print("{------------------------------------o0o-----------------------------------}")
    print(" :::[오늘 대전의 날씨]:::")
    url1 = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%8C%80%EC%A0%84+%EB%82%A0%EC%94%A8&oquery=%EB%B6%80%EC%82%B0+%EB%82%A0%EC%94%A8&tqi=hSey1wprvmZssAXOPghsssssttl-154610"
    res1 = requests.get(url1)
    res1.raise_for_status()
    soup1 = BeautifulSoup(res1.text, "lxml")
    cast = soup1.find("p", attrs={"class":"summary"}).get_text().replace("° ","°").replace("요 ","요 |")
    lowest_temp = soup1.find("span", attrs={"class":"lowest"}).get_text().replace("최저기온","")
    highest_temp = soup1.find("span", attrs={"class":"highest"}).get_text().replace("최고기온","")
    rain_chance = soup1.find("dl", attrs={"class":"summary_list"}).find("dd", attrs={"class":"desc"}).get_text()
    sunset =  soup1.find("li", attrs={"class":"item_today type_sun"}).find("span", attrs={"class":"txt"}).get_text()
    

    url2 = "https://weather.naver.com/today/07110101?targetId=compare"
    res2 = requests.get(url2)
    res2.raise_for_status()
    soup2 = BeautifulSoup(res2.text, "lxml")
    curr_temp = soup2.find("strong", attrs={"class":"current"}).get_text().replace("현재 온도","")
    dust1 = soup2.find("a", attrs={"onclick":"nclk_v2(this, 'wtk.pm10cd', '', '')"}).find("em", attrs={"class":"level_text"}).get_text()
    dust2 = soup2.find("a", attrs={"onclick":"nclk_v2(this, 'wtk.pm25cd', '', '')"}).find("em", attrs={"class":"level_text"}).get_text()
    summary_list2 = soup2.find("dl", attrs={"class":"summary_list"}).get_text().replace("\n"," ").replace("체감","체감온도 :").replace(" 습도"," | 습도 :").replace("% ","% | ").replace("s ","s | ")
    ultraviolet = soup2.find("a", attrs={"onclick":"nclk_v2(this, 'wtk.uvictcd', '', '')"}).find("em", attrs={"class":"level_text"}).get_text()

    print()
    print(" {}".format(cast))
    print()
    print(" 현재 기온 : {}".format(curr_temp))
    print()
    print(" 최저기온 : {}| 최고기온 : {}".format(lowest_temp, highest_temp))
    print()
    print(" 강수 확률 : {}{}".format(rain_chance, summary_list2))
    print()
    print(" 미세먼지 : {} | 초미세먼지 : {} | 자외선 : {} | 일몰시각 {}".format(dust1, dust2, ultraviolet, sunset))
    print("{------------------------------------o0o-----------------------------------}")

def scrape_weather_jeju():
    print()
    print("{------------------------------------o0o-----------------------------------}")
    print(" :::[오늘 제주의 날씨]:::")
    url1 = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%A0%9C%EC%A3%BC+%EB%82%A0%EC%94%A8&oquery=%EB%8C%80%EC%A0%84+%EB%82%A0%EC%94%A8&tqi=hSe0vsprvh8ssnYudwsssssssdd-461659"
    res1 = requests.get(url1)
    res1.raise_for_status()
    soup1 = BeautifulSoup(res1.text, "lxml")
    cast = soup1.find("p", attrs={"class":"summary"}).get_text().replace("° ","°").replace("요 ","요 |")
    lowest_temp = soup1.find("span", attrs={"class":"lowest"}).get_text().replace("최저기온","")
    highest_temp = soup1.find("span", attrs={"class":"highest"}).get_text().replace("최고기온","")
    rain_chance = soup1.find("dl", attrs={"class":"summary_list"}).find("dd", attrs={"class":"desc"}).get_text() 
    sunset =  soup1.find("li", attrs={"class":"item_today type_sun"}).find("span", attrs={"class":"txt"}).get_text()
    
    url2 = "https://weather.naver.com/today/14110630?targetId=compare"
    res2 = requests.get(url2)
    res2.raise_for_status()
    soup2 = BeautifulSoup(res2.text, "lxml")
    curr_temp = soup2.find("strong", attrs={"class":"current"}).get_text().replace("현재 온도","")
    dust1 = soup2.find("a", attrs={"onclick":"nclk_v2(this, 'wtk.pm10cd', '', '')"}).find("em", attrs={"class":"level_text"}).get_text()
    dust2 = soup2.find("a", attrs={"onclick":"nclk_v2(this, 'wtk.pm25cd', '', '')"}).find("em", attrs={"class":"level_text"}).get_text()
    summary_list2 = soup2.find("dl", attrs={"class":"summary_list"}).get_text().replace("\n"," ").replace("체감","체감온도 :").replace(" 습도"," | 습도 :").replace("% ","% | ").replace("s ","s | ")
    ultraviolet = soup2.find("a", attrs={"onclick":"nclk_v2(this, 'wtk.uvictcd', '', '')"}).find("em", attrs={"class":"level_text"}).get_text()

    print()
    print(" {}".format(cast))
    print()
    print(" 현재 기온 : {}".format(curr_temp))
    print()
    print(" 최저기온 : {}| 최고기온 : {}".format(lowest_temp, highest_temp))
    print()
    print(" 강수 확률 : {}{}".format(rain_chance, summary_list2))
    print()
    print(" 미세먼지 : {} | 초미세먼지 : {} | 자외선 : {} | 일몰시각 {}".format(dust1, dust2, ultraviolet, sunset))
    print("{------------------------------------o0o-----------------------------------}")

def scrape_weather_daegu():
    print()
    print("{------------------------------------o0o-----------------------------------}")
    print(" :::[오늘 대구의 날씨]:::")
    url1 = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%8C%80%EA%B5%AC+%EB%82%A0%EC%94%A8&oquery=%EB%8C%80%EA%B5%AC+%EB%82%A0%EC%94%A8&tqi=hSfvglp0J1ssssbc4fZssssssvl-359487"
    res1 = requests.get(url1)
    res1.raise_for_status()
    soup1 = BeautifulSoup(res1.text, "lxml")
    cast = soup1.find("p", attrs={"class":"summary"}).get_text().replace("° ","°").replace("요 ","요 |")
    lowest_temp = soup1.find("span", attrs={"class":"lowest"}).get_text().replace("최저기온","")
    highest_temp = soup1.find("span", attrs={"class":"highest"}).get_text().replace("최고기온","")
    rain_chance = soup1.find("dl", attrs={"class":"summary_list"}).find("dd", attrs={"class":"desc"}).get_text()
    sunset =  soup1.find("li", attrs={"class":"item_today type_sun"}).find("span", attrs={"class":"txt"}).get_text()
    
    url2 = "https://weather.naver.com/today/06110101?targetId=compare"
    res2 = requests.get(url2)
    res2.raise_for_status()
    soup2 = BeautifulSoup(res2.text, "lxml")
    curr_temp = soup2.find("strong", attrs={"class":"current"}).get_text().replace("현재 온도","")
    dust1 = soup2.find("a", attrs={"onclick":"nclk_v2(this, 'wtk.pm10cd', '', '')"}).find("em", attrs={"class":"level_text"}).get_text()
    dust2 = soup2.find("a", attrs={"onclick":"nclk_v2(this, 'wtk.pm25cd', '', '')"}).find("em", attrs={"class":"level_text"}).get_text()
    summary_list2 = soup2.find("dl", attrs={"class":"summary_list"}).get_text().replace("\n"," ").replace("체감","체감온도 :").replace(" 습도"," | 습도 :").replace("% ","% | ").replace("s ","s | ")
    ultraviolet = soup2.find("a", attrs={"onclick":"nclk_v2(this, 'wtk.uvictcd', '', '')"}).find("em", attrs={"class":"level_text"}).get_text()

    print()
    print(" {}".format(cast))
    print()
    print(" 현재 기온 : {}".format(curr_temp))
    print()
    print(" 최저기온 : {}| 최고기온 : {}".format(lowest_temp, highest_temp))
    print()
    print(" 강수 확률 : {}{}".format(rain_chance, summary_list2))
    print()
    print(" 미세먼지 : {} | 초미세먼지 : {} | 자외선 : {} | 일몰시각 {}".format(dust1, dust2, ultraviolet, sunset))
    print("{------------------------------------o0o-----------------------------------}")

def scrape_weather_chuncheon():
    print()
    print("{------------------------------------o0o-----------------------------------}")
    print(" :::[오늘 춘천의 날씨]:::")
    url1 = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%B6%98%EC%B2%9C+%EB%82%A0%EC%94%A8&oquery=%EB%8C%80%EA%B5%AC+%EB%82%A0%EC%94%A8&tqi=hSfZedp0J1ssssn7CysssssstNl-149416"
    res1 = requests.get(url1)
    res1.raise_for_status()
    soup1 = BeautifulSoup(res1.text, "lxml")
    cast = soup1.find("p", attrs={"class":"summary"}).get_text().replace("° ","°").replace("요 ","요 |")
    lowest_temp = soup1.find("span", attrs={"class":"lowest"}).get_text().replace("최저기온","")
    highest_temp = soup1.find("span", attrs={"class":"highest"}).get_text().replace("최고기온","")
    rain_chance = soup1.find("dl", attrs={"class":"summary_list"}).find("dd", attrs={"class":"desc"}).get_text()
    sunset =  soup1.find("li", attrs={"class":"item_today type_sun"}).find("span", attrs={"class":"txt"}).get_text()
    
    url2 = "https://weather.naver.com/today/01110101?targetId=compare"
    res2 = requests.get(url2)
    res2.raise_for_status()
    soup2 = BeautifulSoup(res2.text, "lxml")
    curr_temp = soup2.find("strong", attrs={"class":"current"}).get_text().replace("현재 온도","")
    dust1 = soup2.find("a", attrs={"onclick":"nclk_v2(this, 'wtk.pm10cd', '', '')"}).find("em", attrs={"class":"level_text"}).get_text()
    dust2 = soup2.find("a", attrs={"onclick":"nclk_v2(this, 'wtk.pm25cd', '', '')"}).find("em", attrs={"class":"level_text"}).get_text()
    summary_list2 = soup2.find("dl", attrs={"class":"summary_list"}).get_text().replace("\n"," ").replace("체감","체감온도 :").replace(" 습도"," | 습도 :").replace("% ","% | ").replace("s ","s | ")
    ultraviolet = soup2.find("a", attrs={"onclick":"nclk_v2(this, 'wtk.uvictcd', '', '')"}).find("em", attrs={"class":"level_text"}).get_text()

    print()
    print(" {}".format(cast))
    print()
    print(" 현재 기온 : {}".format(curr_temp))
    print()
    print(" 최저기온 : {}| 최고기온 : {}".format(lowest_temp, highest_temp))
    print()
    print(" 강수 확률 : {}{}".format(rain_chance, summary_list2))
    print()
    print(" 미세먼지 : {} | 초미세먼지 : {} | 자외선 : {} | 일몰시각 {}".format(dust1, dust2, ultraviolet, sunset))
    print("{------------------------------------o0o-----------------------------------}")

def scrape_weather_gangleung():
    print()
    print("{------------------------------------o0o-----------------------------------}")
    print(" :::[오늘 강릉의 날씨]:::")
    url1 = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EA%B0%95%EB%A6%89+%EB%82%A0%EC%94%A8&oquery=%EC%B6%98%EC%B2%9C+%EB%82%A0%EC%94%A8&tqi=hSfZkwp0J1ssssawb80ssssst1d-115653"
    res1 = requests.get(url1)
    res1.raise_for_status()
    soup1 = BeautifulSoup(res1.text, "lxml")
    cast = soup1.find("p", attrs={"class":"summary"}).get_text().replace("° ","°").replace("요 ","요 |")
    lowest_temp = soup1.find("span", attrs={"class":"lowest"}).get_text().replace("최저기온","")
    highest_temp = soup1.find("span", attrs={"class":"highest"}).get_text().replace("최고기온","")
    rain_chance = soup1.find("dl", attrs={"class":"summary_list"}).find("dd", attrs={"class":"desc"}).get_text()
    sunset =  soup1.find("li", attrs={"class":"item_today type_sun"}).find("span", attrs={"class":"txt"}).get_text()
    
    url2 = "https://weather.naver.com/today/01150101?targetId=compare"
    res2 = requests.get(url2)
    res2.raise_for_status()
    soup2 = BeautifulSoup(res2.text, "lxml")
    curr_temp = soup2.find("strong", attrs={"class":"current"}).get_text().replace("현재 온도","")
    dust1 = soup2.find("a", attrs={"onclick":"nclk_v2(this, 'wtk.pm10cd', '', '')"}).find("em", attrs={"class":"level_text"}).get_text()
    dust2 = soup2.find("a", attrs={"onclick":"nclk_v2(this, 'wtk.pm25cd', '', '')"}).find("em", attrs={"class":"level_text"}).get_text()
    summary_list2 = soup2.find("dl", attrs={"class":"summary_list"}).get_text().replace("\n"," ").replace("체감","체감온도 :").replace(" 습도"," | 습도 :").replace("% ","% | ").replace("s ","s | ")
    ultraviolet = soup2.find("a", attrs={"onclick":"nclk_v2(this, 'wtk.uvictcd', '', '')"}).find("em", attrs={"class":"level_text"}).get_text()

    print()
    print(" {}".format(cast))
    print()
    print(" 현재 기온 : {}".format(curr_temp))
    print()
    print(" 최저기온 : {}| 최고기온 : {}".format(lowest_temp, highest_temp))
    print()
    print(" 강수 확률 : {}{}".format(rain_chance, summary_list2))
    print()
    print(" 미세먼지 : {} | 초미세먼지 : {} | 자외선 : {} | 일몰시각 {}".format(dust1, dust2, ultraviolet, sunset))
    print("{------------------------------------o0o-----------------------------------}")

def scrape_weather_ulleungdo():
    print()
    print("{------------------------------------o0o-----------------------------------}")
    print(" :::[오늘 울릉도(독도)의 날씨]:::")
    url1 = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%9A%B8%EB%A6%89%EB%8F%84+%EB%82%A0%EC%94%A8&oquery=%EA%B0%95%EB%A6%89+%EB%82%A0%EC%94%A8&tqi=hSfZFwp0J1ssssl8Otdssssstus-300850"
    res1 = requests.get(url1)
    res1.raise_for_status()
    soup1 = BeautifulSoup(res1.text, "lxml")
    cast = soup1.find("p", attrs={"class":"summary"}).get_text().replace("° ","°").replace("요 ","요 |")
    lowest_temp = soup1.find("span", attrs={"class":"lowest"}).get_text().replace("최저기온","")
    highest_temp = soup1.find("span", attrs={"class":"highest"}).get_text().replace("최고기온","")
    rain_chance = soup1.find("dl", attrs={"class":"summary_list"}).find("dd", attrs={"class":"desc"}).get_text()
    sunset =  soup1.find("li", attrs={"class":"item_today type_sun"}).find("span", attrs={"class":"txt"}).get_text()
    
    url2 = "https://weather.naver.com/today/04940310?targetId=compare"
    res2 = requests.get(url2)
    res2.raise_for_status()
    soup2 = BeautifulSoup(res2.text, "lxml")
    curr_temp = soup2.find("strong", attrs={"class":"current"}).get_text().replace("현재 온도","")
    dust1 = soup2.find("a", attrs={"onclick":"nclk_v2(this, 'wtk.pm10cd', '', '')"}).find("em", attrs={"class":"level_text"}).get_text()
    dust2 = soup2.find("a", attrs={"onclick":"nclk_v2(this, 'wtk.pm25cd', '', '')"}).find("em", attrs={"class":"level_text"}).get_text()
    summary_list2 = soup2.find("dl", attrs={"class":"summary_list"}).get_text().replace("\n"," ").replace("체감","체감온도 :").replace(" 습도"," | 습도 :").replace("% ","% | ").replace("s ","s | ")
    ultraviolet = soup2.find("a", attrs={"onclick":"nclk_v2(this, 'wtk.uvictcd', '', '')"}).find("em", attrs={"class":"level_text"}).get_text()

    print()
    print(" {}".format(cast))
    print()
    print(" 현재 기온 : {}".format(curr_temp))
    print()
    print(" 최저기온 : {}| 최고기온 : {}".format(lowest_temp, highest_temp))
    print()
    print(" 강수 확률 : {}{}".format(rain_chance, summary_list2))
    print()
    print(" 미세먼지 : {} | 초미세먼지 : {} | 자외선 : {} | 일몰시각 {}".format(dust1, dust2, ultraviolet, sunset))
    print("{------------------------------------o0o-----------------------------------}")

def scrape_weather_baekryeongdo():
    print()
    print("{------------------------------------o0o-----------------------------------}")
    print(" :::[오늘 백령도의 날씨]:::")
    url1 = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%B0%B1%EB%A0%B9%EB%8F%84+%EB%82%A0%EC%94%A8&oquery=%EB%8F%85%EB%8F%84+%EB%82%A0%EC%94%A8&tqi=hSfZHsp0J1ssssa2cedssssstr0-148051"
    res1 = requests.get(url1)
    res1.raise_for_status()
    soup1 = BeautifulSoup(res1.text, "lxml")
    cast = soup1.find("p", attrs={"class":"summary"}).get_text().replace("° ","°").replace("요 ","요 |")
    lowest_temp = soup1.find("span", attrs={"class":"lowest"}).get_text().replace("최저기온","")
    highest_temp = soup1.find("span", attrs={"class":"highest"}).get_text().replace("최고기온","")
    rain_chance = soup1.find("dl", attrs={"class":"summary_list"}).find("dd", attrs={"class":"desc"}).get_text()
    sunset =  soup1.find("li", attrs={"class":"item_today type_sun"}).find("span", attrs={"class":"txt"}).get_text()
    
    url2 = "https://weather.naver.com/today/11720330?targetId=compare"
    res2 = requests.get(url2)
    res2.raise_for_status()
    soup2 = BeautifulSoup(res2.text, "lxml")
    curr_temp = soup2.find("strong", attrs={"class":"current"}).get_text().replace("현재 온도","")
    dust1 = soup2.find("a", attrs={"onclick":"nclk_v2(this, 'wtk.pm10cd', '', '')"}).find("em", attrs={"class":"level_text"}).get_text()
    dust2 = soup2.find("a", attrs={"onclick":"nclk_v2(this, 'wtk.pm25cd', '', '')"}).find("em", attrs={"class":"level_text"}).get_text()
    summary_list2 = soup2.find("dl", attrs={"class":"summary_list"}).get_text().replace("\n"," ").replace("체감","체감온도 :").replace(" 습도"," | 습도 :").replace("% ","% | ").replace("s ","s | ")
    ultraviolet = soup2.find("a", attrs={"onclick":"nclk_v2(this, 'wtk.uvictcd', '', '')"}).find("em", attrs={"class":"level_text"}).get_text()

    print()
    print(" {}".format(cast))
    print()
    print(" 현재 기온 : {}".format(curr_temp))
    print()
    print(" 최저기온 : {}| 최고기온 : {}".format(lowest_temp, highest_temp))
    print()
    print(" 강수 확률 : {}{}".format(rain_chance, summary_list2))
    print()
    print(" 미세먼지 : {} | 초미세먼지 : {} | 자외선 : {} | 일몰시각 {}".format(dust1, dust2, ultraviolet, sunset))
    print("{------------------------------------o0o-----------------------------------}")

def scrape_weather_cheongju():
    print()
    print("{------------------------------------o0o-----------------------------------}")
    print(" :::[오늘 청주의 날씨]:::")
    url1 = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%B2%AD%EC%A3%BC+%EB%82%A0%EC%94%A8&oquery=%EB%B0%B1%EB%A0%B9%EB%8F%84+%EB%82%A0%EC%94%A8&tqi=hSfa6wp0J1ssssflXRssssssthN-002525"
    res1 = requests.get(url1)
    res1.raise_for_status()
    soup1 = BeautifulSoup(res1.text, "lxml")
    cast = soup1.find("p", attrs={"class":"summary"}).get_text().replace("° ","°").replace("요 ","요 |")
    lowest_temp = soup1.find("span", attrs={"class":"lowest"}).get_text().replace("최저기온","")
    highest_temp = soup1.find("span", attrs={"class":"highest"}).get_text().replace("최고기온","")
    rain_chance = soup1.find("dl", attrs={"class":"summary_list"}).find("dd", attrs={"class":"desc"}).get_text()
    sunset =  soup1.find("li", attrs={"class":"item_today type_sun"}).find("span", attrs={"class":"txt"}).get_text()
    
    url2 = "https://weather.naver.com/today/16111101?targetId=compare"
    res2 = requests.get(url2)
    res2.raise_for_status()
    soup2 = BeautifulSoup(res2.text, "lxml")
    curr_temp = soup2.find("strong", attrs={"class":"current"}).get_text().replace("현재 온도","")
    dust1 = soup2.find("a", attrs={"onclick":"nclk_v2(this, 'wtk.pm10cd', '', '')"}).find("em", attrs={"class":"level_text"}).get_text()
    dust2 = soup2.find("a", attrs={"onclick":"nclk_v2(this, 'wtk.pm25cd', '', '')"}).find("em", attrs={"class":"level_text"}).get_text()
    summary_list2 = soup2.find("dl", attrs={"class":"summary_list"}).get_text().replace("\n"," ").replace("체감","체감온도 :").replace(" 습도"," | 습도 :").replace("% ","% | ").replace("s ","s | ")
    ultraviolet = soup2.find("a", attrs={"onclick":"nclk_v2(this, 'wtk.uvictcd', '', '')"}).find("em", attrs={"class":"level_text"}).get_text()

    print()
    print(" {}".format(cast))
    print()
    print(" 현재 기온 : {}".format(curr_temp))
    print()
    print(" 최저기온 : {}| 최고기온 : {}".format(lowest_temp, highest_temp))
    print()
    print(" 강수 확률 : {}{}".format(rain_chance, summary_list2))
    print()
    print(" 미세먼지 : {} | 초미세먼지 : {} | 자외선 : {} | 일몰시각 {}".format(dust1, dust2, ultraviolet, sunset))
    print("{------------------------------------o0o-----------------------------------}")

def scrape_weather_gwangju():
    print()
    print("{------------------------------------o0o-----------------------------------}")
    print(" :::[오늘 광주의 날씨]:::")
    url1 = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EA%B4%91%EC%A3%BC+%EB%82%A0%EC%94%A8&oquery=%EC%B2%AD%EC%A3%BC+%EB%82%A0%EC%94%A8&tqi=hSfagsp0J1ssssapbBZssssss24-421558"
    res1 = requests.get(url1)
    res1.raise_for_status()
    soup1 = BeautifulSoup(res1.text, "lxml")
    cast = soup1.find("p", attrs={"class":"summary"}).get_text().replace("° ","°").replace("요 ","요 |")
    lowest_temp = soup1.find("span", attrs={"class":"lowest"}).get_text().replace("최저기온","")
    highest_temp = soup1.find("span", attrs={"class":"highest"}).get_text().replace("최고기온","")
    rain_chance = soup1.find("dl", attrs={"class":"summary_list"}).find("dd", attrs={"class":"desc"}).get_text()
    sunset =  soup1.find("li", attrs={"class":"item_today type_sun"}).find("span", attrs={"class":"txt"}).get_text()
    
    url2 = "https://weather.naver.com/today/05110101?targetId=compare"
    res2 = requests.get(url2)
    res2.raise_for_status()
    soup2 = BeautifulSoup(res2.text, "lxml")
    curr_temp = soup2.find("strong", attrs={"class":"current"}).get_text().replace("현재 온도","")
    dust1 = soup2.find("a", attrs={"onclick":"nclk_v2(this, 'wtk.pm10cd', '', '')"}).find("em", attrs={"class":"level_text"}).get_text()
    dust2 = soup2.find("a", attrs={"onclick":"nclk_v2(this, 'wtk.pm25cd', '', '')"}).find("em", attrs={"class":"level_text"}).get_text()
    summary_list2 = soup2.find("dl", attrs={"class":"summary_list"}).get_text().replace("\n"," ").replace("체감","체감온도 :").replace(" 습도"," | 습도 :").replace("% ","% | ").replace("s ","s | ")
    ultraviolet = soup2.find("a", attrs={"onclick":"nclk_v2(this, 'wtk.uvictcd', '', '')"}).find("em", attrs={"class":"level_text"}).get_text()

    print()
    print(" {}".format(cast))
    print()
    print(" 현재 기온 : {}".format(curr_temp))
    print()
    print(" 최저기온 : {}| 최고기온 : {}".format(lowest_temp, highest_temp))
    print()
    print(" 강수 확률 : {}{}".format(rain_chance, summary_list2))
    print()
    print(" 미세먼지 : {} | 초미세먼지 : {} | 자외선 : {} | 일몰시각 {}".format(dust1, dust2, ultraviolet, sunset))
    print("{------------------------------------o0o-----------------------------------}")

def scrape_weather_jeonju():
    print()
    print("{------------------------------------o0o-----------------------------------}")
    print(" :::[오늘 전주의 날씨]:::")
    url1 = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%A0%84%EC%A3%BC+%EB%82%A0%EC%94%A8&oquery=%EA%B4%91%EC%A3%BC+%EB%82%A0%EC%94%A8&tqi=hSfaOdp0J1ssssOzfswssssssmK-240186"
    res1 = requests.get(url1)
    res1.raise_for_status()
    soup1 = BeautifulSoup(res1.text, "lxml")
    cast = soup1.find("p", attrs={"class":"summary"}).get_text().replace("° ","°").replace("요 ","요 |")
    lowest_temp = soup1.find("span", attrs={"class":"lowest"}).get_text().replace("최저기온","")
    highest_temp = soup1.find("span", attrs={"class":"highest"}).get_text().replace("최고기온","")
    rain_chance = soup1.find("dl", attrs={"class":"summary_list"}).find("dd", attrs={"class":"desc"}).get_text()
    sunset =  soup1.find("li", attrs={"class":"item_today type_sun"}).find("span", attrs={"class":"txt"}).get_text()
    
    url2 = "https://weather.naver.com/today/13111101?targetId=compare"
    res2 = requests.get(url2)
    res2.raise_for_status()
    soup2 = BeautifulSoup(res2.text, "lxml")
    curr_temp = soup2.find("strong", attrs={"class":"current"}).get_text().replace("현재 온도","")
    dust1 = soup2.find("a", attrs={"onclick":"nclk_v2(this, 'wtk.pm10cd', '', '')"}).find("em", attrs={"class":"level_text"}).get_text()
    dust2 = soup2.find("a", attrs={"onclick":"nclk_v2(this, 'wtk.pm25cd', '', '')"}).find("em", attrs={"class":"level_text"}).get_text()
    summary_list2 = soup2.find("dl", attrs={"class":"summary_list"}).get_text().replace("\n"," ").replace("체감","체감온도 :").replace(" 습도"," | 습도 :").replace("% ","% | ").replace("s ","s | ")
    ultraviolet = soup2.find("a", attrs={"onclick":"nclk_v2(this, 'wtk.uvictcd', '', '')"}).find("em", attrs={"class":"level_text"}).get_text()

    print()
    print(" {}".format(cast))
    print()
    print(" 현재 기온 : {}".format(curr_temp))
    print()
    print(" 최저기온 : {}| 최고기온 : {}".format(lowest_temp, highest_temp))
    print()
    print(" 강수 확률 : {}{}".format(rain_chance, summary_list2))
    print()
    print(" 미세먼지 : {} | 초미세먼지 : {} | 자외선 : {} | 일몰시각 {}".format(dust1, dust2, ultraviolet, sunset))
    print("{------------------------------------o0o-----------------------------------}")

''' ---- Weather Web Scraping Function Definition Completed.---- '''

print("★...| 환영합니다! |...★")
print()
time.sleep(1)

print("2021년 육군사관학교 정보보호부에서 제작한 '실시간 대한민국 주요 도시 날씨 정보 알리미'입니다.")
print()
time.sleep(2)

print("모든 날씨 정보는 기상청의 실시간 자료를 자동검색하여 이용자에게 제공되며, 원하는 지역의 숫자를 입력할 경우, 검색이 자동으로 진행됩니다.")
print()
time.sleep(2.5)

print("다음 중 날씨 정보를 알고 싶은 지역을 골라 숫자를 적어주십시오.")

time.sleep(2)

print()

while True:
    print("1. 서울 / 2. 부산 / 3. 대전 / 4. 제주 / 5. 대구 / 6. 춘천 \n7. 강릉 / 8. 울릉도(독도) / 9. 백령도 / 10. 청주 / 11. 광주 / 12. 전주")
    print()
    region = input("입력 -> ")
    if region == "1":
        scrape_weather_seoul()
        time.sleep(2)
        print()
        question = input("다른 지역의 날씨도 검색해보시겠습니까? 원한다면 y, 그렇지 않고 종료를 원하면 n을 입력해주십시오. -> ")
        print()

        if question == 'y':
            continue

        if question == 'n':
            print("이용해주셔서 감사합니다. 좋은 하루 되십시오 ^^")
            print("프로그램을 종료합니다.")
            break

    elif region == "2":
        scrape_weather_busan()
        time.sleep(2)
        print()
        question = input("다른 지역의 날씨도 검색해보시겠습니까? 원한다면 y, 그렇지 않고 종료를 원하면 n을 입력해주십시오. -> ")
        print()

        if question == 'y':
            continue

        if question == 'n':
            print("이용해주셔서 감사합니다. 좋은 하루 되십시오 ^^")
            print("프로그램을 종료합니다.")
            break

    elif region == "3":
        scrape_weather_daejeon()
        time.sleep(2)
        print()
        question = input("다른 지역의 날씨도 검색해보시겠습니까? 원한다면 y, 그렇지 않고 종료를 원하면 n을 입력해주십시오. -> ")
        print()

        if question == 'y':
            continue

        if question == 'n':
            print("이용해주셔서 감사합니다. 좋은 하루 되십시오 ^^")
            print("프로그램을 종료합니다.")
            break

    elif region == "4":
        scrape_weather_jeju()
        time.sleep(2)
        print()
        question = input("다른 지역의 날씨도 검색해보시겠습니까? 원한다면 y, 그렇지 않고 종료를 원하면 n을 입력해주십시오. -> ")
        print()

        if question == 'y':
            continue

        if question == 'n':
            print("이용해주셔서 감사합니다. 좋은 하루 되십시오 ^^")
            print("프로그램을 종료합니다.")
            break

    elif region == "5":
        scrape_weather_daegu()
        time.sleep(2)
        print()
        question = input("다른 지역의 날씨도 검색해보시겠습니까? 원한다면 y, 그렇지 않고 종료를 원하면 n을 입력해주십시오. -> ")
        print()

        if question == 'y':
            continue

        if question == 'n':
            print("이용해주셔서 감사합니다. 좋은 하루 되십시오 ^^")
            print("프로그램을 종료합니다.")
            break

    elif region == "6":
        scrape_weather_chuncheon()
        time.sleep(2)
        print()
        question = input("다른 지역의 날씨도 검색해보시겠습니까? 원한다면 y, 그렇지 않고 종료를 원하면 n을 입력해주십시오. -> ")
        print()

        if question == 'y':
            continue

        if question == 'n':
            print("이용해주셔서 감사합니다. 좋은 하루 되십시오 ^^")
            print("프로그램을 종료합니다.")
            break

    elif region == "7":
        scrape_weather_gangleung()
        time.sleep(2)
        print()
        question = input("다른 지역의 날씨도 검색해보시겠습니까? 원한다면 y, 그렇지 않고 종료를 원하면 n을 입력해주십시오. -> ")
        print()

        if question == 'y':
            continue

        if question == 'n':
            print("이용해주셔서 감사합니다. 좋은 하루 되십시오 ^^")
            print("프로그램을 종료합니다.")
            break

    elif region == "8":
        scrape_weather_ulleungdo()
        time.sleep(2)
        print()
        question = input("다른 지역의 날씨도 검색해보시겠습니까? 원한다면 y, 그렇지 않고 종료를 원하면 n을 입력해주십시오. -> ")
        print()

        if question == 'y':
            continue

        if question == 'n':
            print("이용해주셔서 감사합니다. 좋은 하루 되십시오 ^^")
            print("프로그램을 종료합니다.")
            break

    elif region == "9":
        scrape_weather_baekryeongdo()
        time.sleep(2)
        print()
        question = input("다른 지역의 날씨도 검색해보시겠습니까? 원한다면 y, 그렇지 않고 종료를 원하면 n을 입력해주십시오. -> ")
        print()

        if question == 'y':
            continue

        if question == 'n':
            print("이용해주셔서 감사합니다. 좋은 하루 되십시오 ^^")
            print("프로그램을 종료합니다.")
            break

    elif region == "10":
        scrape_weather_cheongju()
        time.sleep(2)
        print()
        question = input("다른 지역의 날씨도 검색해보시겠습니까? 원한다면 y, 그렇지 않고 종료를 원하면 n을 입력해주십시오. -> ")
        print()

        if question == 'y':
            continue

        if question == 'n':
            print("이용해주셔서 감사합니다. 좋은 하루 되십시오 ^^")
            print("프로그램을 종료합니다.")
            break

    elif region == "11":
        scrape_weather_gwangju()
        time.sleep(2)
        print()
        question = input("다른 지역의 날씨도 검색해보시겠습니까? 원한다면 y, 그렇지 않고 종료를 원하면 n을 입력해주십시오. -> ")
        print()

        if question == 'y':
            continue

        if question == 'n':
            print("이용해주셔서 감사합니다. 좋은 하루 되십시오 ^^")
            print("프로그램을 종료합니다.")
            break

    elif region == "12":
        scrape_weather_jeonju()
        time.sleep(2)
        print()
        question = input("다른 지역의 날씨도 검색해보시겠습니까? 원한다면 y, 그렇지 않고 종료를 원하면 n을 입력해주십시오. -> ")
        print()

        if question == 'y':
            continue

        if question == 'n':
            print("이용해주셔서 감사합니다. 좋은 하루 되십시오 ^^")
            print("프로그램을 종료합니다.")
            break

    else:
        print("죄송합니다. 입력하신 지명은 보기에 없는 지명입니다. 지명을 잘못 입력하진 않으셨는지 다시 확인해주시기 바랍니다.")
        continue
