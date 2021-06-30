from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json 

def scrape():
    options = Options()
    options.binary_location = "./google-chrome"
    options.headless = True
    browser = webdriver.Chrome(options=options, executable_path='./chromedriver')
    browser.get("https://www.worldometers.info/")
    array0 = browser.find_elements_by_xpath('//span[contains(@class,"counter-item")]')
    array1 = browser.find_elements_by_xpath('//span[@class="rts-counter"][not(contains(@rel, "oil_years")) and not(contains(@rel,"cd_oil_reserves_0"))]')

    stats = [ele.get_attribute('innerText') for ele in array1]
    stats[7] = "$" + stats[7]
    stats[8] = "$" + stats[8]
    stats[9] = "$" + stats[9]
    stats[17] = "$" + stats[17]
    stats[32] = "$" + stats[32]
    stats[33] = "$" + stats[33]
    stats[-2] = "$" + stats[-2]


    names = [ele.get_attribute('innerText').replace('\n'," ") for ele in array0]

    names[27] = names[27] + " (tons)"
    names[37] = names[37][:-11]
    names[38] = "Energy used today" + names[38][1:]
    names[39] = "Energy used today" + names[39][1:]
    names[40] = names[40] + " (MWh)"

    with open("livedata.json", "w+") as f:
        json.dump(dict(zip(names,stats)), f)

