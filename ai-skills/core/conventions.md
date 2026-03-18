## Project Conventions (Frappe / ERPNext)

### Database & Multisite
- โปรเจกต์นี้รัน Frappe/ERPNext ด้วย Docker (ดู `docker-compose.yml`)
- ทุก site แยกข้อมูลกันอย่างชัดเจน ใช้ `SITE_NAME` จาก environment variable ใน container

### Custom App
- ทุก customization ระดับโค้ด (doctype ใหม่, api, server script จำนวนมาก) ควรอยู่ใน **custom app** ไม่ทำใน Core App โดยตรง
- อ้างอิงคู่มือสร้าง app: `https://docs.frappe.io/framework/user/en/tutorial/create-an-app`

### Fixtures / Seed Data
- Seed data ให้ใช้ **fixtures** เป็นหลัก แทนการ insert ข้อมูลตรงจาก script แบบ ad-hoc
- ตั้งชื่อ fixture file ให้สื่อความหมาย เช่น `customer_groups.json`, `default_taxes.json`

### Workspace / Dashboard
- เวลาแก้ workspace (dashboard) ให้คิดจาก use-case จริงของผู้ใช้ เช่น Sales / Accounting / Warehouse
- ไม่ควรสร้าง workspace ซ้ำกับของ ERPNext ถ้าไม่จำเป็น ให้ขยาย/ปรับของเดิมก่อน

