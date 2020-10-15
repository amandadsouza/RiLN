import os
import constantes
from os import path
from wordcloud import WordCloud
from processamentoComBD import BD

def repeteString(texto, n):
    """ Repete uma string n vezes e retorna sua concatenacao em nova string

    Args:
        texto (str): texto a ser repetido
        n (int): numero de vezes a ser repetida

    Returns:
        str: nova string com o numero de repeticao
    """    
    return ' '.join([texto for i in range(n)])

def gravarStringEmArquivo(texto, nomeArq):
    """ Grava variavel string em arquivo texto

    Args:
        texto (str): string a ser gravada em arquivo 
        nomeArq (str): nome do arquivo com path
    """    
    with open(nomeArq, 'w', encoding="utf-8") as text_file:
        text_file.write(texto)

def gerarNuvemDePalavras(nomeArq, nomePng):
    """ Gera imagem com nuvem de palavras baseado em arquivo texto 
        Deve ser chamada depois do metodo separaStopWords() que gera o arquivo texto

    Args:
        nomeArq (str): Nome completo do arquivo (com path)
        nomePng (str): Nome do arquivo a ser salvo (sem path)
    """
    # get data directory (using getcwd() is needed to support running example in generated IPython notebook)
    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

    # Read the whole text.
    text = open(path.join(d, nomeArq)).read()

    # Generate a word cloud image
    wordcloud = WordCloud(width=1600, height=800, background_color="white", repeat=False, collocations=False).generate(text)
    wordcloud.to_file(constantes.PATH_RESULTADOS + nomePng)
    # Display the generated image:
    # the matplotlib way:
    import matplotlib.pyplot as plt
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")

    # lower max_font_size
    # wordcloud = WordCloud(max_font_size=40).generate(text)
    # plt.figure()
    # plt.imshow(wordcloud, interpolation="bilinear")
    # plt.axis("off")
    # plt.show()

def gerarListaTermosRepetidos():
    """ Percorre o banco de dados e gera uma lista de termos repetidos
        Os termos unicos serao aqueles com apenas uma ocorrencia 
    """    
    banco = BD(constantes.BD_SQL_RESPOSTAS)
    with banco:
        tipoResposta = ['TODAS', 'ANAMNESE', 'EVOLUCAO']
        for tipo in tipoResposta:
            tabela = banco.listarRespostas(tipo)
            for linha in tabela:



