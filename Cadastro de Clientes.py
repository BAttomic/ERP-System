# Este é um programa feito para ERP (MEI) em Python durante processos de estudos e aprendizagem. Sua comercializacao é proibida!
# Desenvolvido por Bernardo Cordeiro Motta em 2023. Contatos: (31) 98422-9488, bernardo.motta@ufv.br, @B_Attomic, Attomic#8792

from tkinter import *
from tkinter import ttk
import sqlite3

root=Tk() #Criacao da janela

class Funcs():

    def conecta_bd(self):
        self.CONEXAO=sqlite3.connect('clientes.db')
        self.cursor=self.CONEXAO.cursor()
        print("Conectado ao banco de dados!")
    
    def desconecta_bd(self):
        self.CONEXAO.close()
        print("Desconectado do banco de dados!")
    
    def cria_tabela(self):
        self.conecta_bd()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS clientes (
            NOME CHAR(60) NOT NULL,
            APELIDO text,
            CODIGO INTERGER PRIMARY KEY,
            CPF_CNPJ text,
            RG_IE text,
            TELEFONE1 CHAR(15),
            TELEFONE2 text,
            EMAIL text,
            UF text,
            CIDADE_MUNICIPIO text,
            BAIRRO_DISTRITO text,
            RUA text,
            NUMERO text,
            CEP text,
            OUTRAS_INFORMACOES text
        )""")
        self.CONEXAO.commit()
        self.desconecta_bd()
        
    def botao_novo_cliente(self): #Adiciona os clientes na lista
        if self.ENTRIES_['NOME'].get()=="" and self.ENTRIES_['CPF_CNPJ'].get()=="" and self.ENTRIES_['RG_IE'].get()=="":
            print("Preencha os campos de NOME, CPF_CNPJ e RG_IE!")
        else:
            self.conecta_bd()
            self.cursor.execute("""INSERT INTO clientes (NOME, APELIDO, CODIGO, CPF_CNPJ, RG_IE, TELEFONE1, TELEFONE2, EMAIL, UF, CIDADE_MUNICIPIO, BAIRRO_DISTRITO, RUA, NUMERO, CEP, OUTRAS_INFORMACOES) VALUES (:NOME, :APELIDO, :CODIGO, :CPF_CNPJ, :RG_IE, :TELEFONE1, :TELEFONE2, :EMAIL, :UF, :CIDADE_MUNICIPIO, :BAIRRO_DISTRITO, :RUA, :NUMERO, :CEP, :OUTRAS_INFORMACOES)""", {'NOME': self.ENTRIES_['NOME'].get(), 'APELIDO': self.ENTRIES_['APELIDO'].get(), 'CODIGO': self.ENTRIES_['CODIGO'].get(), 'CPF_CNPJ': self.ENTRIES_['CPF_CNPJ'].get(), 'RG_IE': self.ENTRIES_['RG_IE'].get(), 'TELEFONE1': self.ENTRIES_['TELEFONE1'].get(), 'TELEFONE2': self.ENTRIES_['TELEFONE2'].get(), 'EMAIL': self.ENTRIES_['EMAIL'].get(), 'UF': self.ENTRIES_['UF'].get(), 'CIDADE_MUNICIPIO': self.ENTRIES_['CIDADE_MUNICIPIO'].get(), 'BAIRRO_DISTRITO': self.ENTRIES_['BAIRRO_DISTRITO'].get(), 'RUA': self.ENTRIES_['RUA'].get(), 'NUMERO': self.ENTRIES_['NUMERO'].get(), 'CEP': self.ENTRIES_['CEP'].get(), 'OUTRAS_INFORMACOES': self.ENTRIES_['OUTRAS_INFORMACOES'].get()})
            print("Cliente %s adicionado com sucesso!" % self.ENTRIES_['NOME'].get())
            self.CONEXAO.commit()
            self.desconecta_bd()
            self.salvar_cliente_bd()
            self.botao_limpar()

    def salvar_cliente_bd(self): #Seleciona os clientes da lista
        self.LISTACLIENTES.delete(*self.LISTACLIENTES.get_children())
        self.conecta_bd()
        LISTA=self.cursor.execute("""SELECT CODIGO, NOME, APELIDO, CPF_CNPJ, RG_IE, TELEFONE1, TELEFONE2, EMAIL, UF, CIDADE_MUNICIPIO, BAIRRO_DISTRITO, RUA, NUMERO, CEP, OUTRAS_INFORMACOES FROM clientes ORDER BY NOME ASC""")
        for i in LISTA:
            self.LISTACLIENTES.insert("", END, values=i)
        self.desconecta_bd()
    
    def botao_limpar(self): #Limpa os campos de entrada 
        for nome,item in self.ENTRIES_.items():
            item.delete(0, END)
        print("Campos limpos com sucesso!")

    def botao_deletar(self):
        self.conecta_bd()
        self.cursor.execute("""DELETE FROM clientes WHERE CODIGO = ?""", (self.ENTRIES_['CODIGO'].get(),))
        self.CONEXAO.commit()
        print("Cliente %s deletado com sucesso!" % self.ENTRIES_['NOME'].get())
        self.desconecta_bd()
        self.salvar_cliente_bd()
        self.botao_limpar()

    def OnDoubleClick(self, event): #Seleciona os clientes da lista e devolve os dados para os campos de entrada
        self.botao_limpar()
        self.LISTACLIENTES.selection()
        
        for i in self.LISTACLIENTES.selection():
            c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15 = self.LISTACLIENTES.item(i, 'values')
            self.ENTRIES_['CODIGO'].insert(END, c1)
            self.ENTRIES_['NOME'].insert(END, c2)
            self.ENTRIES_['APELIDO'].insert(END, c3)
            self.ENTRIES_['CPF_CNPJ'].insert(END, c4)
            self.ENTRIES_['RG_IE'].insert(END, c5)
            self.ENTRIES_['TELEFONE1'].insert(END, c6)
            self.ENTRIES_['TELEFONE2'].insert(END, c7)
            self.ENTRIES_['EMAIL'].insert(END, c8)
            self.ENTRIES_['UF'].insert(END, c9)
            self.ENTRIES_['CIDADE_MUNICIPIO'].insert(END, c10)
            self.ENTRIES_['BAIRRO_DISTRITO'].insert(END, c11)
            self.ENTRIES_['RUA'].insert(END, c12)
            self.ENTRIES_['NUMERO'].insert(END, c13)
            self.ENTRIES_['CEP'].insert(END, c14)
            self.ENTRIES_['OUTRAS_INFORMACOES'].insert(END, c15)

class Software(Funcs):

    def __init__(self): #Inicializador
        self.root=root
        self.tela() #Chamada da funcao tela
        self.interface() #Chamada da funcao frames 
        self.cria_tabela() #Chamada da funcao cria_tabela
        self.salvar_cliente_bd() #Chamada da funcao salvar_cliente_bd
        root.mainloop()
    
    def tela(self): #Janela
        self.root.title("Cadastro de Clientes") #Titulo da Janela
        self.root.configure(background='#87CEFA') #Cor de fundo
        self.root.attributes('-fullscreen', True) #Tela cheia

    def interface(self): #Localizacao dos campos!

        self.POSICOES={
            #f_rx = Frame relx
            #f_ry = Frame rely
            #f_rw = Frame relwidth
            #f_rh = Frame relheight
            #l_rw = Label relwidth
            #e_rx = Entry relx
            #e_rw = Entry relwidth
            #width = Tamanho em pixels
            "CODIGO":             {"col":"c1",  "headings":"Cód",       "text": "Código",                   "f_rx": 0.020, "f_ry": 0.040, "f_rw": 0.100, "f_rh": 0.050, "l_rw": 0.350, "e_rx": 0.350, "e_rw": 0.650, "width": -30,  },
            "NOME":               {"col":"c2",  "headings":"Nome",      "text": "Nome",                     "f_rx": 0.140, "f_ry": 0.040, "f_rw": 0.570, "f_rh": 0.050, "l_rw": 0.050, "e_rx": 0.050, "e_rw": 0.950, "width": 230,  },
            "APELIDO":            {"col":"c3",  "headings":"Apelido",   "text": "Apelido",                  "f_rx": 0.730, "f_ry": 0.040, "f_rw": 0.250, "f_rh": 0.050, "l_rw": 0.140, "e_rx": 0.140, "e_rw": 0.860, "width": 50,   },
            "CPF_CNPJ":           {"col":"c4",  "headings":"CPF/CNPJ",  "text": "CPF ou\nCNPJ",             "f_rx": 0.020, "f_ry": 0.110, "f_rw": 0.470, "f_rh": 0.050, "l_rw": 0.080, "e_rx": 0.080, "e_rw": 0.920, "width": -25,  },
            "RG_IE":              {"col":"c5",  "headings":"RG/IE",     "text": "RG ou\nIE",                "f_rx": 0.510, "f_ry": 0.110, "f_rw": 0.470, "f_rh": 0.050, "l_rw": 0.060, "e_rx": 0.060, "e_rw": 0.940, "width": -25,  },
            "TELEFONE1":          {"col":"c6",  "headings":"Fone 1",    "text": "Telefone 1",               "f_rx": 0.020, "f_ry": 0.180, "f_rw": 0.225, "f_rh": 0.050, "l_rw": 0.200, "e_rx": 0.200, "e_rw": 0.800, "width": -5,   },
            "TELEFONE2":          {"col":"c7",  "headings":"Fone 2",    "text": "Telefone 2",               "f_rx": 0.265, "f_ry": 0.180, "f_rw": 0.225, "f_rh": 0.050, "l_rw": 0.200, "e_rx": 0.200, "e_rw": 0.800, "width": -5,   },
            "EMAIL":              {"col":"c8",  "headings":"Email",     "text": "Email",                    "f_rx": 0.510, "f_ry": 0.180, "f_rw": 0.470, "f_rh": 0.050, "l_rw": 0.070, "e_rx": 0.070, "e_rw": 0.930, "width": -100, },
            "UF":                 {"col":"c9",  "headings":"UF",        "text": "UF",                       "f_rx": 0.020, "f_ry": 0.250, "f_rw": 0.160, "f_rh": 0.050, "l_rw": 0.110, "e_rx": 0.110, "e_rw": 0.890, "width": -100, },
            "CIDADE_MUNICIPIO":   {"col":"c10", "headings":"Cidade",    "text": "Cidade ou\nMunicípio",     "f_rx": 0.200, "f_ry": 0.250, "f_rw": 0.380, "f_rh": 0.050, "l_rw": 0.130, "e_rx": 0.130, "e_rw": 0.870, "width": 10,   },
            "BAIRRO_DISTRITO":    {"col":"c11", "headings":"Bairro",    "text": "Bairro ou\nDistrito",      "f_rx": 0.600, "f_ry": 0.250, "f_rw": 0.380, "f_rh": 0.050, "l_rw": 0.100, "e_rx": 0.100, "e_rw": 0.900, "width": 10,   },
            "RUA":                {"col":"c12", "headings":"Rua",       "text": "Rua",                      "f_rx": 0.020, "f_ry": 0.320, "f_rw": 0.560, "f_rh": 0.050, "l_rw": 0.050, "e_rx": 0.050, "e_rw": 0.950, "width": 50,   },
            "NUMERO":             {"col":"c13", "headings":"Nº",        "text": "Nº",                       "f_rx": 0.600, "f_ry": 0.320, "f_rw": 0.130, "f_rh": 0.050, "l_rw": 0.130, "e_rx": 0.150, "e_rw": 0.850, "width": -100, },
            "CEP":                {"col":"c14", "headings":"CEP",       "text": "CEP",                      "f_rx": 0.750, "f_ry": 0.320, "f_rw": 0.230, "f_rh": 0.050, "l_rw": 0.100, "e_rx": 0.100, "e_rw": 0.900, "width": -100, },
            "OUTRAS_INFORMACOES": {"col":"c15", "headings":"Outras",    "text": "Outras ou\nInformações",   "f_rx": 0.020, "f_ry": 0.390, "f_rw": 0.960, "f_rh": 0.050, "l_rw": 0.060, "e_rx": 0.060, "e_rw": 0.940, "width": -100, },
        }

        #Dicionários vázios para armazenar os Frames, Labels, Entries e Botoes
        self.FRAMES_={}
        self.LABELS_={}
        self.ENTRIES_={}
        self.BOTAO_={}

        for nome, pos in self.POSICOES.items(): 
            #Criação dos Frames
            self.FRAMES_[nome]=Frame(self.root, border=4, highlightbackground='#00BFFF', highlightthickness=2, background='#FFFFFF')
            self.FRAMES_[nome].place(relx=pos["f_rx"], rely=pos["f_ry"], relwidth=pos["f_rw"], relheight=pos["f_rh"])

            #Criação dos Labels
            self.LABELS_[nome]=Label(self.FRAMES_[nome], text=pos["text"]+':', font=('Arial', 9, 'bold'), bg='#FFFFFF')
            self.LABELS_[nome].place(relx=0.00, rely=0.00, relwidth=pos["l_rw"], relheight=1.00)

            #Criação dos Entries
            self.ENTRIES_[nome]=Entry(self.FRAMES_[nome], font=('Arial', 10, 'bold'), bg='#FFFFFF')
            self.ENTRIES_[nome].place(relx=pos["e_rx"], rely=0.00, relwidth=pos["e_rw"], relheight=1.00)

        #Lista de Clientes
        self.FRAMES_LISTA_CLIENTES=Frame(self.root, border=4, highlightbackground='#00BFFF', highlightthickness=2, background='#FFFFFF')
        self.FRAMES_LISTA_CLIENTES.place(relx=0.020, rely=0.460, relwidth=0.960, relheight=0.320)
        
        self.LISTACLIENTES=ttk.Treeview(self.FRAMES_LISTA_CLIENTES, show="headings", columns=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "c11", "c12", "c13", "c14", "c15"))
        self.LISTACLIENTES.place(relx=0.00, rely=0.00, relwidth=0.99, relheight=1.00)
        
        for nome,pos in self.POSICOES.items():
            self.LISTACLIENTES.heading(pos["col"], text=pos["headings"], anchor=CENTER)
            self.LISTACLIENTES.column(pos["col"], width=pos["width"])
            
        #Scrollbar
        self.SCROLLLISTACLIENTES=Scrollbar(self.FRAMES_LISTA_CLIENTES, orient='vertical')
        self.SCROLLLISTACLIENTES.place(relx=0.99, rely=0.00, relwidth=0.01, relheight=1.00)
        self.LISTACLIENTES.configure(yscroll=self.SCROLLLISTACLIENTES.set)
        self.LISTACLIENTES.bind("<Double-1>", self.OnDoubleClick)

        #Botões
        BOTOES={
            "LIMPAR":     {"text": "LIMPAR\nCAMPOS",        "command": self.botao_limpar,       "b_rx": 0.0000, "b_rw": 0.2425},
            "SALVAR":     {"text": "SALVAR\nALTERAÇÕES",    "command": '',                      "b_rx": 0.2525, "b_rw": 0.2425},
            "DELETAR":    {"text": "DELETAR\nCLIENTE",      "command": self.botao_deletar,      "b_rx": 0.5050, "b_rw": 0.2425},
            "NOVO":       {"text": "NOVO\nCLIENTE",         "command": self.botao_novo_cliente, "b_rx": 0.7575, "b_rw": 0.2425},
        }

        self.FRAMES_BOTOES=Frame(self.root, border=4, highlightbackground='#00BFFF', highlightthickness=2, background='#FFFFFF')
        self.FRAMES_BOTOES.place(relx=0.020, rely=0.800, relwidth=0.960, relheight=0.160)

        for nome, pos in BOTOES.items():
            self.BOTAO_[nome]=Button(self.FRAMES_BOTOES, text=pos["text"], font=('Arial', 10, 'bold'), bg='#87CEFA', command=pos["command"])
            self.BOTAO_[nome].place(relx=pos["b_rx"], rely=0.00, relwidth=pos["b_rw"], relheight=1.00)

Software() #Chamada da classe