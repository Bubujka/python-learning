#!/usr/bin/env python3
"""Puffy +_+"""

import click

@click.group()
def cli():
    pass

@click.command()
@click.option('--engine', type=float, help='Тип базы данных')
@click.argument('name')
def initdb(engine, name):
    print(engine, name)
    click.echo('initing')

@click.command()
def dropdb():
    click.echo('droping')

cli.add_command(initdb)
cli.add_command(dropdb)

if __name__ == '__main__':
    cli()


# # @click.command()
# def hello():
#     """ Do magic """
#     click.echo('Helo world')
#
# if __name__ == '__main__':
#     hello()
