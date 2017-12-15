#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import sys


## FUNÇÕES DO GAUSS JORDAN ##

def Escalona(x,resp):
 resp2=np.zeros(n*n, float)
 resp2=resp
 lamda=[]
 moddet=0
 op=0
 for tt in xrange(0, n*n):
  for t in xrange(tt+1,n*n):
   lamda.append(x.item(t,tt)/x.item(tt,tt))
   resp2[t]=resp2[t]-lamda[-1]*resp2[tt]
   x[t]=np.copy(x[t]-lamda[-1]*x[tt])
 return x,lamda,op,resp2



def CalculoDet(x):
 det=1
 for i in xrange(0,n):
  det=det*x.item(i,i)
 return det

def Substitui(x,resp2):
 y=resp2
 for i in xrange(n*n-1,-1,-1):
  j=n-1
  while (j>i):
   y[i]=y[i]-x.item(i,j)*y[j]
   j=j-1
  y[i]=y[i]/x.item(i,i)
 return y

def Coeficientes(z,y):
 w=np.zeros([n*n], float)
 for tt in xrange(0,n*n):
  for t in xrange(0,n*n):
   w[tt]=np.copy(w[tt]+y[t]*z.item(tt,t))
 return w

def FazTudo(x,resp):
 z=np.copy(x)
 n=len(x)+1
 moddet=0
 x,l,op,resp2=Escalona(x,resp)
# printmat(x)
 det=CalculoDet(x)
 y=Substitui(x,resp2)
 simply=[ round(elem,2) for elem in y ]
 w=Coeficientes(z,y)
 return simply

################################################

def printmat(aux2):
 for i in xrange((n)**2-1,-1,-1):
  for j in xrange((n)**2-1,-1,-1):
   print  aux2.item(i,j),
  print ''
def printmask():
 for i in xrange(n-1,-1,-1):
  for j in xrange(n-1,-1,-1):
   print  mask[i*n+j],
  print ''



n=100
aux=np.zeros(n*n, float)
aux2=np.zeros((n*n,n*n), float)
mask=np.zeros(n*n, float)


for i in xrange(n):
 mask[i]=1.
 aux[i]=100.
for i in xrange(n-1,n/2,-1):
 mask[n*i+n/2]=1
for i in xrange(n*n-1,n*n-n-1,-1):
 mask[i]=1
for i in xrange(n/2-n/5-1,n/2+n/5):
 mask[n*n/2+i]=1

for i in xrange(n*n):
 aux2.itemset((i,i),1)
 if(mask[i]!=1):
  aux2.itemset((i,i),4)
  aux2.itemset((i,i-n), -1)
  aux2.itemset((i,i-1), -1)
  aux2.itemset((i,i+1), -1)
  aux2.itemset((i,i+n), -1)

y=FazTudo(aux2,aux)

for i in xrange(n-1,-1,-1):
 for j in  xrange(n-1,-1,-1):
  print y[i*n+j],
 print ''

