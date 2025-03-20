import json
import time
from collections import Counter

calibration_data = [
    '9lnn', 'nine7pzrxnnkthreesdjxphsrf4hc8', 'three6115nqhllcmpmzcfour', 'vpqjnvmltx8fivefive',
    'vrlqlj5fivesixninebqhgcpgmgkmflvn', '76eighteight7', '8qkmnsjxbfhcpsvn4', 'oneninexqdseven4threefive',
    'rpcvmnng162fivesixseven', '31628eightthree', '83d6fsfqdghztwo7bmvrlh', 'gknfcdqlrs25', '9gkkth2ps',
    'bxnvsjxqleight9ninenine', 'rsmcrqlnhsmjhspseven96vsckknrggbjd4tgtgbkxgvt', '8seveneightcxrh',
    'tkmfour8fivevl9one', '8mgrxk', 'fourbgckqkeight6f', 'threetwo3eight652pp', 'ninefivetwojbhglxfxzfctwo8',
    'jmjtcvpsxzdbkbqthree1qmgznpbzlthree4six1', 'foursix5', '6nbdzdlmqpdlgpcclc', '24',
    'pseven3threeeightseven', '7nine7gjdksbtqrrdsr', '5ppflb48tkcffone8six', 'five2two7hstbbqzrninegbtwo2',
    'eightfblzpmhs4', 'fbbdeightzzsdffh8jbjzxkclj', '3nine6five1',
]

def extrair_numeros(linhas):
    numeros = []
    for linha in linhas:
        digitos = ''.join(filter(str.isdigit, linha))
        if not digitos:
            numeros.append(0)
        else:
            numeros.append(int(digitos[0] * 2) if len(digitos) == 1 else int(digitos[0] + digitos[-1]))
    return numeros

# Medir tempo de execução serial
start_serial = time.time()
numeros_extraidos = extrair_numeros(calibration_data)
soma_total = sum(numeros_extraidos)
end_serial = time.time()
tempo_serial = end_serial - start_serial

# Contagem de números
contagem_numeros = dict(Counter(numeros_extraidos))

resultado_final = {
    "numeros_extraidos": numeros_extraidos,
    "contagem_numeros": contagem_numeros,
    "soma_total": soma_total,
    "tempo_serial": tempo_serial,
    "custo_computacional": "O(M * N), onde M é o número de linhas e N é o processamento de cada linha",
    "uso_memoria": "O(M) para armazenar números extraídos e O(K) para contagem, onde K é o número de valores distintos"
}

# Serializar em JSON
json_resultado = json.dumps(resultado_final, indent=4)
print(json_resultado)
