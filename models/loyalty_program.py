# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LoyaltyProgram(models.Model):
    _name = 'loyalty.program'
    _description = 'Program Promotion'

    name = fields.Char('Promotion', required=True)
    point = fields.Float('Point', required=True)
    active = fields.Boolean('Check Promotion', required=True)

# @api.depends('value')
# def _value_pc(self):
#     for record in self:
#         record.value2 = float(record.value) / 100
