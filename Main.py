import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from PIL import Image

#=================Exercicio 1=================
a2D =np.zeros((10,10),dtype=np.float64)
#Utilizado NumPy-Template preenchido como conceito
#Pego conteudo do In[8]: e In[24]:
#Print(a2D)
a2D[1,0:]= 2
a2D[4,0:]= 2
a2D[7,0:]= 2
a2D[0:,0]= 0
a2D[0:,2]= 0
a2D[0:,1]= 8
a2D[2,0:8]= 5
a2D[0:,8]= -8
#linha, coluna
print(a2D)


#=================Exercicio 2=================
# (a > 0)
a =np.arange(1, 100, 2).reshape(10,5)
#vai de 50 até 1, usando a soma da terceira variavel(arange(começo, fim, metodo))
#Utilizado NumPy-Template preenchido como conceito
#Pego conteudo do In[71]:


# print(a)
print(f"Média das linhas: {a.mean(axis=1)}")
#Mean calcula a media de modo lista.mean(linha (axis(1)))
print(f"Média das colunas: {a.mean(axis=0)}")
#Mean calcula a media de modo lista.mean(coluna (axis(0)))
print(f"Soma dos elementos da última linha: {a.sum(axis=1)[-1]}")
#Sum calcula a soma de modo lista.sum(linha (axis(1)) [index da posição desejada])
print(f"Soma dos elementos da última coluna: {a.sum(axis=0)[-1]}")
#Sum calcula a soma de modo lista.sum(coluna (axis(0)) [index da posição desejada])


#=================Exercicio 3=================

#Utilizado NumPy-Template preenchido como conceito
#Pego conteudo do In[91]:
#Pego conteudo do In[46]:
a=np.array([[ 1.02809624,  0.31011686, -0.24478542, -0.43531192,  0.30234452, -1.5811674],
 [-0.0029375,   1.26637201,  0.14090036,  0.40795145, -0.57373286,  0.43089205],
 [ 1.76380711, -0.80405178,  1.16717726, -0.77396777,  1.89063668,  1.88322279],
 [ 1.26010925, -0.81197676, -0.90776823,  1.27519403, -0.29176333,  1.21126804],
 [ 0.43983984, -0.41200537,  0.85670881, -0.40561811, -0.44112721,  0.48759066],
 [ 0.21434576, -0.28789424, -0.25646132,  2.30080928, -0.34601413, -1.15924328]])
b = a.reshape(2,18)[0,0:]
#Dividi o a em 2 listas iguais usando reshape para alterar forma da lista, b = primeira(superior) parte da lista(a)
c = a.reshape(2,18)[1,0:]
#Dividi o a em 2 listas iguais usando reshape para alterar forma da lista, b = segunda(inferior) parte da lista(a)
b=np.where(b < 0, 0, b)
#Where é uma condicional para todos os itens da lista individualmente, lista.where(condição, substituir, recebendo)
#Substituição podendo ser feita com dados brutos ou resultados de funções e calculos
c= np.where(c < 0, c*-1, c)
# Where é uma condicional para todos os itens da lista individualmente, lista.where(condição, substituir, recebendo)
#Substituição podendo ser feita com dados brutos ou resultados de funções e calculos

d = np.concatenate([b,c])
plt.scatter(d, d)
plt.title('Dados da Matriz Transposta')
plt.plot(d,d,'o')


#=================Exercicio 4=================


#Utilizado Pandas-Template preenchido como conceito
#Pego conteudo do In[139]:
#Pego conteudo do In[80]:

df1 = pd.read_csv(r'C:\Users\guimu\Downloads\enunciado_TI2\dados\alugueis_info.csv', sep=',')
#Data frame 1

beat = lambda e: str(e).replace("R$", "")
beat2 = lambda e: e.replace("," ,"" )
beat3 = lambda e: e.replace("Sem info", "0")
beat4 = lambda e: str(e).replace( "Incluso", "0")
beat5 = lambda e: e.replace("-", "0")
#Funções para replace, tratamento de dados atraves do replace (responsavel por trocar uma variavel por outra)

df2 = pd.read_csv(r'C:\Users\guimu\Downloads\enunciado_TI2\dados\alugueis_valores.csv', sep=',')
#Data frame 2

df2['Condominio']=df2['Condominio'].map(beat)
df2['Condominio']=df2['Condominio'].map(beat2)
df2['Condominio']=df2['Condominio'].map(beat3)
df2['Condominio']=df2['Condominio'].map(beat4)
#Tratamento da coluna Condominio atraves do map (responsavel por aplicar uma função em todos os elementos da lista)

df2['Aluguel']=df2['Aluguel'].map(beat)
df2['Aluguel']=df2['Aluguel'].map(beat2)
#Tratamento da coluna Aluguel atraves do map (responsavel por aplicar uma função em todos os elementos da lista)

df1['Andar']= df1['Andar'].map(beat5)
#Tratamento da coluna Andar atraves do map (responsavel por aplicar uma função em todos os elementos da lista)

df2['IPTU']=df2['IPTU'].map(beat)
df2['IPTU']=df2['IPTU'].map(beat2)
df2['IPTU']=df2['IPTU'].map(beat4)
#Tratamento da coluna IPTU atraves do map (responsavel por aplicar uma função em todos os elementos da lista)

df2['Seguro Incendio']=df2['Seguro Incendio'].map(beat)
#Tratamento da coluna Seguro Incendio atraves do map (responsavel por aplicar uma função em todos os elementos da lista)

df2['Total']=df2['Total'].map(beat)
df2['Total']=df2['Total'].map(beat2)
#Tratamento da coluna Total atraves do map (responsavel por aplicar uma função em todos os elementos da lista)

df2['Cidade']=df2['Cidade'].map(beat)
#Tratamento da coluna Seguro Cidade atraves do map (responsavel por aplicar uma função em todos os elementos da lista)

df1 = df1[['Cidade', 'Area', 'Quartos', 'Banheiros', 'Vagas Garagem', 'Andar', 'Animal', 'Mobiliado']]
df2 = df2[['Condominio', 'Aluguel', 'IPTU', 'Seguro Incendio', 'Total']]
#Organizando as colunas requeridas 
df = pd.concat([df1,df2], axis=1).dropna()
#Concatenação dos data frames 1 e 2, atraves de um eixo em comum, removendo quaisquer valores desconhecidos



df['Cidade']= df['Cidade'].astype('bool')
df['Andar']= df['Andar'].astype('int64')
df['Condominio']=df['Condominio'].astype('float64')
df['Aluguel']=df['Aluguel'].astype('float64')
df['IPTU']=df['IPTU'].astype('float64')
df['Seguro Incendio']=df['Seguro Incendio'].astype('float64')
df['Total']=df['Total'].astype('float64')
#Tratamento de tipos dos dados

df.index.name = 'ID'
#Mudar o titulo dos index, unnamed 0 -> ID

display(df.info())
df.to_csv('alugueis.csv')
#Salvar csv como 'alugueis.csv'


#=================Exercicio 5=================

DF = pd.read_csv(r'C:\Users\guimu\Downloads\enunciado_TI2\enunciado_TI2\alugueis.csv', sep=',')
#Pegando Data Frame (alugueis.csv)
fig, ax = plt.subplots(2,2 ,figsize=(14,14))
#Selecionando atributos do plot, o modificando

y_dados = DF.sort_values(by = "Andar").drop_duplicates()
#Tirando numeros repetidos com drop duplicates, ao mesmo tempo sortando em ordem crescente a variavel Andar e alterando a data frame toda

y_dados = y_dados["Andar"].value_counts()
#Contando aparições de valor singular de Andares e transformando em lista  [0,1,2] -> ([123 vezes, 20 vezes ... vezes])

posi = np.zeros(y_dados.size)
posi[0] = 0.2
#destacar posição 0, por quanto
#----------

plt.subplot(2,2,1)
#Selecionando posição dentro do plot
plt.title("Andar dos Imóveis para Aluguel")
#Modificando o Título
plt.pie(y_dados, labels= y_dados.index, autopct='%1.2f%%',  explode=posi)
#Utilizado Matplotlib-Template preenchido como conceito

#=============================================


y_dados = DF.sort_values(by = "Quartos").drop_duplicates()
#Tirando numeros repetidos com drop duplicates, ao mesmo tempo sortando em ordem crescente a variavel Andar e alterando a  data frame toda


y_dados = y_dados["Quartos"].value_counts()
#Contando aparições de valor singular de Banheiros e transformando em lista  [0,1,2] -> ([123 vezes, 20 vezes ... vezes])


#----------

plt.subplot(2,2,2)
#Selecionando posição dentro do plot
plt.title("Quantidade de Quartos dos Imóveis para Aluguel")
#Modificando o Título
plt.pie(y_dados, labels= y_dados.index, autopct='%1.2f%%')
#Utilizado Matplotlib-Template preenchido como conceito

#=============================================


y_dados = DF.sort_values(by = "Banheiros").drop_duplicates()
#Tirando numeros repetidos com drop duplicates, ao mesmo tempo sortando em ordem crescente a variavel Banheiros e alterando a  data frame toda


y_dados = y_dados["Banheiros"].value_counts()
#Contando aparições de valor singular de Banheiros e transformando em lista  [0,1,2] -> ([123 vezes, 20 vezes ... vezes])


#----------
plt.subplot(2,2,3)
#Selecionando posição dentro do plot
plt.title("Quantidade de Banheiros dos Imóveis para Aluguel")
#Modificando o Título
plt.pie(y_dados, labels= y_dados.index, autopct='%1.2f%%')
#Utilizado Matplotlib-Template preenchido como conceito

#=============================================


y_dados = DF.sort_values(by = "Vagas Garagem").drop_duplicates()
#Tirando numeros repetidos com drop duplicates, ao mesmo tempo sortando em ordem crescente a variavel Vagas Garagem e alterando a  data frame toda
s

y_dados = y_dados["Vagas Garagem"].value_counts()
#Contando aparições de valor de Vagas Garagem e transformando em lista  [0,1,2] -> ([123 vezes, 20 vezes ... vezes])


#----------
plt.subplot(2,2,4)
#Selecionando posição dentro do plot
plt.title("Quantidade de Garagens dos Imóveis para Aluguel")
#Modificando o Título
plt.pie(y_dados, labels= y_dados.index, autopct='%1.2f%%')
#Utilizado Matplotlib-Template preenchido como conceito

plt.show()

#=================Exercicio 6=================

DF = pd.read_csv(r'C:\Users\guimu\Downloads\enunciado_TI2\enunciado_TI2\alugueis.csv', sep=',')
# x_dados = DF["Aluguel"]

#Aluguel/Quartos

y_dados = DF.loc[DF['Mobiliado'] == True]
#Filtrar todos as linhas com Mobiliado == True
y_dadosMedia = y_dados.groupby(['Quartos'])["Aluguel"].mean()
#Pega as a media de todos os alugueis por todos os quartos e os agrupa em um unico data frame
y_dadosLista = y_dadosMedia.to_list()
#Transformando em lista para uso adiante

x_dados = DF.loc[DF['Mobiliado'] == False]
#Filtrar todos as linhas com Mobiliado == False
x_dadosMedia = x_dados.groupby(['Quartos'])["Aluguel"].mean()
#Pega as a media de todos os alugueis por todos os quartos e agrupa em um unico data frame
x_dadosLista = x_dadosMedia.to_list()
#Transformando o data frame em lista para uso adiante

fig, ax = plt.subplots(figsize=(10,5))
#Selecionando atributos do plot, o modificando

ax.plot(label=['Com Mobilia', 'Sem Mobilia'])
ax.set_title('Média do Valor dos Aluguéis')
ax.set_ylabel('Valor em Reais')
ax.set_xlabel('Número de Quartos')
#Setando as labels externas

ax.bar(y_dadosMedia.index-0.2, y_dadosMedia, width=0.4, linewidth=0.5)
ax.bar(x_dadosMedia.index+0.2, x_dadosMedia, width=0.4, linewidth=0)
#Criando as barras, e ajeitando-as de acordo com saída esperada

for i in range(len(y_dadosMedia.index)):
    ax.annotate(round(y_dadosLista[i],2),
                xy=(y_dadosMedia.index[i],y_dadosLista[i]),
                xycoords='data',
                xytext=(y_dadosMedia.index[i]-0.2, y_dadosLista[i]),
                textcoords='data',
                horizontalalignment='center',
                verticalalignment='bottom')
#Pego conceito de matlib-template (Gráfico de barras)  
#Feito arredondamento dos valores, de acordo com a saida esperada
#Utilizado Matplotlib-Template preenchido como conceito

for i in range(len(x_dadosMedia.index)):
    ax.annotate(round(x_dadosLista[i],2),
                xy=(x_dadosMedia.index[i],x_dadosLista[i]),
                xycoords='data',
                xytext=(x_dadosMedia.index[i]+0.2, x_dadosLista[i]),
                textcoords='data',
                horizontalalignment='center',
                verticalalignment='bottom')
#Pego conceito de matlib-template (Gráfico de barras) 
#Feito arredondamento dos valores, de acordo com a saida esperada
#Utilizado Matplotlib-Template preenchido como conceito

ax.set_xticks(np.arange(1,11))
#Ajeitando o index
ax.legend(['Com Mobilia', 'Sem Mobilia'])
#Legendas
plt.show()