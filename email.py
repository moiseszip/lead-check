import csv
import re

#le um arquivo csv e adiciona cada linha em uma array
def ler_emails(caminho_arquivo):
    emails = []
    with open(caminho_arquivo, 'r') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            if linha:  # Verifica se a linha não está vazia
                emails.append(linha[0]) # Assumindo que os emails estão na primeira coluna
    return emails

#valida 1 email
def validar_email(email):
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(padrao, email) is not None

#valida 1 lista de emails e separa em 2 listas
def analisar_emails(emails):
    emails_validos = []
    emails_invalidos = []

    for email in emails:
        if validar_email(email):
            emails_validos.append(email)
        else:
            emails_invalidos.append(email)

    return emails_validos, emails_invalidos

#verificar emails repetidos
def verificar_emails_repetidos(emails):
    emails_repetidos = []
    email_set = set()

    for email in emails:
        if email in email_set:
            emails_repetidos.append(email)
        else:
            email_set.add(email)

    return emails_repetidos

#remove os emails repetidos
def remover_emails_repetidos(emails):
    email_set = set(emails)
    return list(email_set)

#salva os emails validos
def salvar_emails_arquivo(emails, caminho_arquivo):
    with open(caminho_arquivo, 'w', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        for email in emails:
            escritor.writerow([email])

lista_emails = ler_emails('lista_emails.csv')
emails_validos, emails_invalidos = analisar_emails(lista_emails)
emails_unicos = remover_emails_repetidos(emails_validos)
salvar_emails_arquivo(emails_unicos, 'lista_emails_ok.csv')