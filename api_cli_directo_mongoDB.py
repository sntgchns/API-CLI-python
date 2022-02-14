#!/usr/bin/env python
import click, requests
from pymongo import MongoClient
from config import mongoDB

usuario=mongoDB['usuario']
contraseña=mongoDB['contraseña']
nombre_db=mongoDB['nombre_db']

cluster = 'mongodb+srv://{}:{}@cluster0.jxlaq.mongodb.net/{}?retryWrites=true&w=majority'.format(usuario, contraseña, nombre_db)

client = MongoClient(cluster)
db = client.santi
santi = db.santi

personal = db.personal
instrucciones = db.instrucciones
rutas = db.rutas

instrucciones = instrucciones.find_one({'_id': 'instrucciones'})
rutas = rutas.find_one({'_id': 'rutas'})

click.echo('Bienvenido a la API de Santiago Soñora.')

@click.group()
def apisanti():
    '''
    Mensaje de ayuda:
    'Recorda no usar caracteres especiales, acentos ni espacios en blanco.'
    Gracias por conectarte!'
    '''
    pass

@click.group(name='buscar', help='ruta <nombre_ruta> --valor <nombre_dato>')
def obtener_datos():
    pass

@click.command(name='ruta', help='Obtener ruta de la lista de rutas en la API.')
@click.argument('rutas')
@click.option('--valor', '-v', help='Obtener valor de la ruta en la API.')
def obtener_rutas(rutas, valor):
    resultado_ruta = personal.find_one({'_id': rutas})
    try:
        if not valor:
            click.echo(list(resultado_ruta[rutas.capitalize()]))
        else:
            resultado = resultado_ruta[rutas.capitalize()][valor]
            click.echo('El valor "{}" es "{}"'.format(valor, resultado))
            click.echo('Gracias por utilizar el programa.')
    except KeyError:            
        click.echo('El valor "{}" no es válido'.format(valor))

obtener_datos.add_command(obtener_rutas)

apisanti.add_command(obtener_datos)

if __name__ == '__main__':
    apisanti()
