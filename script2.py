#Criando um arquivo de texto

#f = open("C:/Users/Ygor/Documents/demonstracao.txt", "w+")
#for i in range(10):
#   f.write("Esta é a linha %d\r\n" % (i + 1))

#for i in range(2):
#    f.write("Linha %d de origem ao arquivo \r\n" % (i + 1))
   
#f.close()

#f = open("C:/Users/Ygor/Documents/demonstracao.txt", "a+")

#for i in range(3):
#   if (i + 1) == 1:
#       f.write("Primeira linha adicionada \r\n")
#   if (i + 1) == 2:
#       f.write("Segunda linha adicionada \r\n")
#   if (i + 1) == 3:
#       f.write("Terceira linha adicionada \r\n")  
	  
#f.close()

#f = open("C:/Users/Ygor/Documents/demonstracao.txt", "r")

#if f.mode == "r":
 #contents = f.read()
 #print(contents)
 
# f1 = f.readlines()
# for x in f1:
#   print(x)
#f.close()

import os
import shutil
from os import path
def main():
  if path.exists("C:/Users/Ygor/Documents/demonstracao.txt"):
     src = path.realpath("C:/Users/Ygor/Documents/demonstracao.txt");
	 
  head, tail = path.split(src)
  print("path:" + head)
  print("file:" + tail)
  
  dst = src + "Copia"
  shutil.copy(src, dst)
  shutil.copystat(src, dst)
if __name__ == "__main__":
    main()