import tkinter as tk
import random
import time

#criar a porra toda
#########################################
janela = tk.Tk()
janela.geometry('1300x300')
janela.resizable(False, False)
janela.title("")

#Código que roda quando eu quero
#########################################

s=""
current = ""
words = []
with open("palavras.txt", "r") as file:
    s = file.read()

for char in s:
    if char == "\n":
        words.append(current)
        current = ""
    else:
        current += char

s = ""
positions = []
leaderboard = ""

tamanhoFrase = 5
isPlaying = False
startTime = time.time()

def analise(submit):
    global tamanhoFrase
    global isPlaying
    global startTime
    global s
    global leaderboard
    global positions

    if not isPlaying and submit != "":
        startTime = time.time()
        isPlaying = True

    if isPlaying and "Palavras=" in submit and "!" in submit:
        tamanhoFrase = int(submit[9:-1])
        
        input.delete("1.0", tk.END)
        novaFrase()
        isPlaying = False
        return(0)

    if isPlaying and submit == s:
        totalTime = round(float(time.time()-startTime), 2)
        totalKeys = len(s)

        input.delete("1.0", tk.END)
        novaFrase()
        isPlaying = False
        
        positions.append([totalTime, totalKeys])
        positions.sort(key=lambda x: x[0])
        if len(positions) > 5:
            positions = positions[:5]
        leaderboard = ""
        for position in positions:
            leaderboard += str(position[0]) + "s - WPM:" + str(round(5/(position[0]/60),1)) + " - CPM:" + str(round(position[1]/(position[0]/60),1)) + "\n"
        temposRecente.config(text=leaderboard)
        return(1)

    return(0)

#funcoes tkinter
#########################################
def enviar():
    global isPlaying
    user_text = input.get("1.0", tk.END).strip()
    test = analise(user_text)
    if test == 1:
        time.sleep(0.5)
    janela.update()

def novaFrase(*args):
    global s 
    global isPlaying
    global tamanhoFrase
    isPlaying = False
    s = ""
    l = len(words)
    palavras = []

    for i in range(0, tamanhoFrase):
        r = random.randint(0, l-1)
        palavras.append(words[r])
    s = ' '.join(palavras)

    while len(s) > 60:
        maior = max(palavras, key=len)
        lenMaior = len(maior)
        better = [word for word in words if len(word) < lenMaior]
        lenBetter = len(better)
        palavras[palavras.index(maior)] = better[random.randint(0,lenBetter-1)]

        s = ' '.join(palavras)

    input.delete("1.0", tk.END)
    texto.config(text=s)

def rodar(*args):
    enviar()

def rodarTimer(tempo):
    global isPlaying
    tempo.after(1, rodarTimer, tempo)
    if isPlaying:
        tempo.config(text="tempo: " + str(round(float(time.time()-startTime), 2)))
        
#Detalhes, textos
#########################################
texto = tk.Label(janela, text=s, font=("Cascadia Code", 17), width=60,anchor="w", justify="left")
texto.grid(row=0, column=0, padx=10, pady=0)
texto.grid_propagate(False)
tempo = tk.Label(janela, text="tempo: 0:00", font=("Cascadia Code", 15))
tempo.grid(row=2, column=0, padx=10, pady=0)
tituloLB = tk.Label(janela, text="Top 5 tempos:", font=("Cascadia Code", 17), width=30, anchor="w")
tituloLB.grid(row=0, column=1 ,padx=30, pady=0)

temposRecente = tk.Label(janela, text=leaderboard, font=("Cascadia Code", 15), height=6,width=30, anchor="w", justify="left")
temposRecente.grid(row=1, column=1 ,padx=30)

#Botoes
#########################################
newOne = tk.Button(janela, text="Gerar novo",font=("Cascadia Code", 10) ,command=novaFrase, width=40, height=2)
newOne.grid(row=3, column=0, padx=10, pady=10)

#Caixas de input, output
#########################################
input = tk.Text(janela,font=("Cascadia Code", 17), height=1, width=60)
input.grid(row=1, column=0, padx=10, pady=10)
input.bind("<KeyRelease>", rodar)

#iniciar
#########################################
janela.title(words[random.randint(0, len(words)-1)])
novaFrase()
rodarTimer(tempo)
janela.mainloop()