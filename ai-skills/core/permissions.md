## Permissions Rules

**เป้าหมาย:** กัน agent แจก permission เกินความจำเป็น และแยกระดับสิทธิ์ให้ชัด

### หลักทั่วไป
- ใช้แนวคิด **least privilege** – ให้สิทธิ์เท่าที่จำเป็นต่อหน้าที่ของ role นั้น ๆ
- หลีกเลี่ยงการให้สิทธิ์ `System Manager` หรือ `Administrator` กับ user ปกติ
- ถ้าสงสัย ให้ถามก่อนเสมอว่า role ไหนควรเห็น/แก้ไขข้อมูลชุดนี้ได้บ้าง

### การออกแบบ Role
- แยก role ตามหน้าที่งาน เช่น `Sales User`, `Sales Manager`, `Accountant`, `Warehouse User`
- ไม่ผูก role กับชื่อคน เช่น `Somchai Role`

### Permission ของ DocType
- เริ่มจากให้สิทธิ์กับ role ใด role หนึ่ง แล้วขยายทีหลัง อย่าเริ่มจาก “ทุก role เห็นได้หมด”
- เวลาแก้ **Role Permission Manager** ให้เขียนสรุปใน commit message หรือ skill file เสมอว่า “เพิ่มสิทธิ์อะไรให้ใคร”

### Server / Client Script ที่เกี่ยวกับสิทธิ์
- หลีกเลี่ยงการ hard-code role ในโค้ด ถ้าเป็นไปได้ให้ใช้ **User Permission / Role Permission** แทน
- ถ้าจำเป็นต้องเช็ค role ในโค้ด ให้ระบุเหตุผลใน comment สั้น ๆ (สำหรับมนุษย์อ่าน) ว่าทำไมใช้วิธีนี้

