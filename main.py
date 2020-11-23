import tkinter as tk
import artista 
import album 
import musica
import playlist

class LimitePrincipal:
	def __init__(self, raiz, controle):
		self.raiz = raiz
		self.controle = controle
		self.raiz.geometry('400x250')
		self.raiz.title('SpotyLie')

		self.menuBar = tk.Menu(self.raiz)
		self.menuArtista = tk.Menu(self.menuBar)
		self.menuMusica = tk.Menu(self.menuBar)
		self.menuAlbum = tk.Menu(self.menuBar)
		self.menuPlaylist = tk.Menu(self.menuBar)
		self.menuSair = tk.Menu(self.menuBar)

		self.menuArtista.add_command(label = 'Cadastrar', command = self.controle.insereArtista)
		self.menuArtista.add_command(label = 'Consultar', command = self.controle.consultaArtista)
		self.menuBar.add_cascade(label = 'Artista', menu = self.menuArtista) 

		self.menuMusica.add_command(label = 'Cadastrar', command = self.controle.insereMusica)
		self.menuMusica.add_command(label = 'Consultar', command = self.controle.consultaMusica)
		self.menuBar.add_cascade(label = 'Música', menu = self.menuMusica) 

		self.menuAlbum.add_command(label = 'Cadastrar', command = self.controle.insereAlbum)
		self.menuAlbum.add_command(label = 'Consultar', command = self.controle.consultaAlbum)
		self.menuBar.add_cascade(label = 'Álbum', menu = self.menuAlbum)

		self.menuPlaylist.add_command(label = 'Cadastrar', command = self.controle.inserePlaylist)
		self.menuPlaylist.add_command(label = 'Consultar', command = self.controle.consultaPlaylist)
		self.menuBar.add_cascade(label = 'Playlist', menu = self.menuPlaylist)

		self.menuSair.add_command(label = 'Salvar', command = self.controle.salvaDados)
		self.menuSair.add_command(label = 'Não Salvar', command = lambda: self.raiz.destroy())
		self.menuBar.add_cascade(label = 'Sair', menu = self.menuSair)

		self.raiz.config(menu=self.menuBar)

class ControlePrincipal:
	def __init__(self):
		self.raiz = tk.Tk()
		self.limite = LimitePrincipal(self.raiz, self)
		self.controleArtista = artista.ControleArtista()
		self.controleMusica = musica.ControleMusica(self)
		self.controleAlbum = album.ControleAlbum(self)
		self.controlePlaylist = playlist.ControlePlaylist(self)
		
		self.raiz.mainloop()

	def insereArtista(self):
		self.controleArtista.cadastraArtista()
	
	def consultaArtista(self):
		self.controleArtista.consultaArtista()
	
	def insereMusica(self):
		self.controleMusica.cadastraMusica()
	
	def consultaMusica(self):
		self.controleMusica.consultaMusica()

	def insereAlbum(self):
		self.controleAlbum.cadastraAlbum()

	def consultaAlbum(self):
		self.controleAlbum.consultaAlbum()
	
	def inserePlaylist(self):
		self.controlePlaylist.cadastraPlaylist()
		self.controlePlaylist.atualizaListBox()

	def consultaPlaylist(self):
		self.controlePlaylist.consultaPlaylist()

	def salvaDados(self):
		self.controleArtista.salvaArtista()
		self.controleAlbum.salvaAlbum()
		self.controleMusica.salvaMusica()
		self.controlePlaylist.salvaPlaylist()
		self.raiz.destroy()
	

if __name__ == '__main__':
	App = ControlePrincipal()


		
