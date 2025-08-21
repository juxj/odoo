from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    partner_level_id = fields.Many2one(
        "partner.level", string="Partner Level", help="Partner level classification"
    )
    partner_level_rank = fields.Integer(
        string="Level Rank", related="partner_level_id.rank", store=True, readonly=True
    )
