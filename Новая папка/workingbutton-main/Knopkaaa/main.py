import requests
import bs4
import time


# pip install webdriver-manager
# sudo apt install firefox-geckodriver
# which geckodriver
# https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path
def get_anekdot():
    from selenium import webdriver
    url = 'https://www.chosic.com/random-songs-generator-with-links-to-spotify-and-youtube/'

    # EXE_PATH = "chromedriver.exe"  # EXE_PATH это путь до ранее загруженного нами файла chromedriver.exe

    k = 0
    # driver = webdriver.Firefox(executable_path=r"geckodriver\geckodriver.exe")
    driver = webdriver.Chrome(executable_path=r"webdrivers\chromedriver.exe")
    driver.get(url)
    element = driver.find_element_by_id("generate")
    element.click()
    time.sleep(3)
    html = driver.page_source
    # print(html)
    # req_anek = requests.get(url)
    # array_anekdots = []
    soup = bs4.BeautifulSoup(html, "html.parser")
    # result_find = soup.select('button data-title')
    result_find = soup.find('div', id="track-details")

    for children in result_find.children:
        print(children)

        # return (0)
    # result_find = soup.select('button data-title')

    src = ""
    result_find1 = soup.find('div', id="video-container")
    for content in result_find1.contents:
        if isinstance(content, bs4.element.Tag):
            for content2 in content.contents:
                if isinstance(content2, bs4.element.Tag):
                    src = content2.attrs.get("src", "")
                    if src:
                        break

    print(src)
        # if isinstance(contents, bs4.element.Tag) and k>1:
        #     if isinstance("3", bs4.element.dict):
        #       print(src)
        # else:
        #     k=k+1

        # return(0)

    # for result in result_find:
    #     array_anekdots.append(result.getText().strip())
    # return array_anekdots[0]
    # print(result_find)


print(get_anekdot())
# https://stackoverflow.com/questions/11736027/webdriver-wait-for-element-using-java
