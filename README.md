# Auto Canvas

## Requisitos

- Um arquivo no formato xlsx(excel) contendo uma coluna "E-mail" com todos os emails dos seus devs
    - O arquivo pode ser baixado do Google Sheets, você não precisa ter excel instalado 

- Um WebDriver do seu navegador instalado na máquina 
    - Após baixado, o arquivo do programa deve ser colocado na mesma pasta do executável do Python


## Instruções

### Preparação

1. Clonar esse repositório na sua máquina

2. Criar uma planilha no Google Sheets ou no excel chamada **students**

3. Compor a planilha com uma coluna denominada **E-mail** e preenchê-la com todos os emails dos seus devs

4. Caso tenha sido criada com o Google Sheets, fazer o download dessa planilha no formato .xlsx 

5. Colocar o arquivo da planilha na raiz desse projeto 

### Definição das variáveis ambientes

1. **EMAIL_CANVAS** = Email que o facilitador utiliza para acessar o Canvas

2. **PASSWORD_CANVAS** = Senha que o facilitador utiliza para acessar o Canvas

3. **MODULE_PATH** = XPATH 

4. **LOADING_TIME** = É o tempo em segundos de intervalo entre algumas ações durante o processo automatizado. Isso vai depender da velocidade da sua máquina. 
    - Sugestão: mínimo 5 segundos

5. **ACTION** = Qual ação que você deseja fazer:

    a) **add_student** = Adicionar um ou mais estudantes no módulo 

    b) **add_section** = Adicionar sua sessão específica a um ou mais estudantes

    c) **change_names** = mudar nome ordenável de um ou mais estudantes

6. **MODULE_SECTION** = Seção geral do módulo em que fica todos os estudantes da turma

7. **FACILITADOR_SECTION** = Seção do facilitador onde fica somente os estudantes da turma dele