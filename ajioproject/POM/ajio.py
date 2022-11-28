import time
from Data import reading_object


lo_obj = reading_object.read_locators()
class Ajio1:
    def __init__(self,driver):
        self.driver=driver

    def test_signin(self,value1):

        self.driver.find_element(*lo_obj['txt_sign-in']).click()
        self.driver.find_element_by_xpath("//input[@type='text']").send_keys(value1[0])
        time.sleep(5)

        self.driver.find_element(*lo_obj['txt_submit']).click()
        time.sleep(30)
        self.driver.find_element(*lo_obj['txt_mobno_OTP']).send_keys('')

        self.driver.find_element(*lo_obj['txt_submit_00']).click()
        time.sleep(2)
        self.driver.find_element(*lo_obj['txt_mobno_signout']).click()
        time.sleep(2)

class Ajio2:

    def __init__(self, driver):
        self.driver = driver

    def test_email(self,value1):
        time.sleep(2)
        self.driver.find_element(*lo_obj['txt_Email_sign-in']).click()
        time.sleep(2)

        self.driver.find_element(*lo_obj['txt_email-username']).send_keys(value1[1])
        time.sleep(2)
        self.driver.find_element(*lo_obj['txt_submit_01']).click()
        time.sleep(2)
        self.driver.find_element(*lo_obj['txt_gender']).click()
        self.driver.find_element(*lo_obj['txt_name']).send_keys(value1[2])
        self.driver.find_element(*lo_obj['txt_mobno_00']).send_keys(value1[3])
        self.driver.find_element(*lo_obj['txt_pwd_01']).send_keys(value1[4])
        self.driver.find_element(*lo_obj['txt_invitecode']).send_keys('1938')
        self.driver.find_element(*lo_obj['txt_checkbox']).click()
        self.driver.find_element(*lo_obj['txt_send_otp']).click()
        time.sleep(2)
        self.driver.find_element(*lo_obj['txt_login_otp']).click()
        time.sleep(30)
        self.driver.find_element(*lo_obj['txt_otp']).send_keys("")
        time.sleep(2)
        self.driver.find_element(*lo_obj['txt_submit_02']).click()
        time.sleep(2)
        self.driver.find_element(*lo_obj['txt_signout']).click()
        time.sleep(2)

class Ajio3:
    def __init__(self, driver):
        self.driver = driver

    def test_facebook(self,value1):
        time.sleep(2)
        self.driver.find_element(*lo_obj['txt_sign-in_fb']).click()
        time.sleep(5)

        self.driver.find_element(*lo_obj['txt_click_login']).click()
        time.sleep(5)

        handles = self.driver.window_handles
        print(handles)
        self.driver.switch_to.window(handles[1])
        time.sleep(5)
        self.driver.find_element(*lo_obj['txt_email-id']).send_keys(value1[1])
        time.sleep(2)
        self.driver.find_element(*lo_obj['txt_pwd_02']).send_keys(value1[4])
        self.driver.find_element(*lo_obj['txt_login_fb']).click()
        time.sleep(5)
        handles = self.driver.window_handles
        print(handles)
        self.driver.switch_to.window(handles[0])
        time.sleep(5)
        self.driver.find_element(*lo_obj['txt_mobno_01']).send_keys(value1[0])
        time.sleep(2)
        self.driver.find_element(*lo_obj['txt_submit_03']).click()
        self.driver.find_element(*lo_obj['txt_button']).click()
        time.sleep(30)
        self.driver.find_element(*lo_obj['txt_otp_02']).send_keys('')
        self.driver.find_element(*lo_obj['txt_submit_04']).click()
        time.sleep(5)
        self.driver.find_element(*lo_obj['txt_signout_02']).click()
        time.sleep(2)

class Ajio4:
    def __init__(self, driver):
        self.driver = driver

    def test_google(self,value1):
        time.sleep(2)
        self.driver.find_element(*lo_obj['txt_sign-in_google']).click()
        time.sleep(2)
        self.driver.find_element(*lo_obj['txt_google_login']).click()
        time.sleep(5)
        handles = self.driver.window_handles
        print(handles)
        self.driver.switch_to.window(handles[1])
        time.sleep(2)
        self.driver.find_element(*lo_obj['txt_google_email']).send_keys(value1[0])
        self.driver.find_element(*lo_obj['txt_next_page1']).click()
        time.sleep(2)
        self.driver.find_element(*lo_obj['txt_pwd_03']).send_keys(value1[4])
        self.driver.find_element(*lo_obj['txt_next_page2']).click()
        time.sleep(5)
        handles = self.driver.window_handles
        print(handles)
        self.driver.switch_to.window(handles[0])
        time.sleep(5)
        self.driver.find_element(*lo_obj['txt_mobno_02']).send_keys(value1[0])
        self.driver.find_element(*lo_obj['txt_send_otp2']).click()
        self.driver.find_element(*lo_obj['txt_click']).click()
        time.sleep(30)
        self.driver.find_element(*lo_obj['txt_Enter_otp']).send_keys('')
        time.sleep(2)
        self.driver.find_element(*lo_obj['txt_submit_button']).click()
        time.sleep(5)
        self.driver.find_element(*lo_obj['txt_signout_03']).click()
        time.sleep(2)











