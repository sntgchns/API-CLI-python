#!/usr/bin/env python
import click, requests


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
            print('Gracias por utilizar la API de Santiago Soñora.')
    click.echo('Para obtener datos, ingrese el nombre de la ruta: ')
    resultado_rutas = requests.get('https://sntgchns.herokuapp.com/api').json()
    click.echo(list(resultado_rutas[3]))
    ruta = click.prompt('Ingrese la ruta', type=str)
    resultado_ruta = requests.get('https://sntgchns.herokuapp.com/api/santi/{}'.format(ruta)).json()
    if ruta != 'intereses':
        click.echo(list(resultado_ruta[ruta.capitalize()]))
        valor = click.prompt('Ingrese el dato a buscar', type=str)
        click.echo(resultado_ruta[ruta.capitalize()][valor])
        cerrar_programa()
    else:
        click.echo(list(resultado_ruta[ruta.capitalize()]))
        cerrar_programa()

apisanti.add_command(obtener_dato)

if __name__ == '__main__':
    apisanti()
