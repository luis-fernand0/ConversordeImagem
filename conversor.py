from tkinter import *
import tkinter.filedialog
from tkinter import messagebox
from PIL import Image, ImageTk


# SELECIONANDO A IMAGEM

class Conversor:

    def __init__(self):

        self.img_salvar = None
        self.imagem = None
        self.img = None
        self.photo = None
        self.redimensionada = None

        # FERRAMNETAS E TEXTOS
        botao1 = Button(janela, text='Importar arquivo', command=self.ExibirIMG,
                        bg='#32a852', fg='white', font=25)
        botao2 = Button(frame1, text='Converter e Salvar', bg='#32a852', fg='white', font=25,
                        command=self.Converter_E_Salvar)
        botao3 = Button(frame1, text='Deletar', command=self.Deletar, bg='#cc1b0e',
                        fg='white', font=25)
        texto1 = Label(frame1, text='Converter para:', font=25, bg='light blue')

        self.valor_radio = tkinter.IntVar()
        self.botao4 = Radiobutton(frame1, text='PDF', font=25, variable=self.valor_radio,
                                  value=1, bg='light blue')
        self.botao5 = Radiobutton(frame1, text='JPG', font=25, variable=self.valor_radio,
                                  value=2, bg='light blue')

        # POSIÇÕES DAS FERRAMENTAS E TEXTOS
        botao1.pack(fill=BOTH)
        botao2.pack(side='bottom', fill=BOTH)
        botao3.pack(side='bottom', before=botao2, fill=BOTH)
        texto1.pack(side='left', padx=(300, 0))
        self.botao4.pack(padx=(0, 300))
        self.botao5.pack(padx=(0, 300))

    def ExibirIMG(self):
        # PEDINDO PARA O USUARIO SELECIONAR A IMAGEM DESEJADA
        try:
            self.img = Image.open(tkinter.filedialog.askopenfilename())
            self.img_salvar = self.img.convert('RGB')

        except:
            messagebox.showinfo(title='Erro', message='Erro, não aceitamos esse tipo de arquivo!')

        try:
            # REDIMENSIONANDO A IMAGEM
            self.redimensionada = self.img.resize((600, 400))
            self.photo = ImageTk.PhotoImage(self.redimensionada)

        except:
            pass

        # EXIBINDO A IMAGEM
        self.imagem = Label(image=self.photo)
        self.imagem.Image = self.photo
        self.imagem.pack(padx=(50, 50), pady=(50, 50))

    def Deletar(self):
        self.imagem.destroy()

    def Converter_E_Salvar(self):
        salvar = self.valor_radio.get()
        if salvar == 1:
            self.img_salvar.save(f'{tkinter.filedialog.asksaveasfilename()}.pdf')
        elif salvar == 2:
            self.img_salvar.save(f'{tkinter.filedialog.asksaveasfilename()}.jpg')


janela = Tk()

# CONFIGURAÇÕES DA JANELA
frame1 = Frame(janela, bg='light blue')
frame1.pack(side='bottom', fill=BOTH)
janela.title('Conversor de Imagem')
janela.config(bg='light blue')
janela.geometry('800x650')
janela.minsize(800, 650)
janela.maxsize(800, 650)

janela_conversor = Conversor()

janela.mainloop()
