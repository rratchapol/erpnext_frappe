\"\"\"Example: Extend Sales Order behavior.

NOTE: This file is for AI few-shot reference only, not necessarily imported by the app yet.
\"\"\"

import frappe


def validate_sales_order(doc, method=None):
    \"\"\"Example validation hook for Sales Order.

    Business rules (example):
    - Prevent negative qty
    - Ensure posting_date is not in the far past
    \"\"\"
    for item in doc.items:
        if item.qty <= 0:
            frappe.throw(\"Quantity must be greater than zero.\")

