from odoo import models,fields,api
from odoo.exceptions import ValidationError

class PaymentManagement(models.Model):
    _name = 'payment'
    _inherit = 'customer.model'
    _description = 'payment management'

    hotel_payment_id = fields.Integer(string='payment id')
    hotel_payment_date = fields.Date(string='payment date')

    price = fields.Float(string='price')
    currency = fields.Char(string='currency')



    state = fields.Selection([
        ('draft','Make payment'),
        ('in_progress','In Progress...'),
        ('completed','Completed'),
    ],default='draft')


    _sql_constraints = [
        ('hotel_payment_id_uniq', 'unique (hotel_payment_id)', "Tag ID already exists !"),
    ]



    @api.constrains('price')
    def check(self):
        for rec in self:
            if rec.price < 0:
               raise ValidationError('invalid negative value')