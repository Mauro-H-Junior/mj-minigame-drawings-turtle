### Desafio 2


from turtle import Turtle

t = Turtle()

def frente_tras():
    resultado = int(input('Quantos pixels devem ser percorridos?\n>'))
    return resultado

def esquerda_direita_frente(tt):

    angulo_valido = False
    while angulo_valido == False:
        angulo = input('\E:(esquerda), D:(direita), N:(não rotacionar)?\n>')
        if angulo == 'D':
            rotacionar_direita_frente(tt)
            angulo_valido=True
           
        elif angulo == 'E':
            rotacionar_direita_frente(tt)
            angulo_valido=True
        elif angulo =='N':
            nao_rotacionar_frente(tt)
            angulo_valido=True
        else:
            print('\nOPS, DIGITE E para esquerda ou D para direita')

def esquerda_direita_tras(tt):
    angulo_valido = False
    while angulo_valido == False:
        angulo = input('\E:(esquerda), D:(direita), N:(não rotacionar)?\n>')
        if angulo == 'D':
            rotacionar_direita_tras(tt)
            angulo_valido=True
           
        elif angulo == 'E':
            rotacionar_esquerda_tras(tt)
            angulo_valido=True
        elif angulo =='N':
            nao_rotacionar_tras(tt)
            angulo_valido=True
        else:
            print('\nOPS, DIGITE E para esquerda ou D para direita')

def rotacionar_direita_frente(ttd):
    pixel_angulo = int(input('Quantos pixels devem ser rotacionados?\n>'))
    t.right(pixel_angulo)
    t.forward(pixel_lado)

def rotacionar_direita_tras(ttd):
    pixel_angulo = int(input('Quantos pixels devem ser rotacionados?\n>'))
    t.right(pixel_angulo)
    t.backward(pixel_lado)

def rotacionar_esquerda_frente(tte):
    pixel_angulo = int(input('Quantos pixels devem ser rotacionados?\n>'))
    t.left(pixel_angulo)
    t.forward(pixel_lado)

def rotacionar_esquerda_tras(tte):
    pixel_angulo = int(input('Quantos pixels devem ser rotacionados?\n>'))
    t.left(pixel_angulo)
    t.backward(pixel_lado)

def nao_rotacionar_frente(ttn):
    t.forward(pixel_lado)

def nao_rotacionar_tras(ttn):
    t.backward(pixel_lado)


while True:
    lado = (input('\nF:(frente), T:(trás)?\n>'))
    
#-------------------------------------------------      
    if lado == 'F':
        
        pixel_lado = frente_tras()

        esquerda_direita_frente(t)
          
#--------------------------------------------------   
    if lado == 'T':
        
        pixel_lado = frente_tras()

        esquerda_direita_tras(t)

    if lado not in ('T','F','N'):
        print('VALOR INVÁLIDO PRESS F:(frente), T:(trás)!\n')
        

    pergunta = input('Continuar Andando?\n>')
    if pergunta not in ('sim', 's', 'SIM', 'S'):
        break
            
    
             

    

 
 