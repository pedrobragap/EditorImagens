from os import path
from PIL import Image, ImageEnhance, ImageOps


class Editor():
	img = None
	img_formato = None
	img_local = None
	img_nome = None
	img_ext = None

	def resetar(self):
		self.img = None
		self.img_formato = None
		self.img_local = None
		self.img_nome = None
		self.img_ext = None

	def carregar_imagem(self, imagem):
		try:
			self.img = Image.open(imagem)
			self.img_temp = self.img
			self.img_formato = self.img.format
			self.img_local = path.dirname(path.realpath(imagem))
			self.img_nome, self.img_ext = path.splitext(path.basename(imagem))
			print('Imagem carregada!')
			return True
		except:
			print('Falha ao carregar imagem.')
			return False

	def girar_imagem(self, sentido='horario', angulo=90):
		if (sentido == 'horario'):
			self.img = self.img.rotate(angulo * -1, expand=True)
		elif (sentido == 'anti_horario'):
			self.img = self.img.rotate(angulo, expand=True)

	def remover_cor_imagem(self):
		conversor = ImageEnhance.Color(self.img)
		#self.img = conversor.enhance(0)
		self.img = ImageOps.equalize(self.img)

		
	
	def cor_imagem(self,a):
		conversor = ImageEnhance.Color(self.img)
		self.img_temp = conversor.enhance(a)

	def brilho_imagem(self,b):
		conversorb = ImageEnhance.Brightness(self.img)
		self.img = conversorb.enhance(b)

	def contraste_imagem(self,c):
		conversorc = ImageEnhance.Contrast(self.img)
		self.img = conversorc.enhance(c)



	def salvar(self):
		ln = self.img_local + '/' + self.img_nome + 'edit'+ self.img_ext
		self.img.save(ln, self.img_formato)
		self.resetar()

ed = Editor()