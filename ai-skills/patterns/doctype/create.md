## Pattern: Create New DocType (with basic fields)

**Use this when:** ต้องการให้ agent ช่วยออกแบบและสร้าง DocType ใหม่ใน custom app

### Inputs (เติมให้ครบก่อนสั่ง)
- Business purpose: อธิบายว่า DocType นี้ใช้ทำอะไร ในกระบวนการไหน
- Relations: ต้อง link กับ DocType ไหนบ้าง (เช่น Customer, Item)
- Fields: รายการ field ที่ต้องการ (label + type + คำอธิบายสั้น ๆ)
- Permissions: role ไหนควรอ่าน/เขียน/สร้าง/ลบ ได้

### Steps the agent should follow
1. แปลง requirement ด้านบนให้เป็นตาราง fields (fieldname, label, type, options, required, description)
2. เสนอชื่อ DocType (Title Case) และ module ที่เหมาะสม
3. ออกแบบ permissions เบื้องต้นตาม `core/permissions.md`
4. ระบุไฟล์/คำสั่งที่ต้องใช้ (เช่น `bench new-app`, `bench --site ... install-app`, update ใน `doctype` JSON)

### Output format (strict)
- Summary: สรุป business purpose ของ DocType
- Fields Table: Markdown table ของ fields ทั้งหมด
- Permissions Plan: รายการ role + level ของสิทธิ์
- Implementation Plan: ลำดับขั้นตอนที่จะลงมือในโค้ด (ไม่ต้องเขียนโค้ดเต็มในไฟล์นี้)

