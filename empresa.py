import tkinter as tk
from tkinter import messagebox

class Produto:
    def __init__(self, nome, codigo, preco, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        messagebox.showinfo("Sucesso", "Produto adicionado ao estoque.")

    def atualizar_quantidade(self, codigo, quantidade):
        for produto in self.produtos:
            if produto.codigo == codigo:
                produto.quantidade += quantidade
                messagebox.showinfo("Sucesso", "Quantidade atualizada!")
                return
        messagebox.showwarning("Aviso", "Produto não encontrado.")

# Instanciar objetos fora da classe
produto1 = Produto("Produto1", 1, 10.0, 20)
produto2 = Produto("Produto2", 2, 15.0, 15)

# Exemplo de uso
estoque = Estoque()
estoque.adicionar_produto(produto1)
estoque.adicionar_produto(produto2)
estoque.atualizar_quantidade(1, 5)
estoque.atualizar_quantidade(3, 10)  # Produto não existente

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == "admin" and password == "password":
        messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
    else:
        messagebox.showwarning("Aviso", "Credenciais inválidas.")

root = tk.Tk()

# Label de Usuário
username_label = tk.Label(root, text="Usuário:")
username_label.pack()

# Entrada de Usuário
username_entry = tk.Entry(root)
username_entry.pack()

# Label de Senha
password_label = tk.Label(root, text="Senha:")
password_label.pack()

# Entrada de Senha
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Botão de Login
login_button = tk.Button(root, text="Login", command=login)
login_button.pack()

root.mainloop()
