#!/usr/bin/env python
import click, requests


print('Bienvenido a la API de Santiago Soñora.')

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
    global resultado_ruta, ruta
    resultado_ruta = requests.get('https://sntgchns.herokuapp.com/api/santi/' + rutas).json()    
    if not valor:        
        click.echo(list(resultado_ruta[rutas.capitalize()].keys()))
    else:
        resultado = resultado_ruta[rutas.capitalize()][valor]
        print('{}'.format(resultado))
        print('Gracias por utilizar el programa.')            

obtener_datos.add_command(obtener_rutas)

apisanti.add_command(obtener_datos)

if __name__ == '__main__':
    apisanti()
