#import psycopg2
import sqlite3
import constantes

# conn = psycopg2.connect(host='localhost', database='teseamanda', user='postgres', password='admin')
# cursor = conn.cursor()

connSqlite = sqlite3.connect(constantes.BD_SQL_RESPOSTAS)
cursorSqlite = connSqlite.cursor()

def criarEstruturaSqlite():
    cursorSqlite.execute("""CREATE TABLE if not exists respostas 
                            (   cd_documento integer,
                                ds_documento text,
                                cd_editor_registro integer,
                                tp_objeto text,
                                cd_metadado integer,
                                cd_campo integer,
                                ds_campo text,
                                resposta text,
                                respostaTratada text,
                                quantStopWords integer,
                                quantNoStopWords integer,
                                quantCID integer,
                                quantSiglas integer,
                                quantTerminologia integer )
                        """ )

def inserirRegistrosSqlite():
    sql = 'select * from dw_amanda.respostas_gineco'
    cursor.execute(sql) 
    dataset = cursor.fetchall()
    for registro in dataset:
        print('postgreSQL' + str(registro[0]) + ' | ' + str(registro[1]))
        cursorSqlite.execute("INSERT INTO respostas (cd_documento, ds_documento, cd_editor_registro, tp_objeto, cd_metadado, cd_campo, ds_campo, resposta) VALUES (?, ?, ?, ?, ?, ?, ?, ?) ", (registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6], registro[7]))
        connSqlite.commit()

def listarRegistrosSqlite():
    sql = 'select * from respostas'
    dataset = cursorSqlite.execute(sql)
    for registro in dataset:
        print('sqlite: ' + str(registro[7]))

if __name__ == "__main__":
    #criarEstruturaSqlite()
    #inserirRegistrosSqlite()
    listarRegistrosSqlite()

    conn.close()
    connSqlite.close()
