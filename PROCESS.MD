# PROCESS.MD — คู่มือทำ TASK.MD ตั้งแต่ต้นจนครบ

> คู่มือนี้เขียนจากประสบการณ์จริง รวม pitfall ที่เจอและวิธีแก้ไว้ด้วย

---

## สารบัญ

1. [Setup Frappe Framework ด้วย Docker](#1-setup-frappe-framework-ด้วย-docker)
2. [สร้าง New Site และติดตั้ง ERPNext](#2-สร้าง-new-site-และติดตั้ง-erpnext)
3. [สร้าง Custom App](#3-สร้าง-custom-app)
4. [Customize Field ของ DocType ใน ERPNext](#4-customize-field-ของ-doctype-ใน-erpnext)
5. [สร้าง DocType ใหม่](#5-สร้าง-doctype-ใหม่)
6. [Seed Data ด้วย Fixtures](#6-seed-data-ด้วย-fixtures)
7. [Inject Custom JavaScript เข้า Form](#7-inject-custom-javascript-เข้า-form)
8. [สร้าง Dashboard / Workspace](#8-สร้าง-dashboard--workspace)
9. [สร้าง New Site เพิ่มใน Container เดิม](#9-สร้าง-new-site-เพิ่มใน-container-เดิม)

---

## 1. Setup Frappe Framework ด้วย Docker

### 1.1 โครงสร้างโปรเจกต์

```
frappe_erpnext/
├── docker-compose.yml   ← กำหนด services
├── .env                 ← ตัวแปร environment (ยังไม่มีต้องสร้าง)
└── apps/
    └── red_queen_custom/   ← custom app (จะสร้างใน step 3)
```

### 1.2 สร้างไฟล์ .env

สร้างไฟล์ `.env` ในโฟลเดอร์โปรเจกต์:

```env
DB_PASSWORD=admin
ADMIN_PASSWORD=admin
ERPNEXT_VERSION=v15.0.0
SITE_NAME=mysite.localhost
```

### 1.3 รัน Docker

```powershell
# รันทุก service ใน background
docker compose up -d

# ดู log ระหว่างรอ (ใช้ Ctrl+C เพื่อหยุดดู log ได้ ไม่กระทบ container)
docker logs -f frappe_erpnext-frappe-1
```

### 1.4 เช็กว่าพร้อมแล้ว

รอจนเห็น log ว่า `Starting Frappe Server...` แล้วเปิดเบราว์เซอร์:

```
http://mysite.localhost:8000
```

เข้าสู่ระบบด้วย `Administrator` / `admin`

> **Tip:** ครั้งแรกใช้เวลาหลายนาที เพราะ Frappe ต้อง init database และ install ERPNext

---

## 2. สร้าง New Site และติดตั้ง ERPNext

> ในโปรเจกต์นี้ `docker-compose.yml` ทำขั้นตอนนี้ให้อัตโนมัติแล้ว (`bench new-site` และ `install-app erpnext`)  
> ถ้า site ยังไม่มี หรืออยากสร้างเพิ่มด้วยมือ ให้ทำตาม [ข้อ 9](#9-สร้าง-new-site-เพิ่มใน-container-เดิม)

### เช็ก site ที่มีอยู่

```powershell
docker exec -it frappe_erpnext-frappe-1 bench --site mysite.localhost list-apps
```

ควรเห็น: `frappe`, `erpnext`, `red_queen_custom`

---

## 3. สร้าง Custom App

### 3.1 สร้าง App ใหม่

```powershell
docker exec -it frappe_erpnext-frappe-1 bench new-app red_queen_custom
```

> ระบบจะถามชื่อ, description, publisher, email, license — กรอกตามต้องการ

### 3.2 Copy App ออกมาที่เครื่อง (เพื่อ sync)

```powershell
# รันที่โฟลเดอร์โปรเจกต์
docker cp frappe_erpnext-frappe-1:/home/frappe/frappe-bench/apps/. ./apps/
```

### 3.3 เปิด Volume Mapping ใน docker-compose.yml

ใน `docker-compose.yml` แก้ไข volumes ของ service `frappe` ให้มี:

```yaml
volumes:
  - sites-data:/home/frappe/frappe-bench/sites
  - ./apps/red_queen_custom:/home/frappe/frappe-bench/apps/red_queen_custom
```

แล้ว restart:

```powershell
docker compose up -d
```

### 3.4 ติดตั้ง App เข้า Site

```powershell
docker exec -it frappe_erpnext-frappe-1 bench --site mysite.localhost install-app red_queen_custom
```

### 3.5 Install Python Package (สำคัญ — ป้องกัน ModuleNotFoundError)

```powershell
docker exec -it frappe_erpnext-frappe-1 /home/frappe/frappe-bench/env/bin/python -m pip install -e /home/frappe/frappe-bench/apps/red_queen_custom
```

### 3.6 Build Frontend และ Restart

```powershell
docker exec -it frappe_erpnext-frappe-1 bench build
docker compose restart frappe
```

### 3.7 เปิด Developer Mode

```powershell
docker exec -it frappe_erpnext-frappe-1 bench --site mysite.localhost set-config developer_mode 1
docker compose restart frappe
```

### 3.8 เช็กผลลัพธ์

```powershell
docker exec -it frappe_erpnext-frappe-1 bench --site mysite.localhost list-apps
```

ต้องเห็น `red_queen_custom` ในรายการ

---

## 4. Customize Field ของ DocType ใน ERPNext

ทำผ่าน UI ไม่ต้องใช้ command:

1. ไปที่ **Setup → Customize Form**
2. เลือก DocType ที่ต้องการ เช่น `Customer`
3. เพิ่ม/แก้ไข field ได้เลย
4. กด **Update**

> การ Customize จะบันทึกเป็น Property Setter ใน database ไม่ได้แก้ไข source code

---

## 5. สร้าง DocType ใหม่

### 5.1 สร้างผ่าน UI (วิธีง่ายที่สุด)

1. ไปที่ **Build (เมนูบน) → DocType**
2. กด **New**
3. ตั้งชื่อ เช่น `Customer Visit Log`
4. เลือก Module เป็น `Red Queen Custom`
5. เพิ่ม Fields:

| Field Label     | Fieldname        | Fieldtype    | Required |
|-----------------|------------------|--------------|----------|
| Customer        | customer         | Link (Customer) | ✓     |
| Visit Date      | visit_date       | Date         | ✓        |
| Sales Person    | sales_person     | Data         |          |
| Location        | location         | Data         |          |
| Note            | note             | Small Text   |          |
| Next Action     | next_action      | Small Text   |          |

6. ตั้ง Permissions ตามต้องการ
7. กด **Save**

> **หมายเหตุ:** DocType ที่สร้างผ่าน UI จะบันทึกใน Database เท่านั้น ไม่มี Python Module folder ใน app  
> ซึ่งจะส่งผลต่อการ inject JS (ดูข้อ 7)

---

## 6. Seed Data ด้วย Fixtures

### 6.1 กำหนด Fixtures ใน hooks.py

แก้ไขไฟล์ `apps/red_queen_custom/red_queen_custom/hooks.py`:

```python
fixtures = ["Customer Visit Log"]
```

### 6.2 สร้างข้อมูลใน UI ก่อน

ไปที่ DocType `Customer Visit Log` แล้วสร้าง record ตัวอย่างก่อน 1-2 รายการ

### 6.3 Export Fixtures

```powershell
docker exec -it frappe_erpnext-frappe-1 bench --site mysite.localhost export-fixtures
```

ไฟล์ JSON จะถูกสร้างที่:  
`apps/red_queen_custom/red_queen_custom/fixtures/customer_visit_log.json`

### 6.4 Import Fixtures (ใช้ตอน setup site ใหม่)

```powershell
# ติดตั้ง app แล้ว fixtures จะ import อัตโนมัติ หรือรัน manual:
docker exec -it frappe_erpnext-frappe-1 bench --site mysite.localhost migrate
```

หรือถ้าต้องการ import fixtures เฉพาะ:

```powershell
docker exec -it frappe_erpnext-frappe-1 bench --site mysite.localhost import-fixtures
```

---

## 7. Inject Custom JavaScript เข้า Form

> **⚠️ สำคัญ — เข้าใจก่อน:**  
> มี 2 วิธี inject JS เข้า form:
> - **`doctype_js` ใน hooks.py** → ใช้ได้เฉพาะ DocType ที่สร้างเป็น Python Module (มีโฟลเดอร์ใน app)
> - **Client Script (UI)** → ใช้ได้กับทุก DocType รวม DocType ที่สร้างจาก UI
>
> DocType `Customer Visit Log` สร้างจาก UI → ต้องใช้ **Client Script**

---

### วิธีที่ 1: Client Script ผ่าน UI (แนะนำ)

1. ไปที่ **Build → Client Script**
2. กด **New**
3. กรอกข้อมูล:
   - **DocType**: `Customer Visit Log`
   - **Name**: `Customer Visit Log Welcome`
   - **Script**:

```javascript
frappe.ui.form.on('Customer Visit Log', {
    refresh(frm) {
        console.log('Custom JS loaded!');
        frappe.msgprint('Welcome to Customer Visit Log!');
    }
});
```

4. กด **Save**
5. Clear cache และ Hard Refresh:

```powershell
docker exec -it frappe_erpnext-frappe-1 bench --site mysite.localhost clear-cache
```

แล้วกด **Ctrl+Shift+R** (hard refresh) ในเบราว์เซอร์

> **⚠️ Pitfall — Developer Mode ทำให้ Client Script เป็น readonly:**  
> เมื่อเปิด developer_mode=1, Client Script ใน UI จะเป็น read-only แก้ไขไม่ได้  
> ต้องใช้ **วิธีที่ 2** แทน

---

### วิธีที่ 2: สร้าง/แก้ไข Client Script ผ่าน Browser Console (Developer Mode)

เปิด Browser DevTools → Console → วางโค้ดนี้:

#### สร้าง Client Script ใหม่:

```javascript
frappe.call({
    method: 'frappe.client.insert',
    args: {
        doc: {
            doctype: 'Client Script',
            name: 'Customer Visit Log Welcome',
            dt: 'Customer Visit Log',
            script: `frappe.ui.form.on('Customer Visit Log', {
    refresh(frm) {
        console.log('Custom JS loaded!');
        frappe.msgprint('Welcome to Customer Visit Log!');
    }
});`,
            enabled: 1
        }
    },
    callback: function(r) {
        console.log('Created!', r);
    }
});
```

#### แก้ไข Script ที่มีอยู่แล้ว:

```javascript
frappe.call({
    method: 'frappe.client.set_value',
    args: {
        doctype: 'Client Script',
        name: 'Customer Visit Log Welcome',
        fieldname: 'script',
        value: `frappe.ui.form.on('Customer Visit Log', {
    refresh(frm) {
        console.log('Custom JS loaded!');
        frappe.msgprint('ยินดีต้อนรับสู่ Customer Visit Log!');
    }
});`
    },
    callback: function(r) {
        frappe.msgprint('Updated successfully!');
    }
});
```

หลังจากรันแล้ว:

```powershell
docker exec -it frappe_erpnext-frappe-1 bench --site mysite.localhost clear-cache
```

แล้วกด **Ctrl+Shift+R** ในเบราว์เซอร์ แล้วเปิด form อีกครั้ง

---

### วิธีที่ 3: doctype_js ใน hooks.py (สำหรับ DocType ที่มี Python Module)

> วิธีนี้ใช้ได้เฉพาะ DocType ที่สร้างผ่าน `bench` หรือมี Python Module folder ใน app เท่านั้น

**ขั้นตอน:**

1. สร้างไฟล์ JS ใน app:

```
apps/red_queen_custom/red_queen_custom/public/js/my_doctype.js
```

```javascript
frappe.ui.form.on('My DocType', {
    refresh(frm) {
        frappe.msgprint('Hello from file!');
    }
});
```

2. แก้ไข `hooks.py`:

```python
doctype_js = {
    "My DocType": "public/js/my_doctype.js"
}
```

3. Build และ restart:

```powershell
docker exec -it frappe_erpnext-frappe-1 bench build --app red_queen_custom --force
docker exec -it frappe_erpnext-frappe-1 bench --site mysite.localhost clear-cache
docker compose restart frappe
```

---

## 8. สร้าง Dashboard / Workspace

### 8.1 สร้าง Workspace ใหม่ผ่าน UI

1. ไปที่ **Build → Workspace**
2. กด **New**
3. ตั้งชื่อ เช่น `Red Queen`
4. เลือก **Module**: `Red Queen Custom`
5. กด **Save**

### 8.2 เพิ่ม Shortcuts และ Cards ใน Workspace

หลังจาก save แล้ว กด **Customize** (ปุ่มด้านบนขวา) เพื่อแก้ไข layout:

- **Add Shortcut**: เพิ่ม link ไป DocType, Report หรือหน้าต่างๆ
- **Add Card**: แสดง DocType list
- **Add Chart**: แสดงกราฟจาก Report

### 8.3 เช็กผลลัพธ์

Workspace ใหม่จะปรากฏในแถบซ้ายมือของ ERPNext

> **Tip:** ถ้าไม่เห็น Workspace อาจต้อง clear cache ก่อน:
>
> ```powershell
> docker exec -it frappe_erpnext-frappe-1 bench --site mysite.localhost clear-cache
> ```

---

## 9. สร้าง New Site เพิ่มใน Container เดิม

### เป้าหมาย: ทดสอบว่า 2 sites แยกข้อมูลกันจริง

### 9.1 สร้าง Site ใหม่

```powershell
docker exec -it frappe_erpnext-frappe-1 bench new-site mysite2.localhost --db-host db --mariadb-root-password admin --admin-password admin --no-mariadb-socket
```

### 9.2 ติดตั้ง ERPNext ใน Site ใหม่

```powershell
docker exec -it frappe_erpnext-frappe-1 bench --site mysite2.localhost install-app erpnext
```

### 9.3 ติดตั้ง Custom App (ถ้าต้องการ)

```powershell
docker exec -it frappe_erpnext-frappe-1 bench --site mysite2.localhost install-app red_queen_custom
```

### 9.4 Restart

```powershell
docker compose restart frappe
```

### 9.5 เข้าถึง Site ใหม่

```
http://mysite2.localhost:8000
```

> เบราว์เซอร์ต้องรู้จัก hostname `mysite2.localhost`
> ถ้าเปิดไม่ได้ ให้เพิ่มใน hosts file:
>
> **Windows:** แก้ไข `C:\Windows\System32\drivers\etc\hosts`
>
> ```
> 127.0.0.1  mysite.localhost
> 127.0.0.1  mysite2.localhost
> ```

### 9.6 ทดสอบการแยกข้อมูล

- สร้าง Customer ใน `mysite.localhost`
- เปิด `mysite2.localhost` → ไม่ควรเห็น Customer นั้น
- แต่ละ site มี database แยกกันสมบูรณ์

---

## คำสั่งที่ใช้บ่อย (Quick Reference)

```powershell
# รัน/หยุด Docker
docker compose up -d
docker compose down
docker compose restart frappe

# ดู logs
docker logs -f frappe_erpnext-frappe-1

# Clear cache
docker exec -it frappe_erpnext-frappe-1 bench --site mysite.localhost clear-cache
docker exec -it frappe_erpnext-frappe-1 bench --site mysite.localhost clear-website-cache

# Build frontend
docker exec -it frappe_erpnext-frappe-1 bench build
docker exec -it frappe_erpnext-frappe-1 bench build --app red_queen_custom --force

# Restart bench (ไม่ restart docker)
docker exec -it frappe_erpnext-frappe-1 bench restart

# Migrate database (หลัง install/update app)
docker exec -it frappe_erpnext-frappe-1 bench --site mysite.localhost migrate

# Export fixtures
docker exec -it frappe_erpnext-frappe-1 bench --site mysite.localhost export-fixtures

# เช็ก apps ที่ install
docker exec -it frappe_erpnext-frappe-1 bench --site mysite.localhost list-apps

# เข้า bash ใน container
docker exec -it frappe_erpnext-frappe-1 bash

# Copy files จาก container มาเครื่อง
docker cp frappe_erpnext-frappe-1:/home/frappe/frappe-bench/apps/. ./apps/
```

---

## Pitfalls ที่เจอและวิธีแก้

| ปัญหา | สาเหตุ | วิธีแก้ |
|-------|--------|---------|
| Custom JS ไม่โหลดผ่าน `doctype_js` | DocType สร้างจาก UI ไม่มี Python Module | ใช้ Client Script แทน |
| Client Script เป็น readonly | เปิด developer_mode=1 | แก้ผ่าน Browser Console ด้วย `frappe.client.set_value` |
| `frappe.client.insert` ฟ้อง "Please set the document name" | ต้องระบุ `name` field | เพิ่ม `name: 'ชื่อ script'` ใน doc object |
| หน้า site ไม่ขึ้น / static file ไม่โหลด | assets symlink ไม่ได้สร้าง | รัน `bench build --force` แล้ว restart |
| `ModuleNotFoundError` ตอน restart | Python package ไม่ได้ install | รัน `pip install -e apps/red_queen_custom` |
| เห็นหน้า Setup Wizard หลัง install ERPNext | ยังไม่ได้ทำ setup wizard ครั้งแรก | ทำตาม wizard ให้ครบ |
