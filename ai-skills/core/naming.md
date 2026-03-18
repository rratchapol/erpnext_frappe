## Naming Rules (Frappe / ERPNext)

**เป้าหมาย:** ให้ชื่อ DocType, field, module, และไฟล์ต่าง ๆ สม่ำเสมอ อ่านง่าย และโยงกับโดเมนธุรกิจได้ทันที

### DocType
- ใช้ชื่อ DocType เป็น **Title Case** ภาษาอังกฤษ เช่น `Sales Order`, `Customer Profile`
- ถ้าเป็น DocType ที่ใช้ภายในเท่านั้น ให้ใส่คำบ่งบอกเช่น `Internal Setting`, `Integration Log`
- หลีกเลี่ยงการใช้ตัวย่อที่ทีมไม่คุ้น เช่น `SO`, `PR` ถ้าไม่จำเป็น

### Field
- `fieldname` ใช้ **snake_case** ภาษาอังกฤษ เช่น `customer_name`, `posting_date`
- ถ้าชื่อ field มีหน่วย เช่น THB, percent, qty ให้ใส่ท้ายชื่อ เช่น `amount_thb`, `discount_percent`, `ordered_qty`
- ชื่อ field ต้องสื่อความหมายจากมุมมองธุรกิจ ไม่ใช่เทคนิค เช่น `tax_rate` แทน `value1`

### Module / App
- app_name ใช้ snake_case เช่น `witsawa_core`, `retail_extension`
- ถ้าสร้าง custom app สำหรับลูกค้าหนึ่งราย ให้มี prefix ลูกค้า เช่น `witsawa_xyz_custom`

### File / Script
- Client Script / Server Script ที่ผูกกับ DocType ใด ให้รวมชื่อ DocType ในชื่อไฟล์ด้วย เช่น:
  - `customer_client_script.js`
  - `sales_order_server_script.py`

