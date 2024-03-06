from dataclasses import field
from pydoc import html
import string
from turtle import color

from pkg_resources import require
from odoo import api, fields, models

class Sopoorte(models.Model):
    _name = 'soporte'
    ticket =   fields.Char(string='Ticket')
    titulo = fields.Char(string='Titulo')
    solicitud = fields.Char(html='Solicitud')
    descripcion = fields.Char(string='Descripcion')
    mejora
    