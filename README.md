# RAG Basics - Embedding Tutorial

Đây là mã nguồn mẫu cho bài hướng dẫn về kỹ thuật Embedding và Semantic Search cơ bản. Trong tutorial này, chúng ta sử dụng thư viện `sentence-transformers` và model `keepitreal/vietnamese-sbert` để biến văn bản tiếng Việt thành vector và tìm kiếm câu trả lời tương đồng.

## Cài đặt và Chạy thử nghiệm

> **Lưu ý 1:** Yêu cầu cài đặt sẵn Python phiên bản từ 3.8 đến 3.11 trên máy.
> **Lưu ý 2:** Hãy đảm bảo bạn chạy tất cả các lệnh dưới đây từ thư mục gốc của repository, vì dữ liệu trong `sample_texts.json` đang được đọc bằng đường dẫn tương đối.

Mở terminal và thực thi tuần tự các lệnh sau:

```bash
# Clone repository về máy
git clone https://github.com/thaiptit123/rag-basics-embedding.git
cd rag-basics-embedding

# Kiểm tra phiên bản Python
python3 --version

# Tạo môi trường ảo và kích hoạt
# Trên Linux/macOS:
python3 -m venv venv
source venv/bin/activate
# Trên Windows:
# python -m venv venv
# venv\Scripts\activate

# Cài đặt các thư viện cần thiết
pip install -r requirements.txt

# Kiểm tra thư viện và môi trường
python3 check_env.py

# Chạy hệ thống tìm kiếm ngữ nghĩa
python3 semantic_search.py
```

Lần đầu tiên chạy, hệ thống sẽ tự động kết nối Internet và tải model ngôn ngữ từ Hugging Face về thư mục `model_cache` trong repo. Các lần sau hệ thống sẽ tải rất nhanh hoàn toàn offline.

> **Lưu ý về Threshold:** Trong code `semantic_search.py`, biến `THRESHOLD = 0.3` chỉ là giá trị minh họa để lọc các kết quả quá kém. Trong thực tế, bạn cần hiệu chỉnh thông số này bằng tập validation của từng bài toán hoặc dữ liệu riêng.
