from odoo import fields, models

class ResPartner(models.Model):
    _inherit = "res.partner"

    level_id = fields.Many2one(
        "res.partner.level",
        string="用户等级",
        help="选择该联系人的用户等级",
        index=True,
    )
