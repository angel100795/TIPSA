#-*- coding:utf-8 -*-

from openerp import _, api, fields, models
from suds.client import Client

class tipsa_servicio(models.Model):
    _name = 'tipsa.servicio'
    _description = 'Integracion'
    name = fields.Char('Nombre del servicio')
    url_login = fields.Char('URL login', required=True)
    url_accion = fields.Char('URL accion', required=True)
    agencia = fields.Char('Agencia')
    user = fields.Char('Usuario', required=True)
    password = fields.Char('Contraseña', required=True)
    opcion = fields.Selection([('Etiqueta','Generar Etiqueta')],
        'Opcion', required=True)



    @api.multi
    def conect(self):
        client = Client(self.url_login)
        print client


