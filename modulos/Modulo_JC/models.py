from odoo import models,fields,api

# class modulojc1(models.Model):
#     _name="modulo.jc1"
    
#     name=fields.Char
    
class Clase_condicion_pago(models.Model):
    _name="condicionpagojc"
    
    cod_cond_pago=fields.Char("Codigo")
    name=fields.Char("Plazo de Pago")
    tipo_cond_pago=fields.Selection([('draft','borrador'),('progress','proceso')])
    
class Clase_producto(models.Model):
    _name="productojc"
    
    cod_product=fields.Char("Codigo")
    name=fields.Char("Nombre")
    precio_product=fields.Float("Precio")
    estado_product=fields.Selection([('available','disponible'),('stock','reservado')])
    category_product=fields.Selection([('clothes','ropa'),('tools','herramientas'),('food','comida')])
    tipo_product=fields.Boolean("Tipo")
    
class Clase_empleado(models.Model):
    _name="empleadojc"
    
    cod_empleadojc=fields.Char("Codigo")
    name=fields.Char("Nombre")
    
class Clase_clientejc(models.Model):
    _name="clientejc"
    
    cod_cliente=fields.Char("Codigo")
    name=fields.Char("Nombre")
    condicion_pago_cliente=fields.Many2one("condicionpagojc", string="Condicion de Pago")
    
class Clase_ventajc(models.Model):
    _name="ventasjc"
    
    cod_venta=fields.Char("Codigo")
    cliente_venta=fields.Many2one("clientejc",string="Cliente")
    tag_id=fields.Many2many("empleadojc",string="Tags")
    condicion_pago_cliente=fields.Many2one(string="Condicion", related="cliente_venta.condicion_pago_cliente")
    producto_linea_id=fields.One2many("lineaventajc","clase_id",string="Lineas de Clase")

class Clase_ventalineajc(models.Model):
    _name="lineaventajc"
    _description="Clase lineas Ventas JC"
    
    @api.depends("price_unit","qty")
    def _compusubtotal(self):
        
        for rec in self:
            rec.lineatotal=rec.price_unit*rec.qty
    
    product_id=fields.Many2one("productojc",string="Producto")
    price_unit=fields.Float(string="Precio",related="product_id.precio_product")
    qty=fields.Integer("Cantidad")
    lineatotal=fields.Float("Total",compute="_compusubtotal")
    clase_id=fields.Many2one("ventasjc","Clase")