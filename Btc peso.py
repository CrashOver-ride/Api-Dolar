#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  clase1_3.py
#  
#  Copyright 2020 Crash Override
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  

#importamos las biblitecas nesesaria para operar el scrip
import requests
from influxdb import InfluxDBClient
import time

#Datos de del Host de la base de datos(ip,puerto,usuario,contraseña)
client = InfluxDBClient(host='192.168.0.200', port=8086, username='fedelopez47', password='1234' )
#Nombre de la base de datosexit
client.switch_database('Dolar')


while True:

 #Url de la API que se hace el pedido
 r = requests.get("https://criptoya.com/api/buenbit/btc/ars")
 #Obtecion de los datos que se va a enviar a la base de datos
 datos = r.json()

 #Empezamos el proceso de Transformación de data 

 compra = datos["ask"]
 #llamamos la parte de la api que nos intera
 compra =float(compra)
 #Transformamosa float los datos (esto facilita la lectura de otros servicio como grafana)
 
 #Empezamos el proceso de Transformación de data otra Vez


 venta = datos["bid"]
 #llamamos la parte de la api que nos intera
 venta  =float(venta)
 #Transformamosa float los datos (esto facilita la lectura de otros servicio como grafana)
 
 
 #usamos la funcion time para grabar el tiempo en la base de datos
 fecha =time.asctime()

 #finalisa el proceso de transformacio de data

 #realizamos un print para "ver" como marcha todo
 print(fecha,compra,venta)

 #se trasnforma la data en un json que entienda la base de datos (Influxdb)
 json_body = [ {  
  #nombre de la tabla de la base de datos(measurement)        
 "measurement": "BTC",                   
 "tags": {                   
          "X-Moneda": "Pesos",                  
 },                
 #datos a cargar (aka compra,venta,fecha del dolar)               
 "fields": {   
        "Compra": (compra) , 
        "Venta":  (venta) ,
        "Fecha":  (fecha)               
  }          }     ] 
 
 #Se graba los datos en la base de datos
 client.write_points(json_body)  

 #Con este comando regualamos las llamadas a la api (evitar que te bloque el server)
 time.sleep(300)




