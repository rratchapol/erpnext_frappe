แนวคิดก่อน – ใช้ยังไงให้ไม่งง
เวลาใช้ AI ทำงาน Frappe/ERPNext ให้คิดแบบนี้:

core/ = กติกากลาง (ให้อ่าน/แนบเสมอถ้างานแตะโค้ดหรือ DocType)
knowledge/ = ข้อมูลอ้างอิง (แนบเมื่อเกี่ยวกับ hooks / doctypes / api)
patterns/ = “ฟอร์มงาน” ที่จะให้ AI ทำ (เลือกไฟล์ pattern ให้ตรงงาน)
examples/ = ตัวอย่างโค้ดให้ AI เลียนแบบสไตล์
ต่อไปนี้คือ “ตัวอย่าง prompt” ที่คุณหยิบไปใช้/ดัดแปลงได้เลย

1) ทำตาม TASK.MD ทั้งแพ็ก (ตั้งค่า + เล่น module + custom app เบื้องต้น)
Prompt ตัวอย่าง

ใช้โปรเจกต์ Frappe/ERPNext นี้ที่รันด้วย docker (ดู docker-compose.yml)
อ่าน TASK.MD แล้วช่วยวาง step by step ให้หน่อยว่า

ต้องรันคำสั่งอะไรบ้างบน docker เพื่อ
setup frappe + ERPNext
สร้าง new site และลง ERPNext
สร้าง custom app ใหม่ตาม docs
แต่ละขั้นให้บอกคำสั่งที่ต้องรัน + เช็กยังไงว่าทำสำเร็จ
อย่าเพิ่งเขียนโค้ด แค่วางแผนและ list คำสั่งทีละขั้นให้เข้าใจง่ายสำหรับ beginner

(ตรงนี้ยังไม่ต้องแนบ ai-skills/* ก็ได้ เป็นแค่ setup flow)

2) ให้ AI ช่วย “ออกแบบ DocType ใหม่” ตาม pattern
ไฟล์ที่ควรแนบให้ AI ดู

ai-skills/core/naming.md
ai-skills/core/permissions.md
ai-skills/core/conventions.md
ai-skills/patterns/doctype/create.md
(ถ้าเกี่ยวกับ ERPNext core) เพิ่ม ai-skills/knowledge/doctypes.md
Prompt ตัวอย่าง

ช่วยออกแบบ DocType ใหม่ใน custom app สำหรับเก็บ “Customer Visit Log”

ใช้กติกาจากไฟล์ต่อไปนี้:

ai-skills/core/naming.md
ai-skills/core/permissions.md
ai-skills/core/conventions.md
pattern ai-skills/patterns/doctype/create.md
Requirement:

บันทึกการเยี่ยมลูกค้าแต่ละครั้ง
ต้อง link ไปที่ Customer ของ ERPNext
เก็บ field: วันที่ไปเยี่ยม, ผู้เยี่ยม (Sales User), สถานที่, note สั้น ๆ, next_action
ให้ Sales User สร้าง/แก้ได้ แต่ Manager ปรับแก้ย้อนหลังและลบได้
ทำตาม output format ที่ระบุใน pattern:

Summary
Fields Table
Permissions Plan
Implementation Plan (ลิสต์ขั้นตอน bench / ไฟล์ที่จะต้องสร้าง/แก้)
3) ให้ AI เขียน validation logic สำหรับ DocType นั้น
ไฟล์ที่ควรแนบ

ai-skills/core/*
ai-skills/patterns/doctype/validation.md
ai-skills/patterns/server/server_script.md (ถ้ามีส่วน server)
(ตัวอย่าง) ai-skills/examples/sales_order.py
Prompt ตัวอย่าง

สำหรับ DocType “Customer Visit Log” ที่ออกแบบไว้ก่อนหน้า
ใช้ pattern ใน ai-skills/patterns/doctype/validation.md และ ai-skills/patterns/server/server_script.md
พร้อมดูสไตล์จาก ai-skills/examples/sales_order.py

ช่วยออกแบบ validation rules ดังนี้:

วันที่เยี่ยมต้องไม่อยู่ในอนาคตเกิน 7 วัน
ต้องเลือก Customer เสมอ
ถ้ามี next_action ให้บังคับกรอก note อย่างน้อย 20 ตัวอักษร
ให้ตอบเป็น:

Rules Summary
Validation Plan (อะไรอยู่ฝั่ง server, อะไรใช้ client script)
Example Snippets (pseudo-code / ตัวอย่างฟังก์ชันที่ควรมี)
4) ให้ AI สร้าง custom API ฝั่ง backend
ไฟล์ที่ควรแนบ

ai-skills/core/*
ai-skills/knowledge/api.md
ai-skills/patterns/api/basic.md
ตัวอย่าง ai-skills/examples/customer_api.py
Prompt ตัวอย่าง

อยากได้ custom API สำหรับค้นหา Customer แบบง่าย ๆ
ใช้ pattern ใน ai-skills/patterns/api/basic.md และดูตัวอย่างจาก ai-skills/examples/customer_api.py

Requirement:

method: GET
path: /api/method/… (ให้ช่วยเสนอชื่อ)
input: partial customer_name (string)
output: list ของลูกค้าที่ชื่อ match (ไม่เกิน 20 รายการ) พร้อม fields: name, customer_name, customer_group
เฉพาะผู้ใช้ที่มี role Sales User หรือ Sales Manager เท่านั้นที่เรียกได้
ให้ตอบเป็น API Spec + Implementation Plan โดยยังไม่ต้องเขียนโค้ดเต็ม 100%

5) ให้ AI เขียน client script บนฟอร์ม ERPNext
ไฟล์ที่ควรแนบ

ai-skills/core/*
ai-skills/patterns/client/form_script.md
ai-skills/knowledge/hooks.md (ถ้าจะผูกผ่าน hooks)
Prompt ตัวอย่าง

อยากเพิ่ม client script บน DocType Sales Order
ใช้ pattern ai-skills/patterns/client/form_script.md

Behavior ที่ต้องการ:

เวลาเลือก Customer แล้ว ให้ดึง field customer_group มาแสดงใน read-only field หนึ่ง
ถ้ายอดรวม (grand_total) เกิน 100,000 ให้โชว์ warning บนฟอร์ม
ช่วยออกแบบ:

Behavior Summary
Event Mapping (ใช้ event ของ Frappe อะไรบ้าง)
Implementation Plan (ควรสร้างผ่าน Client Script UI หรือไฟล์ .js ใน app ดีในเคสนี้)
