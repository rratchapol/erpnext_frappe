\"\"\"Example: Simple customer lookup API.

NOTE: Example only, adjust app/module path when integrating.
\"\"\"

import frappe


@frappe.whitelist()
def get_customer_basic(name: str) -> dict:
    \"\"\"Return basic customer info (example shape).

    Response shape:
    {
        \"data\": {...},
        \"success\": true
    }
    \"\"\"
    doc = frappe.get_doc(\"Customer\", name)
    return {
        \"data\": {
            \"name\": doc.name,
            \"customer_name\": doc.customer_name,
            \"customer_group\": doc.customer_group,
        },
        \"success\": True,
    }

