{
    "name": "Partner extension",
    "version": "1.0",
    "summary": "Extends res.partner model",
    "description": "Adds custom fields to the res.partner model and updates the view.",
    "author": "Fer",
    "depends": ["base", "sale"],
    "data": [
        "security/ir.model.access.csv",
        "views/res_partner_views.xml",
        "views/location_fields_views.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
