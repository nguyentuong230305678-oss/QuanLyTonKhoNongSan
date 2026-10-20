# TRƯỜNG ĐẠI HỌC TÀI NGUYÊN VÀ MÔI TRƯỜNG TP.HCM
## KHOA CÔNG NGHỆ THÔNG TIN

---

### BÁO CÁO TIẾN ĐỘ VÀ NHẬT KÝ THỰC HIỆN ĐỒ ÁN
# ĐỀ TÀI: XÂY DỰNG PHẦN MỀM QUẢN LÝ TỒN KHO NÔNG SẢN
### (Áp Dụng Nguyên Tắc Xuất Kho FEFO & Kiểm Soát Hạn Dùng)

- **Sinh viên thực hiện:** Nguyễn Ngọc Cát Tường
- **Mã số sinh viên:** 1250080226
- **Lớp:** 12_ĐH_THMT
- **Khóa:** 2023 – 2027
- **Giảng viên hướng dẫn:** ThS. Ngô Tân Khai
- **Thời gian cập nhật:** Tháng 10/2026

---

## 📊 BẢNG 1: BÁO CÁO TIẾN ĐỘ CÁC HẠNG MỤC

| Hạng mục công việc | Tiến độ | Ghi chú chi tiết tình trạng thực hiện |
| :--- | :---: | :--- |
| **1. Khảo sát nghiệp vụ & Thiết kế CSDL (Tuần 1–4)** | **100%** | Đã hoàn tất khảo sát nghiệp vụ kho nông sản thực tế. Xây dựng xong sơ đồ Use Case, Activity, Sequence và thiết kế CSDL quan hệ 12 bảng chuẩn hóa. |
| **2. Cấu trúc Backend & Xác thực phân quyền (Tuần 5–6)** | **100%** | Khởi tạo dự án Django, cấu hình ORM SQLite/PostgreSQL, xây dựng xác thực bảo mật PBKDF2, phân quyền 4 vai trò (Admin, Thủ kho, Nhân viên, Khách hàng). |
| **3. Quản lý Danh mục, Cơ sở nhập & Vùng trồng (Tuần 7)** | **100%** | Hoàn thiện quản lý nông sản với đầy đủ thông tin: Vùng trồng (Đà Lạt, Tiền Giang...), tiêu chuẩn VietGAP, cơ sở nhập (HTX), gợi ý mùa vụ và live preview ảnh trực tiếp. |
| **4. Phân hệ Nhập kho & Sinh mã Lô Barcode (Tuần 8)** | **100%** | Lập phiếu nhập kho từ nhà cung cấp, tự động sinh mã Lô hàng `LOT-...`, gán vị trí kệ kho (Khu A/B, Kệ, Tầng), hỗ trợ in tem Barcode dán bao bì. |
| **5. Phân hệ Xuất kho theo thuật toán FEFO (Tuần 9)** | **100%** | Cài đặt thành công thuật toán tự động quét các lô có hạn dùng gần nhất (EXP Date) xuất trước; cơ chế khóa Transaction an toàn chống âm kho; xuất phiếu PDF. |
| **6. Cửa hàng Nông sản Online & Quét VietQR (Tuần 10)** | **100%** | Xây dựng giao diện mua sắm phân loại theo 4 mùa vụ; bắt buộc đăng nhập trước khi đặt hàng; tự động sinh mã VietQR Napas 247 thanh toán đúng số tiền đơn hàng. |
| **7. Kiểm kê kho & Báo cáo hao hụt (Tuần 11)** | **100%** | Chức năng kiểm kê định kỳ đối soát tồn sổ sách vs thực tế; lập biên bản ghi nhận dập nát, hư hỏng hoặc hủy hàng hết hạn. |
| **8. Báo cáo thống kê & Trích xuất dữ liệu (Tuần 12)** | **100%** | Dashboard chỉ số KPI thời gian thực; ma trận cảnh báo HSD 3 cấp màu (Đỏ - Vàng - Xanh); script xuất CSDL ra file Excel 12 sheet và SQL dump. |
| **9. Kiểm thử hệ thống & Hoàn thiện giao diện (Tuần 13)** | **95%** | Đã chạy kiểm thử 8 kịch bản tích hợp thành công 100%; sửa lỗi tràn container giao diện, tối ưu nút tìm kiếm và tạo trang người dùng (`/profile/`). |
| **10. Viết báo cáo & Chuẩn bị bảo vệ (Tuần 14–15)** | **85%** | Đã hoàn thành toàn bộ nội dung Báo cáo đồ án chi tiết (Lời mở đầu, Chương 1, 2, 3 và Kết luận); đang hoàn thiện slide thuyết trình và kịch bản demo. |

---

## 🛠️ BẢNG 2: "NHỮNG THỨ LÀM ĐƯỢC" (KẾT QUẢ THỰC TẾ ĐÃ TRIỂN KHAI)

| Việc đã làm | Kết quả thực tế đạt được | Ghi chú kỹ thuật bên hông |
| :--- | :--- | :--- |
| **1. Khởi tạo môi trường & Cấu trúc dự án** | Thiết lập môi trường ảo Python 3.14 (`env`), cài đặt Django 6.1, openpyxl, cấu hình kết nối CSDL và static files. | Thư mục: `c:\QuanLyTonKhoNongSan\quanlykho\` chạy server tại cổng `8000`. |
| **2. Thiết kế và Migrate Cơ sở dữ liệu** | Tạo 12 Model thực thể trong `core/models.py`, chạy migration thành công 100% không phát sinh lỗi (`0001` đến `0003`). | Bảng: `Product`, `Batch`, `Receipt`, `Issue`, `IssueDetail`, `CustomerOrder`, `Supplier`, `Partner`, `Location`, `Category`, `WasteReport`, `UserProfile`. |
| **3. Xây dựng bộ dữ liệu thực tế (Seed Data)** | Nạp sẵn 8 mặt hàng nông sản chủ lực Việt Nam (Xoài Cát Hòa Lộc, Gạo ST25, Bưởi Da Xanh, Cà chua bi, Bắp cải...), 3 Nhà cung cấp HTX và các vị trí kệ kho. | Đầy đủ dữ liệu mẫu chuẩn VietGAP, OCOP và vùng trồng nổi tiếng để demo trực tiếp. |
| **4. Thuật toán xuất kho FEFO tự động** | Lập trình logic sắp xếp Lô hàng theo `exp_date` tăng dần trong `outbound_view`. Hệ thống tự động đề xuất và trừ tồn từng lô cận hạn trước, hỗ trợ phân tách lô nếu số lượng xuất lớn hơn 1 lô. | Sử dụng `Batch.objects.select_for_update()` và `transaction.atomic()` đảm bảo an toàn tuyệt đối, không bao giờ bị âm kho. |
| **5. Cảnh báo HSD 3 cấp màu trên Dashboard** | Xây dựng bảng **FEFO Matrix**: Cấp đỏ (HSD < 7 ngày - ưu tiên xuất ngay), Cấp vàng (HSD 7–15 ngày), Cấp xanh (> 15 ngày an toàn). Sửa triệt để lỗi co ép container và cắt chữ ở cột Thao tác. | Hiển thị thông minh ngày HSD kèm badge cảnh báo trong 1 cột, nút `⚡ Xuất FEFO` và `🏷 In tem` luôn hiển thị rõ ràng 100%. |
| **6. Form thêm nông sản đầy đủ** | Thiết kế form thêm mới nông sản tại `/products/` với: Live Image Preview (xem ảnh trực tiếp), Cơ sở nhập (Supplier), Vùng trồng (Origin), Tiêu chuẩn chất lượng (VietGAP/GlobalGAP), Gợi ý mùa vụ, Nhiệt độ kho. | Tự động kiểm tra URL ảnh, nếu hợp lệ sẽ hiển thị ngay trong khung xem trước. |
| **7. Trang Chi tiết Nông sản chuyên sâu** | Xây dựng route `/products/<id>/` hiển thị ảnh lớn, thông số bảo quản, tồn khả dụng, mô tả sản phẩm và **Bảng danh sách toàn bộ các Lô hàng thực tế** của sản phẩm đó trong kho. | Khách xem có nút đặt mua; Thủ kho xem có nút Xuất FEFO và Nhập thêm lô mới. |
| **8. Cửa hàng Nông sản & Thanh toán VietQR** | Xây dựng giao diện `/store/` gợi ý nông sản theo 4 mùa vụ; tích hợp thanh toán tự động tạo mã VietQR chuẩn ngân hàng MBBank/Napas 247 và phương thức COD. | Chuỗi liên kết động: `https://img.vietqr.io/image/MB-0901234567-compact2.png?...` đúng số tiền và mã đơn. |
| **9. Bắt buộc đăng nhập trước khi đặt hàng** | Khách vãng lai bấm "Đặt mua" sẽ bật Modal popup giải thích lý do cần tài khoản và điều hướng đến đăng nhập; `checkout_view` kiểm tra và tự chuyển hướng kèm `?next=...`. | Khi đăng nhập xong, hệ thống tự động đưa khách trở lại đúng trang đặt hàng của sản phẩm vừa chọn. |
| **10. Trang Người dùng & Bảo mật cá nhân** | Tạo trang `/profile/` cho phép xem thông tin định danh, vai trò role, cập nhật Họ tên, SĐT, Địa chỉ giao hàng và đổi mật khẩu an toàn (xác thực mật khẩu cũ). | Tự động điền trước thông tin người nhận vào trang Checkout khi khách đặt hàng. |
| **11. Quản trị Tài khoản & Ma trận RBAC** | Xây dựng trang `/users/`: Thống kê tài khoản theo role; Lọc tài khoản; Đổi vai trò (Modal); Khóa/Mở khóa tài khoản; Reset mật khẩu; Bảng Ma trận phân quyền 8 phân hệ cho 4 Role. | Độc quyền cho Quản trị viên (ADMIN); có cơ chế ngăn Admin tự khóa chính mình. |
| **12. Thiết kế lại Nút và Thanh tìm kiếm** | Nâng cấp thanh tìm kiếm dạng Pill Bar hiện đại, có icon kính lúp, nút xóa tìm kiếm `✕` và nút tìm kiếm nổi bật trên cả 3 trang: Cửa hàng, Danh mục nông sản và Lô hàng. | Hỗ trợ tìm kiếm theo tên, mã hàng, mã lô `LOT-...` và lọc kết hợp nhóm hàng. |
| **13. Sinh tem Barcode & In nhãn Lô hàng** | Tạo view `/batches/<id>/barcode/` render tem nhãn chuẩn dán lên bao bì: Tên sản phẩm, Mã lô, Ngày SX (MFG), Hạn dùng (EXP), Vị trí kệ kho và mã vạch Barcode. | Tương thích lệnh in trình duyệt (`window.print()`) để in trực tiếp ra máy in tem nhiệt. |
| **14. Xuất Báo cáo Excel 12 Sheet & SQL Dump** | Lập trình script `export_db.py` sử dụng thư viện `openpyxl` xuất toàn bộ CSDL ra file Excel 12 sheet có định dạng tiêu đề, màu sắc đẹp; xuất file sao lưu `database_dump.sql` và `.json`. | File kết quả lưu tại: `C:\QuanLyTonKhoNongSan\DuLieu_CoSoDuLieu_QuanLyKhoNongSan.xlsx` và `database_dump.sql`. |

---

## 🌐 BẢNG 3: DANH SÁCH LIÊN KẾT TRẢI NGHIỆM VÀ ĐỐI SOÁT HỆ THỐNG

| Chức năng / Phân hệ | Đường dẫn truy cập (URL) | Tài khoản kiểm thử đề xuất | Trạng thái |
| :--- | :--- | :--- | :---: |
| **Trang chủ Dashboard (FEFO Matrix)** | http://127.0.0.1:8000/ | `thukho` / `thukho123` hoặc `admin` / `123` | **Hoạt động tốt** |
| **Quản lý Nông sản & Cơ sở nhập** | http://127.0.0.1:8000/products/ | `admin` / `123` (Có quyền thêm nông sản) | **Hoạt động tốt** |
| **Chi tiết Nông sản (Mẫu Xoài Cát)** | http://127.0.0.1:8000/products/1/ | Khách hoặc Nhân sự kho | **Hoạt động tốt** |
| **Quản lý Lô hàng & Tem Barcode** | http://127.0.0.1:8000/batches/ | `thukho` / `thukho123` | **Hoạt động tốt** |
| **Mẫu in Tem Barcode lô hàng** | http://127.0.0.1:8000/batches/1/barcode/ | `thukho` / `thukho123` (In tem dán thùng) | **Hoạt động tốt** |
| **Tạo phiếu Nhập kho & Sinh lô mới** | http://127.0.0.1:8000/inbound/ | `thukho` / `thukho123` | **Hoạt động tốt** |
| **Xuất kho tự động theo FEFO** | http://127.0.0.1:8000/outbound/ | `thukho` / `thukho123` (Quét lô hạn gần) | **Hoạt động tốt** |
| **Cửa hàng Nông sản theo mùa vụ** | http://127.0.0.1:8000/store/ | Khách vãng lai / Đối tác mua sỉ | **Hoạt động tốt** |
| **Hồ sơ Người dùng & Đổi mật khẩu** | http://127.0.0.1:8000/profile/ | Bất kỳ tài khoản nào sau đăng nhập | **Hoạt động tốt** |
| **Quản trị Tài khoản & Phân quyền Role** | http://127.0.0.1:8000/users/ | `admin` / `123` (Độc quyền Admin) | **Hoạt động tốt** |
| **Giao diện Django Admin CSDL** | http://127.0.0.1:8000/admin/ | `admin` / `123` | **Hoạt động tốt** |

---

## 📌 NHẬN XÉT VÀ KẾ HOẠCH BẢO VỆ ĐỒ ÁN (TUẦN 14 – 15)

1. **Về sản phẩm phần mềm:** 
   - Hệ thống phần mềm đã hoàn thiện toàn bộ các luồng nghiệp vụ phức tạp nhất, đặc biệt là cơ chế **FEFO** và tự động hóa thanh toán **VietQR**, chạy mượt mà, không phát sinh lỗi ngoại lệ nào khi kiểm thử.
2. **Về tài liệu báo cáo:**
   - Đã biên soạn đầy đủ báo cáo theo chuẩn hình thức của Khoa Công nghệ Thông tin, Trường Đại học Tài nguyên và Môi trường TP.HCM tại tệp `BAO_CAO_DO_AN_NGUYEN_NGOC_CAT_TUONG.md`.
3. **Kế hoạch chuẩn bị cho buổi bảo vệ:**
   - Soạn thảo Slide thuyết trình PowerPoint tóm tắt 20 slide nêu bật tính cấp thiết, kiến trúc giải pháp, thuật toán FEFO và các chỉ số vận hành kho.
   - Quay video ngắn (3–5 phút) quay lại toàn bộ kịch bản demo: Nhập hàng sinh lô Barcode -> Cảnh báo HSD trên Dashboard -> Xuất kho FEFO -> Khách đặt hàng quét VietQR -> Xuất báo cáo Excel.
