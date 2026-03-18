## Pattern: Query API (list/filter)

**Use this when:** ต้องการให้ agent สร้าง endpoint สำหรับ query ข้อมูล (filter, sort, paginate)

### Inputs
- DocType เป้าหมาย
- ฟิลด์ที่อนุญาตให้ filter/sort
- จำนวนเรคคอร์ดสูงสุดต่อหน้า (page size limit)
- Role ที่มีสิทธิ์เข้าถึงข้อมูลชุดนี้

### Steps the agent should follow
1. ออกแบบ parameter สำหรับ filter (เช่น `customer`, `from_date`, `to_date`, `status`)
2. เสนอ query strategy:
   - `frappe.get_list` / `frappe.get_all` พร้อม filter
   - หรือใช้ `frappe.qb` ถ้าจำเป็นต้อง join หลาย table
3. กำหนดรูปแบบผลลัพธ์ เช่น:
   - `data` (list)
   - `total_count`
   - `page` / `page_size`

### Output format
- Query Spec: input params, allowed filters, sorting rules, pagination
- Example Response: โครง JSON ที่คาดว่าจะได้

