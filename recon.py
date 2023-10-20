import requests
url = "http://localhost:4200"

#lista_de_arquivos = open('lista-de-arquivos-angular.txt')
lista_de_arquivos = open('common.txt')

for linha in lista_de_arquivos.readlines():
    url_teste = url + "/" + linha.replace("\n", "")
    requisicao = requests.get(url_teste)
    if(requisicao.status_code == 400):
        continue
    if(requisicao.status_code == 200):
        print("[+] Diretório ou arquivo encontraro: ", linha.replace("\n", ""))
    else:
        print("[+] Diretório ou arquivo não encontrado (" + str(requisicao.status_code) + "):", linha.replace("\n", ""))

