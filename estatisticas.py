# coding: latin-1
from BDRespostas import BD
import constantes


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

        #banco.processaBigramas()
        banco.processaTrigramas() 