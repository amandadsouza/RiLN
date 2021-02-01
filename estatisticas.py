# coding: latin-1
from processamentoComBD import BD
import constantes
import processamentoTextual as pText 
import preProcessamentoTextual as pre

if __name__ == "__main__":
    banco = BD(constantes.BD_SQL_RESPOSTAS)
    with banco:
        #banco.trataStopWords('N')
        #banco.separaStopWords()
        #banco.trataNgrams() - a definir
        #banco.countUniGramForArq()
        #banco.countCIDForArq()
        #banco.countCIDForBD()
        #banco.countSiglaForTxt()

        # pText.processarUniGramas() 
        #pText.processaBigramas()
        #pText.processaTrigramas() 
        #banco.exportarBancoDeDados()

        # pText.gerarNuvemDePalavras('texto.txt', 'stop.png')
        # pText.gerarNuvemDePalavras(constantes.PATH_RESULTADOS + 'stopWords-ParaNuvem-Todas.txt', 'stopWords-ParaNuvem-Todas.png')
        # pText.gerarNuvemDePalavras(constantes.PATH_RESULTADOS + 'stopWords-ParaNuvem-Anamnese.txt', 'stopWords-ParaNuvem-Anamnese.png')
        # pText.gerarNuvemDePalavras(constantes.PATH_RESULTADOS + 'stopWords-ParaNuvem-Evolucao.txt', 'stopWords-ParaNuvem-Evolucao.png')

        # pText.processarSinaisSintomas() 
        # pText.gerarNuvemDePalavras(constantes.PATH_RESULTADOS + 'sinaisSintomas-ParaNuvem-Todas.txt', 'sinaisSintomas-ParaNuvem-Todas.png')
        # pText.gerarNuvemDePalavras(constantes.PATH_RESULTADOS + 'sinaisSintomas-ParaNuvem-Anamnese.txt', 'sinaisSintomas-ParaNuvem-Anamnese.png')
        # pText.gerarNuvemDePalavras(constantes.PATH_RESULTADOS + 'sinaisSintomas-ParaNuvem-Evolucao.txt', 'sinaisSintomas-ParaNuvem-Evolucao.png')

        #pText.processarUniGramas() 
        #pText.processarTerminologia(constantes.ARQ_TERMINOLOGIAS_AFIRMATIVAS, "Terminologias-Afirmativas.xlsx")
        #pText.processarTerminologia(constantes.ARQ_TERMINOLOGIAS_NEGATIVAS, "Terminologias-Negativas.xlsx")

        # pText.processarTerminologiaComNGramas(constantes.ARQ_TERMINOLOGIAS_AFIRMATIVAS, "Terminologias-Afirmativas-nGram-5.xlsx", 5)
        # pText.processarTerminologiaComNGramas(constantes.ARQ_TERMINOLOGIAS_NEGATIVAS, "Terminologias-Negativas-nGram-5.xlsx", 5)
        
        # dicionario = pText.carregaDicionarioComMinimoDeItens(constantes.PATH_RESULTADOS+"bigramas-dict-Anamnese.pickle", 10)
        # pText.gerarNuvemDePalavrasPorDicionario(dicionario, "bigramas-dict-Anamnese.png") 
        # dicionario = pText.carregaDicionarioComMinimoDeItens(constantes.PATH_RESULTADOS+"bigramas-dict-Evolucao.pickle", 10)
        # pText.gerarNuvemDePalavrasPorDicionario(dicionario, "bigramas-dict-Evolucao.png") 

        # dicionario = pText.carregaDicionarioComMinimoDeItens(constantes.PATH_RESULTADOS+"trigramas-dict-Anamnese.pickle", 10)
        # pText.gerarNuvemDePalavrasPorDicionario(dicionario, "trigramas-dict-Anamnese.png") 
        # dicionario = pText.carregaDicionarioComMinimoDeItens(constantes.PATH_RESULTADOS+"trigramas-dict-Evolucao.pickle", 10)
        # pText.gerarNuvemDePalavrasPorDicionario(dicionario, "trigramas-dict-Evolucao.png") 

        # pText.processarSinaisSintomasPorTermosProximos(4)

        # pText.processarTerminologia(constantes.PATH_LISTAS + "Term-Diag-Jargao-para-Processamento.txt", "Term-Diag-Jargao-para-Processamento.xlsx")
        # pText.processarTerminologia(constantes.PATH_LISTAS + "Term-Diag-CID-para-Processamento.txt", "Term-Diag-CID-para-Processamento.xlsx") 

        # pText.processarTerminologia(constantes.PATH_LISTAS + "Diagnostico-final-para-processamento.txt", "Diagnostico-final-para-processamento.xlsx") 
        # dicionario = pText.carregaDicionarioComMinimoDeItens(constantes.PATH_RESULTADOS+"Diagnostico-final-para-processamento.xlsx-todos.pickle", 5)
        # pText.gerarNuvemDePalavrasPorDicionario(dicionario, "Diagnostico-final-para-processamento-todos.png") 
        
        