#Acacia Calegari
#114153997
#Lista02

import math 

#1- a) Funcao q retorna a media de 3 numeros inteiros
def mediade3(a,b,c):
    """dado 3 numeros inteiros retornar a media.int,
    int, int - float"""
    return(a+b+c)/3

#1- b) Funcao q retorna a diferenca do maior dos 3 numeros da mediade3 em relacao a media
def maiormedia3(a,b,c):
    """retorna o maior valor da media3 em relacao a media
    int, int, int - float"""
    return max(a,b,c), mediade3(a,b,c)

#1- c) Funcao q retorna a soma do menor dos 3 numeros com a media
def menorsomamedia(a,b,c):
    """ retorna a soma do menor dos 3 numeros com a media
    int, int , int -float"""
    return min(a,b,c) + mediade3(a,b,c)



#2- funcao q calcula o discriminante(delta) da equacao de segundo grau
def delta(a,b,c):
    """funcao q retorna o delta 
    int,int,int - int"""
    return (b**2 - (4 * a * c))
	
#2- a) funcao q calcula a primeira raiz real de uma equacao de segundo grau, e retorna a soma da raiz com o discriminante(delta)
def x1(a,b,c):
    """ funcao q soma o delta com a raiz real de uma eq de 2 grau e divide por 2*a(dois vezes a)
    int, int, int - float"""
    return (-b + math.sqrt (delta(a,b,c)) / (2*a))

#2- b) funcao q calcula a segunda raiz real de uma equacao de segundo grau, e retorna a subtracao da raiz com o discriminante(delta)
            
def x2(a,b,c):
    """ funcao q subtrai o delta com a raiz real de uma eq de 2 grau e divide por 2*a(dois vezes a)
    int, int, int - float"""
    return (-b - math.sqrt (delta(a,b,c)) / (2*a))



#3- a) funcao q calcula o numero de termos da soma de uma progressao aritmetica dados valores inical(a1), final(an) e razao(r)
def termos(a1, an, r):
    """ funcao q calcula o numero de termos de uma pa
    float,float,float - float"""
    return ((an-a1)/r)+1


#3- b)funcao q calcula a soma da pa dados valores inicial, final e razao
def somadapa(a1, an, r):
    """funcao q calcula a soma da pa
    float,float,float - float"""
    return ((a1+an)*termos(a1,an,r))/2


#4- funcao q define base(r), lateral(r,h) e total(r,h) para calcular a area de um cilindro reto
def base (r):
    """calcula a area da base do cilindro dado o raio(r)
    float - float"""
    return math.pi*r**2

def lateral(r,h):
    """calcula a area lateral do cilinddro dado o raio(r) e a altura(h)
    float,float - float"""
    return base(r)*h


def total(r,h):
    """calcula a area total do cilindro dado o raio(r),e a altura(h)
    float, float - float"""
    return lateral(r,h) + 2 * base(r)


#5- a) funcao q calcula hipotenusa de um triangulo retangulo dados os catetos
def hipotenusa(ca,cb):
    """calcula a hipotenusa dados catetos ca,cb
    float, float - float"""
    return math.sqrt(ca**2 + cb**2)

#5- b)funcao q calcula a distancia entre dois pontos num plano dadas coordenadas
def distancia(x1,y1,x2,y2):
    """calcula distancia entre 2 pontos dadas coordenadas
    float,float - float"""
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

#5- c)funcao q calcula o perimetro de um triangulo reto dados catetos definidos na questao 5-a)
def perimetro(c1,c2):
    """calcula perimetro do triangulo dados catetos, e usando a hipotenusa da questao a
    float,float - float"""
    return c1+c2+hipotenusa(c1,c2)

#5- d)funcao q calcula a soma do quadrado do seno com o quadrado do cosseno de um angulo
def quadradosenocos (a):
    """ funcao q recebe um angulo e calcula a soma do quadrado do seno e do cosseno
    int - int"""
    return math.sin (math.radians(a))**2 + math.cos (math.radians(a))**2

#5- e)funcao q calcula o comprimento do circulo
def comprimentocirculo (raio):
    """ funcao q calcula o comprimento do circulo
    float - float"""
    return 2 * math.pi * raio



#6- funcao q calcula a area de um setor circular dados raio e angulo. com argumento default para o angulo, de forma q se nenhum angulo for informado a funcao retorna a area do circulo inteiro
def setor(raio,angulo=360):
    """calcula area do setor circular
        float, int- float"""
    return (angulo/180)*((math.pi*raio**2)/2)


#7- a)funcao q calcula o maior numero de bobmbons com o dinheiro q tem, e o troco q recebe dados o dinheiro e o preco do bombom
def bombom(dim,preco):
    """calcula a maior quantidade de bombom de acordo com o preco e o dinheiro q se tem, e o valor de troco
    float,float - int,float"""
    return int(dim/preco),float(dim%preco)

#7- b)funcao q calcula imc, dados altura e o peso de uma pessoa
def imc(peso,alt):
    """calcula imc dados peso e alt
    float, float - float"""
    return peso/(alt**2)

#7- c)funcao q retorna um numero exato de carros para grupos de amigos, lembrando q em cada carro pode entrar até 5 pessoas
def carros(gnt):
    """ dado um numero de pessoas retorna a quantidade de carros
    int - int"""
    return math.ceil(gnt / 5)


#8- funcao que, dados o raio da pista e a distância que um atleta corre em uma pista circularel percorre, e retorna o número de voltas
def voltadoatleta(distancia,raio):
    """funcao q calcula o numero de voltas do atleta apos percorrer a distancia na pista circular usando a funcao comprimentocirculo
    float, float - float"""
    return distancia / comprimentocirculo(raio)


#9- funcao q calcula a quantidade maxima de bolos que se pode fazer dados os igredientes
def bolos (farinha,ovo,leite):
    """calcula a quantidade maxima de bolos dados os igredientes
    float, int, float - int"""
    return min(farinha//2, ovo//3, leite//5)
