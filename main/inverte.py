def inverte(string: str) -> str:
    string = string[::-1]
    return string


if __name__ == '__main__':
    a = 'abcdefghijklmnopqrstuvwxyz'
    print(inverte(a))
    b = 'Maria Karolina :)'
    print(inverte(b))
