from odoo import fields, models, api


class PartnerLevel(models.Model):
    _name = 'partner.level'
    _description = 'Level Customer'

    name = fields.Text('Level name', required=True)
    loyalty_point = fields.Float('Level Point', required=True)
    description = fields.Text('Level Description ')
