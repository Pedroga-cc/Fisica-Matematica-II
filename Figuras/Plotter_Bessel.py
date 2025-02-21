# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from scipy.special import *

style.use('classic')

colores = ['#2B7EA0', '#E76F51', '#2a9d8f', '#F4A261', '#000945', '#D56C2C']
# dasheses=[[],[5,2],[5,5],[5,2,2,2],[2,2], [3,3]]
linestyles = ['-', '--', ':', '-.', (0, (5,2)), (0, (5,5,3))]

x = np.linspace(-10,10,1000)

fig = plt.figure(figsize=(8,6))
for n in range(6):
    plt.plot(x,jn(n,x),colores[n], linestyle=linestyles[n],label='$n= $'+str(n), linewidth=2)
plt.grid()
plt.xlabel(r'$x$',fontsize=15)
plt.ylabel(r'$J_n(x)$',fontsize=15)
plt.ylim(-1.1,1.1)
#title(r'Funciones de Bessel de $1^{a}$ especie y orden entero')
plt.legend(loc='best', ncols=2, fontsize=12)
plt.ylim(-0.7,1.1)
plt.savefig('./Figuras/Bessel_first_Kind.pdf')

# $N_{\nu}(x)$

fig = plt.figure(figsize=(8,6))
for n in range(6):
    plt.plot(x,yn(n,x),colores[n], linestyle=linestyles[n],label='$n= $'+str(n), linewidth=2)
plt.grid()
plt.xlabel(r'$x$',fontsize=15)
plt.ylabel(r'$Y_n(x)$',fontsize=15)
plt.ylim(-1.1,1.1)
#title(r'Funciones de Bessel de $2^{da}$ especie y orden entero')
plt.legend(loc='best',fontsize=12)
plt.ylim(-2,0.7)
plt.savefig('./Figuras/Bessel_second_kind.pdf')


# $I_{\nu}(z)$

x = np.linspace(-4,4,1000)
fig = plt.figure(figsize=(8,6))
for n in range(6):
    plt.plot(x,iv(n,x),colores[n], linestyle=linestyles[n],label='$n= $'+str(n), linewidth=2)
plt.grid()
plt.xlabel(r'$x$',fontsize=15)
plt.ylabel(r'$I_n(x)$',fontsize=15)
#title(r'Funciones modificadas de Bessel de $1^{\circ}$ especie a orden entero',fontsize=13)
plt.legend(loc='best',fontsize=12)
plt.xlim(-4,4)
plt.ylim(-10,12)
plt.savefig('./Figuras/Bessel-modified-first-kind.pdf')


# $K_{\nu}(z)$

x = np.linspace(0,4,1000)
fig = plt.figure(figsize=(8,6))
for n in range(6):
    plt.plot(x,kv(n,x),colores[n], linestyle=linestyles[n],label='$n= $'+str(n), linewidth=2)
plt.grid()
plt.xlabel(r'$x$',fontsize=15)
plt.ylabel(r'$K_n(x)$',fontsize=15)
#title(r'Funciones modificadas de Bessel de $2^{\circ}$ especie a orden entero',fontsize=13)
plt.legend(loc='best',fontsize=12)
plt.ylim(0,4)
plt.savefig('./Figuras/Bessel-modified-second-kind.pdf')


# #$j_{n}(x)$:

x = np.linspace(0,10,1000)

fig = plt.figure(figsize=(8,6))
for n in range(6):
    plt.plot(x,spherical_jn(n,x),colores[n], linestyle=linestyles[n],label='$n= $'+str(n), linewidth=2)
plt.grid()
plt.xlabel(r'$x$',fontsize=15)
plt.ylabel(r'$j_n(x)$',fontsize=15)
#title(ur'Funciones Esféricas de Bessel de $1^{\circ}$ especie a orden entero',fontsize=12)
plt.legend(loc='best',fontsize=12, ncols=3)
plt.ylim(-0.5,1.1)
plt.savefig('./Figuras/Bessel-Esferica-first-kind.pdf')


# #$n_{n}(x)$:

x = np.linspace(-20,20,1000)
fig = plt.figure(figsize=(8,6))
for n in range(6):
    plt.plot(x,spherical_yn(n,x),colores[n], linestyle=linestyles[n],label='$n= $'+str(n), linewidth=2)
plt.grid()
plt.xlabel(r'$x$',fontsize=15)
plt.ylabel(r'$y_n(x)$',fontsize=15)
#title(ur'Funciones Esféricas de Bessel de $1^{\circ}$ especie a orden entero',fontsize=12)
plt.legend(loc='best',fontsize=12, ncols=3)
plt.ylim(-0.5,1.1)
plt.savefig('./Figuras/Bessel-Esferica-second-kind.pdf')

# #$i_{n}(x)$:

x = linspace(0,5,1000)
fig = figure(figsize=(8,6))
for n in range(5):
    plot(x,spherical_in(n,x),colores[n], dashes=dasheses[n],label='$n= $'+str(n), linewidth=2)
grid()
xlabel(r'$x$',fontsize=15)
ylabel(r'$i_n(x)$',fontsize=15)
#title(ur'Funciones Esféricas Modificadas de Bessel de $1^{\circ}$ especie a orden entero',fontsize=12)
legend(loc='best',fontsize=12)
savefig('../figs/fig-Bessel-Esferica-i.pdf')


# #$k_{n}(x)$:


x = linspace(5,1000)
fig = figure(figsize=(8,6))
for n in range(5):
    plot(x,spherical_kn(n,x),colores[n], dashes=dasheses[n],label='$n= $'+str(n), linewidth=2)
grid()
xlabel(r'$x$',fontsize=15)
ylabel(r'$k_n(x)$',fontsize=15)
#title(ur'Funciones Esféricas Modificadas de Bessel de $2^{\circ}$ especie a orden entero',fontsize=12)
legend(loc='best',fontsize=12)
ylim(-1,15)