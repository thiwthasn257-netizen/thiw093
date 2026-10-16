# Happy Paw 3

โปรเจกต์ตัวอย่างระบบโรงแรมสัตว์เลี้ยง แยกเป็นชั้นดังนี้:

- **MariaDB** เก็บข้อมูล pets, rooms และ bookings
- **Repository** ติดต่อฐานข้อมูล
- **Service** เป็นชั้นกลางให้ API, UI และ MCP เรียกใช้
- **FastAPI** ให้บริการ REST API ที่พอร์ต 8000
- **NiceGUI** แสดงหน้าเว็บที่พอร์ต 8080
- **FastMCP** เปิดเครื่องมือให้ MCP client เรียกดูข้อมูลสัตว์เลี้ยง

## เตรียมระบบ

ต้องติดตั้ง [uv](https://docs.astral.sh/uv/) และ Docker Compose ก่อน จากโฟลเดอร์โปรเจกต์:

```powershell
Copy-Item .env.example .env
uv sync
docker compose up -d
```

MariaDB จะสร้างตารางและข้อมูลตัวอย่างครั้งแรกที่เริ่ม container โดย SQL เริ่มต้นจะทำงานเฉพาะเมื่อ volume ฐานข้อมูลยังว่าง

## เริ่มใช้งาน

เปิด terminal แยกตามบริการ:

```powershell
uv run uvicorn app.api.main:app --reload --port 8000
```

```powershell
uv run python -m app.ui.main
```

```powershell
uv run python -m app.mcp.server
```

- API: <http://127.0.0.1:8000>
- เอกสาร API: <http://127.0.0.1:8000/docs>
- NiceGUI: <http://127.0.0.1:8080>
- `GET /pets` และ `GET /pets/{pet_id}` ใช้ข้อมูลจากฐานข้อมูลเดียวกัน

ทดสอบการเชื่อมต่อฐานข้อมูลได้ด้วย:

```powershell
uv run python -m app.database.connection
```

## ตั้งค่า MCP client

เพิ่ม server ในไฟล์ตั้งค่าของ MCP client โดยแก้ path ให้ตรงกับตำแหน่งโปรเจกต์และ Python ใน `.venv`:

```json
{
  "mcpServers": {
    "happy_paw3": {
      "command": "C:\\path\\to\\happy_paw3\\.venv\\Scripts\\python.exe",
      "args": ["-m", "app.mcp.server"],
      "env": {
        "PYTHONPATH": "C:\\path\\to\\happy_paw3"
      }
    }
  }
}
```

FastMCP ใช้ stdio สำหรับ MCP client ส่วน FastAPI และ NiceGUI ทำงานเป็นเว็บแอปแยกกัน

## หมายเหตุ

- ค่ารหัสผ่านใน `.env.example` มีไว้สำหรับการพัฒนาในเครื่องเท่านั้น อย่าใช้กับระบบจริง
- แก้ `.env` ได้ตามต้องการ โดยค่าฐานข้อมูลสำหรับแอปและ MariaDB ต้องสอดคล้องกัน
- หากต้องการเริ่มฐานข้อมูลใหม่ทั้งหมด ให้หยุด container และลบ volume `happy_paw3_data` ด้วยคำสั่ง `docker compose down -v` ข้อมูลใน volume จะถูกลบ
