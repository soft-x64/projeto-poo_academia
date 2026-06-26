from datetime import date
from models.execeptions import FichaSemExercicioError

class ItemFicha:
    def __init__(self, exercicio, series: int, repeticoes: int, carga: float):
        self.exercicio = exercicio
        self.series = series
        self.repeticoes = repeticoes
        self.carga = carga
    
    def __str__(self):
        return f"{self.exercicio.nome}: {self.series}x{self.repeticoes} ({self.carga}kg)"


class FichaTreino: # Corrigida a indentacao (agora esta fora da outra classe)
    def __init__(self, aluno, instrutor, data_criacao: date = None):
        self.aluno = aluno
        self.instrutor = instrutor
        self.data_criacao = data_criacao or date.today() # Corrigido para .today()
        self._itens = [] # Inicializada a lista de itens que faltava

    def adicionar_item(self, item: ItemFicha):
        self._itens.append(item)
    
    def finalizar(self):
        if not self._itens:
            raise FichaSemExercicioError("Ficha de treino precisa de pelo menos um exercicio")

    def __str__(self):
        # Removidos os underlines das variaveis aluno e instrutor para bater com o __init__
        linhas = [f"Ficha de {self.aluno.nome} (Instrutor: {self.instrutor.nome})"]
        linhas += [f"  - {item}" for item in self._itens]
        return "\n".join(linhas)
