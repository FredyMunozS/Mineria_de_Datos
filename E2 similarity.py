# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 09:41:35 2019

@author: Admin
"""

import csv
import pandas as pd


#Importar los datos
with open('C:/Users/Admin/Documents/1. Universidad/5. Mineria de datos/Tarea 2/E2-Data.csv') as inputfile:
    results = list(csv.reader(inputfile, delimiter=';'))

#Crear un DF vacio para almacenar los resultados parciales
columns = ['Texto1','Texto2', 'Palabra', 'Q1', 'Q2', 'Cobertura']    
dfComparison = pd.DataFrame(columns=columns)


#Reemplazar signos de puntuacion

j=0    
for i in results:
    results[j][0]=results[j][0].replace('.', '')
    results[j][0]=results[j][0].replace(',', '')
    results[j][0]=results[j][0].replace('(', '')
    results[j][0]=results[j][0].replace(')', '')
    results[j][0]=results[j][0].replace('-', '')
    results[j][0]=results[j][0].replace(':', '')
    results[j][0]=word_count(results[j][0])
    j=j+1



#Comparar cada palabra con todos los vectores
i=0
for k in results:
    j=0  
    for l in results:
        for m in results[i][0]:
            try:
                T1= 'Texto'+repr(i)
                T2= 'Texto'+repr(j)
                Word= m
                Q1=results[i][0][m]
                Q2=results[j][0][m]
                Coverage=min(Q1,Q2)/max(Q1,Q2)
                df2 = pd.DataFrame([[T1,T2,Word,Q1,Q2,Coverage]], columns=columns)
                dfComparison=dfComparison.append(df2)
            except KeyError:
                Q2=0
                Coverage=min(Q1,Q2)/max(Q1,Q2)
                df2 = pd.DataFrame([[T1,T2,Word,Q1,Q2,Coverage]], columns=columns)
                dfComparison=dfComparison.append(df2)
                
        j=j+1
    i=i+1
    print(repr(int(i/len(results)*100))+' %')



#Agrupa por textos      
df2=dfComparison.groupby(['Texto1','Texto2'])['Cobertura'].mean().to_frame(name='Similarity').reset_index()    
    

  

Output=pd.crosstab(df2.Texto1, df2.Texto2, values=df2.Similarity, aggfunc='mean')




def word_count(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


 


    