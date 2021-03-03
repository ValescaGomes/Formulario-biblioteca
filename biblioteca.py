from tkinter import *

#Criando objeto 'raiz' de Tk()
root = Tk()

#Fornecendo geometria para o formulário
root.geometry("500x500")

#Fornecendo título para o formulário
root.title('Biblioteca Nacional')

# o codigo abaixo cria um 'Label' para o Formulário de Registro e usa o método place().
label_0 =Label(root,text="Biblioteca Nacional", width=20,font=("bold",20))
#O método de lugar no tkinter é o gerenciador de geometria usado para organizar os widgets colocando-os em uma posição específica
label_0.place(x=90,y=60)

# o codigo abaixo cria um 'Label' para Nome completo e usa o método place ().
label_1 =Label(root,text="Nome Completo", width=20,font=("bold",10))
label_1.place(x=80,y=130)

# o codigo abaixo aceitará o texto da string de entrada do usuário.
entry_1=Entry(root)
entry_1.place(x=240,y=130)

# o codigo abaixo cria um 'Label' para e-mail e usa o método place ().
label_3 =Label(root,text="Email", width=20,font=("bold",10))
label_3.place(x=68,y=180)

entry_3=Entry(root)
entry_3.place(x=240,y=180)

#o codigo abaixo cria um 'Label' para Sexo e usa o método place().
label_4 =Label(root,text="Sexo", width=20,font=("bold",10))
label_4.place(x=70,y=230)

#a variável 'var' mencionada aqui contém o valor inteiro, por deault 0
var=IntVar()

# o codigo abaixo cria um 'Radio button' e usa o método  place()
Radiobutton(root,text="Masculino",padx= 5, variable= var, value=1).place(x=235,y=230)
Radiobutton(root,text="Feminino",padx= 20, variable= var, value=2).place(x=290,y=230)

# o codigo abaixo cria um 'Label' para país e usa o método place().
label_5=Label(root,text="País",width=20,font=("bold",10))
label_5.place(x=70,y=280)

#isso cria uma lista de países disponíveis na lista suspensa.
list_of_country=[ 'Brasil' ,'Argentina' , 'Alemanha' ,'África' ,'Austria']

#a variável 'c' mencionada aqui contém o valor da string, por padrão
c=StringVar()
droplist=OptionMenu(root,c, *list_of_country)
droplist.config(width=15)
c.set('Escolha seu país')
droplist.place(x=240,y=280)

#isso cria o widget 'Label' para Idioma e usa o método place().
label_6=Label(root,text="Idioma",width=20,font=('bold',10))
label_6.place(x=75,y=330)

#a variável 'var1' mencionada aqui contém o valor inteiro, por padrão 0
var1=IntVar()
#isso cria o widget Checkbutton e usa o método place ().
Checkbutton(root,text="Inglês", variable=var1).place(x=230,y=330)

#a variável 'var2' mencionada aqui contém o valor inteiro, por padrão 0
var2=IntVar()
Checkbutton(root,text="Português Brasil", variable=var2).place(x=290,y=330)

#isso cria um botão para enviar os detalhes fornecidos pelo usuário
Button(root, text='Salvar' , width=20,bg="black",fg='white').place(x=180,y=380)

# executando o loop principal.
root.mainloop()