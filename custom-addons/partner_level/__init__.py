from . import models


from odoo import api, SUPERUSER_ID

def post_init_move_menu(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    # Our menu
    menu = env.ref('partner_level.menu_partner_level_root', raise_if_not_found=False)
    if not menu:
        return
    # Try a list of likely XMLIDs first
    xmlids = [
        'contacts.menu_contacts_configuration',
        'contacts.menu_contacts_config',
        'contacts.menu_contacts',
        'contacts.menu_all_contacts',  # just in case
    ]
    parent = None
    for xid in xmlids:
        parent = env.ref(xid, raise_if_not_found=False)
        if parent:
            break
    # If still not found, try to locate a menu named "配置" / "Configuration" under Contacts
    if not parent:
        Menu = env['ir.ui.menu']
        candidates = Menu.search([('name', 'in', ['配置', 'Configuration'])])
        for cand in candidates:
            # climb up to root and see if any ancestor looks like Contacts
            p = cand.parent_id
            while p:
                if p.name in ('联系人', 'Contacts'):
                    parent = cand
                    break
                p = p.parent_id
            if parent:
                break
    # As a final fallback, leave it under Settings -> Custom (base.menu_custom)
    if parent and parent.id != menu.parent_id.id:
        menu.write({'parent_id': parent.id})
