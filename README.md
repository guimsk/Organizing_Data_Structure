# Trabalho realizado na cadeira Programação orientada a dados 2° semestre PUCRS.
# Trabalho focado em uso de Matplotlib, Pandas e Numpy, afim de criar graficos utilizando dados que devem ser tratados antes de uso. 
# Enunciado das questões segue abaixo:


# Questao 1.
 Manipulação de Dados Vetorial

_Atenção: não será permitido o uso de laços nesta parte do trabalho sobre manipulação vetorial._

_Atenção: Todas as questões valem 1 ponto nesta parte do trabalho._

# Crie um array 2D `shape(10,10)`  e realize operações de indexação e fatiamento para obter o seguinte resultado.

```bash
[[ 0.  8.  0.  0.  0.  0.  0.  0. -8.  0.]
 [ 0.  8.  0.  2.  2.  2.  2.  2. -8.  2.]
 [ 5.  5.  5.  5.  5.  5.  5.  5. -8.  0.]
 [ 0.  8.  0.  0.  0.  0.  0.  0. -8.  0.]
 [ 0.  8.  0.  2.  2.  2.  2.  2. -8.  2.]
 [ 0.  8.  0.  0.  0.  0.  0.  0. -8.  0.]
 [ 0.  8.  0.  0.  0.  0.  0.  0. -8.  0.]
 [ 0.  8.  0.  2.  2.  2.  2.  2. -8.  2.]
 [ 0.  8.  0.  0.  0.  0.  0.  0. -8.  0.]
 [ 0.  8.  0.  0.  0.  0.  0.  0. -8.  0.]]
 ```


 # Questao 2.
 # Crie um array 2D com a sequência de números ímpares no intervalo 0 a 100 e faça as seguintes operações:
- Média das linhas
- Média das colunas
- Soma dos elementos da última linha
- Soma dos elementos da última coluna

**Resultado Esperado:**
```bash
Média das linhas: [ 5. 15. 25. 35. 45. 55. 65. 75. 85. 95.]
Média das colunas: [46. 48. 50. 52. 54.]

Soma dos elementos da última linha: 475
Soma dos elementos da última coluna: 540
```

# Questao 3.
# Particione verticalmente ao meio o array `a`, armazenando a parte superior em `b` e inferior em `c`. Depois, tranforme os números negativos em positivos do array `c` e atribua `0` para os valores negativos do array `b`. Ao final das transformações, concatene `b` com `c` e forneça um gráfico de dispersão com os dados da matriz transposta (conforme está abaixo).

```python
a=np.array([[ 1.02809624,  0.31011686, -0.24478542, -0.43531192,  0.30234452, -1.5811674],
 [-0.0029375,   1.26637201,  0.14090036,  0.40795145, -0.57373286,  0.43089205],
 [ 1.76380711, -0.80405178,  1.16717726, -0.77396777,  1.89063668,  1.88322279],
 [ 1.26010925, -0.81197676, -0.90776823,  1.27519403, -0.29176333,  1.21126804],
 [ 0.43983984, -0.41200537,  0.85670881, -0.40561811, -0.44112721,  0.48759066],
 [ 0.21434576, -0.28789424, -0.25646132,  2.30080928, -0.34601413, -1.15924328]])
```
**Resultado Esperado**
![image.png](attachment:image.png)


# Questao 4.
# Forneça um único DataFrame a partir dos dados contidos em `alugueis_info.csv` e `alugueis_valores.csv`. Depois de corrigir os dados, salve o DataFrame corrigido em um arquivo chamado `alugueis.csv` para reusar nas próximas questões.

_Obs: Para quem usar laços nesta questão, terá um desconto de 25% na nota._


**Resultado Esperado do DataFrame:**
```bash
<class 'pandas.core.frame.DataFrame'>
Int64Index: 6073 entries, 0 to 6079
Data columns (total 13 columns):
 #   Column           Non-Null Count  Dtype  
---  ------           --------------  -----  
 0   Cidade           6073 non-null   bool   
 1   Area             6073 non-null   float64
 2   Quartos          6073 non-null   int64  
 3   Banheiros        6073 non-null   int64  
 4   Vagas Garagem    6073 non-null   int64  
 5   Andar            6073 non-null   int64  
 6   Animal           6073 non-null   bool   
 7   Mobiliado        6073 non-null   bool   
 8   Condominio       6073 non-null   float64
 9   Aluguel          6073 non-null   float64
 10  IPTU             6073 non-null   float64
 11  Seguro Incendio  6073 non-null   float64
 12  Total            6073 non-null   float64
dtypes: bool(3), float64(6), int64(4)
memory usage: 539.7 KB
```
**Os 5 primeiros registros do DataFrame:**
![image.png](attachment:image.png)


# Questao 5.
# Forneça um painel de visualização `Axes(2,2)` para os dados de `alugueis.csv` com os seguintes gráficos de pizza em ordem:

- Ocorrência do andar dos imóveis para aluguel.
- Ocorrência da quantidade de quartos dos imóveis para aluguel.
- Ocorrência da quantidade de banheiros dos imóveis para aluguel.
- Ocorrência da quantidade de garagens dos imóveis para aluguel.

**Resultado Esperado**
![image.png](attachment:image.png)


# Questao 6.
# Para a base de dados `alugueis.csv`, apresente um gráfico de barras com a média do valor dos aluguéis relativo ao número de quartos para os imóveis com e sem mobilia. 

**Resultado Esperado:**
![image-2.png](attachment:image-2.png)