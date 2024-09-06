livros = []

def add_book(livros):
    add_book = input("adicione um livro: ")
    livros.append(add_book)

def listar_livros():
    for livro in livros:
        

add_book()
print(livros)