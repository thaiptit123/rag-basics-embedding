# RAG Basics - Embedding Tutorial

Đây là mã nguồn mẫu cho bài hướng dẫn về kỹ thuật Embedding và Semantic Search cơ bản. Trong tutorial này, chúng ta sử dụng thư viện `sentence-transformers` và model `keepitreal/vietnamese-sbert` để biến văn bản tiếng Việt thành vector và tìm kiếm câu trả lời tương đồng.

## Yêu cầu hệ thống
- Python 3.8 đến 3.11 (Không dùng Python 3.12+ do không tương thích PyTorch 2.0.1)

## Cài đặt và Chạy thử nghiệm

> **Lưu ý:** Hãy đảm bảo bạn chạy tất cả các lệnh dưới đây từ **thư mục gốc của repository**, vì dữ liệu trong `sample_texts.json` đang được đọc bằng đường dẫn tương đối.

Mở terminal và thực thi tuần tự các lệnh sau:

### 1. Clone repository về máy

```bash
git clone https://github.com/thaiptit123/rag-basics-embedding.git
cd rag-basics-embedding
```

### 2. Tạo môi trường ảo và cài đặt

**Trên Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
python3 check_env.py
```

**Trên Windows (PowerShell):**
```powershell
py -3.10 -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python check_env.py
```

**Trên Windows (Command Prompt):**
```bat
py -3.10 -m venv venv
venv\Scripts\activate.bat
python -m pip install -r requirements.txt
python check_env.py
```

Sau khi chạy `check_env.py` thành công và in ra thông tin phiên bản, bạn đã có thể chạy script chính.

### 3. Chạy hệ thống tìm kiếm ngữ nghĩa

```bash
python3 semantic_search.py
```

Lần đầu tiên chạy, hệ thống sẽ tự động kết nối Internet và tải model ngôn ngữ từ Hugging Face về thư mục `model_cache` trong repo. Các lần sau hệ thống sẽ tải rất nhanh hoàn toàn offline.

> **Lưu ý về Threshold:** Trong code `semantic_search.py`, biến `THRESHOLD = 0.3` chỉ là giá trị minh họa để lọc các kết quả quá kém. Trong thực tế, bạn cần hiệu chỉnh thông số này bằng tập validation của từng bài toán hoặc dữ liệu riêng.
