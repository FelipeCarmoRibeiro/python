import tkinter as tk
from tkinter import messagebox

def enviar_convite():
    messagebox.showinfo("Convite Aceito!", "te vejo la! 🐱☕")

janela = tk.Tk()
janela.title("Convite para o café com a bia que eu amo tanto ☕🐱")
janela.geometry("600x300")
janela.configure(bg="#fce4ec")  

mensagem = """Oi, Bia! 🐱
Que tal tomar um café comigo no seasoncafe?
É uma cafeteria cheia de gatinhos fofos!
Vai ser divertido! Me avisa se quiser ir.
Ah o @ do insta deles: seasoncoffee.co😊"""

label = tk.Label(janela, text=mensagem, font=("Arial", 12), bg="#fce4ec", wraplength=350, justify="center")
label.pack(pady=30)

botao = tk.Button(janela, text="Aceitar Convite", font=("Arial", 12, "bold"), bg="#ff80ab", fg="white", command=enviar_convite)
botao.pack(pady=20)

janela.mainloop()
