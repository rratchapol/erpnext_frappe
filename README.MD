services:
กำหนด container หลักที่ระบบนี้ต้องใช้

1. db
image: mariadb:10.6
ใช้ MariaDB เวอร์ชัน 10.6 เป็นฐานข้อมูลหลัก
command:
กำหนด character set และ collation ให้รองรับภาษาไทย/Unicode
environment:
กำหนดรหัสผ่าน root ของ MariaDB จากตัวแปร .env
volumes:
เก็บข้อมูลฐานข้อมูลไว้ใน volume db-data เพื่อความถาวร

2. redis-cache, redis-queue, redis-socketio
image: redis:6.2-alpine
ใช้ Redis 3 ตัว แยกตามหน้าที่ (cache, queue, socketio) ตามมาตรฐาน Frappe/ERPNext

3. frappe
image: frappe/erpnext:${ERPNEXT_VERSION}
ใช้ image ERPNext ตามเวอร์ชันที่กำหนดใน .env
depends_on:
รอให้ db และ redis ทั้ง 3 ตัวพร้อมก่อนเริ่ม
environment:
กำหนดค่าการเชื่อมต่อฐานข้อมูลและ Redis ให้ container รู้จัก
volumes:
sites-data:/home/frappe/frappe-bench/sites
เก็บข้อมูลของ Frappe/ERPNext (config, ไฟล์แนบ, ฯลฯ) ใน Docker volume
(มีตัวเลือกคอมเมนต์ไว้: ./sites:/home/frappe/frappe-bench/sites ถ้าต้องการให้ sync กับโฟลเดอร์บน host)
ports:
"8000:8000"
เปิดพอร์ต 8000 ให้เข้าถึงเว็บแอปจากภายนอก
command:
สั่งรัน bash script หลายขั้นตอน:
รอให้ MariaDB พร้อม
สร้างไฟล์ config common_site_config.json ให้ชี้ไปที่ service ต่าง ๆ ใน docker
สร้างไฟล์ apps.txt ถ้ายังไม่มี (ระบุแอป frappe, erpnext)
สร้าง site ใหม่ถ้ายังไม่มี (ใช้ bench new-site)
ติดตั้งแอป erpnext ใน site
สั่งรัน Frappe Server

4. 
volumes:
db-data:
เก็บข้อมูลฐานข้อมูล MariaDB
sites-data:
เก็บข้อมูลของ Frappe/ERPNext (sites, config, ไฟล์แนบ ฯลฯ)

-------------------------

command ที่ใช้

docker logs -f frappe_erpnext-frappe-1    [ ดู log docker ]

docker compose up -d                      [ docker run ]

docker compose down -v                    [ docker stop ]


--------------------------

# 1. สร้าง App ใหม่
docker exec -it frappe_erpnext-frappe-1 bench new-app red_queen_custom

# 2. ติดตั้ง App เข้า Site
docker exec -it frappe_erpnext-frappe-1 bench --site mysite.localhost install-app red_queen_custom

# 3. Build Frontend (สำคัญมาก)
docker exec -it frappe_erpnext-frappe-1 bench --site mysite.localhost build

# 4. Check 
docker exec -it frappe_erpnext-frappe-1 bench --site mysite.localhost list-apps

# 5. Install App
docker exec -it frappe_erpnext-frappe-1 /home/frappe/frappe-bench/env/bin/python -m pip install -e /home/frappe/frappe-bench/apps/red_queen_custom

# 6. Restart เพื่อให้เห็นผล
docker compose restart frappe   



-----------------------------------------

กรณี css ไม่เเสดง

# 1. ลบ assets เก่าและสร้างใหม่
docker exec -it frappe_erpnext-frappe-1 bash -c "rm -rf sites/assets/* && bench build"

# 2. Clear cache ทุกส่วน
docker exec -it frappe_erpnext-frappe-1 bench --site mysite.localhost clear-cache

# 3. Clear website cache
docker exec -it frappe_erpnext-frappe-1 bench --site mysite.localhost clear-website-cache

# 4. Restart เพื่อให้เห็นผล
docker compose restart frappe   


-------------------------------------------

# 1. ดึงไฟล์ทั้งหมดจาก Docker มาที่เครื่อง (รันที่โฟลเดอร์โปรเจกต์)
docker cp frappe_erpnext-frappe-1:/home/frappe/frappe-bench/apps/. ./apps/

# 2. เปิด comment
- ./apps:/home/frappe/frappe-bench/apps

# 3. รัน docker compose up -d
docker compose up -d


---------------------------------------------

# 1. Export Fixtures
docker exec -it frappe_erpnext-frappe-1 bench --site mysite.localhost export-fixtures

------------------------------------------------

# 1. เปิด Developer Mode ให้กับ Site
docker exec -it frappe_erpnext-frappe-1 bench --site mysite.localhost set-config developer_mode 1

# 2. Restart เพื่อให้ค่าใหม่ทำงาน
docker compose restart frappe
