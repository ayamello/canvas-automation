import dotenv
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


dotenv.load_dotenv()
environs = dotenv.dotenv_values('.env')

######################## Read worksheet ##########################
table = pd.read_excel('./students.xlsx')

list_emails = ', '.join(list(table['Email']))

list_names = list(table['Nome'])
#################################################################
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

browser = webdriver.Chrome(options=options)

browser.get('https://alunos2.kenzie.com.br')

######################## Canvas Login ##########################
input_email = WebDriverWait(browser, timeout=3).until(lambda b: b.find_element(By.XPATH,
                                   '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/form[1]/div[1]/input'))
input_email.send_keys(environs['EMAIL_CANVAS'])

input_password = browser.find_element(By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/form[1]/div[2]/input')
input_password.send_keys(environs['PASSWORD_CANVAS'] + Keys.ENTER)
#################################################################

module = WebDriverWait(browser, timeout=3).until(lambda b: b.find_element(By.XPATH, environs['MODULE_PATH']))
module.click()

time.sleep(2)

link_peoples = WebDriverWait(browser, timeout=3).until(lambda b: b.find_element(By.XPATH, 
                                        '/html/body/div[2]/div[2]/div[2]/div[2]/nav/ul/li[6]/a'))
link_peoples.click()

######################## Add students list to Canvas ##########################
# if(environs['ACTION'] == 'add_student'):
#     btn_add_student = browser.find_element(By.XPATH,
#                                            '/html/body/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[2]/div/div[2]/a')
#     btn_add_student.click()

#     text_area = browser.find_element(By.XPATH,
#                                      '/html/body/span/span/span/div[2]/div/div/fieldset[2]/label/span/span[1]/span[2]/div/textarea')
#     text_area.click()
#     text_area.send_keys(list_emails)

#     select_section = browser.find_element(By.XPATH,
#                                           '//*[@id="peoplesearch_select_section"]')

#     browser.execute_script('arguments[0].removeAttribute("disabled"); arguments[0].value=arguments[1]',
#                            select_section, environs['FACILITADOR_SECTION'])

#     browser.find_element(By.XPATH,
#                          '/html/body/span/span/span/div[3]/button[2]').click()

######################## Add students list to a section canvas or change names students list ##########################
if(environs['ACTION'] == 'add_section' or environs['ACTION'] == 'change_names'):
    array_emails = list_emails.split(', ')
    
    for i in range(len(array_emails)):
        time.sleep(2)
        field_email = WebDriverWait(browser, timeout=3).until(lambda b: b.find_element(By.XPATH,
                                           '/html/body/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[2]/div/div[2]/input'))
        field_email.send_keys(array_emails[i])

        time.sleep(2)

        three_dots = WebDriverWait(browser, timeout=3).until(lambda b: b.find_element(By.XPATH,
                        '/html/body/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr/td[9]/div/a/i'))
        three_dots.click()

        if(environs['ACTION'] == 'add_section'):
            btn_edit_section = WebDriverWait(browser, timeout=5).until(EC.visibility_of_element_located((By.XPATH, 
                        '/html/body/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr/td[9]/div/ul/li[2]')))                       
            btn_edit_section.click()

            field_section = WebDriverWait(browser, timeout=3).until(lambda b: b.find_element(By.XPATH,
                                                                '//*[@id="edit_sections"]/div/div/input'))
            field_section.send_keys(
               environs['FACILITADOR_SECTION'])
            time.sleep(2)
            field_section.send_keys(Keys.ENTER)

            WebDriverWait(browser, timeout=3).until(lambda b: b.find_element(By.XPATH,
                                                            '/html/body/div[3]/div[3]/div/button[1]')).click()

            field_email.clear()
        else:
            btn_user_details = WebDriverWait(browser, timeout=5).until(EC.visibility_of_element_located((By.XPATH,
                    '/html/body/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[9]/div/ul/li[4]')))
            btn_user_details.click()
            time.sleep(2)
            
            try:
                btn_user_edit = browser.find_element(By.XPATH, 
                                            '/html/body/div[2]/div[2]/div[2]/div[3]/div[1]/div/fieldset/table/tbody/tr[6]/td/a[1]')
                btn_user_edit.click()

                full_name_field = WebDriverWait(browser, timeout=3).until(lambda b: b.find_element(By.XPATH, 
                                                '/html/body/div[3]/div[2]/form/table/tbody/tr[1]/td[2]/input'))
                full_name_field.send_keys(list_names[i])
                    
                display_name_field = browser.find_element(By.XPATH, 
                                                '/html/body/div[3]/div[2]/form/table/tbody/tr[3]/td[2]/input')
                display_name_field.clear()
                display_name_field.send_keys(list_names[i])

                btn_update_user = browser.find_element(By.XPATH, '/html/body/div[3]/div[2]/form/div/button[2]')
                btn_update_user.click()
                    
                link_peoples_back = WebDriverWait(browser, timeout=2).until(EC.visibility_of_element_located((By.XPATH, 
                                                '/html/body/div[2]/div[2]/div[2]/div[2]/nav/ul/li[6]/a')))
                link_peoples_back.click()
                time.sleep(2)
            except NoSuchElementException:
                link_peoples_back = WebDriverWait(browser, timeout=2).until(EC.visibility_of_element_located((By.XPATH, 
                                            '/html/body/div[2]/div[2]/div[2]/div[2]/nav/ul/li[6]/a')))
                link_peoples_back.click()
                time.sleep(2)
            
browser.quit()
