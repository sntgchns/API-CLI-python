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
    pass

@click.command(name='santi', help='Obtener datos de Santiago Soñora.')
def obtener_dato():
    def cerrar_programa():
        programa = click.prompt('Desea realizar otra consulta? (s/n)', type=str, default='s')
        if programa == 's' or programa == 'S':
            apisanti()
        else:
            click.echo('Gracias por utilizar la API de Santiago Soñora.')
    click.echo('Para obtener datos, ingrese el nombre de la ruta: ')
    try:
        # resultado_rutas = personal.find_one({'_id': rutas})
        click.echo(list(rutas['Rutas']['rutas']))
        ruta = click.prompt('Ingrese la ruta', type=str)
        try:
            resultado_ruta = personal.find_one({'_id': ruta})
            if ruta != 'intereses':
                click.echo(list(resultado_ruta[ruta.capitalize()]))
                valor = click.prompt('Ingrese el dato a buscar', type=str)
                click.echo(resultado_ruta[ruta.capitalize()][valor])
                cerrar_programa()
            else:
                click.echo(list(resultado_ruta[ruta.capitalize()]))
                cerrar_programa()
        except KeyError:
            click.echo('El valor "{}" no es válido'.format(valor))
            cerrar_programa()
    except TypeError:
        click.echo('La ruta "{}" no es válida.'.format(ruta))
        cerrar_programa()

apisanti.add_command(obtener_dato)

if __name__ == '__main__':
    apisanti()