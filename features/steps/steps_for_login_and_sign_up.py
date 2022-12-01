import time

from behave import *
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



@given('I am on website Jules.app login page')
def accessing_jules_login_page(context):
    context.driver=webdriver.Chrome(ChromeDriverManager().install())
    context.driver.get("https://jules.app/sign-in")
    context.driver.maximize_window()
    z=context.driver.current_url
    print(z)
    time.sleep(5)



@when('I enter an invalid user name')
def invalid_user_input(context):
    user_field=context.driver.find_element(By.CSS_SELECTOR, '#root > div > div.css-1kq6ix3 > form > div > div:nth-child(1) > div > div > input')
    user_field.send_keys('hermanionut')
    time.sleep(5)


@when('I enter an invalid password')
def invalid_pass_input(context):
    pass_field = context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[2]/div/div/input')
    pass_field.send_keys('z')
    time.sleep(5)


@then('I am not able to press the login button')
def login_button_disabled(context):
    login_btn = context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[3]/button')
    assert login_btn.is_enabled()==False


@then('Close the browser')
def closing_browser(context):
    context.driver.quit()
    time.sleep(5)

@when('I enter a valid user name')
def valid_user_input(context):
    user_field = context.driver.find_element(By.CSS_SELECTOR,'#root > div > div.css-1kq6ix3 > form > div > div:nth-child(1) > div > div > input')
    user_field.send_keys('banda1@securethering.com')
    time.sleep(5)

@when('I enter a valid password')
def valid_pass_input(context):
    pass_field = context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[2]/div/div/input')
    pass_field.send_keys('Unique123!')
    time.sleep(5)

@when('I press submit button')
def login_button_enabled(context):
    login_btn = context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[3]/button')
    login_btn.submit()
    time.sleep(5)

@then('I receive the non validated user message')
def non_validated_user(context):
    non_validated=context.driver.find_element(By.XPATH,'//*[@id="client-snackbar"]/div/div[2]')
    assert non_validated.is_displayed() == True
    time.sleep(5)


@then('I receive the Incorrect email/pass message')
def incorrect_credentials_message(context):
    invalid_mess = context.driver.find_element(By.XPATH,'//*[@id="client-snackbar"]/div')
    assert invalid_mess.is_displayed() ==True

@when('I enter a non validated user name')
def nonvalidated_user_input(context):
    user_field = context.driver.find_element(By.CSS_SELECTOR,'#root > div > div.css-1kq6ix3 > form > div > div:nth-child(1) > div > div > input')
    user_field.send_keys('hermanionutcatalin@yahoo.ro')
    time.sleep(5)

@when('I enter a blank user name')
def blank_user_input(context):
    user_field = context.driver.find_element(By.CSS_SELECTOR,'#root > div > div.css-1kq6ix3 > form > div > div:nth-child(1) > div > div > input')
    user_field.send_keys('')
    time.sleep(5)

@then('I see the enter a valid user message')
def invalid_email_message(context):
    mail_mess = context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[1]/div/p')
    assert mail_mess.is_displayed() ==True
    time.sleep(5)

@when('I enter a password then delete it')
def enter_pass_and_delete(context):
    pass_field = context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[2]/div/div/input')
    pass_field.send_keys('Unique123!')
    pass_field.send_keys(Keys.CONTROL + 'a')
    pass_field.send_keys(Keys.BACK_SPACE)
    time.sleep(5)

@then('I see the enter a valid pass message')
def invalid_pass_message(context):
    pass_mess =context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[2]/div/p')
    p=pass_mess.is_displayed()
    assert p==True
    time.sleep(5)


@given('I am on the sign-up page of Jules.app')
def accessing_jules_signup_page(context):
    context.driver=webdriver.Chrome(ChromeDriverManager().install())
    context.driver.get("https://jules.app/sign-up")
    context.driver.maximize_window()
    assert context.driver.current_url=='https://jules.app/sign-up'
    time.sleep(5)

@when('I am selecting personal account')
def selecting_personal(context):
    context.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[4]/div[2]/div/div[3]/label/span[1]/span/input').click()
    context.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[4]/div[2]/div/div[5]/button/span[1]').click()
    time.sleep(5)


@then('I should be able to reconfirm Unique123! and capture a print screen with the account not-validate message')
def re_confr(context):
    rp=context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div/input')
    rp.send_keys('Unique123!')
    context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[3]/button').send_keys(Keys.ENTER)
    time.sleep(2)
    context.driver.save_screenshot('sucessfull.png')
    time.sleep(2)

#please change this email after running one time the test, both here and in feature file
@when('I am introducing the me yog jatopel309@covbase.com Unique123!')
def entering_data(context):
    f = context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div/input')
    f.send_keys('me')
    f.send_keys(Keys.ENTER)
    time.sleep(2)
    l=context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div/input')
    l.send_keys('yog')
    l.send_keys(Keys.ENTER)
    time.sleep(5)
    e = context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div/input')
    e.send_keys('jatopel309@covbase.com')
    e.send_keys(Keys.ENTER)
    time.sleep(5)
    p = context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div/input')
    p.send_keys('Unique123!')
    p.send_keys(Keys.ENTER)
    time.sleep(5)

    @when('I am introducing the "{first_name}" "{last_name}" "{email_address}" "{pwd}"')
    def entering(context,first_name,last_name,email_address,pwd):
        f = context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div/input')
        f.send_keys(first_name)
        f.send_keys(Keys.ENTER)
        time.sleep(5)
        l = context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div/input')
        l.send_keys(last_name)
        l.send_keys(Keys.ENTER)
        time.sleep(5)
        e = context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div/input')
        e.send_keys(email_address)
        e.send_keys(Keys.ENTER)
        time.sleep(5)
        p = context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div/input')
        p.send_keys(pwd)
        p.send_keys(Keys.ENTER)
        time.sleep(5)

@then('I should be able to reconfirm "{pwd}" and capture a print screen with the account not-validate message')
def reconf(context,pwd):
    rp = context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div/input')
    rp.send_keys(pwd)
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[3]/button').send_keys(Keys.ENTER)
    time.sleep(2)
    sign_up=context.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[4]/div[2]/div/div[1]/span')
    assert sign_up.text=='A verification link has been sent to the email address you provided. Please verify your email to activate your account.'
    time.sleep(2)