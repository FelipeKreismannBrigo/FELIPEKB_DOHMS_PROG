import tkinter as tk

calculo=str()

def inserir_texto(x):
   
    global calculo

    calculo=calculo+x
    texto.delete(1.0,"end")
    texto.insert(1.0,calculo)
    

def avaliar():
    
    global calculo
    
    a=str(eval(texto.get(1.0,"end")))
    calculo=str()
    inserir_texto(a)

def apagar():

    global calculo
    
    calculo=str()
    texto.delete(1.0,"end")

janela = tk.Tk()

#janela.geometry("400x400")

texto = tk.Text(janela, height=4, width=19, font=("Arial", 24))
texto.grid(columnspan=4)

botao1 = tk.Button(janela, text="1", command=lambda:inserir_texto("1"), width=13, height=4, font=("Arial", 12))
botao1.grid(column=1, row=1)
botao2 = tk.Button(janela, text="2", command=lambda:inserir_texto("2"), width=13, height=4, font=("Arial", 12))
botao2.grid(column=2, row=1)
botao3 = tk.Button(janela, text="3", command=lambda:inserir_texto("3"), width=13, height=4, font=("Arial", 12))
botao3.grid(column=3, row=1)
botao4 = tk.Button(janela, text="4", command=lambda:inserir_texto("4"), width=13, height=4, font=("Arial", 12))
botao4.grid(column=1, row=2)
botao5 = tk.Button(janela, text="5", command=lambda:inserir_texto("5"), width=13, height=4, font=("Arial", 12))
botao5.grid(column=2, row=2)
botao6 = tk.Button(janela, text="6", command=lambda:inserir_texto("6"), width=13, height=4, font=("Arial", 12))
botao6.grid(column=3, row=2)
botao7 = tk.Button(janela, text="7", command=lambda:inserir_texto("7"), width=13, height=4, font=("Arial", 12))
botao7.grid(column=1, row=3)
botao8 = tk.Button(janela, text="8", command=lambda:inserir_texto("8"), width=13, height=4, font=("Arial", 12))
botao8.grid(column=2, row=3)
botao9 = tk.Button(janela, text="9", command=lambda:inserir_texto("9"), width=13, height=4, font=("Arial", 12))
botao9.grid(column=3, row=3)
botao10 = tk.Button(janela, text="0", command=lambda:inserir_texto("0"), width=13, height=4, font=("Arial", 12))
botao10.grid(column=2, row=4)
botao11 = tk.Button(janela, text=")", command=lambda:inserir_texto(")"), height=4, width=13, font=("Arial",12)) #lambda 
botao11.grid(column=3, row=4)
botao12 = tk.Button(janela, text="(", command=lambda:inserir_texto("("), height=4, width=13, font=("Arial",12)) #lambda 
botao12.grid(column=1, row=4)
botao13_mais = tk.Button(janela, text="+", command=lambda:inserir_texto("+"), width=13, height=4, font=("Arial", 12))
botao13_mais.grid(column=4, row=1)
botao14_menos = tk.Button(janela, text="-", command=lambda:inserir_texto("-"), width=13, height=4, font=("Arial", 12))
botao14_menos.grid(column=4, row=2)
botao15_mult = tk.Button(janela, text="*", command=lambda:inserir_texto("*"), width=13, height=4, font=("Arial", 12))
botao15_mult.grid(column=4, row=3)
botao15_div = tk.Button(janela, text="/", command=lambda:inserir_texto("/"), width=13, height=4, font=("Arial", 12))
botao15_div.grid(column=4, row=4)
botao16_igual = tk.Button(janela, text="=", command=lambda:avaliar(), width=27, height=4, font=("Arial", 12))
botao16_igual.grid(column=1, row=5, columnspan=2)
botao16_C = tk.Button(janela, text="C", command=lambda:apagar(), width=27, height=4, font=("Arial", 12))
botao16_C.grid(column=3, row=5, columnspan=2)

janela.mainloop()