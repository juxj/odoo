from odoo import models, fields, api


class PartnerLevel(models.Model):
    _name = 'partner.level'
    _description = 'Partner Level'
    _order = 'rank, name'

    name = fields.Char('Level Name', required=True, translate=True)
    rank = fields.Integer('Rank', required=True, default=1, help="Lower rank has higher priority")
    color = fields.Integer('Color Index', default=0)
    active = fields.Boolean('Active', default=True)
    description = fields.Text('Description')
    
    partner_count = fields.Integer('Partners Count', compute='_compute_partner_count')

    @api.depends()
    def _compute_partner_count(self):
        for level in self:
            level.partner_count = self.env['res.partner'].search_count([
                ('partner_level_id', '=', level.id)
            ])

    def action_view_partners(self):
        """Action to view partners with this level"""
        return {
            'name': f'Partners - {self.name}',
            'type': 'ir.actions.act_window',
            'res_model': 'res.partner',
            'view_mode': 'list,form',
            'domain': [('partner_level_id', '=', self.id)],
            'context': {'default_partner_level_id': self.id},
        }

    _sql_constraints = [
        ('unique_rank', 'unique(rank)', 'Rank must be unique!'),
        ('positive_rank', 'check(rank > 0)', 'Rank must be positive!'),
    ]