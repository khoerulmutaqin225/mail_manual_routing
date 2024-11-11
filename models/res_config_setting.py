from odoo import models, fields, _, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    lost_allowed_model_ids = fields.Many2many('ir.model')
    lost_allowed_model_ids_str = fields.Char()
    notify_about_lost_messages = fields.Boolean()
    notify_lost_user_ids = fields.Many2many('res.users')
    notify_lost_user_ids_str = fields.Char()
