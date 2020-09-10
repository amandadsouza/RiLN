# coding: latin-1
from string import punctuation
import re
from nltk.tokenize import RegexpTokenizer
import constantes

#stop words from: https://github.com/stopwords-iso/stopwords-pt
stopWords = ["a","acerca","adeus","agora","ainda","alem","algmas","algo","algumas","alguns","ali","além","ambas","ambos","ano","anos","antes","ao","aonde","aos","apenas","apoio","apontar","apos","após","aquela","aquelas","aquele","aqueles","aqui","aquilo","as","assim","através","atrás","até","aí","baixo","bastante","bem","boa","boas","bom","bons","breve","cada","caminho","catorze","cedo","cento","certamente","certeza","cima","cinco","coisa","com","como","comprido","conhecido","conselho","contra","contudo","corrente","cuja","cujas","cujo","cujos","custa","cá","da","daquela","daquelas","daquele","daqueles","dar","das","debaixo","dela","delas","dele","deles","demais","dentro","depois","desde","desligado","dessa","dessas","desse","desses","desta","destas","deste","destes","deve","devem","deverá","dez","dezanove","dezasseis","dezassete","dezoito","dia","diante","direita","dispoe","dispoem","diversa","diversas","diversos","diz","dizem","dizer","do","dois","dos","doze","duas","durante","dá","dão","dúvida","e","ela","elas","ele","eles","em","embora","enquanto","entao","entre","então","era","eram","essa","essas","esse","esses","esta","estado","estamos","estar","estará","estas","estava","estavam","este","esteja","estejam","estejamos","estes","esteve","estive","estivemos","estiver","estivera","estiveram","estiverem","estivermos","estivesse","estivessem","estiveste","estivestes","estivéramos","estivéssemos","estou","está","estás","estávamos","estão","eu","exemplo","falta","fará","favor","faz","fazeis","fazem","fazemos","fazer","fazes","fazia","faço","fez","fim","final","foi","fomos","for","fora","foram","forem","forma","formos","fosse","fossem","foste","fostes","fui","fôramos","fôssemos","geral","grande","grandes","grupo","ha","haja","hajam","hajamos","havemos","havia","hei","hoje","hora","horas","houve","houvemos","houver","houvera","houveram","houverei","houverem","houveremos","houveria","houveriam","houvermos","houverá","houverão","houveríamos","houvesse","houvessem","houvéramos","houvéssemos","há","hão","iniciar","inicio","ir","irá","isso","ista","iste","isto","já","lado","lhe","lhes","ligado","local","logo","longe","lugar","lá","maior","maioria","maiorias","mais","mal","mas","me","mediante","meio","menor","menos","meses","mesma","mesmas","mesmo","mesmos","meu","meus","mil","minha","minhas","momento","muito","muitos","máximo","mês","na","nada","nao","naquela","naquelas","naquele","naqueles","nas","nem","nenhuma","nessa","nessas","nesse","nesses","nesta","nestas","neste","nestes","no","noite","nome","nos","nossa","nossas","nosso","nossos","nova","novas","nove","novo","novos","num","numa","numas","nunca","nuns","não","nível","nós","número","o","obra","obrigada","obrigado","oitava","oitavo","oito","onde","ontem","onze","os","ou","outra","outras","outro","outros","para","parece","parte","partir","paucas","pegar","pela","pelas","pelo","pelos","perante","perto","pessoas","pode","podem","poder","poderá","podia","pois","ponto","pontos","por","porque","porquê","portanto","posição","possivelmente","posso","possível","pouca","pouco","poucos","povo","primeira","primeiras","primeiro","primeiros","promeiro","propios","proprio","própria","próprias","próprio","próprios","próxima","próximas","próximo","próximos","puderam","pôde","põe","põem","quais","qual","qualquer","quando","quanto","quarta","quarto","quatro","que","quem","quer","quereis","querem","queremas","queres","quero","questão","quieto","quinta","quinto","quinze","quáis","quê","relação","sabe","sabem","saber","se","segunda","segundo","sei","seis","seja","sejam","sejamos","sem","sempre","sendo","ser","serei","seremos","seria","seriam","será","serão","seríamos","sete","seu","seus","sexta","sexto","sim","sistema","sob","sobre","sois","somente","somos","sou","sua","suas","são","sétima","sétimo","só","tal","talvez","tambem","também","tanta","tantas","tanto","tarde","te","tem","temos","tempo","tendes","tenha","tenham","tenhamos","tenho","tens","tentar","tentaram","tente","tentei","ter","terceira","terceiro","terei","teremos","teria","teriam","terá","terão","teríamos","teu","teus","teve","tinha","tinham","tipo","tive","tivemos","tiver","tivera","tiveram","tiverem","tivermos","tivesse","tivessem","tiveste","tivestes","tivéramos","tivéssemos","toda","todas","todo","todos","trabalhar","trabalho","treze","três","tu","tua","tuas","tudo","tão","tém","têm","tínhamos","um","uma","umas","uns","usa","usar","vai","vais","valor","veja","vem","vens","ver","verdade","verdadeiro","vez","vezes","viagem","vindo","vinte","você","vocês","vos","vossa","vossas","vosso","vossos","vários","vão","vêm","vós","zero","à","às","área","é","éramos","és","último"]


def retirarExcessoDeEspacos(text):
    """ Retira dois ou mais espaços entre as palavras
    
    Arguments:
        text {str} -- Texto a ser tratado
    
    Returns:
        str -- Texto sem excesso de espaços entre as palavras 
    """    
    resp = re.sub("[ ]{2,}", " ", text)
    return resp

def retirarCaracteresEspeciais(text):
    """ Retira do texto alguns caracteres que atrapalham a analise
    
    Arguments:
        text {str} -- Texto a ser tratado
    
    Returns:
        str -- Texto sem caracteres improprios aa analise 
    """    
    for c in punctuation:
        text = text.replace(c, ' ')
    text = text.replace('–', '').replace('•', '') #caracter especial que nao eh o hifen e nao estah em punctuation 
    #text = text.replace('(', ' ').replace(')', '').replace('[', '').replace(']', '').replace('<', '').replace('>', '').replace('+', '').replace('=', '')   
    return text 

def retirarQuebraDeLinha(text):
    """ Retira a quebra de linha no das frases, se houver
    
    Arguments:
        text {str} -- Texto a ser tratado
    
    Returns:
        str -- Texto sem caracteres de quebra de linha
    """    
    text = text.replace('\n', ' ')
    return text

def retirarStopWords(text): 
    """ Retira palavras indesejadas do texto
    
    Arguments:
        text {str} -- Texto a ser tratado

    Returns:
        str -- Texto sem palavras indesejadas
    """   	
    text = text.replace('fig', '') 
    return text 

def contarStopWords(text):
    """ Percorre o texto e conta quantas stop words estao presentes mediante o array pre-definido
    
    Arguments:
        text {str} -- Texto a ser analisado
    
    Returns:
        dict -- Dicionario com texto, quantidade de stop words e quantidade de palavras nao consideradas stop words
    """
    palavrasDoTexto = text.split(' ')
    quantStopWords = 0
    quantNaoStopWords = 0
    for palavra in palavrasDoTexto:
        if palavra in stopWords:
            quantStopWords += 1
        else:
            quantNaoStopWords += 1 
    resposta = {
        "texto" : text,
        "stop" : quantStopWords ,
        "noStop" : quantNaoStopWords
    }
    return resposta

def limpaTexto(text):
    """ Centraliza a chamada das principais funcoes para tratamento do texto
    
    Arguments:
        text {str} -- Texto a ser tratado
    
    Returns:
        str -- Texto alterado todo em minusculas (case folding) apos as funcoes de tratamento serem invocadas 
    """    
    novoTexto = retirarQuebraDeLinha(text)
    novoTexto = retirarCaracteresEspeciais(novoTexto)
    novoTexto = retirarExcessoDeEspacos(novoTexto).strip()
    return novoTexto.lower()

def tokenizeString(text):
    """ Recebe uma frase e retorna as palavras separadas em array 

    Arguments:
        text {str} -- Texto a ser tokenizado

    Returns:
        list -- Um array (lista) de palavras separadas por posicao 
    """    
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)
    return tokens   

def carregarCIDcomoArray():
    """ Le o arquivo texto com as siglas da CID e gera um array em minusculas 

    Returns:
        list -- Siglas da CID em minusculas 
    """    
    with open(constantes.ARQ_CID, 'r') as file:
        lista = file.read().splitlines()
        listaMinuscula = [x.lower() for x in lista]
        return listaMinuscula

def carregarSiglasComoArray():
    """ Le o arquivo com siglas tecnicas e gera um array em minusculas

    Returns:
        list -- Siglas tecnicas em minusculas 
    """    
    lista = open(constantes.ARQ_SIGLAS, 'r').read().splitlines()
    listaMinuscula = [x.lower() for x in lista] 
    return listaMinuscula

