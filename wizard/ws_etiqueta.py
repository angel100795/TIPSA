# -*- coding: utf-8 -*-

from openerp import _, api, fields, models
import requests
from requests.auth import HTTPBasicAuth  # or HTTPDigestAuth, or OAuth1, etc.
from suds.transport.http import HttpAuthenticated
from suds.client import Client
import base64


class res_partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

class tipsa_servicio(models.Model):
    _name = 'tipsa.servicio'
    _inherit = 'tipsa.servicio'


class ws_etiqueta(models.Model):
    _name = 'ws.etiqueta'
    _description = 'Datos para etiqueta'
    opcion = fields.Many2one('tipsa.servicio',string="Opcion")
    agencia = fields.Many2one('res.partner', string="Agencia")
    albaran = fields.Char('Albaran', required=True)
    id_reporte = fields.Char('ID del reporte')
    formato = fields.Selection([('1','PDF'),
        ('2','TXT')],default="1")
    bulto_desde = fields.Char('Bulto desde')
    bulto_hasta = fields.Char('Bulto hasta')
    posicion_ini = fields.Char('Posicion inicial')

    @api.multi
    def genera_etiqueta(self):
        url = self.opcion.url_login
        t = HttpAuthenticated()
        client = Client(url, transport=t,
            username=self.opcion.user,
            password=self.opcion.password)
        print ("------------>>>>>", client)












