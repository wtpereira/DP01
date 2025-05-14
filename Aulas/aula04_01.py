autor = {'nome': 'Machado de Assis', 'email': 'm@m', 'telefone': '123', 'biografia': 'biom'}
categoria = {'nome': 'Romance'}
editora = {'nome': 'Rocco', 'endereco': 'Rua x', 'telefone': '889898'}


livro = {
    'titulo': 'Dom Casmurro',
    'ano': 1890,
    'paginas': 200,
    'isbn': 'AFDS34324',
    'autor': autor,
}

print(livro['autor']['nome'])

print(livro.get('autor').get('nome'))

print(f'Resumo do livro: {livro.get("resumo", "---")}')
print(f'Resumo do livro: {livro["resumo"]}')  # Essa linha vai resultar em erro.

print('Fim do programa!')
