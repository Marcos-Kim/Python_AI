# -*- coding: utf-8 -*-
"""ProjetoFinal.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tJR1z0STtKfsarcPiv26Lano6CkXrRWN
"""

# importando as bibliotecas

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random

# Definir o nome do arquivo csv
nome_arquivo_csv = 'telecom_churn.csv'

# definindo função
def gerar_dados_telecom(num_telecom):
  dados = []
  for _ in range (num_telecom):
    inadimplencia = random.randint(0,1)
    tempo_contrato_meses = random.randint(0,360)
    valor_servicos = round(random.uniform(15,2000),2)
    suporte_ultimos_12_meses = random.randint(0,1)
    tipo_servico = random.choice(['Móvel','Banda Larga','TV','Fibra dedicada','Voip','Familia 1','Familia 2','Corp 1','Corp 2'])
    desconto = round(random.uniform(0,15),2)
    dados.append([inadimplencia,tempo_contrato_meses,valor_servicos,suporte_ultimos_12_meses,tipo_servico,desconto])
    return dados

# gerando os dados
dados_telecom = gerar_dados_telecom(1000)

# dados no arquivo csv gerado

cabecalho = ['inadimplencia','tempo_contrato_meses','valor_servicos','suporte_ultimos_12_meses','tipo_servico','desconto']
df = pd.DataFrame(dados_telecom,columns=cabecalho)
df.to_csv(nome_arquivo_csv, index = False)

df = pd.read_csv(nome_arquivo_csv)

print(df.describe())

print(df.info())

plt.figure(figsize=(10, 6))
sns.countplot(x='inadimplencia', data=df)
plt.title('Adimplentes e Inadimplentes')
plt.xlabel('Adimplente (0) e Inadimplente(1)')
plt.ylabel('desconto')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x='inadimplencia', data=df)
plt.title('Adimplentes e Inadimplentes')
plt.xlabel('Adimplente (0) e Inadimplente(1)')
plt.ylabel('tempo_contrato_meses')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x='inadimplencia', data=df)
plt.title('Adimplentes e Inadimplentes')
plt.xlabel('Adimplente (0) e Inadimplente(1)')
plt.ylabel('valor_servicos')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x='inadimplencia', data=df)
plt.title('Adimplentes e Inadimplentes')
plt.xlabel('Adimplente (0) e Inadimplente(1)')
plt.ylabel('suporte_ultimos_12_meses')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x='inadimplencia', data=df)
plt.title('Adimplentes e Inadimplentes')
plt.xlabel('Adimplente (0) e Inadimplente(1)')
plt.ylabel('tipo_servico')
plt.show()