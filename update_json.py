import json

data = []
with open("sample_texts.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Change items 11-20 to be about Land Law
new_texts = [
    "Điều kiện cấp Giấy chứng nhận quyền sử dụng đất, quyền sở hữu tài sản gắn liền với đất cho hộ gia đình, cá nhân đang sử dụng đất.",
    "Trình tự, thủ tục bồi thường, hỗ trợ, tái định cư khi Nhà nước thu hồi đất vì mục đích quốc phòng, an ninh; phát triển kinh tế - xã hội.",
    "Nguyên tắc lập, phê duyệt quy hoạch, kế hoạch sử dụng đất phải bảo đảm tính thống nhất, đồng bộ và phát triển bền vững.",
    "Người sử dụng đất nông nghiệp được chuyển đổi cơ cấu cây trồng, vật nuôi trên đất nông nghiệp theo quy định của pháp luật.",
    "Nhà nước cho thuê đất thu tiền thuê đất một lần cho cả thời gian thuê hoặc thu tiền thuê đất hàng năm.",
    "Thời hạn giao đất, cho thuê đất đối với tổ chức để sử dụng vào mục đích sản xuất nông nghiệp, lâm nghiệp, nuôi trồng thủy sản không quá 50 năm.",
    "Người Việt Nam định cư ở nước ngoài được phép nhập cảnh vào Việt Nam được mua, thuê mua nhà ở gắn liền với quyền sử dụng đất ở.",
    "Tranh chấp đất đai đã được hòa giải tại Ủy ban nhân dân cấp xã mà không thành thì được giải quyết tại Tòa án nhân dân.",
    "Đất phi nông nghiệp bao gồm đất ở, đất xây dựng trụ sở cơ quan, đất sử dụng vào mục đích quốc phòng, an ninh và đất phi nông nghiệp khác.",
    "Ủy ban nhân dân các cấp có trách nhiệm tổ chức quản lý, bảo vệ diện tích đất chưa sử dụng tại địa phương."
]

for i in range(10):
    data[10 + i]["topic"] = "luat_dat_dai"
    data[10 + i]["text"] = new_texts[i]

with open("sample_texts.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
