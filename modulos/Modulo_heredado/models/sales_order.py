from odoo import api,fields,models

class Ventaheredado(models.Model):
    _inherit="sale.order"
    
    confirmed_user_id=fields.Many2one('res.users',string="Usuario Confirmado")
    approved_user_id=fields.Many2one('res.users',string="Usuario Aprobado")
    create_user_id=fields.Many2one('res.users',string="Usuario Aprobado")