from odoo import fields, models, api


class ResConfigSetting(models.Model):
    _name = 'config.setting'
    loyalty_email_notify = fields.Boolean('check')
