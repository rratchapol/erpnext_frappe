## Pattern: DocType Validation Logic

**Use this when:** ต้องการให้ agent ออกแบบกติกา validate สำหรับ DocType (เช่น ตรวจ stock, ตรวจ limit, ตรวจวันที่)

### Inputs
- DocType name และ use-case (สั้น ๆ)
- Business rules ที่ต้องการบังคับใช้ (เป็น bullet list)
- Error messages ที่อยากให้แสดง (ถ้ามีสำนวนเฉพาะ)

### Steps the agent should follow
1. แปลง business rules เป็น pseudo-code (if/else) ก่อน
2. ระบุว่า logic ใดควรอยู่ใน:
   - Python server logic (`validate`, `before_save`, `before_submit`, ฯลฯ)
   - Client script (เช่น ป้องกันผู้ใช้กรอกข้อมูลผิดตั้งแต่หน้า UI)
3. เสนอ error message ที่เข้าใจง่ายสำหรับผู้ใช้ธุรกิจ (ไม่ใช่ dev)

### Output format
- Rules Summary: bullet list ของกติกาแต่ละข้อ
- Validation Plan: แยกเป็น server-side vs client-side
- Example Snippets: ตัวอย่าง function signature / event ที่ควรใช้ (ยังไม่ต้องอิมพลีเมนต์เต็มในไฟล์นี้)

