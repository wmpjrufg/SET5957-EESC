#!/usr/bin/env python
# coding: utf-8

# **=========================================================================  
# FUNÇÃO 1: DETERMINAÇÃO DOS GRAUS DE LIBERDADE DOS ELEMENTOS
# =========================================================================**  

# In[1]:


def graus_de_lib_totais(nNos, nGrauPorNo):
    nGdlTotal = nNos*nGrauPorNo
    gdlTotal = np.linspace(1, nGdlTotal, num=nGdlTotal)
    return nGdlTotal, gdlTotal

def graus_de_lib_restritos(nApo, apoios):
    for apo in np.linspace(1,nApo,nApo): 
        no = apoios[apo,1]
        resticaoX = apoios[apo,2]
        if resticaoX==1
            
    nGdlRestrito = 1
    gdlRestrito = 1 
    return nGdlRestrito, gdlRestrito

def graus_de_lib_livres(gdlTotal, gdlRestrito):
    gdlLivre = np.setdiff1d(gdlTotal, gdlRestrito)
    nGdlLivre = gdlLivre.shape
    return nGdlLivre, gdlLivre


# In[2]:


import numpy as np
nNos = 10
nGrauPorNo = 2

nGdlTotal, gdlTotal = graus_de_lib_totais(nNos, nGrauPorNo)
print(nGdlTotal)
print(gdlTotal)

nGdlRestrito, gdlRestrito = graus_de_lib_restritos(3, 1)
print(nGdlRestrito)
print(gdlRestrito)

nGdlLivre, gdlLivre = graus_de_lib_livres(gdlTotal, [5, 6, 8])
print(gdlLivre)
print(nGdlLivre)


# In[ ]:





# In[ ]:




