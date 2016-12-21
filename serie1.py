# Facultad de Ingenieria Universidad de Buenos Aires

# Script Name		: serie1.py
# Author				: Rolon Leonel
# Created				: 20th Dic 2016
# Last Modified		:
# Version				: python 2.7

# Descripcion: estos ejercicios estan escritos en funciones 
# 				los cuales su nombre denota el ejercicio a resolver

def msj(texto):
	print "ingrese"+texto

# 1 algunos conseptos basicos

def p11a():
        msj("nombre: ")
        nombre = raw_input()
        print "Hola "+nombre

def p11b():
        msj("primer numero: ")
        n = input()
        msj("segundo numero")
        n2 = input()
        r = n*n2
        print "el producto es ",r

def p12a():
        msj("base: ")
        base = input()
        msj("altura: ")
        h = input()
        r = 2*base + 2*h
        print "El perimetro es: ",r

def p12b():
        msj("base: ")
        base = input()
        msj("altura: ")
        h = input()
        r = base * h
        print "El area es ",r

def p12d():
        msj("radio: ")
        radio = input()
        r = 2*3.14*radio 
        print "El perimetro es ",r

def p12e():
        msj("radio: ")
        radio = input()
        r = 2**(-1)*3.14*radio**(2) 
        print "El area es ",r

                
def p12f():
        msj("radio: ")
        radio = input()
        r = 4*3**(-1)*3.14*radio 
        print "El volumen es ",r

def p12g():
        msj("cateto1: ")
        cat1 = input()
        msj("cateto2: ")
        cat2 = input()
        h = math.sqrt(cat1**2+cat2**2)
        print "la hipotenusa es ",h

#----------------------------------------------
def p13a():
        for i in range(5):
                print i*i

def p13b():
        for i in range(2,6):
                print i, 2**i

#----------------------------------------------
def p14():
        msj("numero: ")
        n = input()
        r = factorial(n)
        print "El factorial es ",r

#-----------------------------------------------
def p15a():
        msj("dato1: ")
        n = input()
        msj("dato2: ")
        n2 = input()
        r4 = 1.0*1
        r = n + n2
        r2 = n - n2
        r3 = n * n2
        r4 = float(n) / float(n2)
        print "suma ",r
        print "resta ",r2
        print "multiplicacion ",r3
        print "divicion ",r4

def p15b():
        msj("numero: ")
        n = input()
        for i in range(11):
                print i,"x",n,"= ",n*i
#--------------------------------------------	