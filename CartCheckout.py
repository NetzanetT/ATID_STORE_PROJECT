from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import *


driver = webdriver.Chrome("C:/webdeiver/chromedriver.exe")

def init():
    driver = webdriver.Chrome("C:/webdeiver/chromedriver.exe")
    driver.get("https://www.atid.store")
    driver.implicitly_wait(30)
    driver.maximize_window()
    return driver

def test_add_to_cart():
    # 1 Check the add to cart button is clickable or not.
    driver=init()
    #ACCOSSORIES PAGE
    driver.find_element(By.XPATH ,"//li[@id='menu-item-671']//a[@class='menu-link'][normalize-space()='Accessories']").click()
    driver.execute_script("window.scrollTo(0,200);")
    sleep(3)
    #Anchor Bracelet product
    driver.find_element(By.XPATH, "//h2[contains(text(),'Anchor Bracelet')]").click()
    driver.execute_script("window.scrollTo(0,200);")
    #Add to cart button
    driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click()
    sleep(3)
    driver.quit()

def test_verify_adding_item():
    #2 Check after Adding one item to the cart and verify.
    # ACCOSSORIES PAGE
    driver=init()
    driver.find_element(By.XPATH, "//li[@id='menu-item-671']//a[@class='menu-link'][normalize-space()='Accessories']").click()
    driver.execute_script("window.scrollTo(0,200);")
    #Anchor Bracelet product
    driver.find_element(By.XPATH, "//h2[contains(text(),'Anchor Bracelet')]").click()
    driver.execute_script("window.scrollTo(0,200);")
    # Add to cart button
    driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click()
    #Click on view cart button
    driver.find_element(By.XPATH, "//span[normalize-space()='1']").click()
    sleep(3)
    driver.quit()

def test_check_count_increase():
    #3 Check on adding the new products into the cart and whether the count is increasing or not.
    driver = init()
    driver.find_element(By.XPATH,"//li[@id='menu-item-671']//a[@class='menu-link'][normalize-space()='Accessories']").click()
    driver.find_element(By.XPATH, "//h2[contains(text(),'Black Over-the-shoulder Handbag')]").click()
    # Add to cart
    driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click()
    #ACCOSSORIES PAGE
    driver.find_element(By.XPATH, "//li[@id='menu-item-671']//a[@class='menu-link'][normalize-space()='Accessories']").click()
    #Anchor Bracelet product
    driver.find_element(By.XPATH, "//h2[contains(text(),'Anchor Bracelet')]").click()
    driver.execute_script("window.scrollTo(0,200);")
    #Add to cart button
    driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click()
    #Click on view cart button to see if the quantity is increased
    driver.find_element(By.XPATH, "//span[@class='count']").click()
    driver.execute_script("window.scrollTo(0,200);")
    sleep(3)
    driver.quit()

def test_same_twice():
    #4 Check when the same item is added multiple times to the cart.
    #GOLD CHAIN
    driver = init()
    driver.find_element(By.XPATH,"//li[@id='menu-item-671']//a[@class='menu-link'][normalize-space()='Accessories']").click()
    driver.find_element(By.XPATH, "// h2[contains(text(), 'Bright Gold Purse With Chain')]").click()
    driver.execute_script("window.scrollTo(0,200);")
    # Add to cart twice
    driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click()
    sleep(2)
    driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click()
    sleep(2)
    driver.quit()

def test_check_cart():
    #5 Check that the added item is displayed in the cart.
    # ACCOSSORIES PAGE
    driver.find_element(By.XPATH, "//li[@id='menu-item-671']//a[@class='menu-link'][normalize-space()='Accessories']").click()
    driver.find_element(By.XPATH, "// h2[contains(text(), 'Bright Red Bag')]").click()
    # Add to cart
    driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click()
    driver.find_element(By.XPATH, "//span[@class='count']").click()
    driver.execute_script("window.scrollTo(0,200);")
    sleep(3)
    driver.quit()

def test_remove_item():
    #6 Check after removing all items in the cart.
    # ACCOSSORIES PAGE
    driver = init()
    driver.find_element(By.XPATH, "//li[@id='menu-item-671']//a[@class='menu-link'][normalize-space()='Accessories']").click()
    driver.execute_script("window.scrollTo(0,200);")
    driver.find_element(By.XPATH, "    //h2[contains(text(),'Buddha Bracelet')]").click()
    # Add to cart
    driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click()
    #go to my cart page
    driver.find_element(By.XPATH, "//span[@class='count']").click()
    # remove the item
    driver.find_element(By.XPATH, "//a[@aria-label='Remove this item']").click()
    sleep(2)
    # ACCOSSORIES PAGE
    driver.find_element(By.XPATH, "//li[@id='menu-item-671']//a[@class='menu-link'][normalize-space()='Accessories']").click()
    sleep(2)
    driver.quit()

def test_remove():
    #7 Check that the count is changing on adding or removing items from the cart.
    driver = init()
    driver.find_element(By.XPATH,"//li[@id='menu-item-671']//a[@class='menu-link'][normalize-space()='Accessories']").click()
    #add product to the basket
    driver.find_element(By.XPATH, "// h2[contains(text(), 'Bright Gold Purse With Chain')]").click()
    driver.execute_script("window.scrollTo(0,200);")
    # Add to cart
    driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click()
    driver.find_element(By.XPATH,"//li[@id='menu-item-671']//a[@class='menu-link'][normalize-space()='Accessories']").click()
    driver.find_element(By.XPATH, "//h2[normalize-space()='Bright Red Bag']").click()
    #Add another product
    driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click()
    #go to my cart
    driver.find_element(By.XPATH, "//span[normalize-space()='2']").click()
    # remove one item
    driver.find_element(By.XPATH, "//a[@aria-label='Remove this item']").click()
    sleep(2)
    driver.quit()

def test_add_multipale():
    #8.1 Check after Adding multiple items of different types and verify.
    #8.2 Check that the UI of the add to cart is as per the requirement.
    driver = init()
    driver.find_element(By.XPATH,"//li[@id='menu-item-671']//a[@class='menu-link'][normalize-space()='Accessories']").click()
    #add product to the basket
    driver.find_element(By.XPATH, "// h2[contains(text(), 'Bright Gold Purse With Chain')]").click()
    driver.execute_script("window.scrollTo(0,200);")
    # Add to cart
    driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click()
    driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click()
    driver.find_element(By.XPATH,"//li[@id='menu-item-671']//a[@class='menu-link'][normalize-space()='Accessories']").click()
    driver.find_element(By.XPATH, "//h2[normalize-space()='Bright Red Bag']").click()
    #Add another product
    driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click()
    driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click()
    #go to my cart
    driver.find_element(By.XPATH, "//div[@role='alert']//a[@class='button wc-forward'][normalize-space()='View cart']").click()
    sleep(3)
    driver.quit()

def test_add_multipale():
    #8.1 Check after Adding multiple items of different types and verify.
    #8.2 Check that the UI of the add to cart is as per the requirement.
    driver = init()
    driver.find_element(By.XPATH,"//li[@id='menu-item-671']//a[@class='menu-link'][normalize-space()='Accessories']").click()
    #add product to the basket
    driver.find_element(By.XPATH, "// h2[contains(text(), 'Bright Gold Purse With Chain')]").click()
    driver.execute_script("window.scrollTo(0,200);")
    # Add to cart
    driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click()
    driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click()
    driver.find_element(By.XPATH,"//li[@id='menu-item-671']//a[@class='menu-link'][normalize-space()='Accessories']").click()
    driver.find_element(By.XPATH, "//h2[normalize-space()='Bright Red Bag']").click()
    #Add another product
    driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click()
    driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click()
    #go to my cart
    driver.find_element(By.XPATH, "//div[@role='alert']//a[@class='button wc-forward'][normalize-space()='View cart']").click()
    sleep(3)
    driver.quit()


def test_cart2checkout():
    #9 Check User can access the Checkout-Page only after adding the product to the cart
    driver = init()
    #ACCOSSORIES PAGE
    driver.find_element(By.XPATH, "//li[@id='menu-item-671']//a[@class='menu-link'][normalize-space()='Accessories']").click()
    driver.execute_script("window.scrollTo(0,200);")
    # Anchor Bracelet product
    driver.find_element(By.XPATH, "//h2[contains(text(),'Anchor Bracelet')]").click()
    driver.execute_script("window.scrollTo(0,200);")
    # Add to cart button
    driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click()
    #move to cart page
    driver.find_element(By.XPATH,"//div[contains(@class,'ast-site-header-cart-li')]//bdi[1]").click()
    #write unvalid coupon
    driver.find_element(By.XPATH,"// input[ @ id = 'coupon_code']").send_keys("g-unit")
    driver.find_element(By.XPATH, "//button[contains(text(),'Apply coupon')]").click()
    #Choose shipping method
    driver.execute_script("window.scrollTo(0,1000);")
    driver.find_element(By.XPATH, "//input[@id='shipping_method_0_local_pickup1']").click()
    driver.execute_script("window.scrollTo(0,800);")
    sleep(2)
    driver.find_element(By.XPATH, "//input[@id='shipping_method_0_flat_rate3']").click()
    driver.execute_script("window.scrollTo(0,800);")
    sleep(2)
    driver.find_element(By.XPATH, "//input[@id='shipping_method_0_flat_rate4']").click()
    driver.execute_script("window.scrollTo(0,800);")
    sleep(2)
    driver.find_element(By.XPATH, "//input[@id='shipping_method_0_free_shipping2']").click()
    sleep(2)
    driver.find_element(By.XPATH, "//a[contains(text(),'Proceed to checkout')]").send_keys(Keys.ENTER)
    driver.execute_script("window.scrollTo(0,800);")
    sleep(2)
    driver.quit()

def test_checkout():
    #10 test checkout with valid details
    driver = init()
    # ACCOSSORIES PAGE
    driver.find_element(By.XPATH, "//li[@id='menu-item-671']//a[@class='menu-link'][normalize-space()='Accessories']").click()
    driver.execute_script("window.scrollTo(0,200);")
    # Add Anchor Bracelet product to basket
    driver.find_element(By.XPATH, "//h2[contains(text(),'Anchor Bracelet')]").click()
    driver.execute_script("window.scrollTo(0,200);")
    # Add to cart button
    driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click()
    # move to cart page
    driver.find_element(By.XPATH,"//div[contains(@class,'ast-site-header-cart-li')]//bdi[1]").click()
    # Choose shipping method
    driver.execute_script("window.scrollTo(0,1000);")
    driver.find_element(By.XPATH, "//input[@id='shipping_method_0_free_shipping2']").click()
    driver.find_element(By.XPATH, "//a[contains(text(),'Proceed to checkout')]").send_keys(Keys.ENTER)
    sleep(2)
    driver.execute_script("window.scrollTo(0,200);")
    #Enter shipping details
    driver.find_element(By.XPATH, "//input[@id='billing_first_name']").send_keys("Emanuel")
    driver.find_element(By.XPATH, "//input[@id='billing_last_name']").send_keys("Maharat")
    driver.find_element(By.XPATH, "//input[@id='billing_company']").send_keys("YEMI")
    driver.execute_script("window.scrollTo(0,200);")
    driver.find_element(By.XPATH, "//input[@id='billing_address_1']").send_keys("YEMI")
    driver.find_element(By.XPATH, "//input[@id='billing_address_2']").send_keys("sharon 11")
    driver.find_element(By.XPATH, "//input[@id='billing_address_1']").send_keys("3")
    driver.find_element(By.XPATH, "//input[@id='billing_postcode']").send_keys("5648")
    driver.execute_script("window.scrollTo(0,200);")
    driver.find_element(By.XPATH, "//input[@id='billing_city']").send_keys("Lod")
    driver.find_element(By.XPATH, "//input[@id='billing_phone']").send_keys("0539829892")
    driver.find_element(By.XPATH, "//input[@id='billing_email']").send_keys("yemiker@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='ship-to-different-address-checkbox']").click()
    driver.find_element(By.XPATH, "//input[@id='ship-to-different-address-checkbox']").click()
    driver.find_element(By.XPATH, "//textarea[@id='order_comments']").send_keys("bla bla bla")
    #choose shipping method
    driver.find_element(By.XPATH, "//input[@id='shipping_method_0_local_pickup1']").click()
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='shipping_method_0_flat_rate3']").click()
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='shipping_method_0_flat_rate4']").click()
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='shipping_method_0_free_shipping2']").click()
    driver.find_element(By.XPATH, "//button[@id='place_order']").send_keys(Keys.ENTER)
    sleep(3)
    driver.quit()

def test_checkout_check():
    #11 Check in the checkout page user can see all the details of the product like Name, Quantity, Amount, etc.
    driver = init()
    # ACCOSSORIES PAGE
    driver.find_element(By.XPATH, "//li[@id='menu-item-671']//a[@class='menu-link'][normalize-space()='Accessories']").click()
    driver.execute_script("window.scrollTo(0,200);")
    # Add Anchor Bracelet product to basket
    driver.find_element(By.XPATH, "//h2[contains(text(),'Anchor Bracelet')]").click()
    driver.execute_script("window.scrollTo(0,200);")
    # Add to cart button
    driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click()
    # move to cart page
    driver.find_element(By.XPATH,"//div[contains(@class,'ast-site-header-cart-li')]//bdi[1]").click()
    # move to checkout page
    driver.find_element(By.XPATH, "//a[contains(text(),'Proceed to checkout')]").send_keys(Keys.ENTER)
    driver.execute_script("window.scrollTo(0,600);")
    sleep(3)
    driver.quit()

def test_checkout_blank():
    #12 Check error message is displayed or not when the user leaves one mandatory field blank.
    driver = init()
    # ACCOSSORIES PAGE
    driver.find_element(By.XPATH, "//li[@id='menu-item-671']//a[@class='menu-link'][normalize-space()='Accessories']").click()
    driver.execute_script("window.scrollTo(0,200);")
    # Add Anchor Bracelet product to basket
    driver.find_element(By.XPATH, "//h2[contains(text(),'Anchor Bracelet')]").click()
    driver.execute_script("window.scrollTo(0,200);")
    # Add to cart button
    driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click()
    # move to cart page
    driver.find_element(By.XPATH,"//div[contains(@class,'ast-site-header-cart-li')]//bdi[1]").click()
    # move to checkout page
    driver.find_element(By.XPATH, "//a[contains(text(),'Proceed to checkout')]").send_keys(Keys.ENTER)
    driver.execute_script("window.scrollTo(0,600);")
    #Enter shipping details
    driver.find_element(By.XPATH, "//input[@id='billing_first_name']").send_keys("Emanuel")
    driver.find_element(By.XPATH, "//input[@id='billing_last_name']").send_keys("Maharat")
    driver.find_element(By.XPATH, "//input[@id='billing_company']").send_keys("YEMI")
    driver.execute_script("window.scrollTo(0,200);")
    driver.find_element(By.XPATH, "//input[@id='billing_address_1']").send_keys("YEMI")
    sleep(2)
    driver.find_element(By.XPATH, "//button[@id='place_order']").send_keys(Keys.ENTER)
    sleep(2)
    driver.quit()

def test_invalid_coupon():
    #13 Check the error message for the invalid coupon.
    #13.1 Check that the price of the cart is not discounted when we apply an invalid coupon.
    driver = init()
    # ACCOSSORIES PAGE
    driver.find_element(By.XPATH, "//li[@id='menu-item-671']//a[@class='menu-link'][normalize-space()='Accessories']").click()
    driver.execute_script("window.scrollTo(0,200);")
    # Add Anchor Bracelet product to basket
    driver.find_element(By.XPATH, "//h2[contains(text(),'Anchor Bracelet')]").click()
    driver.execute_script("window.scrollTo(0,200);")
    # Add to cart button
    driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click()
    # move to cart page
    driver.find_element(By.XPATH,"//div[contains(@class,'ast-site-header-cart-li')]//bdi[1]").click()
    # move to checkout page
    driver.find_element(By.XPATH, "//a[contains(text(),'Proceed to checkout')]").send_keys(Keys.ENTER)
    #Enter on coupon button
    driver.find_element(By.XPATH, "//a[@class='showcoupon']").click()
    sleep(2)
    driver.find_element(By.XPATH, "//input[@id='coupon_code']").click()
    sleep(2)
    driver.find_element(By.XPATH, "//input[@id='coupon_code']").send_keys("gunit")
    driver.find_element(By.XPATH, "//button[@name='apply_coupon']").send_keys(Keys.ENTER)
    sleep(3)
    driver.execute_script("window.scrollTo(0,800);")
    driver.quit()

def test_invalid_details():
    #14 test checkout with invalid details
    driver = init()
    # ACCOSSORIES PAGE
    driver.find_element(By.XPATH, "//li[@id='menu-item-671']//a[@class='menu-link'][normalize-space()='Accessories']").click()
    driver.execute_script("window.scrollTo(0,200);")
    # Add Anchor Bracelet product to basket
    driver.find_element(By.XPATH, "//h2[contains(text(),'Anchor Bracelet')]").click()
    driver.execute_script("window.scrollTo(0,200);")
    # Add to cart button
    driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click()
    # move to cart page
    driver.find_element(By.XPATH,"//div[contains(@class,'ast-site-header-cart-li')]//bdi[1]").click()
    # Choose shipping method
    driver.execute_script("window.scrollTo(0,1000);")
    driver.find_element(By.XPATH, "//input[@id='shipping_method_0_free_shipping2']").click()
    driver.find_element(By.XPATH, "//a[contains(text(),'Proceed to checkout')]").send_keys(Keys.ENTER)
    sleep(2)
    driver.execute_script("window.scrollTo(0,200);")
    #Enter shipping details
    driver.find_element(By.XPATH, "//input[@id='billing_first_name']").send_keys("Emanuel")
    driver.find_element(By.XPATH, "//input[@id='billing_last_name']").send_keys("Maharat")
    driver.find_element(By.XPATH, "//input[@id='billing_company']").send_keys("YEMI")
    driver.execute_script("window.scrollTo(0,200);")
    driver.find_element(By.XPATH, "//input[@id='billing_address_1']").send_keys("YEMI")
    driver.find_element(By.XPATH, "//input[@id='billing_address_2']").send_keys("@##$")
    driver.find_element(By.XPATH, "//input[@id='billing_address_1']").send_keys("3")
    driver.find_element(By.XPATH, "//input[@id='billing_postcode']").send_keys("5648")
    driver.execute_script("window.scrollTo(0,200);")
    driver.find_element(By.XPATH, "//input[@id='billing_city']").send_keys("$$$")
    driver.find_element(By.XPATH, "//input[@id='billing_phone']").send_keys("0539829892")
    driver.find_element(By.XPATH, "//input[@id='billing_email']").send_keys("yemikergmail.com")
    driver.find_element(By.XPATH, "//input[@id='ship-to-different-address-checkbox']").click()
    driver.find_element(By.XPATH, "//input[@id='ship-to-different-address-checkbox']").click()
    driver.find_element(By.XPATH, "//textarea[@id='order_comments']").send_keys("bla bla bla")
    #choose shipping method
    driver.find_element(By.XPATH, "//input[@id='shipping_method_0_local_pickup1']").click()
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='shipping_method_0_flat_rate3']").click()
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='shipping_method_0_flat_rate4']").click()
    sleep(3)
    driver.find_element(By.XPATH, "//input[@id='shipping_method_0_free_shipping2']").click()
    driver.find_element(By.XPATH, "//button[@id='place_order']").send_keys(Keys.ENTER)
    sleep(3)
    driver.quit()
