# Auto Canvas

## Requisitos

- Um arquivo no formato xlsx(excel) contendo duas colunas: "Nome" e "Email" referentes aos seus devs
    - O arquivo pode ser baixado do Google Sheets, você não precisa ter excel instalado 

- Um WebDriver do seu navegador instalado na máquina 
    - Após baixado, o arquivo do programa deve ser colocado na mesma pasta do executável do Python


## Instruções

### Preparação

1. Clonar esse repositório na sua máquina

2. Criar uma planilha no Google Sheets ou no excel chamada **students**

3. Compor a planilha com uma coluna denominada **Email** e preenchê-la com todos os emails dos seus devs

4. Caso tenha sido criada com o Google Sheets, fazer o download dessa planilha no formato .xlsx 

5. Colocar o arquivo da planilha na raiz desse projeto 

### Definição das variáveis ambientes

1. **EMAIL_CANVAS** = Email que o facilitador utiliza para acessar o Canvas

2. **PASSWORD_CANVAS** = Senha que o facilitador utiliza para acessar o Canvas

3. **MODULE_PATH** = XPATH completo do elemento da página correspondente ao módulo atual

4. **ACTION** = Ação que você deseja fazer:

    a) **add_section** = Adicionar sua sessão específica a um ou mais estudantes

    b) **change_names** = mudar nome ordenável de um ou mais estudantes (ainda não implementada)

5. **FACILITADOR_SECTION** = Seção do facilitador onde fica somente os estudantes da turma dele
