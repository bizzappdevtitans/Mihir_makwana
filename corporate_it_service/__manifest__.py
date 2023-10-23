{
    "name": "Corporate IT Services",
    "version": "15.0.0.0.1",
    "category": "Services",
    "summary": "Corporate IT Services",
    "website": "https://github.com/OCA/product-variant",
    "depends": ["base", "mail", "hr"],
    "data": [
        "security/ir.model.access.csv",
        "views/applicant_views.xml",
        "views/job_position_views.xml",
        "views/corporate_it_services_menu_views.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}
