## Creación de socket **no seguro** en Python.

> Procedo a realizar otro ejemplo que consiste en conectarme con un terminal al un socket **no seguro** y verificar con *Wireshark* que la confidencialidad de los mensajes es nula.

El código del servidor es este:

```python
#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
#-------------------------------------------------------------------------------
# Name:        server.py
# Purpose:     servidor socket NO seguro
# Author:      DiegoMGuillén
# Contacto:    
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
```

Lo ejecutamos desde PowerShell con `py -3 server.py` y esto sería lo que nos muestra una vez enviamos el mensaje desde el terminal.

![image-20200413100611196](https://github.com/diegostreetbob/SocketsSSL_TLS/blob/master/imagenesP4/image-20200413100611196.png)

### Análisis de tráfico capturado

Esta es la captura realizada con *Wireshark*:

<img src="https://github.com/diegostreetbob/SocketsSSL_TLS/blob/master/imagenesP4/image-20200413101252821.png" alt="image-20200413101252821" style="zoom:150%;" />

Donde  vemos los siguiente:

Línea 17: Cliente envía mensaje a servidor, podemos apreciar que el mensaje enviado es totalmente visible.

![image-20200413101509645](https://github.com/diegostreetbob/SocketsSSL_TLS/blob/master/imagenesP4/image-20200413101509645.png)

Línea 18: El servidor responde, y también podemos ver claramente el mensaje enviado por este.

![image-20200413101620093](https://github.com/diegostreetbob/SocketsSSL_TLS/blob/master/imagenesP4/image-20200413101620093.png)



<div class="page-break"></div>

***

# Enlaces de interés.

Repositorio para el ejemplo mostrado de sockets seguros: 

https://github.com/diegostreetbob/SocketsSSL_TLS

Repositorio para el ejemplo mostrado de sockets no seguros: 

https://github.com/diegostreetbob/SocketNO_SSL_TLS

# Referencias bibliográficas.

https://docs.python.org/3.7/library/ssl.html



<div class="page-break"></div>
