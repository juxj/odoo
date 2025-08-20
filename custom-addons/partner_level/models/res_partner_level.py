from odoo import fields, models

class ResPartnerLevel(models.Model):
    _name = "res.partner.level"
    _description = "用户等级"

    code = fields.Char("代码", required=True)
    name = fields.Char("等级名称", required=True, translate=True)
    comments = fields.Text("备注")

    _sql_constraints = [
        ("code_unique", "unique(code)", "代码必须唯一！"),
    ]
