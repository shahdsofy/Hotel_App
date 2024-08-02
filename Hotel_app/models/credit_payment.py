from odoo import models,fields


class PaymentCredit(models.Model):
    _inherit = 'payment'
    _description = 'payment management'

    Credit = fields.Boolean("Credit", default=False)

