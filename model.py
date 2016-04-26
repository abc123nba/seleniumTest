#coding=utf-8

#登录
def login(dr):
    dr.find_element_by_id('idInput').clear()
    dr.find_element_by_id('idInput').send_keys('hcr258')
    dr.find_element_by_id('pwdInput').clear()
    dr.find_element_by_id('pwdInput').send_keys('hcr20160422')
    dr.find_element_by_id('loginBtn').click()

#退出
def logout(dr):
    dr.find_element_by_link_text(u'退出').click()

