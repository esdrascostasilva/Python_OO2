class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._like = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def like(self):
        return self._like

    def dar_like(self):
        self._like += 1

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._like} Likes'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.duracao} min - {self.ano} - {self._like} Likes'

class Netflix(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.temporadas} Temp. - {self.ano} - {self.like} Likes'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)

vingadores = Filme("vingadores", 2016, 170)
atlanta = Netflix("atlanta", 2019, 1)
ruby = Filme("Ruby", 1993, 210)
sexedu = Netflix("Sex education", 2018, 2)

vingadores.dar_like()
vingadores.dar_like()
ruby.dar_like()
ruby.dar_like()
ruby.dar_like()
sexedu.dar_like()
sexedu.dar_like()
sexedu.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_series = [vingadores, atlanta, sexedu, ruby]

play_fds = Playlist("PlayList FDS", filmes_series)

for x in play_fds:
    print(x)

print(f'Tamanho do playlist: {len(play_fds)}')
print(f'Tem na lista? {sexedu in play_fds}')
