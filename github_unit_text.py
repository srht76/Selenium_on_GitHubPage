import unittest
from selenium import webdriver
import time
import list_object_to_int


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        url = "https://github.com/topics/python"
        driver.get(url)
        time.sleep(2)
        ##
        # scroll pages
        scroll_js_com = """window.scrollTo(0, document.body.scrollHeight);
               var lenOfPage=document.body.scrollHeight;
               return lenOfPage; """
        len_of_page = driver.execute_script(scroll_js_com)
        match = False
        import copy

        while not match:
            last_count = copy.deepcopy(len_of_page)
            time.sleep(2)
            len_of_page = driver.execute_script(scroll_js_com)
            if last_count == len_of_page:
                match = True
        time.sleep(5)
        ###
        # click on loading more button to reach next 3 pages to  existing data
        star_total = 0
        for count in range(3):
            loading_more_xpath = """
            /html/body/div[5]/main/div[2]/div[2]/div/div[1]/form/button
            """
            try:
                load_more_button = driver.find_element_by_xpath(loading_more_xpath)
                load_more_button.click()
                time.sleep(1)
                ##
                # titles on github pages
                elements = driver.find_elements_by_css_selector(".f3.text-gray.text-normal.lh-condensed")
                titles = [element.text for element in elements]
                # titles = [element.text for element in elements] we can write this as below
                # titles = []
                # for element in elements:
                #    titles.append(element.text)

                # Write all links a file
                with open("title.txt", "w", encoding="UTF-8") as file:
                    for title_count,t in enumerate(titles):
                        file.write(str(title_count) + ".\n" + t + "\n")
                        file.write("**************************\n")

                """elem = driver.find_elements_by_xpath(\"//*[@href]\") >>> all href ob page"""

                link = [a.get_attribute('href') for a in driver.find_elements_by_xpath('.//a[@class="text-bold"]')]
                #  these three command lines refer to the up line
                # link = []
                # for a in driver.find_elements_by_xpath('.//a[@class="text-bold"]'):
                # link.append(a.get_attribute('href'))

                # Write all links a file
                with open("links.txt", "w", encoding="UTF-8") as file:
                    for link_count, a in enumerate(link):
                        file.write(str(link_count) + ".\n" + a + "\n")
                        file.write("**************************\n")
                star = []
                stars = driver.find_elements_by_css_selector(".social-count.float-none")
                for element in stars:
                    star.append(element.text)
                    star_total = star_total + list_object_to_int.list_object_sum(element.text)
            except Exception as e:
                print(e)
                break
        print("total stars are : ", star_total)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

