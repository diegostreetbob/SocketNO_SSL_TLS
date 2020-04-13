#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
#-------------------------------------------------------------------------------
# Name:        server.py
# Purpose:     servidor socket NO seguro
# Author:      DiegoMGuillén
# Contacto:    dmartinez17@alu.ucam.edu
# Created:     13/04/2020
# Notas:
# Testeado con Python 3.7.6
#-------------------------------------------------------------------------------
################################################################################
from socket import *
import sys
import re
import ssl
import traceback
################################################################################
def main():
    #creación del socket
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind((gethostname(), 8801))
    serverSocket.listen(10)
    while True:
        print('1.Activo y preparado para recibir conexiones\n')
        connectionSocket, addr = serverSocket.accept()
        try:
          mensaje = connectionSocket.recv(1024)
          mensajeclte = " _Hola soy tu servidor_"
          print("2.Mensaje recibido desde el cliente: ", mensaje)
          print("3.Respondiendo a cliente con: ", mensajeclte)
          connectionSocket.send(mensajeclte.encode())
          #cerramos la conexión
          connectionSocket.shutdown(SHUT_RDWR)
          connectionSocket.close()
          print("4.Cliente desconectado....\n")
        except IOError:
            connectionSocket.shutdown(SHUT_RDWR)
            connectionSocket.close()
    serverSocket.close()
    sys.exit(0)
################################################################################
if __name__ == '__main__':
    main()
