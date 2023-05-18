from odoo import api,fields,models

class Product_Heredado(models.Model):
    _inherit="product.template"
    
    status_product=fields.Selection([('Normal','normal'),('Baja rotacion','bajarotacion'),('alternativo','alternativo')])