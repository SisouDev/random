import json
from typing import List, Tuple

"""O cálculo da média deve ser feito apenas nos dias com faturamento."""


def Faturamento(Vetor: List[int]) -> Tuple[int, int, int]:
    menor = Vetor[0]
    maior = Vetor[0]
    media = sum(Vetor)/len(Vetor)
    cont = 0
    for i in Vetor:
        if i < menor:
            menor = i
        if i > maior:
            maior = i
        if i > media:
            cont += 1
    return menor, maior, cont


if __name__ == '__main__':
    a = [x for x in range(30, 310)]
    print(Faturamento(a))
    b = [y for y in range(40, 410)]
    print(Faturamento(b))
    c = [z for z in range(50, 510)]
    print(Faturamento(c))

    json_file = open('faturamento.json', 'w')
    json.dump(Faturamento(a), json_file)
    json_file.close()
    json_file = open('faturamento.json', 'r')
    print(json.load(json_file))
    json_file.close()
