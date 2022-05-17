from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select


#BUTTONS TESTS
shopNowWomen= "//main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/a[1]/span[1]/span[1]"
shopNowMen= "//main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/a[1]/span[1]/span[1]"
checkOut= "//span[contains(text(),'Check Out')]"
#SEARCH FIELD
search ="//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]"
insertKeys= "//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/form[1]/label[1]/input[1]"
clickSearch= "//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]"
prudactName="//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/article[1]/div[1]/div[1]/header[1]/h2[1]/a[1]"
prudactDescr="//main[1]/div[1]/article[1]/div[1]/div[1]/div[2]"


def init():
    driver= webdriver.Chrome("..\Driver\chromedriver.exe")
    driver.get("https://atid.store/")
    driver.maximize_window()
    return driver

#TEST 1
def test_Buttons_Menu():
    driver= init()
    #ul of menu links
    driver.find_elements(By.ID,"ast-hf-menu-1")
    #index
    p=0
    while p<7:
        links= driver.find_elements(By.CLASS_NAME,"menu-link")
        links[p].click()
        p=p+1

#TEST 2
def test_Buttons_MidBar():
    driver= init()
    #logo button
    driver.find_element(By.XPATH,"//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/a[1]/img[1]").click()
    #cart button
    driver.find_element(By.XPATH,"//span[contains(text(),'0')]").click()
    driver.back()
    #shop now button
    driver.find_element(By.CLASS_NAME,"elementor-button-text").click()
    driver.back()
    #find more button
    driver.find_element(By.XPATH,"//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/a[1]").click()
    driver.back()
    #shop now women department
    driver.find_element(By.XPATH,shopNowWomen).click()
    driver.back()
    #shop now men department
    driver.find_element(By.XPATH,shopNowMen).click()
    driver.back()
    #checkOut
    driver.find_element(By.XPATH,checkOut).click()
    driver.quit()

#TEST 3
def test_Buttons_ProductsImags():
    driver= init()
    #UL of all prudacts imags(10 prudacts images)
    driver.find_elements(By.CLASS_NAME,"products columns-5")
    #index
    p=0
    #loop that run all images(li) in ul and click
    while p>10:
        images = driver.find_elements(By.XPATH,"//main[1]/article[1]/div[1]/div[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/ul[1]/li[1]")
        images[p].click()
        driver.back()
        p=p+1
        driver.find_elements(By.XPATH,"//main[1]/article[1]/div[1]/div[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/ul[1]/li[1]")

#TEST 4
def test_Buttins_slider():
    driver= init()
    #MOVE FORWARD
    driver.find_element(By.XPATH,"//main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]").click()
    #MOVE BACKWARD
    driver.find_element(By.XPATH,"//main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]").click()
    driver.quit()


#TEST 5
def test_Buttons_Footer():
    driver= init()
    #Quick links buttons
    quickLinks= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,"menu-quick-links")))
    quickLinks.click()
    #For her buttons
    for_her= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//ul[@id='menu-for-her']")))
    for_her.click()
    #For him buttons
    driver.find_elements(By.ID,"menu-for-him")
    p=0
    while p<5:
        button= driver.find_elements(By.XPATH,"//body[1]/div[1]/footer[1]/div[1]/div[1]/div[1]/div[3]/aside[1]/div[1]/section[1]/nav[1]/ul[1]/li/a")
        button[p].click()
        driver.back()
        p=p+1
        driver.find_elements(By.XPATH, "//body[1]/div[1]/footer[1]/div[1]/div[1]/div[1]/div[3]/aside[1]/div[1]/section[1]/nav[1]/ul[1]/li/a")

#############################TESTS FOR SEARCH FIELD###################################33

##TEST 6
def test_DisplayPrudact_AnchlorBracelte():
    driver = init()
    #search field
    driver.find_element(By.XPATH,search).click()
    #insert prudact name in field
    driver.find_element(By.XPATH, insertKeys).send_keys("Anchor Bracelet")
   #click search
    driver.find_element(By.XPATH,clickSearch).click()
   #verify the prudact name is correct
    itemName= driver.find_element(By.XPATH,prudactName).get_attribute("innerText")
    assert itemName== "Anchor Bracelet"
    #verify the description is correct
    description= driver.find_element(By.XPATH,prudactDescr).get_attribute("innerText")
    assert description == "Nam nec tellus a odio tincidunt auctor a ornare odio. Sed non mauris vitae erat consequat auctor eu in elit. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Mauris in erat justo. Nullam ac urna eu felis dapibus condimentum sit amet a augue. Sed non neque elit sed."
    driver.quit()


##TEST 7
def test_DisplayPrudact_Flamingo_Tshirt():
    driver = init()
    #search field
    driver.find_element(By.XPATH,search).click()
    #insert prudact name in field
    driver.find_element(By.XPATH, insertKeys).send_keys("Flamingo Tshirt")
   #click search
    driver.find_element(By.XPATH,clickSearch).click()
   #verify the prudact name is correct
    itemName= driver.find_element(By.XPATH,prudactName).get_attribute("innerText")
    assert itemName== "Flamingo Tshirt"
    #verify the description is correct
    description= driver.find_element(By.XPATH,prudactDescr).get_attribute("innerText")
    assert description == "Nam nec tellus a odio tincidunt auctor a ornare odio. Sed non mauris vitae erat consequat auctor eu in elit. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Mauris in erat justo. Nullam ac urna eu felis dapibus condimentum sit amet a augue. Sed non neque elit sed ."
    driver.quit()

##TEST 8
def test_DisplayPrudact_Dark_GrayJeans():
    driver = init()
    # click on search
    driver.find_element(By.XPATH,search).click()
    # insert Dark gray jeans in search field
    driver.find_element(By.XPATH,insertKeys).send_keys("Dark Gray Jeans")
    # click search
    driver.find_element(By.XPATH,clickSearch).click()
    #verify the prudact name is correct
    itemName= driver.find_element(By.XPATH,prudactName).get_attribute("innerText")
    assert itemName== "Dark Gray Jeans"
    #verify the description is correct
    description= driver.find_element(By.XPATH,prudactDescr).get_attribute("innerText")
    assert description == "Nam nec tellus a odio tincidunt auctor a ornare odio. Sed non mauris vitae erat consequat auctor eu in elit. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Mauris in erat justo. Nullam ac urna eu felis dapibus condimentum sit amet a augue. Sed non neque elit sed."
    driver.quit()

##TEST 9
def test_DisplayError_When_searchField_isNull():
    driver= init()
    #click on search
    driver.find_element(By.XPATH,search).click()
    #field is null
    driver.find_element(By.XPATH,insertKeys).send_keys("")
    #click search
    driver.find_element(By.XPATH,clickSearch).click()
    #search reasult
    result= driver.find_element(By.XPATH,"//main[1]/section[1]/div[1]").get_attribute("innerText")
    assert result == "Sorry, but nothing matched your search terms. Please try again with some different keywords.\n\nSearch for:\n "
    driver.quit()

##TEST 10
def test_DisplayError_When_Search_UnexistItem_Watch():
    driver= init()
    #click on search
    driver.find_element(By.XPATH, search).click()
    #insert "watch" in search field
    driver.find_element(By.XPATH, insertKeys).send_keys("Watch")
    #click search
    driver.find_element(By.XPATH,clickSearch).click()
    #search reasult
    result= driver.find_element(By.XPATH,"//main[1]/section[1]/div[1]").get_attribute("innerText")
    assert result == "Sorry, but nothing matched your search terms. Please try again with some different keywords.\n\nSearch for:\n "
    driver.quit()

#TEST 11
def test_DisplayError_When_Search_numbers():
    driver= init()
    #click on search
    driver.find_element(By.XPATH, search).click()
    #insert "watch" in search field
    driver.find_element(By.XPATH, insertKeys).send_keys("1234")
    #click search
    driver.find_element(By.XPATH,clickSearch).click()
    #search reasult
    result= driver.find_element(By.XPATH,"//main[1]/section[1]/div[1]").get_attribute("innerText")
    assert result == "Sorry, but nothing matched your search terms. Please try again with some different keywords.\n\nSearch for:\n "
    driver.quit()

#TEST 12
def test_DisplayError_When_Search_signs():
    driver= init()
    #click on search
    driver.find_element(By.XPATH, search).click()
    #insert "watch" in search field
    driver.find_element(By.XPATH, insertKeys).send_keys("@#$%^&!")
    #click search
    driver.find_element(By.XPATH,clickSearch).click()
    #search reasult
    result= driver.find_element(By.XPATH,"//main[1]/section[1]/div[1]").get_attribute("innerText")
    assert result == "Sorry, but nothing matched your search terms. Please try again with some different keywords.\n\nSearch for:\n "
    driver.quit()


#################################UI TEST - HOMEPAGE ###########################################

#TEST 13
def test_UI_HomePage():
    driver= init()

    #menu bar
    menuBar = driver.find_element(By.XPATH, "//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]").get_attribute("innerText")
    assert menuBar == "HOME\nSTORE\nMEN\nWOMEN\nACCESSORIES\nABOUT\nCONTACT US\nSearch\n0.00\xa0₪ 0"

    # information
    middleBar = driver.find_element(By.XPATH,"//main[1]/article[1]/div[1]/div[1]/div[1]/section[3]/div[1]/div[1]/div[1]/section[2]").get_attribute("innerText")
    assert middleBar == 'Worldwide Shipping\n\nIt elit tellus, luctus nec ullamcorper mattis, pulvinar dapibus leo.\n\nBest Quality\n\nIt elit tellus, luctus nec ullamcorper mattis, pulvinar dapibus leo.\n\nBest Offers\n\nIt elit tellus, luctus nec ullamcorper mattis, pulvinar dapibus leo.\n\nSecure Payments\n\nIt elit tellus, luctus nec ullamcorper mattis, pulvinar dapibus leo.'

    # footer
    footer = driver.find_element(By.XPATH, "//body[1]/div[1]/footer[1]/div[1]/div[1]/div[1]").get_attribute("innerText")
    assert footer == 'Quick Links\nHome\nAbout\nCart\nContact Us\nFor Her\nWomen Jeans\nTops and Shirts\nWomen Jackets\nHeels and Flats\nWomen Accessories\nFor Him\nMen Jeans\nMen Shirts\nMen Shoes\nMen Accessories\nMen Jackets'

    # copyrights
    copyrights = driver.find_element(By.XPATH, "//body[1]/div[1]/footer[1]/div[2]/div[1]").get_attribute("innerText")
    assert copyrights == "Copyright © 2022 ATID Demo Store\n\nPowered by ATID College"

    #sales bar
    sales= driver.find_element(By.XPATH,"//main[1]/article[1]/div[1]/div[1]/div[1]/section[2]").get_attribute("innerText")
    assert sales == "Previous\nNext\n20% Off On Tank Tops\n\nLorem ipsum dolor sit amet consec tetur.\n\nSHOP NOW\nLatest Eyewear For You\n\nLorem ipsum dolor sit amet consec tetur.\n\nSHOP NOW\nLet's Lorem Suit Up!\n\nLorem ipsum dolor sit amet consec tetur.\n\nCHECK OUT"

    #prudacts
    prudacts= driver.find_element(By.XPATH,"//main[1]/article[1]/div[1]/div[1]/div[1]/section[3]/div[1]/div[1]/div[1]").get_attribute("innerText")
    assert prudacts == "Featured Products\nSale!\nATID Yellow Shoes\nMen\n150.00 ₪ 120.00 ₪\nRated\n4.50\nout of 5\nSale!\nATID Blue Shoes\nMen\n120.00 ₪ 80.00 ₪\nRated\n4.00\nout of 5\nDark Brown Jeans\nMen\n150.00 ₪\nRated\n4.33\nout of 5\nBlue Denim Jeans\nWomen\n150.00 ₪\nRated\n0\nout of 5\nBasic Gray Jeans\nWomen\n100.00 ₪\nRated\n4.00\nout of 5\nSale!\nBlue Denim Shorts\nWomen\n150.00 ₪ 130.00 ₪\nRated\n3.00\nout of 5\nSale!\nFlamingo Tshirt\nWomen\n150.00 ₪ 50.00 ₪\nRated\n4.75\nout of 5\nAnchor Bracelet\nAccessories\n250.00 ₪\nRated\n3.73\nout of 5\nBoho Bangle Bracelet\nAccessories\n45.00 ₪\nRated\n5.00\nout of 5\nLight Brown Purse\nAccessories\n75.00 ₪\nRated\n3.00\nout of 5\nLimited Time Offer\nSpecial Edition\n\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Ut elit tellus, luctus nec ullamcorper mattis, pulvinar dapibus leo.\n\nBuy This T-shirt At 20% Discount, Use Code OFF20\nSHOP NOW\nWorldwide Shipping\n\nIt elit tellus, luctus nec ullamcorper mattis, pulvinar dapibus leo.\n\nBest Quality\n\nIt elit tellus, luctus nec ullamcorper mattis, pulvinar dapibus leo.\n\nBest Offers\n\nIt elit tellus, luctus nec ullamcorper mattis, pulvinar dapibus leo.\n\nSecure Payments\n\nIt elit tellus, luctus nec ullamcorper mattis, pulvinar dapibus leo."

    #limited editon
    limited= driver.find_element(By.XPATH,"//main[1]/article[1]/div[1]/div[1]/div[1]/section[3]/div[1]/div[1]/div[1]/section[1]/div[2]/div[1]/div[1]").get_attribute("innerText")
    assert limited == 'Limited Time Offer\nSpecial Edition\n\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Ut elit tellus, luctus nec ullamcorper mattis, pulvinar dapibus leo.\n\nBuy This T-shirt At 20% Discount, Use Code OFF20\nSHOP NOW'
    driver.quit()






