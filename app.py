import dotenv
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


dotenv.load_dotenv()
environs = dotenv.dotenv_values('.env')

######################## Read worksheet ##########################
table = pd.read_excel('./students.xlsx')

list_emails = ', '.join(list(table['Email']))
#################################################################

browser = webdriver.Edge()

browser.get('https://alunos2.kenzie.com.br')

time.sleep(int(environs['LOADING_TIME']))

######################## Canvas Login ##########################
input_email = browser.find_element(By.XPATH,
                                   '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/form[1]/div[1]/input')
input_email.send_keys(environs['EMAIL_CANVAS'])

input_password = browser.find_element(By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/form[1]/div[2]/input')
input_password.send_keys(environs['PASSWORD_CANVAS'] + Keys.ENTER)
#################################################################

module = browser.find_element(By.XPATH, environs['MODULE_PATH'])

time.sleep(int(environs['LOADING_TIME']))

module.click()

time.sleep(int(environs['LOADING_TIME']))

link_peoples = browser.find_element(By.XPATH,
                                    '/html/body/div[2]/div[2]/div[2]/div[2]/nav/ul/li[6]/a')
link_peoples.click()

time.sleep(int(environs['LOADING_TIME']))

######################## Actions ##########################
if(environs['ACTION'] == 'add_student'):
    btn_add_student = browser.find_element(By.XPATH,
                                           '/html/body/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[2]/div/div[2]/a')
    btn_add_student.click()

    text_area = browser.find_element(By.XPATH,
                                     '/html/body/span/span/span/div[2]/div/div/fieldset[2]/label/span/span[1]/span[2]/div/textarea')
    text_area.click()
    text_area.send_keys(list_emails)

    select_section = browser.find_element(By.XPATH,
                                          '//*[@id="peoplesearch_select_section"]')

    browser.execute_script('arguments[0].removeAttribute("disabled"); arguments[0].value=arguments[1]',
                           select_section, environs['FACILITADOR_SECTION'])

    browser.find_element(By.XPATH,
                         '/html/body/span/span/span/div[3]/button[2]').click()


elif(environs['ACTION'] == 'add_section' or environs['ACTION'] == 'change_names'):
    array_emails = list_emails.split(', ')
    for i in range(len(array_emails)):
        field_email = browser.find_element(By.XPATH,
                                           '/html/body/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[2]/div/div[2]/input')
        field_email.send_keys(array_emails[i])

        time.sleep(3)

        three_dots = browser.find_element(By.XPATH,
                                          '/html/body/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr/td[9]/div/a/i')
        three_dots.click()

        time.sleep(2)

        if(environs['ACTION'] == 'add_section'):
            btn_edit_section = browser.find_element(By.XPATH,
                                                    '/html/body/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr/td[9]/div/ul/li[2]')
            btn_edit_section.click()

            time.sleep(3)

            field_section = browser.find_element(By.XPATH,
                                                 '//*[@id="edit_sections"]/div/div/input')
            field_section.send_keys(
                environs['FACILITADOR_SECTION'] + Keys.ENTER)
            time.sleep(2)
            field_section.send_keys(Keys.ENTER)

            browser.find_element(By.XPATH,
                                 '/html/body/div[3]/div[3]/div/button[2]').click()

            field_email.clear()
        # else:
        #     btn_user_details = browser.find_element(By.XPATH,
        #                                             '/html/body/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[9]/div/ul/li[4]')
        #     btn_user_details.click()

        #     time.sleep(int(environs['LOADING_TIME']))

            # continua

# browser.quit()
