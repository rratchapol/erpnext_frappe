## Pattern: Server Script / Backend Logic

**Use this when:** ต้องการให้ agent ออกแบบ/เขียน logic ฝั่ง server (Python) เช่น validation หนัก ๆ, background job, integration

### Inputs
- DocType / Feature เป้าหมาย
- Trigger: ใช้ event อะไร (`validate`, `before_submit`, scheduler, webhook ฯลฯ)
- Business rules แบบละเอียด

### Steps the agent should follow
1. แยก logic ที่ควรอยู่ใน:
   - DocType class (เช่น method `validate`, `on_submit`)
   - Server Script (ใน UI) ถ้าเป็น single function
   - Background job (ผ่าน `frappe.enqueue`) ถ้าต้องใช้เวลานาน
2. คิดถึง error handling และ logging (`frappe.log_error`) สำหรับเคสผิดปกติ
3. อ้างอิง `core/permissions.md` ถ้า logic เกี่ยวกับสิทธิ์ผู้ใช้

### Output format
- Logic Summary
- Event / Trigger Mapping
- Implementation Plan: class/method/function ไหน, อยู่ไฟล์ไหน

