from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    location_field = fields.Many2one(
        "partner_extension.location_fields", string="Field"
    )
