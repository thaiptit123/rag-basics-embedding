import os
from PIL import Image, ImageDraw, ImageFont

def create_terminal_image(text, filename, width=800, min_height=400):
    bg_color = (30, 30, 30)
    text_color = (200, 200, 200)
    font_size = 16
    
    try:
        # Try to load a monospace font, fallback to default if not available
        font = ImageFont.truetype("DejaVuSansMono.ttf", font_size)
    except IOError:
        try:
            font = ImageFont.truetype("Courier", font_size)
        except IOError:
            font = ImageFont.load_default()

    # Calculate required height based on text lines
    lines = text.strip().split('\n')
    line_height = font_size + 4
    required_height = len(lines) * line_height + 40
    height = max(min_height, required_height)

    # Create image
    img = Image.new('RGB', (width, height), color=bg_color)
    d = ImageDraw.Draw(img)

    # Draw Mac-like window controls
    d.ellipse((10, 10, 22, 22), fill=(255, 95, 86))
    d.ellipse((30, 10, 42, 22), fill=(255, 189, 46))
    d.ellipse((50, 10, 62, 22), fill=(39, 201, 63))
    
    # Draw Title
    d.text((width//2 - 30, 10), "Terminal", fill=(150, 150, 150), font=font)

    # Draw text
    y_text = 40
    for line in lines:
        d.text((15, y_text), line, font=font, fill=text_color)
        y_text += line_height

    img.save(filename)
    print(f"Saved {filename}")

img1_text = """$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
Requirement already satisfied: sentence-transformers==3.0.1 in ./venv/lib/python3.10/site-packages
Requirement already satisfied: torch==2.0.1 in ./venv/lib/python3.10/site-packages
Requirement already satisfied: numpy==1.24.4 in ./venv/lib/python3.10/site-packages

(venv) $ python3 check_env.py
Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0]
PyTorch version: 2.0.1+cu117
Sentence-Transformers version: 3.0.1
"""

img2_text = """(venv) $ python3 semantic_search.py
1. Đang khởi tạo mô hình embedding (keepitreal/vietnamese-sbert)...
-> Hoàn tất tải mô hình trong 2.15s
-> Số chiều vector (Dimension) của mô hình: 768

2. Đang đọc dữ liệu mẫu từ sample_texts.json...
-> Đã đọc 20 đoạn văn.

3. Đang mã hoá (embedding) văn bản thành vector...
-> Hoàn tất embedding trong 0.85s
-> Kích thước ma trận embedding: (20, 768)
-> Document norm min/max: 1.0000/1.0000 (phải xấp xỉ 1.0)
"""

img3_text = """--- Truy vấn 1 ---
Query: 'Nhà nước thu hồi đất trong trường hợp nào?'
Kết quả Top 3:
ID   | Score  | Topic       | Trích đoạn
-------------------------------------------------------
4    | 0.5295 | luat_dat_dai | Nhà nước thu hồi đất vì mục ...
7    | 0.5019 | luat_dat_dai | Nguyên tắc bồi thường về đất...
2    | 0.4300 | luat_dat_dai | Đất đai thuộc sở hữu toàn dâ...
-------------------------------------------------------

--- Truy vấn 2 ---
Query: 'Việt kiều có được mua nhà đất ở Việt Nam không?'
Kết quả Top 3:
ID   | Score  | Topic       | Trích đoạn
-------------------------------------------------------
17   | 0.7473 | luat_dat_dai | Người Việt Nam định cư ở nướ...
2    | 0.4423 | luat_dat_dai | Đất đai thuộc sở hữu toàn dâ...
11   | 0.4392 | luat_dat_dai | Điều kiện cấp Giấy chứng nhậ...
-------------------------------------------------------

--- Truy vấn 3 ---
Query: 'Hôm nay thời tiết thế nào?'
Kết quả Top 3:
ID   | Score  | Topic       | Trích đoạn
-------------------------------------------------------
Không tìm thấy kết quả phù hợp.
-------------------------------------------------------
"""

create_terminal_image(img1_text, "env_check.png", width=750, min_height=250)
create_terminal_image(img2_text, "model_load.png", width=750, min_height=280)
create_terminal_image(img3_text, "search_results.png", width=750, min_height=420)
