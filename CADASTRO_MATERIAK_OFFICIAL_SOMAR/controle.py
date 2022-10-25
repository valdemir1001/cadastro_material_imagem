from distutils.util import execute
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import width
from PIL import Image,ImageTk
import PIL


from listas import *
import sqlite3



root = Tk()

class Funcoes():
    def limpa_tela_entrada(self):
        # Limpa a tela da ENTRADA NO ESTOQUE
        self.codigo_entrada.delete(0,'end')
        self.cbx_material_entrada.delete(0,'end')
        self.entry_quant_entrada.delete(0,'end')
        self.cbx_tipo_entrada.delete(0,'end')
        self.entry_data_entrada.delete(0,'end')
        
    def limpa_tela_saida(self):
        # Limpa a tela da SAIDA DO ESTOQUE
        self.codigo_saida.delete(0,'end')
        self.cbx_material_saida.delete(0,'end')
        self.entry_quant_saida.delete(0,'end')
        self.cbx_tipo_saida.delete(0,'end')
        self.entry_data_saida.delete(0,'end')

    def limpa_tela_estoque(self):
        # Limpa a tela do ESTOQUE
        self.codigo_estoque.delete(0,'end')
        self.cbx_material_estoque.delete(0,'end')
        self.entry_quant_estoque.delete(0,'end')
        self.cbx_tipo_estoque.delete(0,'end')
        self.entry_data_estoque.delete(0,'end')
        
    def conecta_bd(self):
        self.conn = sqlite3.connect('cordeirinho.bd')
        self.cursor = self.conn.cursor()

        print('Conectado ao Banco Estoque')
        
    def desconecta_bd(self):
        self.conn.close()
        
    def monta_tabelas_entrada(self):
        self.conecta_bd()
        print('Banco ENTRADA CONECTADO')

    # Criar Tabelas
        self.cursor.execute(""" 
                            CREATE TABLE IF NOT EXISTS entrada (
                                codigo_entrada INTEGER PRIMARY KEY AUTOINCREMENT,
                                material_entrada VARCHAR(100) NOT NULL,
                                quantidade_entrada INTEGER NOT NULL,
                                tipo_entrada VARCHAR(30),
                                data_entrada DATA
                                )
                            """)
        self.conn.commit(); print('Tabela entrada Criada')
        self.desconecta_bd()
        
    def monta_tabelas_saida(self):
        self.conecta_bd()
        print('Banco SAIDA CONECTADO')
        
    # Criar Tabelas
        self.cursor.execute(""" 
                            CREATE TABLE IF NOT EXISTS saida (
                                codigo_saida INTEGER PRIMARY KEY,
                                material_saida VARCHAR(100) NOT NULL,
                                quantidade_saida INTEGER NOT NULL,
                                tipo_saida VARCHAR(30),
                                data_saida DATA
                                )
                            """)
        self.conn.commit(); print('Tabela SAIDA Criada')
        self.desconecta_bd()

    def monta_tabelas_estoque(self):
        self.conecta_bd()
        print('Banco ESTOQU CONECTADO')

    # Criar Tabelas
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS estoque (
                                codigo_estoque INTEGER PRIMARY KEY,
                                material_estoque VARCHAR(100) NOT NULL,
                                quantidade_estoque INTEGER NOT NULL,
                                tipo_estoque VARCHAR(30),
                                data_estoque DATA
                                )
                            """)
        self.conn.commit(); print('Tabela ESTOQUE Criada')
        self.desconecta_bd()
 
    def variaveis_entrada(self):
        self.v_codigo_entrada = self.codigo_entrada.get()
        self.v_material_entrada = self.cbx_material_entrada.get()
        self.v_quantidade_entrada = self.entry_quant_entrada.get()
        self.v_tipo_entrada = self.cbx_tipo_entrada.get()
        self.v_data_entrada = self.entry_data_entrada.get()

    def variaveis_saida(self):
        self.v_codigo_saida = self.codigo_saida.get()
        self.v_material_saida = self.cbx_material_saida.get()
        self.v_quantidade_saida = self.entry_quant_saida.get()
        self.v_tipo_saida = self.cbx_tipo_saida.get()
        self.v_data_saida = self.entry_data_saida.get()

    def variaveis_estoque(self): 
        self.v_codigo_estoque = self.codigo_estoque.get()
        self.v_material_estoque = self.cbx_material_estoque.get()
        self.v_quantidade_estoque = self.entry_quant_estoque.get()
        self.v_tipo_estoque = self.cbx_tipo_estoque.get()
        self.v_data_estoque = self.entry_data_estoque.get()
        
    def add_material_entrada(self):
        #codigo = self.codigo_entrada.get()       
            '''if codigo == '':
                messagebox.showinfo(title='ENTRADA DE MATERIAL',message='FALTA ADICIONAR O CAMPO CÓDIGO!') 
                self.desconecta_bd
            else:'''
            self.variaveis_entrada()
            self.conecta_bd()
            self.cursor.execute("""
                                INSERT INTO entrada(material_entrada,quantidade_entrada,tipo_entrada,data_entrada)
                                VALUES (?,?,?,?)""",(self.v_material_entrada,self.v_quantidade_entrada,self.v_tipo_entrada,self.v_data_entrada))
            self.conn.commit()
            self.desconecta_bd()
            self.select_lista_entrada()
            self.limpa_tela_entrada()
    
    def add_material_saida(self):
        if self.codigo_saida.get() == '':
            messagebox.showinfo(title='SAÍDA DO MATERIAL',message='FALTA ADICIONAR O CAMPO CÓDIGO!')        
            self.desconecta_bd
        else:
            self.variaveis_saida()
            self.conecta_bd()
            self.cursor.execute("""
                                INSERT INTO saida(codigo_saida,material_saida,quantidade_saida,tipo_saida,data_saida)
                                VALUES (?,?,?,?,?)""",(self.v_codigo_saida,self.v_material_saida,self.v_quantidade_saida,self.v_tipo_saida,self.v_data_saida))
            self.conn.commit()
            self.desconecta_bd()
            self.select_lista_saida()
            self.limpa_tela_saida()

    def select_lista_entrada(self):
        self.lista_material_entrada.delete(*self.lista_material_entrada.get_children())
        self.conecta_bd()
        lista = self.cursor.execute("""
                                SELECT codigo_entrada, material_entrada,quantidade_entrada,tipo_entrada,data_entrada 
                                FROM entrada 
                                ORDER BY material_entrada ASC""")
        for i in lista:
            self.lista_material_entrada.insert('','end', values=i)

        self.desconecta_bd()
        
    def select_lista_saida(self):
        self.lista_material_saida.delete(*self.lista_material_saida.get_children())
        self.conecta_bd()
        lista = self.cursor.execute("""
                                SELECT codigo_saida, material_saida, quantidade_saida, tipo_saida, data_saida 
                                FROM saida 
                                ORDER BY material_saida ASC""")
        for i in lista:
            self.lista_material_saida.insert('','end', values=i)

        self.desconecta_bd()   
        
    def OnDoubleClick_entrada(self,event):
        self.limpa_tela_entrada()
        self.lista_material_entrada.selection()
        
        for n in self.lista_material_entrada.selection():
            col1,col2,col3,col4,col5 = self.lista_material_entrada.item(n, 'values')
            
            self.codigo_entrada.insert(END,col1)
            self.cbx_material_entrada.insert(END,col2)
            self.entry_quant_entrada.insert(END,col3)
            self.cbx_tipo_entrada.insert(END,col4)
            self.entry_data_entrada.insert(END,col5)
            
        self.desconecta_bd()

    def OnDoubleClick_saida(self,event):
        self.limpa_tela_saida()
        self.lista_material_saida.selection()
        
        for n in self.lista_material_saida.selection():
            col1,col2,col3,col4,col5 = self.lista_material_saida.item(n, 'values')
            
            self.codigo_saida.insert(END,col1)
            self.cbx_material_saida.insert(END,col2)
            self.entry_quant_saida.insert(END,col3)
            self.cbx_tipo_saida.insert(END,col4)
            self.entry_data_saida.insert(END,col5)
            
        self.desconecta_bd()    

    def deleta_material_entrada(self):
        resposta = messagebox.askquestion(title='Apagar Registro',message='Voce deseja Apagar o registro selecionado?')
        if resposta == 'yes':
            self.variaveis_entrada()
            self.conecta_bd()
            self.cursor.execute("""
                                    DELETE FROM entrada WHERE codigo_entrada = ? """,(self.v_codigo_entrada,))
            self.conn.commit()   
            self.desconecta_bd()
            self.limpa_tela_entrada()
            self.select_lista_entrada()

        else:
            self.desconecta_bd
          
    def deleta_material_saida(self):
        resposta = messagebox.askquestion(title='APAGAR REGISTRO',message='Voce deseja APAGAR o registro selecionado?')
        if resposta == 'yes':
            self.variaveis_saida()
            self.conecta_bd()
            self.cursor.execute("""
                                    DELETE FROM saida WHERE codigo_saida = ? """,(self.v_codigo_saida,))
            self.conn.commit()   
            self.desconecta_bd()
            self.limpa_tela_entrada()
            self.select_lista_entrada()
        else:
            self.desconecta_bd

    def alterar_material_entrada(self):
        resposta = messagebox.askquestion(title='ALTERAR REGISTRO',message='Voce deseja ALTERAR o registro selecionado?')
        if resposta == 'yes':  
            self.variaveis_entrada()
            self.conecta_bd()
            self.cursor.execute("""
                                UPDATE entrada SET material_entrada=?, quantidade_entrada=?, tipo_entrada=?, data_entrada =? 
                                WHERE codigo_entrada = ? """,(self.v_material_entrada,self.v_quantidade_entrada,self.v_tipo_entrada,self.v_data_entrada,self.v_codigo_entrada))         
        
            self.conn.commit()
            self.desconecta_bd()
            self.select_lista_entrada()
            self.limpa_tela_entrada()

        else:
            self.desconecta_bd

    def alterar_material_saida(self):
        resposta = messagebox.askquestion(title='ALTERAR REGISTRO',message='Voce deseja ALTERAR o registro selecionado?')
        if resposta == 'yes': 
            self.variaveis_saida()
            self.conecta_bd()
            self.cursor.execute("""
                                UPDATE saida SET material_saida=?, quantidade_saida=?, tipo_saida=?, data_saida=? 
                                WHERE codigo_saida = ? """,(self.v_material_saida,self.v_quantidade_saida,self.v_tipo_saida,self.v_data_saida,self.v_codigo_saida))

            
            self.conn.commit()
            
            self.desconecta_bd()
            self.select_lista_saida()
            self.limpa_tela_saida()

        else:
            self.desconecta_bd

class Application(Funcoes):
    def __init__(self,master=None):
        self.root = root
        
        self.tela()
        self.abas()
        self.frames_aba1()
        self.frames_aba2()
        self.frames_aba3()
        
        self.windgets()
        self.lista_frame_4_entrada()
        self.lista_frame_4_saida()
        
        self.limpa_tela_entrada()
        self.monta_tabelas_entrada()
        self.monta_tabelas_saida()
        self.select_lista_entrada()

        root.mainloop()
    def tela(self):
        self.root.title('Janela 1')
        self.root.geometry('800x650+450+10')
    # CORES
        self.cor_azul_01 = '#215a6d'
        self.cor_azul_02 = '#17a7a8'
        self.cor_azul_03 = '#101652'
        self.cor_lightgray = 'lightgray'
        self.cor_cinza_01 = '#142738'
        self.cor_cinza_02 = '#122f51'
        self.cor_cinza_03 = '#333e50'
        self.cor_vermelho_01 = '#9e0e30'
        self.cor_vermelho_02 ='#df2a33'
        self.cor_vermelho_03 = '#cf0638'
        self.cor_preto_01 = '#000000'
        self.cor_laranja_01 = '#f93f03'
        self.cor_laranja_02 = '#f8572d'
        self.cor_laranja_03 = '#cf872e'
        self.cor_verde_01 = '#207178'
        self.cor_verde_02 = '#001f21'
        self.cor_verde_03 = '#006666'
        self.cor_verde_04 = '#7ab317'

    def abas(self):
        self.abas = ttk.Notebook(self.root)
        self.aba1 = Frame(self.abas)
        self.aba2 = Frame(self.abas)
        self.aba3 = Frame(self.abas)

        self.aba1.configure(background=self.cor_azul_03)
        self.aba2.configure(background=self.cor_verde_02)
        self.aba3.configure(background=self.cor_vermelho_01)

        self.abas.add(self.aba1, text='entrada no estoque'.upper())
        self.abas.add(self.aba2, text='saída do estoque'.upper())
        self.abas.add(self.aba3, text='estoque e filtros'.upper())

        self.abas.place(relx=0, rely=0, relwidth=1, relheight=1)


    def frames_aba1(self):
        self.frame_1_ab1 = Frame(self.aba1,bg=self.cor_azul_03)
        self.frame_1_ab1.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.10)
        self.frame_2_ab1 = Frame(self.aba1,bg='lightgray')
        self.frame_2_ab1.place(relx=0.01,rely=0.12,relwidth=0.50,relheight=0.40)
        self.frame_3_ab1 = Frame(self.aba1,bg='blue')
        self.frame_3_ab1.place(relx=0.52,rely=0.12,relwidth=0.47,relheight=0.40)
        self.frame_4_ab1 = Frame(self.aba1,bg='gray')
        self.frame_4_ab1.place(relx=0.01,rely=0.54,relwidth=0.98,relheight=0.45)

    def frames_aba2(self):
        self.frame_1_ab2 = Frame(self.aba2,bg=self.cor_verde_02)
        self.frame_1_ab2.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.10)
        self.frame_2_ab2 = Frame(self.aba2,bg='yellow')
        self.frame_2_ab2.place(relx=0.01,rely=0.12,relwidth=0.50,relheight=0.40)
        self.frame_3_ab2 = Frame(self.aba2,bg='blue')
        self.frame_3_ab2.place(relx=0.52,rely=0.12,relwidth=0.47,relheight=0.40)
        self.frame_4_ab2 = Frame(self.aba2,bg='gray')
        self.frame_4_ab2.place(relx=0.01,rely=0.54,relwidth=0.98,relheight=0.45)

    def frames_aba3(self):
        self.frame_1_ab3 = Frame(self.aba3,bg=self.cor_vermelho_01)
        self.frame_1_ab3.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.10)
        self.frame_2_ab3 = Frame(self.aba3,bg='yellow')
        self.frame_2_ab3.place(relx=0.01,rely=0.12,relwidth=0.50,relheight=0.40)
        self.frame_3_ab3 = Frame(self.aba3,bg='blue')
        self.frame_3_ab3.place(relx=0.52,rely=0.12,relwidth=0.47,relheight=0.40)
        self.frame_4_ab3 = Frame(self.aba3,bg='gray')
        self.frame_4_ab3.place(relx=0.01,rely=0.54,relwidth=0.98,relheight=0.45)

    def selecionar_entrada(self,event):
        if self.cbx_material_entrada.get() == 'Cimento':
            self.cbx_tipo_entrada.delete(0,END)
            self.cbx_tipo_entrada.insert(END,tipo[0])
        elif self.cbx_material_entrada.get() == 'Vergalhão 5/16':
            self.cbx_tipo_entrada.delete(0,END)
            self.cbx_tipo_entrada.insert(END,tipo[0])
        elif self.cbx_material_entrada.get() == 'Bica Fina':
            self.cbx_tipo_entrada.delete(0,END)
            self.cbx_tipo_entrada.insert(END,tipo[1])
        elif self.cbx_material_entrada.get() == 'Prego 17x27':
            self.cbx_tipo_entrada.delete(0,END)
            self.cbx_tipo_entrada.insert(END,tipo[2])
        elif self.cbx_material_entrada.get() == 'Areia Lavada':
            self.cbx_tipo_entrada.delete(0,END)
            self.cbx_tipo_entrada.insert(END,tipo[1])
        elif self.cbx_material_entrada.get() == 'Anel de Concreto':
            self.cbx_tipo_entrada.delete(0,END)
            self.cbx_tipo_entrada.insert(END,tipo[0])
        elif self.cbx_material_entrada.get() == 'Bica Grossa':
            self.cbx_tipo_entrada.delete(0,END)
            self.cbx_tipo_entrada.insert(END,tipo[1])
        elif self.cbx_material_entrada.get() == 'Brita 0':
            self.cbx_tipo_entrada.delete(0,END)
            self.cbx_tipo_entrada.insert(END,tipo[1])
        elif self.cbx_material_entrada.get() == 'Bloco de 10':
            self.cbx_tipo_entrada.delete(0,END)
            self.cbx_tipo_entrada.insert(END,tipo[0])
        elif self.cbx_material_entrada.get() == 'Bloco de 15':
            self.cbx_tipo_entrada.delete(0,END)
            self.cbx_tipo_entrada.insert(END,tipo[0])
        elif self.cbx_material_entrada.get() == 'Bloco de 20':
            self.cbx_tipo_entrada.delete(0,END)
            self.cbx_tipo_entrada.insert(END,tipo[0])
        elif self.cbx_material_entrada.get() == 'Manilha 300':
            self.cbx_tipo_entrada.delete(0,END)
            self.cbx_tipo_entrada.insert(END,tipo[0])
        elif self.cbx_material_entrada.get() == 'Manilha 400':
            self.cbx_tipo_entrada.delete(0,END)
            self.cbx_tipo_entrada.insert(END,tipo[0])
        elif self.cbx_material_entrada.get() == 'Manilha 600':
            self.cbx_tipo_entrada.delete(0,END)
            self.cbx_tipo_entrada.insert(END,tipo[0])
        elif self.cbx_material_entrada.get() == 'Meio Fio':
            self.cbx_tipo_entrada.delete(0,END)
            self.cbx_tipo_entrada.insert(END,tipo[0])
        elif self.cbx_material_entrada.get() == 'Vergalhão 4.2':
            self.cbx_tipo_entrada.delete(0,END)
            self.cbx_tipo_entrada.insert(END,tipo[0])
        elif self.cbx_material_entrada.get() == 'Vergalhão 1/4':
            self.cbx_tipo_entrada.delete(0,END)
            self.cbx_tipo_entrada.insert(END,tipo[0])
        elif self.cbx_material_entrada.get() == 'Vergalhão 3/8':
            self.cbx_tipo_entrada.delete(0,END)
            self.cbx_tipo_entrada.insert(END,tipo[0])
        elif self.cbx_material_entrada.get() == 'Boca de Lobo':
            self.cbx_tipo_entrada.delete(0,END)
            self.cbx_tipo_entrada.insert(END,tipo[0])
        elif self.cbx_material_entrada.get() == 'Tábua de 30':
            self.cbx_tipo_entrada.delete(0,END)
            self.cbx_tipo_entrada.insert(END,tipo[0])

    def selecionar_saida(self,event):
        if self.cbx_material_saida.get() == 'Cimento':
            self.cbx_tipo_saida.delete(0,END)
            self.cbx_tipo_saida.insert(END,tipo[0])
        elif self.cbx_material_saida.get() == 'Vergalhão 5/16':
            self.cbx_tipo_saida.delete(0,END)
            self.cbx_tipo_saida.insert(END,tipo[0])
        elif self.cbx_material_saida.get() == 'Bica Fina':
            self.cbx_tipo_saida.delete(0,END)
            self.cbx_tipo_saida.insert(END,tipo[1])
        elif self.cbx_material_saida.get() == 'Prego 17x27':
            self.cbx_tipo_saida.delete(0,END)
            self.cbx_tipo_saida.insert(END,tipo[2])
        elif self.cbx_material_saida.get() == 'Areia Lavada':
            self.cbx_tipo_saida.delete(0,END)
            self.cbx_tipo_saida.insert(END,tipo[1])
        elif self.cbx_material_saida.get() == 'Anel de Concreto':
            self.cbx_tipo_saida.delete(0,END)
            self.cbx_tipo_saida.insert(END,tipo[0])
        elif self.cbx_material_saida.get() == 'Bica Grossa':
            self.cbx_tipo_saida.delete(0,END)
            self.cbx_tipo_saida.insert(END,tipo[1])
        elif self.cbx_material_saida.get() == 'Brita 0':
            self.cbx_tipo_saida.delete(0,END)
            self.cbx_tipo_saida.insert(END,tipo[1])
        elif self.cbx_material_saida.get() == 'Bloco de 10':
            self.cbx_tipo_saida.delete(0,END)
            self.cbx_tipo_saida.insert(END,tipo[0])
        elif self.cbx_material_saida.get() == 'Bloco de 15':
            self.cbx_tipo_saida.delete(0,END)
            self.cbx_tipo_saida.insert(END,tipo[0])
        elif self.cbx_material_saida.get() == 'Bloco de 20':
            self.cbx_tipo_saida.delete(0,END)
            self.cbx_tipo_saida.insert(END,tipo[0])
        elif self.cbx_material_saida.get() == 'Manilha 300':
            self.cbx_tipo_saida.delete(0,END)
            self.cbx_tipo_saida.insert(END,tipo[0])
        elif self.cbx_material_saida.get() == 'Manilha 400':
            self.cbx_tipo_saida.delete(0,END)
            self.cbx_tipo_saida.insert(END,tipo[0])
        elif self.cbx_material_saida.get() == 'Manilha 600':
            self.cbx_tipo_saida.delete(0,END)
            self.cbx_tipo_saida.insert(END,tipo[0])
        elif self.cbx_material_saida.get() == 'Meio Fio':
            self.cbx_tipo_saida.delete(0,END)
            self.cbx_tipo_saida.insert(END,tipo[0])
        elif self.cbx_material_saida.get() == 'Vergalhão 4.2':
            self.cbx_tipo_saida.delete(0,END)
            self.cbx_tipo_saida.insert(END,tipo[0])
        elif self.cbx_material_saida.get() == 'Vergalhão 1/4':
            self.cbx_tipo_saida.delete(0,END)
            self.cbx_tipo_saida.insert(END,tipo[0])
        elif self.cbx_material_saida.get() == 'Vergalhão 3/8':
            self.cbx_tipo_saida.delete(0,END)
            self.cbx_tipo_saida.insert(END,tipo[0])
        elif self.cbx_material_saida.get() == 'Boca de Lobo':
            self.cbx_tipo_saida.delete(0,END)
            self.cbx_tipo_saida.insert(END,tipo[0])
        elif self.cbx_material_saida.get() == 'Tábua de 30':
            self.cbx_tipo_saida.delete(0,END)
            self.cbx_tipo_saida.insert(END,tipo[0])

    def windgets(self):

    # imagem LOGO
        self.img_logo = Image.open('img/figura_png.png')
        self.img_logo = self.img_logo.resize((60, 60))
        self.img_logo = ImageTk.PhotoImage(self.img_logo)

    # Label LOGO
        self.img_logo1 = Label(self.frame_1_ab1,image=self.img_logo,width=900,
                            compound=CENTER,relief=RAISED,anchor=NW,font=('verdana 10 bold'),bg='black')
        self.img_logo1.place(relx=0,rely=0,relwidth=0.08,relheight=0.98)

        self.img_logo1 = Label(self.frame_1_ab1,font=('verdana 32 bold'),fg='white',
                               text='Controle de estoque'.upper(),bg=self.cor_azul_03)
        self.img_logo1.place(relx=0.08, rely=0.05, relwidth=0.92, relheight=0.90)

    # Logo Aba 2
        self.img_logo2 = Label(self.frame_1_ab2,image=self.img_logo,width=900,
                            compound=CENTER,relief=RAISED,anchor=NW,font=('verdana 10 bold'),bg='black')
        self.img_logo2.place(relx=0,rely=0,relwidth=0.08,relheight=0.98)

        self.img_logo2 = Label(self.frame_1_ab2,font=('verdana 32 bold'),fg='white',
                               text='Controle de estoque'.upper(),bg=self.cor_verde_02)
        self.img_logo2.place(relx=0.08, rely=0.05, relwidth=0.92, relheight=0.90)

     # Logo Aba 3
        self.img_logo3 = Label(self.frame_1_ab3,image=self.img_logo,width=900,
                            compound=CENTER,relief=RAISED,anchor=NW,font=('verdana 10 bold'),bg='black')
        self.img_logo3.place(relx=0,rely=0,relwidth=0.08,relheight=0.98)

        self.img_logo3 = Label(self.frame_1_ab3,font=('verdana 32 bold'),fg='white',
                               text='Controle de estoque'.upper(),bg=self.cor_vermelho_01)
        self.img_logo3.place(relx=0.08, rely=0.05, relwidth=0.92, relheight=0.90)


    # Label FRAME2 ABA1 -
        self.lb_entrada_estoque = Label(self.frame_2_ab1,text='entrada de material'.upper(),bg= self.cor_lightgray,
                                        font=('verdana 18 bold'))
        self.lb_entrada_estoque.place(relx=0.10, rely=0.01, relwidth=0.80, relheight=0.15)
        
    # Separador em Linha
        self.separador = ttk.Separator(self.frame_2_ab1)
        self.separador.pack(padx= 5,pady=42, fill= X)
        

    #Label FRAME@ ABA2
        self.lb_saida_estoque = Label(self.frame_2_ab2,text='saída do estoque'.upper(),
                                        font=('verdana 12 bold'))
        self.lb_saida_estoque.place(relx=0.28, rely=0.01, relwidth=0.55, relheight=0.10)

    # Label Material Entrada
        self.lb_entrada_material = Label(self.frame_2_ab1, text='material'.upper(),bg= self.cor_lightgray,
                                        font=('verdana 10 bold'))
        self.lb_entrada_material.place(relx=0.01, rely=0.35, relwidth=0.21, relheight=0.10)
        
    # Label Material Saída
        self.lb_saida_material = Label(self.frame_2_ab2, text='material'.upper(),
                                        font=('verdana 10 bold'))
        self.lb_saida_material.place(relx=0.01, rely=0.35, relwidth=0.21, relheight=0.10)
        
    # Combobox Material Entrada
        self.cbx_material_entrada = ttk.Combobox(self.frame_2_ab1,font=('verdana 12'),values=lista_material)
        self.cbx_material_entrada.set('Material')
        self.cbx_material_entrada.bind('<<ComboboxSelected>>',self.selecionar_entrada)
        self.cbx_material_entrada.place(relx=0.23, rely=0.35, relwidth=0.62, relheight=0.10)
        
    # Combobox Material saida
        self.cbx_material_saida = ttk.Combobox(self.frame_2_ab2,font=('verdana 12'),values=lista_material)
        self.cbx_material_saida.set('Material')
        self.cbx_material_saida.bind('<<ComboboxSelected>>',self.selecionar_saida)
        self.cbx_material_saida.place(relx=0.23, rely=0.35, relwidth=0.62, relheight=0.10)
        
    # Codigo ENTRADA    
        self.lb_codigo_entrada = Label(self.frame_2_ab1, text='codigo'.upper(),font=('verdana 10 bold'),bg= self.cor_lightgray)
        self.lb_codigo_entrada.place(relx=0.05, rely=0.20, relwidth=0.17, relheight=0.10)     
        
        self.codigo_entrada = Entry(self.frame_2_ab1,font=('verdana 10 bold'))
        self.codigo_entrada.place(relx=0.23, rely=0.20, relwidth=0.25, relheight=0.10)
        
    # Codigo SAIDA  
        self.lb_codigo_saida = Label(self.frame_2_ab2, text='codigo'.upper(),
                                        font=('verdana 10 bold'))
        self.lb_codigo_saida.place(relx=0.05, rely=0.20, relwidth=0.17, relheight=0.10) 

        self.codigo_saida = Entry(self.frame_2_ab2,font=('verdana 10 bold'))
        self.codigo_saida.place(relx=0.23, rely=0.20, relwidth=0.25, relheight=0.10)

    # Label Quantidade ENTRADA
        self.lb_quant_entrada = Label(self.frame_2_ab1, text='qt.'.upper(),bg= self.cor_lightgray,
                                           font=('verdana 10 bold'))
        self.lb_quant_entrada.place(relx=0.12, rely=0.50, relwidth=0.10, relheight=0.10)

    # Label Quantidade SAIDA
        self.lb_quant_saida = Label(self.frame_2_ab2, text='qt.'.upper(),
                                      font=('verdana 10 bold'))
        self.lb_quant_saida.place(relx=0.12, rely=0.50, relwidth=0.10, relheight=0.10)

    # Combobox Quantidade ENTRADA
        self.entry_quant_entrada = ttk.Combobox(self.frame_2_ab1,values= quantidade,
                                           font=('verdana 10 bold'))
        self.entry_quant_entrada.place(relx=0.23, rely=0.50, relwidth=0.25, relheight=0.10)

    # Combobox Quantidade SAIDA
        self.entry_quant_saida = ttk.Combobox(self.frame_2_ab2,values= quantidade,
                                           font=('verdana 10 bold'))
        self.entry_quant_saida.place(relx=0.23, rely=0.50, relwidth=0.25, relheight=0.10)

    # Label Tipo ENTRADA
        self.lb_tipo_entrada = Label(self.frame_2_ab1, text='tipo'.upper(),bg= self.cor_lightgray,
                                      font=('verdana 10 bold'))
        self.lb_tipo_entrada.place(relx=0.53, rely=0.50, relwidth=0.10, relheight=0.10)

    # Label Tipo SAIDA
        self.lb_tipo_saida = Label(self.frame_2_ab2, text='tipo'.upper(),
                                      font=('verdana 10 bold'))
        self.lb_tipo_saida.place(relx=0.53, rely=0.50, relwidth=0.10, relheight=0.10)

    # Combobox Tipo ENTRADA
        self.cbx_tipo_entrada = ttk.Combobox(self.frame_2_ab1,values=tipo,
                                             font=('verdana 9 bold'))
        self.cbx_tipo_entrada.place(relx=0.65, rely=0.50, relwidth=0.20, relheight=0.10)

    # Combobox Tipo SAIDA
        self.cbx_tipo_saida = ttk.Combobox(self.frame_2_ab2,values=tipo,
                                             font=('verdana 9 bold'))
        self.cbx_tipo_saida.place(relx=0.65, rely=0.50, relwidth=0.20, relheight=0.10)

    # Label Data ENTRADA
        self.lb_data_entrada = Label(self.frame_2_ab1, text='data'.upper(),bg= self.cor_lightgray,
                                 font=('verdana 10 bold'))
        self.lb_data_entrada.place(relx=0.12, rely=0.65, relwidth=0.10, relheight=0.10)

    # Label Data SAIDA
        self.lb_data_saida = Label(self.frame_2_ab2, text='data'.upper(),
                                        font=('verdana 10 bold'))
        self.lb_data_saida.place(relx=0.12, rely=0.65, relwidth=0.10, relheight=0.10)

    # Entry Data ENTRADA
        self.entry_data_entrada = Entry(self.frame_2_ab1,font=('verdana 10 bold'))
        self.entry_data_entrada.place(relx=0.23, rely=0.65, relwidth=0.25, relheight=0.10)

    # Entry Data SAIDA
        self.entry_data_saida = Entry(self.frame_2_ab2,font=('verdana 10 bold'))
        self.entry_data_saida.place(relx=0.23, rely=0.65, relwidth=0.25, relheight=0.10)

    # Botão data inserir ENTRADA
        self.bt_data_inserir_entrada = Button(self.frame_2_ab1, text='calendário'.upper(),bg= self.cor_azul_02,
                         font=('verdana 10 bold'))
        self.bt_data_inserir_entrada.place(relx=0.55, rely=0.65, relwidth=0.30, relheight=0.10)

    # Botão data inserir SAIDA
        self.bt_data_inserir_saida = Button(self.frame_2_ab2, text='calendário'.upper(),
                         font=('verdana 10 bold'))
        self.bt_data_inserir_saida.place(relx=0.50, rely=0.65, relwidth=0.30, relheight=0.10)

    # Imagens dos Botoes
        self.img_bt_add = Image.open('img/add-user-icon.png')
        self.img_bt_add = self.img_bt_add.resize((43, 43))
        self.img_bt_add = ImageTk.PhotoImage(self.img_bt_add)
    # Imagen editar
        self.img_bt_edit = Image.open('img/edit-user-icon.png')
        self.img_bt_edit = self.img_bt_edit.resize((43, 43))
        self.img_bt_edit = ImageTk.PhotoImage(self.img_bt_edit)
    # Imagen Excluir
        self.img_bt_excluir = Image.open('img/remove-user-icon.png')
        self.img_bt_excluir = self.img_bt_excluir.resize((43, 43))
        self.img_bt_excluir = ImageTk.PhotoImage(self.img_bt_excluir)
    # Imagen Buscar
        self.img_bt_busca = Image.open('img/buscar.png')
        self.img_bt_busca = self.img_bt_busca.resize((43, 43))
        self.img_bt_busca = ImageTk.PhotoImage(self.img_bt_busca)

    # Botão adicionar ENTRADA
        self.img_BT_add = Button(self.frame_2_ab1,command=self.add_material_entrada ,image=self.img_bt_add, width=900,bg='#abdb25',
                               compound=CENTER, relief=RAISED, anchor=NW, font=('verdana 10 bold'))
        self.img_BT_add.place(relx=0.86, rely=0.20, relwidth=0.13, relheight=0.18)

    # Botão adicionar SAIDA
        self.img_BT_add_saida = Button(self.frame_2_ab2,command=self.add_material_saida ,image=self.img_bt_add, width=900,
                               compound=CENTER, relief=RAISED, anchor=NW, font=('verdana 10 bold'), bg='lightgray')
        self.img_BT_add_saida.place(relx=0.86, rely=0.20, relwidth=0.13, relheight=0.18)

    # Botão Alterar ENTRADA
        self.img_BT_edit = Button(self.frame_2_ab1,command=self.alterar_material_entrada ,image=self.img_bt_edit, width=900,
                                 compound=CENTER, relief=RAISED, anchor=NW, font=('verdana 10 bold'),bg='yellow')
        self.img_BT_edit.place(relx=0.86, rely=0.40, relwidth=0.13, relheight=0.18)

     # Botão Alterar SAIDA
        self.img_BT_edit_saida = Button(self.frame_2_ab2,command=self.alterar_material_saida,image=self.img_bt_edit, width=900,
                                 compound=CENTER, relief=RAISED, anchor=NW, font=('verdana 10 bold'), bg='lightgray')
        self.img_BT_edit_saida.place(relx=0.86, rely=0.40, relwidth=0.13, relheight=0.18)

    # Botão Excluir ENTRADA
        self.img_BT_excluir = Button(self.frame_2_ab1,command=self.deleta_material_entrada ,image=self.img_bt_excluir, width=900,
                              compound=CENTER, relief=RAISED, anchor=NW, font=('verdana 10 bold'), bg='red')
        self.img_BT_excluir.place(relx=0.86, rely=0.60, relwidth=0.13, relheight=0.18)

    # Botão Excluir SAIDA
        self.img_BT_excluir_saida = Button(self.frame_2_ab2,command=self.deleta_material_saida ,image=self.img_bt_excluir, width=900,
                              compound=CENTER, relief=RAISED, anchor=NW, font=('verdana 10 bold'), bg='lightgray')
        self.img_BT_excluir_saida.place(relx=0.86, rely=0.60, relwidth=0.13, relheight=0.18)

    # Botão Buscar ENTRADA
        self.img_BT_buscar = Button(self.frame_2_ab1,image=self.img_bt_busca, width=900,
                                 compound=CENTER, relief=RAISED, anchor=NW, font=('verdana 10 bold'), bg='blue')
        self.img_BT_buscar.place(relx=0.86, rely=0.80, relwidth=0.13, relheight=0.18)
        
    # Botão Buscar SAIDA
        self.img_BT_buscar_saida = Button(self.frame_2_ab2, image=self.img_bt_busca, width=900,
                                 compound=CENTER, relief=RAISED, anchor=NW, font=('verdana 10 bold'), bg='lightgray')
        self.img_BT_buscar_saida.place(relx=0.86, rely=0.80, relwidth=0.13, relheight=0.18)
    
    # Limpa Tela ENTRADA
        self.img_BT_limpaT = Button(self.frame_2_ab1,text='Limpa', width=900,command=self.limpa_tela_entrada,
                                 compound=CENTER, relief=RAISED, anchor=NW, font=('verdana 10 bold'), bg='lightgray')
        self.img_BT_limpaT.place(relx=0.50, rely=0.80, relwidth=0.13, relheight=0.18)

    # Limpa Tela SAIDA
        self.img_BT_limpaT_saida = Button(self.frame_2_ab2,text='Limpa', width=900,command=self.limpa_tela_saida,
                                 compound=CENTER, relief=RAISED, anchor=NW, font=('verdana 10 bold'), bg='lightgray')
        self.img_BT_limpaT_saida.place(relx=0.50, rely=0.80, relwidth=0.13, relheight=0.18)

# Tabela
    def lista_frame_4_entrada(self):
        self.lista_material_entrada = ttk.Treeview(self.frame_4_ab1,height=3,columns=('col1','col2','col3','col4','col5'))
        self.lista_material_entrada.heading('#0',text='')
        self.lista_material_entrada.heading('#1', text='COD')
        self.lista_material_entrada.heading('#2', text='MATERIAL')
        self.lista_material_entrada.heading('#3', text='QUANTIDADE')
        self.lista_material_entrada.heading('#4', text='TIPO')
        self.lista_material_entrada.heading('#5', text='DATA')
        self.lista_material_entrada.column('#0',width=1,anchor='center')
        self.lista_material_entrada.column('#1', width=40, anchor='center')
        self.lista_material_entrada.column('#2', width=230, anchor='center')
        self.lista_material_entrada.column('#3', width=100, anchor='center')
        self.lista_material_entrada.column('#4', width=100, anchor='center')
        self.lista_material_entrada.column('#5', width=100, anchor='center')
        self.lista_material_entrada.place(relx=0.01, rely=0.01, relwidth=0.96, relheight=0.96)

        self.scroolista_entrada = Scrollbar(self.frame_4_ab1,orient='vertical')
        self.lista_material_entrada.configure(yscroll=self.scroolista_entrada.set)
        self.scroolista_entrada.place(relx=0.97, rely=0.01, relwidth=0.02, relheight=0.96)
        
        self.lista_material_entrada.bind('<Double-1>',self.OnDoubleClick_entrada)


    def lista_frame_4_saida(self):
        self.lista_material_saida = ttk.Treeview(self.frame_4_ab2,height=3,columns=('col1','col2','col3','col4','col5'))
        self.lista_material_saida.heading('#0',text='')
        self.lista_material_saida.heading('#1', text='COD')
        self.lista_material_saida.heading('#2', text='MATERIAL')
        self.lista_material_saida.heading('#3', text='QUANTIDADE')
        self.lista_material_saida.heading('#4', text='TIPO')
        self.lista_material_saida.heading('#5', text='DATA')
        self.lista_material_saida.column('#0',width=1,anchor='center')
        self.lista_material_saida.column('#1', width=40, anchor='center')
        self.lista_material_saida.column('#2', width=230, anchor='center')
        self.lista_material_saida.column('#3', width=100, anchor='center')
        self.lista_material_saida.column('#4', width=100, anchor='center')
        self.lista_material_saida.column('#5', width=100, anchor='center')
        self.lista_material_saida.place(relx=0.01, rely=0.01, relwidth=0.96, relheight=0.96)

        self.scroolista_saida = Scrollbar(self.frame_4_ab1,orient='vertical')
        self.lista_material_saida.configure(yscroll=self.scroolista_saida.set)
        self.scroolista_saida.place(relx=0.97, rely=0.01, relwidth=0.02, relheight=0.96)
        
        self.lista_material_saida.bind('<Double-1>',self.OnDoubleClick_saida)


Application()
