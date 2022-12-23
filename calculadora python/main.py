#importando o Tkinter
from tkinter import *
from tkinter import ttk

#Cores
cor1 = "#1e1f1e"
cor2 = "#feffff"
cor3 = "#38576b"
cor4 = "#ECEFF1"
cor5 = "#FFAB40"
cor6 = "#6500e8"

janela = Tk()
janela.title("Calculadora") # 340/235 = 520/318
janela.geometry("340x520") #Tamanho da tela --> LxA
janela.config(bg=cor1)

# Criando Frames
frame_tela = Frame(janela, width=340, height=120, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=340, height=400)
frame_corpo.grid(row=1, column=0)

todos_valores = ''

# Unir caracters
def entrar_valores(event):
    global todos_valores
    if event == 'C':
        todos_valores = ''    
        valor_texto.set(todos_valores)
    elif event == '=':
        valor = todos_valores 
        todos_valores = ''
        calcular(valor)
    else:
        todos_valores += str(event)
        valor_texto.set(todos_valores)
    # resultado = eval(todos_valores)
    #passando valor pra tela


#Função para calcular
def calcular(operacao):
    resultado = eval(operacao)
    print(resultado)
    valor_texto.set(resultado)
    entrar_valores(resultado)


#Criando Label
valor_texto = StringVar()
app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=3, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 26'), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)


# Criando Botões
b_1 = Button(frame_corpo,command = lambda: entrar_valores("C"), text="C", width=17, height=4, bg=cor4, border=0, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, command = lambda: entrar_valores("%") , text="%", width=8, height=4, bg=cor4, border=0, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=168, y=0)
b_3 = Button(frame_corpo, command = lambda: entrar_valores("/") , text="/", width=8, height=4, bg=cor5, border=0, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, fg=cor2)
b_3.place(x=254, y=0)

b_4 = Button(frame_corpo, command = lambda: entrar_valores("7") , text="7", width=8, height=4, bg=cor4, border=0, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=86)
b_5 = Button(frame_corpo, command = lambda: entrar_valores("8") , text="8", width=8, height=4, bg=cor4, border=0, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=86, y=86)
b_6 = Button(frame_corpo, command = lambda: entrar_valores("9") , text="9", width=8, height=4, bg=cor4, border=0, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=168, y=86)
b_7 = Button(frame_corpo, command = lambda: entrar_valores("*") , text="*", width=8, height=4, bg=cor5, border=0, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, fg=cor2)
b_7.place(x=254, y=86)

b_8 = Button(frame_corpo, command = lambda: entrar_valores("4") , text="4", width=8, height=4, bg=cor4, border=0, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=172)
b_9 = Button(frame_corpo, command = lambda: entrar_valores("5") , text="5", width=8, height=4, bg=cor4, border=0, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=86, y=172)
b_10 = Button(frame_corpo, command = lambda: entrar_valores("6") , text="6", width=8, height=4, bg=cor4, border=0, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=168, y=172)
b_11 = Button(frame_corpo, command = lambda: entrar_valores("-") , text="-", width=8, height=4, bg=cor5, border=0, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, fg=cor2)
b_11.place(x=254, y=172)

b_12 = Button(frame_corpo, command = lambda: entrar_valores("1") , text="1", width=8, height=4, bg=cor4, border=0, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=258)
b_13 = Button(frame_corpo, command = lambda: entrar_valores("2") , text="2", width=8, height=4, bg=cor4, border=0, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=86, y=258)
b_14 = Button(frame_corpo, command = lambda: entrar_valores("3") , text="3", width=8, height=4, bg=cor4, border=0, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=168, y=258)
b_15 = Button(frame_corpo, command = lambda: entrar_valores("+") , text="+", width=8, height=4, bg=cor5, border=0, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, fg=cor2)
b_15.place(x=254, y=258)

b_16 = Button(frame_corpo, command = lambda: entrar_valores("0") , text="0", width=17, height=4, bg=cor4, border=0, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=322)
b_17 = Button(frame_corpo, command = lambda: entrar_valores("."), text=".", width=8, height=4, bg=cor4, border=0, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=168, y=322)
b_18 = Button(frame_corpo, command = lambda: entrar_valores("="), text="=", width=8, height=4, bg=cor5, border=0, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, fg=cor2)
b_18.place(x=254, y=322)


entrar_valores('')


janela.mainloop() #Cria a execução do app 