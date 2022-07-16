### Desafio 2


from turtle import Turtle

t = Turtle()

while True:
    lado = (input('\nF:(frente), T:(trás)?\n>'))
    
#-------------------------------------------------      
    if lado == 'F':
        
        pixel_lado = int(input('Quantos pixels devem ser percorridos?\n>'))

        angulo_valido = False
        while angulo_valido == False:

            angulo = input('\E:(esquerda), D:(direita), N:(não rotacionar)?\n>')
                              
            if angulo == 'D':
                pixel_angulo = int(input('Quantos pixels devem ser rotacionados?\n>'))
                t.right(pixel_angulo)
                t.forward(pixel_lado)
                angulo_valido = True
                
                            
            elif angulo == 'E':
                pixel_angulo = int(input('Quantos pixels devem ser rotacionados?\n>'))
                t.left(pixel_angulo)
                t.forward(pixel_lado)
                angulo_valido = True

            elif angulo =='N':
                t.forward(pixel_lado) 
                angulo_valido = True   

            else:
                print('\nOPS, DIGITE E para esquerda ou D para direita')
                                        
           
#--------------------------------------------------   
    if lado == 'T':
        
        pixel_lado = int(input('Quantos pixels devem ser percorridos?\n>'))

        angulo_valido = False
        while angulo_valido == False:
            angulo = input('\E:(esquerda), D:(direita), N:(não rotacionar)?\n>')
                        
            if angulo == 'D':                
                pixel_angulo = int(input('Quantos pixels devem ser rotacionados?\n>'))
                t.right(pixel_angulo)
                t.backward(pixel_lado)
                angulo_valido = True
                            
            elif angulo == 'E':
                pixel_angulo = int(input('Quantos pixels devem ser rotacionados?\n>'))
                t.left(pixel_angulo)
                t.backward(pixel_lado)
                angulo_valido = True

            elif angulo == 'N':
                t.backward(pixel_lado)
                angulo_valido = True

            else:
                print('\nOPS, DIGITE E para esquerda , D para direita ou N para não rotacionar')

    if lado not in ('T','F','N'):
        print('VALOR INVÁLIDO PRESS F:(frente), T:(trás)!\n')
        

    pergunta = input('Continuar Andando?\n>')
    if pergunta not in ('sim', 's', 'SIM', 'S'):
        break
            
    
             

    

 
 