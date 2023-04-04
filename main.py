import threading
"""Threading
Não é possível para o programador saber qual será a ordem dos processos
"""

def faz1():
    x = 0
    while x < 10:
        print(' 1tarefa1')
        x += 1


def faz2():
    y = 0
    while y < 10:
        print(' 2tarefa2')
        y += 1


threading.Thread(target=faz2).start()
faz1()
