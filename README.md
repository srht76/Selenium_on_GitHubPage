# Selenium on Github Pages!
Here, I programed a basic unittest on github pages. The code  gives **title 's names**, **link** and **stars count**. I have used a scrolling function when we click the loading more  button  , it continue  to take existing data on page  until the bottom  of page. But I used  a for loop , It gives us just 3 pages .Also if you  want you can change that to get more data.  Because  of the scrolling  function ,it  takes some times to finish.
 
### Environment Setup

- [Install Python](https://www.python.org/downloads/)
- [PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows)
- [Selenium](https://selenium-python.readthedocs.io/)  or install on PyCharm
> Note: I already added   geckodriver.exe  to project file.


### Implementation
![resim](./Screenshot%20(1).png)
[GitHub_Page](https://github.com/topics/python/)

I used the path of 1,2,3 and loading More path
There are various strategies to locate elements in a page. You can use the most appropriate one for your case. I just used some of them. 
-   find_element_by_xpath
-   find_element_by_link_text
-   find_element_by_css_selector
- ....
**To find multiple elements (these methods will return a list):**
-   find_elements_by_xpath
-   find_elements_by_link_text
-   find_elements_by_css_selector
...



 The tearDown method will get called after every test method. So, this is place to do all cleanup functionalities. In the current method, the browser window is closed. You can also call quit method instead of close. The quit will exit all entire browser where as close will close one tab, but if it just one tab, by default most browser will exit entirely.:

```def tearDown(self):
    self.browser.close()
``` 
**
Final lines are some boiler plate code to run the test suite:

```
if __name__ == "__main__":
    unittest.main()
```

### Running Tests
```
total stars are :  7614
.
----------------------------------------------------------------------
Ran 1 test in 47.995s

OK


 
 
