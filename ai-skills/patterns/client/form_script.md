## Pattern: Client Script for DocType Form

**Use this when:** ต้องการให้ agent เขียน/แก้ JavaScript บนฟอร์ม DocType (เช่น validate หน้า UI, auto-fill, hide/show field)

### Inputs
- DocType name
- Events ที่ต้องการใช้ (เช่น `refresh`, `validate`, `before_save`, field triggers)
- Behavior ที่ต้องการ (business logic ฝั่งหน้าเว็บ)

### Steps the agent should follow
1. สรุป behavior ที่ต้องการเป็น bullet list ง่าย ๆ
2. เลือก event ของ Frappe form ให้เหมาะสมกับแต่ละ behavior
3. ออกแบบโครง JS ที่อ่านง่าย และไม่ผูกกับ DOM ตรง ๆ ถ้าใช้ API ของ Frappe ได้ (`frm`, `cur_frm`)

### Output format
- Behavior Summary
- Event Mapping: event → action
- Implementation Plan: จะไปแตะไฟล์/ตำแหน่งไหน (เช่น Client Script ผ่าน UI, หรือไฟล์ `.js` ใน app)

