โครงสร้าง

- API1: รับ request จาก user → ส่งต่อไปยัง API2 → ตอบกลับ
- API2: ตอบกลับข้อความจาก endpoint `/hello`
- มี log `print()` แสดงทุกขั้นตอน

วิธีใช้งาน

1. Clone Repo หรือสร้างไฟล์ตามนี้
2. รันคำสั่งนี้:
```bash
docker-compose up --build
```

3. ทดสอบผ่านเบราว์เซอร์หรือ curl:
```bash
http://localhost:5000/call-api2
```

ผลลัพธ์ที่ได้:
```json
{
  "from": "API1",
  "api2_response": {
    "message": "Hello from API2!"
  }
}
```

วิธีทดสอบ
- API1 จะ print log เมื่อได้รับ request
- API2 จะ print log เมื่อถูกเรียกจาก API1
