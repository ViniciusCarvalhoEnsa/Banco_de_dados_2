# -------------------------------------------------------------------------------------------------- classe professor #
class Professor():

    def __init__(self, nome_professor): # propriedade nome dos professores #
        self.nome_professor = nome_professor

    def ministra_aula(self, assunto): # método para aula ministrada #
        print(f"O professor {self.nome_professor} está ministrando uma aula sobre {assunto}")

# ----------------------------------------------------------------------------------------------------- classe aluno #
class Aluno():

    def __init__(self, nome_aluno): # propriedade nome dos alunos #
        self.nome_aluno = nome_aluno

    def presenca(self): # método para presenca #
        print(f"O aluno {self.nome_aluno} está presente.")

# ------------------------------------------------------------------------------------------------------ classe aula #
class Aula():
    
    def __init__(self, professor, assunto, alunos = []): # propriedades da aula #
        self.professor = professor
        self.assunto = assunto
        self.alunos = alunos

    def adicionar_aluno(self, aluno): # adiciona o objeto aluno na lista alunos #
        self.alunos.append(aluno)

    def listar_presenca(self): # para a presença dos alunos #
        print(f"Presença na aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome_professor}:")

        for aluno in self.alunos: # adiciona aluno na presença #
            aluno.presenca()

# ------------------------------------------------------------------------------------------------------ declarações #
professor = Professor("Jonas") # nome do professor #

aluno1 = Aluno("Vinícius") 
aluno2 = Aluno("Beatriz") # nome dos alunos #
aluno3 = Aluno("John")    

aula = Aula(professor, "Bancos de Dados II") # aula ministrada #

aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2) # adiciona os alunos na aula #
aula.adicionar_aluno(aluno3)

print(aula.listar_presenca()) # saída da lista de presença #