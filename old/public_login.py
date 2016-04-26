#coding=utf-8
from selenium import webdriver
from time import sleep

def login(dr,userName,passWord):
    dr.find_element_by_id('login-form-username').clear()
    dr.find_element_by_id('login-form-username').send_keys(userName)
    sleep(5)
    dr.find_element_by_id('login-form-password').clear()
    dr.find_element_by_id('login-form-password').send_keys(passWord)
    sleep(5)
    dr.find_element_by_id('login-form-remember-me').click()
    dr.find_element_by_id('login').submit()

