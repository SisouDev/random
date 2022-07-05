def main():
    faturamento = {'SP': 67.83643, 'RJ': 36.67866,
                   'MG': 29.22988, 'ES': 27.1654, 'Outros': 19.84953}
    total = sum(faturamento.values())
    for estado, valor in faturamento.items():
        print(f'{estado} - {valor/total*100:.2f}%')


if __name__ == '__main__':
    a = main()
    print(a)
