from odoo import models, fields, _, api


class LostMessageParent(models.Model):
    _name = 'lost.message.parent'
    _description = 'Lost Message Parent'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char()
    schedule_send_ids = fields.One2many(
        'schedule.send',       # Model related
        'res_id',              # Field connect this relation
        string='Scheduled Messages'   # name field for show
    )


class ScheduleSend(models.Model):
    _name = 'schedule.send'
    _description = 'Scheduled Message'

    attachment_ids = fields.Many2many('ir.attachment', string='Attachments')
    await_cron = fields.Boolean('Await Cron')
    body = fields.Html('Contents')
    can_write = fields.Boolean('Can Write')
    extra_vals = fields.Char('Extra Values')
    name = fields.Char('Message Name')
    model = fields.Char('Related Document Model')
    res_id = fields.Many2one('lost.message.parent', string='Parent Lost Message')
    schedule_send = fields.Datetime('Scheduled on')
    subject = fields.Char('Subject')
