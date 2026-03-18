## Frappe / ERPNext AI skills

โฟลเดอร์นี้ใช้เป็น “คู่มือ + แม่แบบ” สำหรับช่วย AI ทำงานกับ Frappe/ERPNext ในโปรเจกต์นี้

- `core/` – กฎกลางที่ต้องยึดตามเสมอ (naming, permissions, conventions)
- `knowledge/` – เอกสารอ้างอิงของ Frappe/ERPNext (hooks, doctypes, api) ใช้เป็น context ประกอบ ไม่ใช่ template generate โค้ดตรง ๆ
- `patterns/` – แม่แบบ prompt สำหรับ generate โค้ด (doctype, api, client script, server script)
- `examples/` – ตัวอย่างโค้ดจริง/เกือบจริง ใช้เป็น few-shot ให้ agent เลียนแบบสไตล์

หลักการใช้ (สรุป):
1. อ่านไฟล์ใน `core/` ก่อนเสมอ เวลาให้ agent แตะ code/doctype ใหม่
2. เวลาอยากให้ agent generate โค้ด ให้เลือกไฟล์ใน `patterns/` ที่ตรงกับงาน แล้วทำตาม structure ข้างในไฟล์นั้น
3. ถ้างานเกี่ยวกับ feature ของ ERPNext/Frappe โดยตรง ให้เปิดไฟล์ใน `knowledge/` เพิ่มเป็น context เพื่อกัน agent มั่ว

