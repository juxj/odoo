{
    "name": "Partner Level",
    "version": "18.0.1.0.0",
    "category": "Contacts",
    "summary": "Add level management for partners",
    "description": """
        Partner Level Management
        ========================
        
        This module adds partner level functionality:
        * Add level field to partners
        * Predefined levels: Bronze (1), Gold (2), Diamond (3)
        * Level configuration menu in Contacts
        * Create, edit, delete levels
    """,
    "author": "Your Name",
    "license": "LGPL-3",
    "depends": ["base", "contacts"],
    "data": [
        "security/ir.model.access.csv",
        "data/partner_level_data.xml",
        "views/partner_level_views.xml",
        "views/res_partner_views.xml",
    ],
    "installable": True,
    "auto_install": False,
    "application": False,
}
