#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Versão do Python usada 3.2

def buildConnectionString(params):
	''' Constrói uma string de conexão a partir de um dicionário de parâmetros.
		Retorna uma string
	'''
	return ";".join(["%s=%s" % (k,v) for k, v in params.items()])

if __name__ == "__main__" :
	myParams = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
	print(buildConnectionString(myParams))