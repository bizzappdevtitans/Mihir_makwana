{
    "name": "Quick Procurement",
    "version": "15.0.0.0.1",
    "category": "Sales/Sales",
    "author": "BizzAppDev",
    "summary": " Quick Procurement for product and variant ",
    "website": "https://www.bizzappdev.com",
    "depends": ["base", "sale", "sale_management", "purchase", "product"],
    "data": [
        "security/ir.model.access.csv",
        "wizard/product_procurement_purchase_order_views.xml",
        "views/product_template_views.xml",
    ],
    "installable": True,
    "license": "Other proprietary",
}
