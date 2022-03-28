from odoo import fields, models, api


class LoyaltyCustomer(models.Model):
    _inherit = 'res.partner'
    _description = 'customer_management'

    loyalty_point = fields.Float('Point Customer', readonly=True)
    loyalty_level = fields.Many2one(comodel_name='partner.level', string='Partner Liver:', readonly=True)

