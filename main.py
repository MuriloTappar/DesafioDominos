import cv2
import numpy as np
from matplotlib import pyplot as plt
from sys import argv
from tkinter import *
from tkinter import filedialog
# cor usada para pintar
# carregar imagem na escala cinza
def carregar_imagem(caminho):
    return cv2.imread(caminho, 0);


# pausa execucao para mostrar as imagens
def bloquear_execucao():
    cv2.waitKey();
    cv2.destroyAllWindows();

# mostra imagem na tela
def mostrar_imagem(nome, img):
    cv2.imshow(nome, img);

# pega os 4 vizinhos de uma coordenada
def vizinhos(img, y, x):
    vizinhos = [];
    if (y + 1 < len(img)):
        vizinhos.append((y + 1, x));
    if (y - 1 >= 0):
        vizinhos.append((y - 1, x));
    if (x + 1 < len(img[y])):
        vizinhos.append((y, x + 1));
    if (x - 1 >= 0):
        vizinhos.append((y, x - 1));
    return vizinhos;

# busca em largura na imagem
def bfs(img, ponto, pintado):#busca em largura que vai marcando os pixels do objeto
    y, x = ponto
    img[y][x] = pintado
    fila = [ponto];
    while fila:
        y, x = fila.pop()
        for vizinho in vizinhos(img, y, x):
            y_v, x_v = vizinho;
            cor = img[y_v][x_v];
            if (cor > 0 and cor != pintado):
                img[y_v][x_v] = pintado;
                fila.append(vizinho);

#pega o valor total de circulos que estão no dominó e o valor total de peças que estão em cima e em baixo
def circulos (img,img2):

    cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 5,
                               param1=118, param2=8, minRadius=0, maxRadius=7)#paramentos de tamanho do raio / localizador de circulo

    circles = np.uint16(np.around(circles))#contador de circulos
#Função HoughCircles serve para verificar se é um circulo aplicando uma transformada de Houngh
    total = circles.shape
    print('Dominó de Circulos')
    print('Valor Total:',total[1])

    pintado = 5
    cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)


    for y in range(50, int(len(img))):
        for x in range(50, len(img[y])):
            cor = img[y][x]
            if cor == 255 and cor != pintado:
                circles2 = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 5,
                                           param1=118, param2=8, minRadius=0, maxRadius=7)
                circles2 = np.uint16(np.around(circles2))
                bfs(img, (y, x), pintado)
                pintado += 5
    total2 = circles2.shape
    print('Quantidade de objetos na parte Inferior:', total2[1])

    pintado = 5
    cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    for y in range(125, len(img2)):
        for x in range(125, len(img2[y])):
            cor = img2[y][x]
            if cor == 255 and cor != pintado:
                circles3 = cv2.HoughCircles(img2, cv2.HOUGH_GRADIENT, 1, 5,
                                            param1=118, param2=8, minRadius=0, maxRadius=7)
                circles3 = np.uint16(np.around(circles3))
                bfs(img2, (y, x), pintado)
                pintado += 5
    total3 = circles3.shape
    print('Quantidade de objetos na parte Superior:', total3[1])

    # Explicação de transformada de Hough
    # A Transformada de Hough é um método
    # padrão para detecção de formas que são
    # facilmente parametrizadas(linhas, círculos, elipses, etc.)
    # em imagens digitalizadas.

    # A idéia é aplicar na imagem uma
    # transformação tal que todos os
    # pontos pertencentes a
    # uma mesma curva sejam mapeados num
    # único ponto de um novo espaço de
    # parametrização da curva procurada.

def quadrados(img,img2):
    qimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    squires = np.uint16(np.around(squires))
    print('Dominó de Quadrados')
    print('Valor Total:')

#função que verifica se o objeto analisado tem angulos de 90º
def angle_cos(p0, p1, p2):
    d1, d2 = (p0-p1).astype('float'), (p2-p1).astype('float')
    return abs( np.dot(d1, d2) / np.sqrt( np.dot(d1, d1)*np.dot(d2, d2) ) )

def teste(img):
    ret, imgT = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)
    ret, imgT2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)
    i = 1 #se tu quiser outro do 1 ao 3 q são circulos altera pra 1, em caso queira ver os quadrados bota qualquer outro valor(domino4.png em diante)
    if (i == 1):
     circulos(imgT,imgT2)

    else:
     quadrados(imgT,imgT2)

if __name__ == '__main__':
    if (len(argv) == 1):
        print('Passe o caminho da imagem a ser carregada.');
    #caminho_arquivo = 'C:\\Users\Murilo Tappar\PycharmProjects\pythonProject\\Domino3.png'
    Tk().withdraw()
    caminho_arquivo = filedialog.askopenfilename()
    img = carregar_imagem(caminho_arquivo)
    ret, imgT = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)
    teste(img)
    mostrar_imagem('original-binaria', imgT)


    bloquear_execucao();
