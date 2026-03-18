## Frappe / ERPNext Hooks – Overview

ใช้ไฟล์นี้เป็น reference เวลาออกแบบการเชื่อม app กับ lifecycle ของ Frappe/ERPNext

- ตัวอย่าง hook ที่ใช้บ่อย:
  - `app_name` / `app_title` / `app_publisher` / `app_description`
  - `doctype_js` – map DocType → client script
  - `doctype_list_js` / `doctype_tree_js`
  - `scheduler_events` – กำหนด job ที่รันตามเวลา
  - `override_doctype_class` – override behavior ของ DocType

เวลา agent จะเพิ่ม/แก้ hook:
- ให้ระบุให้ชัดว่าจะแตะไฟล์ `hooks.py` ของ app ไหน
- อธิบายว่าตัว hook ที่เพิ่มจะมีผลกับ DocType/feature ใด

