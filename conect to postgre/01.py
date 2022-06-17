import psycopg2

# Fazendo a conexão com o banco de dados passando o nome da DB, passando o usuario que geralmente é 'postgres'
# por ser o usuario padrão e a senha do seu banco de dados.

conn = psycopg2.connect(dbname = 'estudo de integração pg e python', user = 'postgres', password = 'pipip12')


#Criando um cursor para navegar pelo bando de dados.

cur = conn.cursor()


#O metodo .execute do cursor serve para executar comando sql dentro do bando de dados.
'''cur.execute("INSERT INTO pequinique (alimento, bebida, pessoa) VALUES ('cookie', 'cerveja', 'Roberval')")'''

cur.execute("select * from pequinique")


#Para printar os resultados do select dentro do Banco de dados é necessario usar o metodo .fetchall, não entendo o pq mas é necessario.

resu = cur.fetchall()



for i in resu:
    print(i)
    print(i[2]) #caso queira imprimir só um valor dentro de uma lista em uma tupla, basta inserir o indice no valor do for nesse caso o 'i'


#O .commit é muito importante para subir as alterações feitas pelo execute do cursos para o Banco de Dados.
#conn.commit()



# Importante sempre fechar a conexão com o banco de dados e também o cursor

cur.close()
conn.close()




