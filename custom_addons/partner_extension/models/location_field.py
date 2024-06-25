from odoo import models, fields

class LocationField(models.Model):
    _name = 'partner_extension.location_fields'
    _description = 'Fields a.k.a. production site locations'

    name = fields.Char(string='Name', required=True)