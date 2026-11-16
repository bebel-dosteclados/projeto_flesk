
# aluno_service.py: guarda e entrega os dados dos alunos (em memória)
lista_aluno = [
    {"id": 1, "nome": "Ana Souza",
     "telefone": "(86) 99999-0001", "cidade": "Teresina"},
    {"id": 2, "nome": "Bruno Lima",
     "telefone": "(86) 99999-0002", "cidade": "Timon"},
    {"id": 3, "nome": "Carla Mendes",
     "telefone": "(86) 99999-0003", "cidade": "Parnaíba"},
]
def listar():
    return lista_aluno