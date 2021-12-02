import hashlib


if __name__ == '__main__':
    arquivo1 = 'a.txt'
    arquivo2 = 'b.txt'

    hash1 = hashlib.new('ripemd160')

    hash1.update(open(arquivo1, 'rb').read())

    hash2 = hashlib.new('ripemd160')

    hash2.update(open(arquivo2, 'rb').read())

    print(f'O arquivo {arquivo1} é diferente do arquivo {arquivo2}\nHash do arquivo a.txt: {hash1.hexdigest()}\n'
          f'Hash do arquivo b.txt: {hash2.hexdigest()}' if hash1.digest() != hash2.digest() else
          f'O arquivo {arquivo1} é igual ao arquivo {arquivo2}\nHash dos arquivos: {hash1.hexdigest()}')
