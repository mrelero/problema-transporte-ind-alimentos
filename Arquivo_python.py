# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 19:05:19 2021

@author: Usuario
"""

import gurobipy as gp

#inicialização de variáveis
fabricas = ["Anastácio", "Nova Andradina", "Dourados", "Campo Grande",  "Caxias do Sul", "Itapetininga - SP", "Naviraí" ,"Brasília", "Manaus", "Ji-Paraná", "Itapetininga - BA", "São Gonçado dos Campos","Feira de Santana", "Araguaína - TO"]
centros_distr = ["Alta Floresta - MT","Diamantino - MT","Araputanga - MT","Vilhena - RO","Pimenta Bueno - RO","Porto Velho","São Miguel do Guaporé - RO","Goiania - GO","Ponta Porã","Anhenguera - SP 1","Osasco - SP","Aparecida de Goiania ","Brasília - DF","Maceió - AL","Cascavel - CE","Caucaia - CE","Itaitinga - CE","Simões Filho - BA","Confresa - MT","Barra do Garças - MT","Pedra Preta - MT","Juara - MT","POontes e Lacerda - MT","Anhenguera - SP 2","Cajamar - SP"]

#Matriz de Distancias e Custos
mat_custos = [[240,236,245,518,983,558,617,322,514,843,285,475,346,789,992,240,532,232,928,946,435,271,226,340,582],
[491,329,565,486,854,848,219,529,930,750,700,504,725,724,507,779,478,927,633,341,305,845,595,420,206],
[895,614,956,383,259,371,927,474,336,306,567,726,635,945,231,487,624,834,470,424,411,647,742,813,525],
[657,759,749,512,464,498,516,793,332,309,986,260,625,271,709,435,1000,926,815,458,872,755,731,577,841],
[639,590,776,617,242,983,899,766,409,371,884,216,912,337,305,610,204,706,522,699,407,280,302,231,585],
[658,230,989,741,483,839,613,258,975,866,745,806,976,729,902,403,468,661,471,387,714,861,918,875,865],
[870,498,308,843,431,248,960,321,646,705,580,646,256,354,322,380,638,292,265,555,676,918,975,787,610],
[347,238,233,756,641,812,834,796,466,281,266,377,661,212,947,719,977,805,836,725,877,541,766,400,218],
[510,830,391,736,373,874,715,507,896,952,608,274,789,846,644,926,624,287,457,771,846,625,569,313,991],
[424,641,314,455,917,721,541,491,626,965,364,806,558,453,802,353,350,742,286,996,763,364,319,690,808],
[866,213,796,778,464,607,396,780,813,441,646,964,466,514,765,655,425,630,786,667,438,837,795,424,583],
[301,208,771,770,920,719,733,212,202,546,558,414,470,210,786,765,698,479,598,562,589,341,324,351,710],
[502,805,851,530,854,307,951,739,296,462,668,844,786,710,483,952,717,291,429,207,996,794,733,410,437],
[309,592,352,681,737,494,295,786,329,671,730,907,855,770,766,329,733,561,960,596,518,447,475,692,816]]

#Custo Coletado
# 3.5 o km a cada 25 toneladas 3,5/km 25Ton
Custo_Transporte = 3.5

#Matriz de Capacidade - Fabricas x Produtos
mat_capacidade = [[25,39,219,95,262,203,269,62,276,228,221,218,9,275,4,235,235,273,216,68],
[19,188,174,87,246,90,48,271,51,259,135,16,202,151,46,103,110,123,106,133],
[237,86,26,34,105,196,71,20,263,209,23,289,10,34,185,81,76,293,123,57],
[165,126,113,74,100,106,127,233,72,296,160,233,116,102,186,1,191,176,7,228],
[239,274,94,25,298,117,293,21,167,290,11,221,260,266,217,54,252,198,72,278],
[235,84,253,86,96,164,143,291,95,143,187,87,218,98,93,279,26,205,175,118],
[136,38,49,269,188,265,20,209,265,209,205,159,62,271,49,1,207,68,34,219],
[286,1,225,224,231,75,135,251,189,22,7,99,174,30,96,247,66,4,171,215],
[177,53,63,73,269,31,289,254,93,68,117,69,266,164,237,297,106,293,132,295],
[122,139,3,224,78,115,59,34,265,120,199,217,99,5,100,287,170,91,64,89],
[217,250,271,133,67,221,183,265,250,29,205,130,222,114,161,298,131,236,111,49],
[140,28,185,89,156,258,254,156,202,96,76,188,105,214,135,246,36,183,2,184],
[204,130,62,137,64,74,135,171,180,231,179,178,180,56,126,48,205,299,66,156],
[197,50,143,33,70,273,213,110,92,172,297,288,249,195,149,244,244,134,81,234]]

#Matriz de Demandas - Centros x Produtos
mat_demandas = [[224,92,61,177,235,291,154,256,296,30,179,294,293,293,152,216,69,111,26,13],
[16,295,18,97,6,64,292,130,295,79,102,131,150,187,239,254,277,132,276,252],
[260,109,256,137,224,84,266,178,74,133,104,13,84,121,231,173,103,81,208,105],
[223,32,285,240,198,193,10,45,97,28,92,156,50,7,198,145,105,15,195,0],
[245,239,145,113,248,147,76,42,158,106,190,162,121,108,9,245,268,85,189,137],
[213,239,118,119,190,65,278,278,168,22,165,178,194,147,20,52,171,244,249,167],
[244,51,203,106,276,149,288,274,203,198,189,273,249,294,18,182,216,98,50,25],
[278,172,224,76,168,20,225,40,271,70,148,2,62,99,67,132,108,273,82,76],
[56,175,22,79,280,80,21,193,245,190,101,227,258,65,163,217,17,66,118,203],
[229,178,238,298,128,36,220,78,147,58,131,121,231,71,103,238,14,261,21,216],
[283,218,61,19,248,253,229,83,28,118,27,20,40,24,50,49,162,191,134,162],
[79,142,110,106,77,100,202,46,260,100,175,264,3,29,215,39,91,249,147,113],
[135,296,75,128,219,11,111,241,28,145,38,252,126,281,268,174,28,154,105,54],
[128,235,11,280,33,100,19,217,34,201,120,99,122,268,128,84,224,20,66,278],
[176,129,136,58,77,85,223,190,187,105,236,129,7,78,175,286,255,69,44,23],
[172,14,3,133,192,105,27,16,144,202,296,49,176,113,145,32,160,18,8,190],
[198,230,172,31,161,193,131,98,240,4,10,11,29,43,201,16,249,15,32,261],
[18,136,277,1,195,230,292,14,293,223,265,127,281,149,291,195,5,210,4,16],
[21,117,105,254,90,57,79,272,5,80,142,49,39,224,45,285,149,92,239,125],
[58,63,255,56,114,193,145,193,217,266,126,89,99,276,254,87,270,270,254,106],
[78,203,148,271,226,233,177,224,29,84,140,87,148,193,169,42,295,220,185,117],
[21,109,226,135,200,251,144,38,268,109,51,122,139,171,87,204,219,170,288,18],
[108,225,89,55,283,225,197,218,206,118,15,207,250,90,224,269,143,29,252,236],
[181,82,62,231,10,88,33,149,121,140,159,220,143,181,9,196,263,189,66,248],
[255,73,294,41,72,125,40,296,112,23,16,18,239,196,224,240,151,68,192,243]]


#Quantidade Total de Fabricas
numero_fabricas = len(fabricas)
numeros_centros = len (centros_distr)
total_familias_produtos = 20

custos = dict()
demandas = dict()
capacidade = dict()
fornecimento_fabrica_produto = dict()
recebimento_centro_produto = dict ()

#genérico enquanto não tem a relação correta
familias_produtos = ["Familia_Produto_{}".format(i+1) for i in range(total_familias_produtos)]

#Dicionario de Custos
for i, fab in enumerate (fabricas):
    for j, cent in enumerate(centros_distr):
        custos[fab, cent] = mat_custos[i][j]

#Dicionario de Capacidades
for i, fab in enumerate (fabricas):
    for j, prod in enumerate(familias_produtos):
        capacidade[fab, prod] = mat_capacidade[i][j]

#Dicionario de Demandas
for i, cent in enumerate (centros_distr):
    for j, prod in enumerate(familias_produtos):
        demandas[cent, prod] = mat_demandas[i][j]


##Monta Listas com Capacidades e Demandas de cada produto
capacidade_produto = dict()
demanda_produto = dict()
aux = 0

for k in familias_produtos:
    for i in fabricas:
        aux = aux + capacidade[i,k]
    capacidade_produto[k] = aux
    aux = 0
aux =0

for k in familias_produtos:
    for j in centros_distr:
        aux = aux + demandas[j,k]
    demanda_produto[k] = aux
    aux = 0

## Modelo
m = gp.Model()

##Variáveis de Transporte
transporte = m.addVars(fabricas, centros_distr, familias_produtos)

c_capacidade = list()
c_demandas = list()
for k in familias_produtos:
    if capacidade_produto[k] > demanda_produto [k]:
        c_capacidade.append(m.addConstrs(gp.quicksum(transporte[i,j,k] for j in centros_distr)<= capacidade[i,k] for i in fabricas))
        c_demandas.append(m.addConstrs(gp.quicksum(transporte[i,j,k] for i in fabricas)== demandas[j,k] for j in centros_distr))
    else:
        c_capacidade.append(m.addConstrs(gp.quicksum(transporte[i,j,k] for j in centros_distr)==capacidade[i,k] for i in fabricas))
        c_demandas.append(m.addConstrs(gp.quicksum(transporte[i,j,k] for i in fabricas)<= demandas[j,k] for j in centros_distr))

      
#c_ofertas = m.addConstrs(gp.quicksum(transporte[i,j,k] for j in centros_distr)<= capacidade[i,k] for i in fabricas for k in familias_produtos)
#c_demandas = m.addConstrs(gp.quicksum(transporte[i,j,k] for i in fabricas)== demandas[j,k] for j in centros_distr for k in familias_produtos)

m.setObjective(gp.quicksum(transporte[i, j,k]* custos[i, j] for i in fabricas for j in centros_distr for k in familias_produtos), sense = gp.GRB.MINIMIZE)

m.optimize()



for i in fabricas:
    for j in centros_distr:
  #      print("Fabrica de {}".format(i))
   #     print ("Para o Centro de Distribuição de {}".format(j)) 
        for k in familias_produtos:
          #  print ("{}: {}".format(k,transporte[i,j,k].X))
             print(transporte[i,j,k].X)
    print("\n")  