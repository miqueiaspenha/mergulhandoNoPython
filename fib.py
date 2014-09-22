#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def fib(n):
	'''
		Esse funcao recebe um numero inteiro e executa u m loop recursivo chamo de fibonacci,
		e só acaba quando o n for igual a 1

		retorna 1
	'''
	print("n = ", n)

	if(n > 1):
		return n * fib(n - 1)
	else :
		print("End of the line")
		return 1

if __name__ == "__main__":
	fib(10)


