from model.editora import Editora

class EditoraDAO:
    tabela_editoras = []

    def listar(self) -> list:
        return EditoraDAO.tabela_editoras

    def adicionar(self, editora: Editora) -> None:
        EditoraDAO.tabela_editoras.append(editora)

    def remover(self, editora_id: int) -> bool:
        encontrado = False

        for index, editora in enumerate(EditoraDAO.tabela_editoras):
            if editora.id == editora_id:
                encontrado = True
                break

        if encontrado:
            EditoraDAO.tabela_editoras.pop(index)

        return encontrado

    def buscar_por_id(self, editora_id) -> Editora:
        for editora in EditoraDAO.tabela_editoras:
            if (editora.id == editora_id):
                return editora
