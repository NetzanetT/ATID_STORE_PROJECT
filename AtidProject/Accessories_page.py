from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver

def init():
    driver = webdriver.Chrome("../Driver/chrome_driver/chromedriver.exe")
    driver.get("https://atid.store/product-category/accessories/")
    driver.maximize_window()
    return driver

#Test 1
def test_Menu_bar_buttons():
    driver = init()
    #Ul id
    driver.find_elements(By.ID,"ast-hf-menu-1")
    page=0
    #Loop on buttons
    while page < 7 :
    #Li class name
        menu_link = driver.find_elements(By.CLASS_NAME, "menu-link")
        menu_link[page].click()
        page = page + 1

#Test 2
def test_logo_links():
    driver = init()
    #Element class name
    driver.find_element(By.CLASS_NAME,"custom-logo").click()

#Test 3
def test_Search_exist_item():
    driver = init()
    #Element of search button
    search = "//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]"

    driver.find_element(By.XPATH,search).click()
    #Class name of search field
    driver.find_element(By.CLASS_NAME,"search-field").send_keys("ATID Blue Shoes")
    driver.find_element(By.XPATH,search).click()

#Test 4
def test_Search_unexist_item():
    driver = init()
    #Element of search button
    search = "//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]"

    driver.find_element(By.XPATH,search).click()
    ##Class name of search field
    driver.find_element(By.CLASS_NAME,"search-field").send_keys("NIKE")
    driver.find_element(By.XPATH,search).click()
    #Element of search results
    Search_Results = driver.find_element(By.XPATH,"//main[1]/section[1]/div[1]").get_attribute("innerText")
    #Assert element with search results
    assert Search_Results == "Sorry, but nothing matched your search terms. Please try again with some different keywords.\n\nSearch for:\n "

#Test 5
def test_cart_link():
    driver = init()
    #Element of cart link
    driver.find_element(By.XPATH,"//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[3]/div[3]/div[1]/div[1]/a[1]").click()


#Test 6
def test_sorting_button():
    driver = init()
    #Ul xpath
    driver.find_elements(By.XPATH,"//main[1]/div[1]/form[1]/select[1]")
    sort_option = 1
    #Loop on buttons
    while sort_option < 5:
    #Li xpath
        a = driver.find_elements(By.XPATH, "//main[1]/div[1]/form[1]/select[1]/option")
        a[sort_option].click()
        sort_option = sort_option + 1

#Test 7
def test_items_Categorieslink():
    driver = init()
    #Ul xpath
    driver.find_elements(By.XPATH,"//body/div[@id='page']/div[@id='content']/div[1]/div[1]/div[1]/div[3]/ul[1]")
    link_num=0
    #Loop on links
    while link_num< 3 :
    #Li xpath
        li = driver.find_elements(By.XPATH, "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/div[1]/div[3]/ul[1]/li/a[1]")
        li[link_num].click()
        link_num = link_num + 1

#Test 8
def test_slider_button():
    driver = init()
    elemLeft ="//body/div[@id='page']/div[@id='content']/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/span[1]"
    elemRight = "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/span[2]"
    elemClick = "//button[contains(text(),'Filter')]"

    sliderLeft = driver.find_element(By.XPATH,elemLeft)

    slider = ActionChains(driver).move_to_element(sliderLeft).pause(1).click_and_hold(sliderLeft)
    slider.move_by_offset(10,0).release().perform()
    driver.find_element(By.XPATH,elemClick).click()

    sliderLeft = driver.find_element(By.XPATH, elemLeft)
    slider = ActionChains(driver).move_to_element(sliderLeft).pause(1).click_and_hold(sliderLeft)

    sliderLeft = driver.find_element(By.XPATH, elemLeft)
    slider.move_by_offset(100,0).release().perform()



    sliderLeft = driver.find_element(By.XPATH, elemLeft)
    slider = ActionChains(driver).move_to_element(sliderLeft).pause(1).click_and_hold(sliderLeft)
    slider.move_by_offset(250,0).release().perform()
    driver.find_element(By.XPATH,elemClick).click()

#Test 9
def test_itemSellers_links():
    driver = init()
    #Ul class_name
    driver.find_elements(By.CLASS_NAME,"product_list_widget")
    link_item=0
    #Loop on link_item
    while link_item < 5 :
    #Li xpath
        li = driver.find_elements(By.XPATH, "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/div[1]/div[4]/ul[1]/li/a[1]")
        li[link_item].click()
        driver.back()
        link_item = link_item + 1

#Test 10
def test_buttons_footer():
    driver = init()

    #Ul class_name
    driver.find_elements(By.ID,"menu-quick-links")
    link_item=0
    #Loop on links
    while link_item < 4 :
    #Li xpath
        li = driver.find_elements(By.XPATH, "//body[1]/div[1]/footer[1]/div[1]/div[1]/div[1]/div[1]/aside[1]/div[1]/section[1]/nav[1]/ul[1]/li/a[1]")
        li[link_item].click()
        driver.back()
        link_item = link_item + 1
    #Ul xpath
    driver.find_elements(By.XPATH, "//ul[@id='menu-for-her']")
    link_item = 0
    #loop on links
    while link_item < 5:
    #Li xpath
        li = driver.find_elements(By.XPATH,"//body[1]/div[1]/footer[1]/div[1]/div[1]/div[1]/div[2]/aside[1]/div[1]/section[1]/nav[1]/ul[1]/li/a[1]")
        li[link_item].click()
        link_item = link_item + 1
    #Element class name
    driver.find_elements(By.CLASS_NAME, "menu-for-him-container")
    link_item = 0
    #Loop on links
    while link_item < 5:
    #Li xpath
        li = driver.find_elements(By.XPATH,"//body[1]/div[1]/footer[1]/div[1]/div[1]/div[1]/div[3]/aside[1]/div[1]/section[1]/nav[1]/ul[1]/li/a[1]")
        li[link_item].click()
        link_item = link_item + 1

#Test 11
def testUI():
    driver = init()
    #Element xpath of menu bar
    elem = driver.find_element(By.XPATH, "//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]").get_attribute("innerText")
    #Assert elem
    assert elem == "HOME\nSTORE\nMEN\nWOMEN\nACCESSORIES\nABOUT\nCONTACT US"

    #TestUI_accessoies
    driver = init()
    a = driver.find_element(By.XPATH, "//body/div[@id='page']/div[@id='content']/div[1]/div[2]/main[1]/div[1]/nav[1]").get_attribute("innerText")
    assert a == "Home\xa0/\xa0Accessories"


    elem = driver.find_element(By.XPATH, "//h1[contains(text(),'Accessories')]").get_attribute("innerText")
    assert elem == "Accessories"


    elem = driver.find_element(By.XPATH, "//p[contains(text(),'Showing all 7 results')]").get_attribute("innerText")
    assert elem == "Showing all 7 results"


    #TestUi of sorting_button
    elem = driver.find_element(By.XPATH, "//main[1]/div[1]/form[1]/select[1]").get_attribute("innerText")
    assert elem == "Default sorting\nSort by popularity\nSort by average rating\nSort by latest\nSort by price: low to high\nSort by price: high to low"

    #TestUi of items
    elem = driver.find_element(By.XPATH,"//body/div[@id='page']/div[@id='content']/div[1]/div[2]/main[1]/div[1]/ul[1]").get_attribute("innerText")
    assert elem == "Anchor Bracelet\nAccessories\n250.00\xa0₪\nRated\n3.73\nout of 5\nBlack Over-the-shoulder Handbag\nAccessories\n85.00\xa0₪\nRated\n4.17\nout of 5\nBoho Bangle Bracelet\nAccessories\n45.00\xa0₪\nRated\n5.00\nout of 5\nSale!\nBright Gold Purse With Chain\nAccessories\n85.00\xa0₪ 80.00\xa0₪\nRated\n4.50\nout of 5\nBright Red Bag\nAccessories\n150.00\xa0₪\nRated\n3.25\nout of 5\nSale!\nBuddha Bracelet\nAccessories\n45.00\xa0₪ 30.00\xa0₪\nRated\n4.50\nout of 5\nLight Brown Purse\nAccessories\n75.00\xa0₪\nRated\n3.00\nout of 5"


    #TestUi buttons_footer
    elem = driver.find_element(By.XPATH,"//body/div[@id='page']/footer[@id='colophon']/div[1]/div[1]").get_attribute("innerText")
    assert elem == "Quick Links\nHome\nAbout\nCart\nContact Us\nFor Her\nWomen Jeans\nTops and Shirts\nWomen Jackets\nHeels and Flats\nWomen Accessories\nFor Him\nMen Jeans\nMen Shirts\nMen Shoes\nMen Accessories\nMen Jackets"
































































