import tkinter as tk
from tkinter import messagebox
import pickle
import os

class Artista:
    def __init__(self, nome):
        self.nome = nome
        self.albuns = []
        self.musicas = []
    
    def getNome(self):
        return self.nome
    
    def getAlbuns(self):
        return self.albuns
    
    def getMusicas(self):
        return self.musicas
    
    def addMusica(self, musica):
        self.musicas.append(musica)
    
    def addAlbum(self, album):
        self.albuns.append(album)

class LimiteInsereArtista(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('250x50')
        self.title('Inserir Artista')
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameBotao = tk.Frame(self)
        self.frameNome.pack()
        self.frameBotao.pack()

        self.labelInsereNome = tk.Label(self.frameNome, text = 'Nome do artista: ')
        self.labelInsereNome.pack(side = 'left')
        self.entraNome = tk.Entry(self.frameNome, width = 20)
        self.entraNome.pack(side = 'left')

        self.botaoCadastrar = tk.Button(self.frameBotao, text = 'Cadastrar')
        self.botaoCadastrar.pack(side = 'left')
        self.botaoCadastrar.bind('<Button>', controle.cadastrarArtistaHandler)

        self.botaoConcluido = tk.Button(self.frameBotao, text = 'Sair')
        self.botaoConcluido.pack(side = 'left')
        self.botaoConcluido.bind('<Button>', controle.concluidoInsereHandler)
    
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultaArtista(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('250x50')
        self.title('Consultar Artista')
        self.controle = controle

        self.frameArtista = tk.Frame(self)
        self.frameBotao = tk.Frame(self)
        self.frameArtista.pack()
        self.frameBotao.pack()

        self.labelNome = tk.Label(self.frameArtista, text = 'Nome do Artista: ')
        self.entraNome = tk.Entry(self.frameArtista, width = 20)
        self.labelNome.pack(side = 'left')
        self.entraNome.pack(side = 'left')

        self.botaoConsultar = tk.Button(self.frameBotao, text = 'Consultar')
        self.botaoConsultar.pack()
        self.botaoConsultar.bind('<Button>', controle.consultarArtistaHandler)

class LimiteMostraArtista:
    def __init__(self, strr, tipo):
        if tipo:
            messagebox.showinfo('Lista de Álbuns', strr)
        else:
            messagebox.showinfo('Aviso', strr)

class ControleArtista:
    def __init__(self):
        if not os.path.isfile('artista.pickle'):
            self.listaArtistas = []
        else:
            with open('artista.pickle', 'rb') as f:
                self.listaArtistas = pickle.load(f)
    
    def getArtistas(self):
        return self.listaArtistas

    # FUNÇÕES DE INICIAÇÃO 
    def cadastraArtista(self):
        self.LimiteCadastraArtista = LimiteInsereArtista(self)
    
    def consultaArtista(self):
        self.LimiteBuscaArtista = LimiteConsultaArtista(self)

    # HANDLERS
    def cadastrarArtistaHandler(self, event):
        nome = self.LimiteCadastraArtista.entraNome.get()
        self.listaArtistas.append(Artista(nome))
        self.LimiteCadastraArtista.mostraJanela('Sucesso', 'Artista cadastrado com sucesso')
        self.limpaNomeInsere(event)
    
    def consultarArtistaHandler(self, event):
        nome = self.LimiteBuscaArtista.entraNome.get()
        tipo = False
        strr = nome + '\n\n'
        for artista in self.getArtistas():
            if nome == artista.getNome():
                tipo = True
                for albuns in artista.getAlbuns():
                    strr += albuns.getTitulo() + '\n\n'
                    for musicas in albuns.getMusicas():
                        strr += musicas.getNroFaixa() + ' ' + musicas.getTitulo() + '\n'
                    strr += '________________________________\n\n'
                LimiteMostraArtista(strr, tipo)
                self.limpaNomeConsulta(event)
                return
        LimiteMostraArtista('Artista não encontrado', tipo)
        self.limpaNomeConsulta(event)
    
    # LIMPA ENTRY
    def limpaNomeInsere(self, event):
        self.LimiteCadastraArtista.entraNome.delete(0, len(self.LimiteCadastraArtista.entraNome.get()))
    
    def limpaNomeConsulta(self, event):
        self.LimiteBuscaArtista.entraNome.delete(0, len(self.LimiteBuscaArtista.entraNome.get()))

    # PERMANÊNCIA E CONCLUÍDO
    def salvaArtista(self):
        if len(self.listaArtistas) != 0:
            with open("artista.pickle", "wb") as f:
                pickle.dump(self.listaArtistas, f)
    
    def concluidoInsereHandler(self, event):
        self.LimiteCadastraArtista.destroy()
    
    def concluidoConsultaHandler(self, event):
        self.LimiteBuscaArtista.destroy()

        

        


        



            

            

        
        
