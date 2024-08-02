from odoo import models,fields


class PaymentCash(models.Model):
    _inherit = 'payment'
    _description = 'payment management'

    Cash = fields.Boolean("Cash", default=False)


