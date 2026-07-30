# RAG Basics - Embedding Tutorial

Đây là mã nguồn mẫu cho bài hướng dẫn về kỹ thuật Embedding và Semantic Search cơ bản. Trong tutorial này, chúng ta sử dụng thư viện `sentence-transformers` và model `keepitreal/vietnamese-sbert` để biến văn bản tiếng Việt thành vector và tìm kiếm câu trả lời tương đồng.

## Cài đặt

Cài đặt các thư viện cần thiết:
```bash
pip install -r requirements.txt
```

## Chạy thử nghiệm

Chạy file `semantic_search.py` để thực hiện tìm kiếm ngữ nghĩa trên tập dữ liệu mẫu:
```bash
python semantic_search.py
```

Lần đầu chạy, hệ thống sẽ tự động tải model từ Hugging Face về thư mục `model_cache`. Các lần sau hệ thống sẽ tải rất nhanh từ bộ nhớ nội bộ.
