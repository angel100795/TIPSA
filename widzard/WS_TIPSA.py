# -*- coding: utf-8 -*-


from openerp import _, api, fields, models


class etiqueta(models.Model):
    _name = 'tipsa.etiqueta'
    _description = 'Datos para etiqueta'
    agencia = fields.Char('Agencia')
    albaran = fields.Char('Albaran', required=True)


