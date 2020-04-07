import os
from selenium import webdriver

print(
    "1: for financial Accounting \n2: for Web\n3:Database\n4: Software engineering\n5:Statistics\n6: OB\n7: DSA\n8: "
    "Econ ")

sub = int(input("enter subject : "))

driver = webdriver.Firefox()


def login():
    uname = "2018is060"
    password = "manthila@1A"

    driver.get("http://ugvle.ucsc.cmb.ac.lk/login/index.php")

    driver.find_element_by_id("username").send_keys(uname)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("loginbtn").click()


def search_subject(subject):
    if subject == 1:
        driver.find_element_by_id("label_3_14").click()
    elif subject == 2:
        driver.find_element_by_id("label_3_15").click()
    elif subject == 3:
        driver.find_element_by_id("label_3_16").click()
    elif subject == 4:
        driver.find_element_by_id("label_3_17").click()
    elif subject == 5:
        driver.find_element_by_id("label_3_18").click()
    elif subject == 6:
        driver.find_element_by_id("label_3_19").click()
    elif subject == 7:
        driver.find_element_by_id("label_3_20").click()
    elif subject == 8:
        driver.find_element_by_id("label_3_21").click()
    else:
        print("not a value")


login()
search_subject(sub)
