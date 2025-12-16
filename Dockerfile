# 1. Base Image: ใช้ Python รุ่นที่มั่นคงเพื่อรัน Logic Engine
FROM python:3.11-slim

# 2. Set Working Directory: กำหนดไดเรกทอรีทำงานภายในคอนเทนเนอร์
WORKDIR /app

# 3. Copy Requirements: คัดลอกไฟล์ requirements.txt มาก่อน (สมมติว่ามีไฟล์นี้)
#    ไฟล์นี้จะบรรจุ libraries ที่ Logic Engine ของเราต้องใช้
COPY requirements.txt .

# 4. Install Dependencies: ติดตั้ง Libraries ที่จำเป็น
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy Application Code: คัดลอก Logic Code ทั้งหมดของโปรเจกต์
#    เครื่องหมายจุด . สองตัว หมายถึง คัดลอกทุกอย่างจากไดเรกทอรีปัจจุบัน
COPY . .

# 6. Expose Port: เปิด Port ที่ Logic Engine ของเราจะใช้ (สมมติว่าเป็น Port 8000)
#    ระบบ API ของเราจะรับ Logic Command ผ่าน Port นี้
EXPOSE 8000

# 7. Start Command: คำสั่งเริ่มต้น Logic Engine เมื่อคอนเทนเนอร์ถูกรัน
#    ปรับ 'your_app_file.py' เป็นชื่อไฟล์หลักที่รัน API ของท่าน
CMD ["python", "main_nexus_api.py"]
