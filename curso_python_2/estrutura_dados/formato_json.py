import json 
import time

# Traduzindo um dicionário em JSON 

pessoa = {
    "nome": "Lucas",
    "idade": 22, 
    "cidade": "Anápolis", 
    "possuiFilhos": True, 
    "formacao": ["Engenharia Civil", "Direito"]
}

# pessoaJson = json.dumps(pessoa, indent= 4, separators= (';', '='))
pessoaJson = json.dumps(pessoa, indent= 4)
print(pessoaJson)

# Salvando o arquivo 


def salvar_arquivo():
    with open('pessoa.json', 'w', encoding= 'utf8') as arquivo: 
        json.dump(pessoa, arquivo, indent= 4)

    time.sleep(1.5)
    print("Salvando arquivo...")

salvar_arquivo()

# Java Script Object Notation
# Transformando uma string em formato JSON 

pessoa_dict = json.loads(pessoaJson)
print(pessoa_dict)


def lendo_arquivo_Json(nome_arquivo: str):

    assert type(nome_arquivo) == str, "O arquivo deve ser um str" 

    with open(nome_arquivo, 'r', encoding= 'utf-8') as arquivo:
        pessoa = json.load(arquivo) 

    print(type(pessoa))
    print(isinstance(json, dict))
    print(pessoa)


def aplicando_Classes()-> None:
    """
        Aplicando o conceito de formato de dados Json 
        seguindo uma lógica de programação orientada a objetos 
    """

    class User: 

        def __init__(self, nome, idade):
            self.nome = nome 
            self.idade = idade 

    usuario = User("Marcos", 25) 

    def encode_function(objeto):

        """
            Esta função recebe um dicionário e o transforma o objeto
        """
        if isinstance(objeto, User): # Verificas se o objeto é uma instância da classe User 
            return {
                "nome": objeto.nome,
                "idade": objeto.idade
            }

        else:
            raise TypeError("Esta funcção lida apenas com objetos da classe User")


    userJson = json.dumps(usuario, default= encode_function) # Transforma o dicionário em um string no formato json
    print(userJson)

def main():

    # nome_arquivo = 'pessoa.json'
    # lendo_arquivo_Json(nome_arquivo)

    aplicando_Classes()

if __name__ == '__main__':
    main()