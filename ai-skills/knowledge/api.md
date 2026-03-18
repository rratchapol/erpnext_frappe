## API – Overview

ERPNext/Frappe มี REST API มาตรฐาน เช่น:
- `GET /api/resource/{DocType}` – list records
- `GET /api/resource/{DocType}/{name}` – get one
- `POST /api/resource/{DocType}` – create
- `PUT /api/resource/{DocType}/{name}` – update

เวลาออกแบบ custom API:
- ถ้าเป็น business logic บางอย่างที่ค่อนข้างพิเศษ ให้ใช้ `frappe.whitelist()` ประกาศ method แล้วเรียกผ่าน `/api/method/...`
- ถ้าต้องการ API แบบ resource-based ใหม่ ใช้ DocType + Permission ควบคุมการเข้าถึงเป็นหลัก

