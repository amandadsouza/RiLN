# coding: latin-1
from processamentoComBD import BD
import constantes
import processamentoTextual as pText 
import preProcessamentoTextual as pre

if __name__ == "__main__":
    banco = BD(constantes.BD_SQL_RESPOSTAS)
    with banco:

        # Stop Words
        # pre.gerarListaEmArquivoDeStopWords()
        # pText.processarTerminologia(constantes.PATH_LISTAS + 'ListaStopWords.txt', "Stop-Words.xlsx")

        # banco.trataStopWords('N')
        # banco.separaStopWords()
        # dicionario = pText.carregaDicionarioComMinimoDeItens(constantes.PATH_RESULTADOS+"SWords-todos.pickle", 10)
        # pText.gerarNuvemDePalavrasPorDicionario(dicionario, "SWords-todos.png") 
        # dicionario = pText.carregaDicionarioComMinimoDeItens(constantes.PATH_RESULTADOS+"SWords-anamnese.pickle", 10)
        # pText.gerarNuvemDePalavrasPorDicionario(dicionario, "SWords-anamnese.png") 
        # dicionario = pText.carregaDicionarioComMinimoDeItens(constantes.PATH_RESULTADOS+"SWords-evolucao.pickle", 10)
        # pText.gerarNuvemDePalavrasPorDicionario(dicionario, "SWords-evolucao.png") 

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

        # Termos afirmativos
        # pText.processarTerminologia(constantes.ARQ_TERMINOLOGIAS_AFIRMATIVAS, "Terminologias-Afirmativas.xlsx")
        # dicionario = pText.carregaDicionarioComMinimoDeItens(constantes.PATH_RESULTADOS+"Terminologias-Afirmativas.xlsx-todos.pickle", 10)
        # pText.gerarNuvemDePalavrasPorDicionario(dicionario, "Terminologias-Afirmativas.xlsx-todos.png") 
        # dicionario = pText.carregaDicionarioComMinimoDeItens(constantes.PATH_RESULTADOS+"Terminologias-Afirmativas.xlsx-anamnese.pickle", 10)
        # pText.gerarNuvemDePalavrasPorDicionario(dicionario, "Terminologias-Afirmativas.xlsx-anamnese.png") 
        # dicionario = pText.carregaDicionarioComMinimoDeItens(constantes.PATH_RESULTADOS+"Terminologias-Afirmativas.xlsx-evolucao.pickle", 10)
        # pText.gerarNuvemDePalavrasPorDicionario(dicionario, "Terminologias-Afirmativas.xlsx-evolucao.png") 

        # Termos negativos 
        # pText.processarTerminologia(constantes.ARQ_TERMINOLOGIAS_NEGATIVAS, "Terminologias-Negativas-v2.xlsx")
        # dicionario = pText.carregaDicionarioComMinimoDeItens(constantes.PATH_RESULTADOS+"Terminologias-Negativas-v2.xlsx-todos.pickle", 10)
        # pText.gerarNuvemDePalavrasPorDicionario(dicionario, "Terminologias-Negativas-v2-todos.png") 
        # dicionario = pText.carregaDicionarioComMinimoDeItens(constantes.PATH_RESULTADOS+"Terminologias-Negativas-v2.xlsx-anamnese.pickle", 10)
        # pText.gerarNuvemDePalavrasPorDicionario(dicionario, "Terminologias-Negativas-v2-anamnese.png") 
        # dicionario = pText.carregaDicionarioComMinimoDeItens(constantes.PATH_RESULTADOS+"Terminologias-Negativas-v2.xlsx-evolucao.pickle", 10)
        # pText.gerarNuvemDePalavrasPorDicionario(dicionario, "Terminologias-Negativas-v2-evolucao.png") 
   
        # pText.processarTerminologiaComNGramas(constantes.ARQ_TERMINOLOGIAS_NEGATIVAS, "Terminologias-Negativas-nGram-5-v2.xlsx", 5)
        # pText.processarTerminologiaComNGramas(constantes.ARQ_TERMINOLOGIAS_AFIRMATIVAS, "Terminologias-Afirmativas-nGram-5.xlsx", 5)

        # Bigramas 
        # dicionario = pText.carregaDicionarioComMinimoDeItens(constantes.PATH_RESULTADOS+"bigramas-dict-Anamnese.pickle", 10)
        # pText.gerarNuvemDePalavrasPorDicionario(dicionario, "bigramas-dict-Anamnese.png") 
        # dicionario = pText.carregaDicionarioComMinimoDeItens(constantes.PATH_RESULTADOS+"bigramas-dict-Evolucao.pickle", 10)
        # pText.gerarNuvemDePalavrasPorDicionario(dicionario, "bigramas-dict-Evolucao.png") 

        # Trigramas 
        # dicionario = pText.carregaDicionarioComMinimoDeItens(constantes.PATH_RESULTADOS+"trigramas-dict-Anamnese.pickle", 10)
        # pText.gerarNuvemDePalavrasPorDicionario(dicionario, "trigramas-dict-Anamnese.png") 
        # dicionario = pText.carregaDicionarioComMinimoDeItens(constantes.PATH_RESULTADOS+"trigramas-dict-Evolucao.pickle", 10)
        # pText.gerarNuvemDePalavrasPorDicionario(dicionario, "trigramas-dict-Evolucao.png") 

        # pText.processarSinaisSintomasPorTermosProximos(4)
        
        # Jargao
        # pText.processarTerminologia(constantes.PATH_LISTAS + "Term-Diag-Jargao-para-Processamento.txt", "Term-Diag-Jargao-para-Processamento.xlsx")
        # pText.processarTerminologia(constantes.PATH_LISTAS + "Term-Diag-CID-para-Processamento.txt", "Term-Diag-CID-para-Processamento.xlsx") 

        # Diagnostico
        # pText.processarTerminologia(constantes.PATH_LISTAS + "Diagnostico-final-para-processamento-final-v2.txt", "Diagnostico-final-para-processamento-final-v2.xlsx") 
        # dicionario = pText.carregaDicionarioComMinimoDeItens(constantes.PATH_RESULTADOS+"Diagnostico-final-para-processamento-final-v2.xlsx-todos.pickle", 10)
        # pText.gerarNuvemDePalavrasPorDicionario(dicionario, "Diagnostico-final-para-processamento-final-v2-todos.png") 
        # dicionario = pText.carregaDicionarioComMinimoDeItens(constantes.PATH_RESULTADOS+"Diagnostico-final-para-processamento-final-v2.xlsx-anamnese.pickle", 10)
        # pText.gerarNuvemDePalavrasPorDicionario(dicionario, "Diagnostico-final-para-processamento-final-v2-anamnese.png") 
        # dicionario = pText.carregaDicionarioComMinimoDeItens(constantes.PATH_RESULTADOS+"Diagnostico-final-para-processamento-final-v2.xlsx-evolucao.pickle", 10)
        # pText.gerarNuvemDePalavrasPorDicionario(dicionario, "Diagnostico-final-para-processamento-final-v2-evolucao.png") 

        # Siglas 
        # pText.processarTerminologia(constantes.ARQ_SIGLAS, "Siglas-Abrev.xlsx")
        # dicionario = pText.carregaDicionarioComMinimoDeItens(constantes.PATH_RESULTADOS+"Siglas-Abrev.xlsx-todos.pickle", 10)
        # pText.gerarNuvemDePalavrasPorDicionario(dicionario, "Siglas-Abrev.xlsx-todos.png") 
        # dicionario = pText.carregaDicionarioComMinimoDeItens(constantes.PATH_RESULTADOS+"Siglas-Abrev.xlsx-anamnese.pickle", 10)
        # pText.gerarNuvemDePalavrasPorDicionario(dicionario, "Siglas-Abrev.xlsx-anamnese.png") 
        # dicionario = pText.carregaDicionarioComMinimoDeItens(constantes.PATH_RESULTADOS+"Siglas-Abrev.xlsx-evolucao.pickle", 10)
        # pText.gerarNuvemDePalavrasPorDicionario(dicionario, "Siglas-Abrev.xlsx-evolucao.png") 

        # Sinais e sintomas
        # pText.processarTerminologia(constantes.ARQ_SINAIS_SINTOMAS, "terminologia_Sinais_Sintomas_FINAL.xlsx")
        # dicionario = pText.carregaDicionarioComMinimoDeItens(constantes.PATH_RESULTADOS+"terminologia_Sinais_Sintomas_FINAL.xlsx-todos.pickle", 10)
        # pText.gerarNuvemDePalavrasPorDicionario(dicionario, "terminologia_Sinais_Sintomas_FINAL.xlsx.png") 
        # dicionario = pText.carregaDicionarioComMinimoDeItens(constantes.PATH_RESULTADOS+"terminologia_Sinais_Sintomas_FINAL.xlsx-anamnese.pickle", 10)
        # pText.gerarNuvemDePalavrasPorDicionario(dicionario, "terminologia_Sinais_Sintomas_FINAL.xlsx-anamnese.png") 
        # dicionario = pText.carregaDicionarioComMinimoDeItens(constantes.PATH_RESULTADOS+"terminologia_Sinais_Sintomas_FINAL.xlsx-evolucao.pickle", 10)
        # pText.gerarNuvemDePalavrasPorDicionario(dicionario, "terminologia_Sinais_Sintomas_FINAL.xlsx-evolucao.png") 

        # Procedimentos
        # pText.processarTerminologia(constantes.PATH_LISTAS + "Procedimentos.txt", "Procedimentos.xlsx")
        # dicionario = pText.carregaDicionarioComMinimoDeItens(constantes.PATH_RESULTADOS+"Procedimentos.xlsx-todos.pickle", 2)
        # pText.gerarNuvemDePalavrasPorDicionario(dicionario, "Procedimentos.xlsx.png") 
        # dicionario = pText.carregaDicionarioComMinimoDeItens(constantes.PATH_RESULTADOS+"Procedimentos.xlsx-anamnese.pickle", 2)
        # pText.gerarNuvemDePalavrasPorDicionario(dicionario, "Procedimentos.xlsx-anamnese.png") 
        # dicionario = pText.carregaDicionarioComMinimoDeItens(constantes.PATH_RESULTADOS+"Procedimentos.xlsx-evolucao.pickle", 2)
        # pText.gerarNuvemDePalavrasPorDicionario(dicionario, "Procedimentos.xlsx-evolucao.png") 

        # CID
        # pText.processarTerminologia(constantes.ARQ_CID, "CID.xlsx")
        # dicionario = pText.carregaDicionarioComMinimoDeItens(constantes.PATH_RESULTADOS+"CID.xlsx-todos.pickle", 2)
        # pText.gerarNuvemDePalavrasPorDicionario(dicionario, "CID.xlsx.png") 
        # dicionario = pText.carregaDicionarioComMinimoDeItens(constantes.PATH_RESULTADOS+"CID.xlsx-anamnese.pickle", 2)
        # pText.gerarNuvemDePalavrasPorDicionario(dicionario, "CID.xlsx-anamnese.png") 
        # dicionario = pText.carregaDicionarioComMinimoDeItens(constantes.PATH_RESULTADOS+"CID.xlsx-evolucao.pickle", 2)
        # pText.gerarNuvemDePalavrasPorDicionario(dicionario, "CID.xlsx-evolucao.png") 
