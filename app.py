'''
PASSOS

início:
1 - abrir o navegador 
2 - acessar alunos2.kenzie.com.br
3 - verificar se está logado
4 - clicar no módulo desejado
4 - clicar em pessoas 

* criar um arquivo excel com nome e email dos devs

3 ações: Adicionar estudante (add_student) | adicionar seção (add_section_to_student) | padronizar nomes (change_names) 

no for: 
5 - escrever email do dev no campo de pesquisa 
6 - clicar nos 3 pontinhos 
7 - clicar em 'editar seções'
8 - escrever nome de seção 
9 - pressionar 'enter'
10 - clicar no botão atualizar
11 - apagar email do campo de pesquisa

'''
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

######################## Read wordsheet ##########################
table = pd.read_excel('./students.xlsx')

list_emails = ', '.join(list(table['Email']))
#################################################################

navegador = webdriver.Edge()

navegador.get('https://alunos2.kenzie.com.br')

time.sleep(int(environs['LOADING_TIME']))

input_email = navegador.find_element(By.XPATH,
                '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/form[1]/div[1]/input')
input_email.send_keys(environs['EMAIL_CANVAS'])

input_password = navegador.find_element(By.XPATH,
                '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/form[1]/div[2]/input')
input_password.send_keys(environs['PASSWORD_CANVAS'] + Keys.ENTER)

module = navegador.find_element(By.XPATH, environs['MODULE_PATH'])

time.sleep(int(environs['LOADING_TIME']))

module.click()

time.sleep(int(environs['LOADING_TIME']))

link_peoples = navegador.find_element(By.XPATH,
                '/html/body/div[2]/div[2]/div[2]/div[2]/nav/ul/li[6]/a')
link_peoples.click()

time.sleep(int(environs['LOADING_TIME']))

if(environs['ACTION'] == 'add_student'):
    btn_add_student = navegador.find_element(By.XPATH,
                '/html/body/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[2]/div/div[2]/a')
    btn_add_student.click()

    text_area = navegador.find_element(By.XPATH,
                '/html/body/span/span/span/div[2]/div/div/fieldset[2]/label/span/span[1]/span[2]/div/textarea')
    text_area.click()
    text_area.send_keys(list_emails)

    select_section = navegador.find_element(By.XPATH,
                '//*[@id="peoplesearch_select_section"]')
    select_section.click()

elif(environs['ACTION'] == 'add_section'):
    array_emails = list_emails.split(', ')
    for i in range(len(array_emails)):
        field_email = navegador.find_element(By.XPATH, 
                '/html/body/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[2]/div/div[2]/input')
        field_email.send_keys(array_emails[i])

        time.sleep(3)

        three_dots = navegador.find_element(By.XPATH,
                '/html/body/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr/td[9]/div/a/i')
        three_dots.click()

        time.sleep(2)

        btn_edit_section = navegador.find_element(By.XPATH, 
                '/html/body/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr/td[9]/div/ul/li[2]')
        btn_edit_section.click()

        time.sleep(3)

        field_section = navegador.find_element(By.XPATH, 
                '//*[@id="edit_sections"]/div/div/input')
        field_section.send_keys(environs['FACILITADOR_SECTION'] + Keys.ENTER)
        time.sleep(2)
        field_section.send_keys(Keys.ENTER)

        navegador.find_element(By.XPATH, 
                '/html/body/div[3]/div[3]/div/button[1]').click()

        field_email.clear()

# navegador.quit()
