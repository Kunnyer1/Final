from odoo import fields, models, api


class LoyaltyHistory(models.Model):
    _name = 'loyalty.history'
    _description = 'Customer History'

    partner_id = fields.Many2one(string='Name Promotion', required=True)
    loyalty_points = fields.Float('Point in Category')
    money_spent = fields.Float('Total Money')
    loyalty_point = fields.Float('Save point ', required=True, readonly=True)
    date_order = fields.Datetime('Date Order Complete')
    name = fields.Char('Reference Number')
    note = fields.Text('Note')
