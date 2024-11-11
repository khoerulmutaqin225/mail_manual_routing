from odoo import _, api, fields, models

class Message(models.Model):   
    _inherit = 'mail.message'
    
    name = fields.Char()    
    lost_comments = fields.Text()
    is_unattached = fields.Boolean()
    attachment_ids = fields.Many2many('ir.attachment')
    
    def action_attach(self):
        pass
    
    @api.depends('name') 
    def _compute_display_name(self):
        for record in self:
            record.display_name = 'Lost Message'