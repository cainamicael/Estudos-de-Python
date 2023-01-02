import json

carros_dictionary = {
    'marca':'honda',
    'modelo':'hrv',
    'cor':'prata' 
}
#dictionary -> objeto json

carros_list = ['honda','volkswagen','ford','fiat','chevrolet']
#list -> array json

carros_tupla = ('honda','volkswagen','ford','fiat','chevrolet')
#tupla -> array json

carros_j = json.dumps(carros_dictionary, indent=4, separators = (':','='), sort_keys=True) #posso passar lista, tupla, dictionary, que a função aceita

"""
indent = 4 diz que terá 4 espaços de indentação
separators diz que eu quero mudar os : para =
sort_keys=True ordem alfabetica
"""
print(carros_j)