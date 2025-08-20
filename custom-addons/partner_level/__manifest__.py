{
    "name": "Partner Level",
    "version": "18.0.1.0.0",
    "summary": "Add configurable user level to contacts",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/res_partner_level_views.xml",
        "views/res_partner_views.xml",
        "data/partner_level_data.xml",
    ],
    "license": "LGPL-3",
    "installable": True,
    "application": False,
    "post_init_hook": "post_init_move_menu"
}