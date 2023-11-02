{
    "name": "Corporate IT Services",
    "version": "15.0.0.0.1",
    "category": "Services",
    "summary": "Corporate IT Services",
    "author": "Bizzappdev",
    "website": "https://www.bizzappdev.com",
    "depends": ["base", "mail", "hr"],
    "data": [
        "security/ir.model.access.csv",
        "data/mail_template_data.xml",
        "data/applications_sequence_generate_views.xml",
        "data/ir_cron_data.xml",
        "wizard/applicant_wizard_views.xml",
        # "views/department_views.xml",
        "views/applicant_stage_views.xml",
        "views/applicant_category_views.xml",
        "views/applicant_views.xml",
        "views/job_position_views.xml",
        "views/corporate_it_services_menu_views.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "Other proprietary",
}
