# coding: latin-1
from bdRespostas import BD
import constantes
import processamentoTextual as pText 

if __name__ == "__main__":
    banco = BD(constantes.BD_SQL_RESPOSTAS)
    with banco:
        #banco.trataStopWords('N')
        banco.separaStopWords()
        #banco.trataNgrams() - a definir
        #banco.countUniGramForArq()
        #banco.countCIDForArq()
        #banco.countCIDForBD()
        #banco.countSiglaForTxt()

        #banco.processaBigramas()
        #banco.processaTrigramas() 
        #banco.exportarBancoDeDados()

        pText.gerarNuvemDePalavras('texto.txt', 'stop.png')
        pText.gerarNuvemDePalavras(constantes.PATH_RESULTADOS + 'stopWords-ParaNuvem-Todas.txt', 'stopWords-ParaNuvem-Todas.png')
        pText.gerarNuvemDePalavras(constantes.PATH_RESULTADOS + 'stopWords-ParaNuvem-Anamnese.txt', 'stopWords-ParaNuvem-Anamnese.png')
        pText.gerarNuvemDePalavras(constantes.PATH_RESULTADOS + 'stopWords-ParaNuvem-Evolucao.txt', 'stopWords-ParaNuvem-Evolucao.png')