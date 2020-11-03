import os
import constantes
import preProcessamentoTextual as pre 
from processamentoComBD import BD 
from os import path 
from wordcloud import WordCloud 
from openpyxl import Workbook 


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

def processarSinaisSintomas():
    wb = Workbook() 
    ws0 = wb.active 
    ws0.title = 'TODAS' 
    ws1 = wb.create_sheet(title='ANAMNESE') 
    ws2 = wb.create_sheet(title='EVOLUCAO') 
    arq = constantes.PATH_RESULTADOS + 'sinais-sintomas.xlsx' 
    colecao = {} 
    tipoResposta = ['TODAS', 'ANAMNESE', 'EVOLUCAO'] 
    siglas = pre.carregarArquivoComoArray(constantes.ARQ_SINAIS_SINTOMAS) 
    for tipo in tipoResposta: 
        banco = BD(constantes.BD_SQL_RESPOSTAS)
        with banco:
            tabela = banco.listarRespostas(tipo) 
            for linha in tabela:
                if (linha[9]):
                    for sigla in siglas:
                        if sigla in linha[9]:
                            if sigla in colecao:
                                valor = colecao.get(sigla)
                                colecao[sigla] = valor + 1
                            else:
                                colecao[sigla] = 1
            for item in colecao:
                if tipoResposta.index(tipo) == 0:
                    ws0.append([item, colecao[item]]) 
                elif tipoResposta.index(tipo) == 1:
                    ws1.append([item, colecao[item]]) 
                elif tipoResposta.index(tipo) == 2:
                    ws2.append([item, colecao[item]]) 
            colecao.clear()
            wb.save(arq)
    print("Arquivo salvo: " + arq)