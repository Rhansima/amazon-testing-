from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import csv

class one():
    def __int__(self, title, price):
        self.title = title
        self.price =price
class two():
    def data(self, name):
        count = 1
        page = 1
        add_page = 10
        maximum = 100

        my_list = []

        url = "https://www.amazon.com/s?k=" + name + "&page=" + str(page)

        my_options = Options()
        my_options.headless = False
        my_options.add_experimental_option("detach" , True)
        my_browser = webdriver.Chrome(ChromeDriverManager().install(), options=my_options)
        my_browser.maximize_window()
        my_browser.get(url)
        my_browser.set_page_load_timeout(12)

        while True:
            try:
                if add_page * page > maximum:
                    break
                if count > add_page :
                    count = 1
                    page = page + 1

                title_path = '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[7]/div/div/span/div/div/div/div[2]/div/div/div[1]/h2/a/span'
                title = my_browser.find_element_by_xpath(title_path)
                title_text = title.get_attribute("innerHTML").splitlines()[0]
                title.click()

                price_path = '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[7]/div/div/span/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/div[1]/a/span/span[2]/span[2]'
                price_text = price_path.get_attribute("innerHTML")

                url = "https://www.amazon.com/s?k=iphone+12"
                my_browser.get(url)
                my_browser.set_page_load_timeout(12)

                my_info = one(title_text , price_text)
                my_list.append(my_info)

                count = count + 1

            except Exception as e:
                print("Excetion on the count number", count, e)
                count = count + 1

                if add_page * page > maximum:
                    break

                if count > add_page:
                    count =1
                    page = page + 1

                    url = "https://www.amazon.com/s?k=iphone+12"
                    my_browser.get(url)
                    my_browser.set_page_load_timeout(12)

                my_browser.close()

                return my_list
fun_call = two()

with open('one.csv' , 'w', newline='', encoding='utf-8') as csv
    data = csv.writer(csvfile, delimiter = ';', quotechar='"' , quoting=csv.QUOTE.MINIMUM)
    for artical in fun_call.data("iphone 12"):
        data.writerow([artical.title, artical.price])



