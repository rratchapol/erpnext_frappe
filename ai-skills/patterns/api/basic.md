## Pattern: Basic API (whitelisted method)

**Use this when:** ต้องการให้ agent สร้าง endpoint ง่าย ๆ เช่น create/update/read ข้อมูลเฉพาะเคส

### Inputs
- Business use-case ของ API (ใครเรียก ใช้ทำอะไร)
- Input parameters ที่ต้องรับ (ชื่อ + type + validation คร่าว ๆ)
- Output structure ที่ต้องการ (fields สำคัญ ๆ)
- Permission model: role / user group ไหนควรใช้ได้

### Steps the agent should follow
1. เสนอชื่อ Python method และ path `/api/method/...` ที่สื่อความหมาย
2. ออกแบบ signature ของ function พร้อม type hints
3. ระบุว่า logic จะใช้ DocType ไหนบ้าง (ผ่าน `frappe.get_doc`, `frappe.get_all`, ฯลฯ)
4. กำหนดโครงสร้าง response ให้สม่ำเสมอ เช่น `{ "data": ..., "message": "", "success": true }`

### Output format
- API Spec (human readable): method, path, inputs, outputs, permission
- Implementation Plan: ไฟล์ไหน, function อะไร, ต้อง import อะไร

