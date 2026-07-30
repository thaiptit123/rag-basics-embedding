import json
import numpy as np
from sentence_transformers import SentenceTransformer
import time


def main():
    print("1. Đang khởi tạo mô hình embedding (keepitreal/vietnamese-sbert)...")
    start_time = time.time()
    # Khởi tạo mô hình. Model sẽ được tải về tự động trong lần đầu tiên chạy.
    MODEL_NAME = "keepitreal/vietnamese-sbert"
    CACHE_DIR = "./model_cache"
    
    model = SentenceTransformer(
        MODEL_NAME,
        cache_folder=CACHE_DIR
    )
    print(f"-> Hoàn tất tải mô hình trong {time.time() - start_time:.2f}s")
    
    # In ra số chiều của vector (Vector Dimension)
    dimension = model.get_sentence_embedding_dimension()
    print(f"-> Số chiều vector (Dimension) của mô hình: {dimension}\n")

    print("2. Đang đọc dữ liệu mẫu từ sample_texts.json...")
    with open('sample_texts.json', 'r', encoding='utf-8') as f:
        docs = json.load(f)
    print(f"-> Đã đọc {len(docs)} đoạn văn.\n")

    print("3. Đang mã hoá (embedding) văn bản thành vector...")
    start_time = time.time()
    texts = [doc["text"] for doc in docs]
    
    # Mã hóa dữ liệu bằng model.encode()
    # - batch_size: Mã hoá theo lô để tăng tốc.
    # - convert_to_numpy: Đưa về định dạng array chuẩn để dễ tính toán bằng numpy.
    # - normalize_embeddings: (Quan trọng) Chuẩn hoá vector về độ dài 1 (L2 norm).
    document_embeddings = model.encode(
        texts, 
        batch_size=8, 
        convert_to_numpy=True,
        normalize_embeddings=True 
    )
    print(f"-> Hoàn tất embedding trong {time.time() - start_time:.2f}s")
    print(f"-> Kích thước ma trận embedding: {document_embeddings.shape}")
    
    # Kiểm tra Norm của Document
    document_norms = np.linalg.norm(document_embeddings, axis=1)
    print(f"-> Document norm min/max: {document_norms.min():.4f}/{document_norms.max():.4f} (phải xấp xỉ 1.0)\n")
    assert np.allclose(document_norms, 1.0, atol=1e-3), "Document embeddings chưa được chuẩn hóa!"

    # 4. Truy vấn thử nghiệm với các chủ đề khác nhau
    queries = [
        "Điều kiện để mở công ty trách nhiệm hữu hạn là gì?",
        "Machine learning khác gì trí tuệ nhân tạo?",
        "Hôm nay thời tiết thế nào?"
    ]
    
    # 5 & 6. Tính toán và hiển thị Top-K (bạn có thể tuỳ chỉnh top_k)
    top_k = 3
    for i, query in enumerate(queries, 1):
        print(f"--- Truy vấn {i} ---")
        print(f"Query: '{query}'")
        
        # Mã hoá câu truy vấn (phải bật normalize_embeddings giống hệt document)
        query_embedding = model.encode(
            query, 
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        # Kiểm tra Norm của Query
        query_norm = np.linalg.norm(query_embedding)
        assert np.isclose(query_norm, 1.0, atol=1e-3), "Query embedding chưa được chuẩn hóa!"

        # Vì vector đã được normalize (độ dài = 1), dot product chính là cosine similarity.
        # Phép nhân ma trận @ chạy rất nhanh bằng numpy
        scores = document_embeddings @ query_embedding
        
        results = []
        for idx in range(len(docs)):
            results.append({
                "id": docs[idx]["id"],
                "topic": docs[idx]["topic"],
                "text": docs[idx]["text"],
                "score": float(scores[idx])
            })

        # Sắp xếp kết quả theo điểm số giảm dần
        results = sorted(results, key=lambda x: x["score"], reverse=True)

        # Lọc kết quả theo Threshold (ví dụ: 0.3)
        # Lưu ý: Ngưỡng này phải được thực nghiệm trên từng tập dữ liệu cụ thể, 
        # không nên đặt mặc định cố định cho mọi bài toán.
        THRESHOLD = 0.3
        filtered_results = [res for res in results if res["score"] >= THRESHOLD]

        print(f"Kết quả Top {top_k}:")
        print(f"{'ID':<4} | {'Score':<6} | {'Topic':<11} | {'Trích đoạn'}")
        
        separator_length = 55
        snippet_length = 28
        print("-" * separator_length)
        
        if not filtered_results:
            print("Không tìm thấy kết quả phù hợp.")
        else:
            for res in filtered_results[:top_k]:
                text = res["text"].replace("\n", " ")
                snippet = (
                    text[:snippet_length] + "..."
                    if len(text) > snippet_length
                    else text
                )

                print(
                    f"{res['id']:<4} | "
                    f"{res['score']:.4f} | "
                    f"{res['topic']:<11} | "
                    f"{snippet}"
                )

        print("-" * separator_length + "\n")

if __name__ == "__main__":
    main()
