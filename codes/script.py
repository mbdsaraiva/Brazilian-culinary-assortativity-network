import os
import requests

# Caminho da pasta onde as imagens serão salvas
output_folder = r"C:\Users\mathe\OneDrive\Área de Trabalho\aed2_receitas"
os.makedirs(output_folder, exist_ok=True)

# Lista de receitas e URLs
receitas = [
    ("1 - Feijoada", "https://static.itdg.com.br/images/640-400/4183f4a52eadb0d86eed283e54e0020c/355811-original.jpg"),
    ("2 - Moqueca_capixaba", "https://static.itdg.com.br/images/640-400/78b56318eb8073f17119bce12ed9a95b/202111-original.jpg"),
    ("3 - Moqueca_baiana", "https://static.itdg.com.br/images/640-400/037a65fddf2e9ebba83b5ca8c24bc4f4/164494-original.jpg"),
    ("4 - Bobo_camarao", "https://static.itdg.com.br/images/640-400/1bbc5829997ddcb75c76edbf754bf63e/192473-original.jpg"),
    ("5 - Baiao_dois", "https://static.itdg.com.br/images/640-400/6aa37c1c701e9e69f841e6834da2da87/shutterstock-1901961571-1-.jpg"),
    ("6 - Arroz_carreteiro", "https://static.itdg.com.br/images/640-400/696079b0c26211198bf7fd81e7283ce9/40607-192620-original.jpg"),
    ("7 - Galinhada", "https://static.itdg.com.br/images/640-400/2726bfbcba92e6bbdcc80cda65d71b17/185731-original.jpg"),
    ("8 - Vatapá", "https://static.itdg.com.br/images/640-400/2adc51a62b7a7500951bdf23afea8a65/270812-original.jpg"),
    ("9 - Sarapatel", "https://static.itdg.com.br/images/640-400/b57927fb81988b0fe270b24d42184ae4/354991-original.jpg"),
    ("10 - Dobradinha", "https://static.itdg.com.br/images/640-400/0103ca084f1d32976c247a54e216d939/306961-original.jpg"),
    ("11 - Picadinho de carne", "https://static.itdg.com.br/images/640-400/d8cfd0b5b0649540782bf14d28a9b972/83157-original.jpg"),
    ("12 - Vaca atolada", "https://static.itdg.com.br/images/640-400/3a7d07fbbb06b62a06ccae55e41c5166/31240-332263-original.jpg"),
    ("13 - Costela no bafo", "https://static.itdg.com.br/images/640-400/2503d735d48ecff5ef4a6fea92d52e2a/107028-original.jpg"),
    ("14 - Frango com quiabo", "https://static.itdg.com.br/images/640-400/09519eded36c4c732bf06bd69bb3b978/171377-original.jpg"),
    ("15 - Rabada com agriao", "https://static.itdg.com.br/images/640-400/9050c2d21f6f34563e206f11487cc0ec/303895-original.jpg"),
    ("16 - Peixada", "https://static.itdg.com.br/images/640-400/0b924c4367ebe37222a5d01236361cb9/moqueca-de-peixe-.png"),
    ("17 - Ensopado de peixe com pirão", "https://static.itdg.com.br/images/640-400/dd395caab0554608d21022369dcdcdcb/295673-original.jpg"),
    ("18 - Escondidinho de carne seca", "https://static.itdg.com.br/images/640-400/f859a181c6d16fa86e801fe56ea9a3aa/189122-original.jpg"),
    ("19 - Escondidinho de frango", "https://static.itdg.com.br/images/640-400/1227f603d1133046616f2bee4e6dbbbb/93443-208905-original.jpg"),
    ("20 - Arroz com pequi", "https://static.itdg.com.br/images/640-400/e37352020b2f0bee4c2686653001e4f4/282472-original.jpg"),
    ("21 - Caldo verde", "https://static.itdg.com.br/images/640-400/6a3ef280580bbd9986366a43419f1251/322097-original.jpg"),
    ("22 - Caldo de mocotó", "https://static.itdg.com.br/images/640-400/5262ebfc89189f26165302e67d0dedd9/144063-original.jpg"),
    ("23 - Sopa de ervilha com bacon", "https://static.itdg.com.br/images/640-400/8e9468098454307a709086912abfdb2a/62095-original.jpg"),
    ("24 - Canja de galinha", "https://static.itdg.com.br/images/640-400/ef27f128b26c39d7b6beb4c7fd1666e7/231735-original.jpg"),
    ("25 - Sopa de mandioca com carne", "https://static.itdg.com.br/images/640-400/aa387dab1d837483e6061fe67b3034f1/97920-original.jpg"),
    ("26 - Farofa", "https://static.itdg.com.br/images/640-400/4b31d2fd20e0e7088b9c9d677f056862/shutterstock-2285596891.jpg"),
    ("27 - Tutu de feijão", "https://static.itdg.com.br/images/640-400/d9ec1bc316f0619e6fa4f63fa18e0e11/64062-original.jpg"),
    ("28 - Feijao tropeiro", "https://static.itdg.com.br/images/640-400/959a789a61de8526bc4f36a248b97255/327806-original.jpg"),
    ("29 - Pamonha Salgada", "https://static.itdg.com.br/images/640-400/7688556be41254852cc7a03dc40124ce/168467-original.jpg"),
    ("30 - Purê de mandioquinha", "https://static.itdg.com.br/images/640-400/0b9af08459350f716a36efbff2083ffc/353888-original.jpg"),
    ("31 - Couve refogada", "https://static.itdg.com.br/images/640-400/05d961610eca0dcf5024940a57eadd93/280727-original.jpg"),
    ("32 - Salada de maionese", "https://static.itdg.com.br/images/640-400/a6b38a7135b03126cfb0fee39cf5b695/shutterstock-1154858464.jpg"),
    ("33 - Acarajé", "https://static.itdg.com.br/images/640-400/2b75916813d2febcb4d9a7f76b3a6585/271488-original.jpg"),
    ("34 - Bolinho de bacalhau", "https://static.itdg.com.br/images/640-400/a71f4fd47fc37eeb98a662bc69e304be/shutterstock-2005565906.jpg"),
    ("35 - Coxinha", "https://static.itdg.com.br/images/640-400/2a143ce9e0d1d812d3a0226681028531/126544-original.jpg"),
    ("36 - Pastel de feira", "https://static.itdg.com.br/images/640-400/5c58ac17e2cfe147a170a01e7d758c78/251463-shutterstock-2279329481-2-.jpg.jpg"),
    ("37 - Kibe frito", "https://static.itdg.com.br/images/640-400/a9377725df13d4de527bd45d83b65a60/143293-original.jpg"),
    ("38 - Pão de queijo", "https://static.itdg.com.br/images/640-400/ce464b65fe55ff7f03a68d7b1d6850c6/318013-original.jpg"),
    ("40 - Torresmo", "https://static.itdg.com.br/images/640-400/e4f6b8a6121b262226b7ef63c4741c60/311551-original.jpg"),
    ("41 - Brigadeiro", "https://static.itdg.com.br/images/640-400/a373f494abb2c3360b9966f5abe130e2/brigadeiro-.jpg"),
    ("42 - Beijinho", "https://static.itdg.com.br/images/640-400/e891be3d214b0c73ddc630dc8d90b429/304466-original.jpg"),
    ("43 - Cocada", "https://static.itdg.com.br/images/640-400/f2f04cc3745585d1264ce43a0317c4d9/193444-original.jpg"),
    ("44 - Pudim de leite condensado", "https://static.itdg.com.br/images/640-400/707f63812d06b57480d0177887226947/318825-original.jpg"),
    ("45 - Bolo de milho", "https://static.itdg.com.br/images/640-400/c889810eae105be4d597fef049fef0d9/103014-original.jpg"),
    ("46 - Bolo de cenoura com cobertura de chocolate", "https://static.itdg.com.br/images/640-400/cae5087c7dc7fea4a8ecc2d8ec52df41/39124-original.jpg"),
    ("47 - Curau", "https://static.itdg.com.br/images/640-400/041f52cee88732a989b67e703806ce03/24300-original.jpg"),
    ("48 - Canjica", "https://static.itdg.com.br/images/640-400/a2cb363357ddcaadefff5d6ec166e9c3/101307-original.jpg"),
    ("49 - Pé de moleque", "https://static.itdg.com.br/images/640-400/73d9081138ee0235fd3a9d36d9defadf/38858-original.jpg"),
    ("50 - Churrasco", "https://static.itdg.com.br/images/640-400/1b871bd5c11551f8abbbae7146d9a580/82306-original.jpg"),

]

# Cabeçalhos para simular um navegador
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
}

for nome_receita, img_url in receitas:
    try:
        response = requests.get(img_url, headers=headers)
        response.raise_for_status()  # Gera exceção para códigos de erro HTTP

        caminho_arquivo = os.path.join(output_folder, f"{nome_receita}.jpg")
        with open(caminho_arquivo, "wb") as f:
            f.write(response.content)

        print(f"Imagem de '{nome_receita}' salva com sucesso!")

    except Exception as e:
        print(f"Erro ao baixar {img_url} ({nome_receita}): {e}")
