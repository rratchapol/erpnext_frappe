## Doctypes – Overview

หลักที่อยากให้ agent จำเวลาแตะ DocType:

- Frappe/ERPNext ใช้ DocType เป็นตัวแทน table และ business object
- แบ่งเป็น:
  - Core DocType ของ ERPNext (เช่น `Sales Order`, `Customer`, `Item`)
  - Custom DocType ใน custom app ของเรา

แนวทาง:
- อย่าแก้โครงสร้าง Core DocType หนัก ๆ ถ้าไม่จำเป็น (หลีกเลี่ยง breaking change เวลา upgrade)
- ถ้าต้องการเก็บข้อมูลเพิ่ม ให้ใช้:
  - Custom Field บน Core DocType
  - หรือสร้าง Custom DocType ใหม่ แล้ว link กลับไปที่ DocType หลัก

