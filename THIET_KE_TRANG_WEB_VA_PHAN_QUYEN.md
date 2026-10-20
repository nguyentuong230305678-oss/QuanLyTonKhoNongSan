# BẢN THIẾT KẾ TRANG WEB & PHÂN QUYỀN HỆ THỐNG QUẢN LÝ TỒN KHO NÔNG SẢN

> **Đề tài**: Xây dựng phần mềm quản lý tồn kho nông sản  
> **Sinh viên thực hiện**: Nguyễn Ngọc Cát Tường (MSSV: 1250080226) - Lớp 12_ĐH_THMT  
> **Đơn vị đào tạo**: Khoa Công nghệ Thông tin – Trường Đại học Tài nguyên và Môi trường TP.HCM  
> **Cán bộ hướng dẫn**: ThS. Ngô Tấn Khai  

---

## I. TỔNG QUAN HIỆN TRẠNG VÀ ĐỐI CHIẾU

### 1. Khảo sát thực tế mã nguồn dự án
Qua kiểm tra toàn bộ cấu trúc dự án `c:\QuanLyTonKhoNongSan\quanlykho` và tài liệu đề cương đồ án:
- **Backend**: Django REST Framework (Python) kết nối cơ sở dữ liệu PostgreSQL (`quanlykho_nongsan`), xác thực bằng `rest_framework_simplejwt`. Đã có 2 ứng dụng:
  - `apps.accounts`: Đăng nhập, cấp Token JWT kèm danh sách `roles`, phân quyền `role_required`.
  - `apps.catalog`: Danh mục nông sản (`Category`, `Product`), Nhà cung cấp (`Supplier`), Đối tác (`Partner`), Vị trí lưu kho (`Location`) và API Public cho khách hàng.
- **Frontend & Giao diện người dùng**:
  - Đầy đủ 6 luồng hoạt động + Cổng Mua hàng Trực tuyến cho Khách hàng.
  - Phân hệ Quên mật khẩu (`/forgot-password/`) và Đăng ký tài khoản khách hàng (`/register/`).
  - Cổng Cửa hàng Nông sản (`/store/`) với ảnh sản phẩm sắc nét, bộ lọc gợi ý nông sản 4 mùa (Xuân, Hạ, Thu, Đông) và huy hiệu nông sản chính vụ.
  - Tích hợp cổng Thanh toán VietQR tự động (quét mã chuyển khoản ngân hàng) và COD.
  - Bảng Dashboard điều khiển với cột Thao tác to rõ, đầy đủ chữ, phân cấp màu FEFO sắc nét (🔴 Cận hạn khẩn cấp, 🟡 Cảnh báo, 🟢 An toàn).


---

## II. MA TRẬN PHÂN QUYỀN NGƯỜI DÙNG (ROLE-BASED ACCESS CONTROL - RBAC)

Hệ thống được thiết kế với 3 nhóm người dùng rõ rệt:
1. **Khách / Đối tác (Public - Không cần đăng nhập)**
2. **Thủ kho / Nhân viên kho (`ROLE_WAREHOUSE_MANAGER`, `ROLE_STAFF`)**
3. **Quản trị viên / Chủ doanh nghiệp (`ROLE_ADMIN`)**

### 1. Ma trận chức năng chi tiết

| Phân hệ / Nghiệp vụ | Chi tiết thao tác | Public (Khách/Đối tác) | Nhân viên kho (`STAFF`) | Thủ kho (`WAREHOUSE_MANAGER`) | Quản trị viên (`ADMIN`) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Khu vực công khai** | Xem danh mục nông sản, quy cách đóng gói, nhiệt độ bảo quản | ✅ | ✅ | ✅ | ✅ |
| | Xem chứng nhận tiêu chuẩn chất lượng (VietGAP, GlobalGAP) & Liên hệ | ✅ | ✅ | ✅ | ✅ |
| **Xác thực & Tài khoản** | Đăng nhập hệ thống (JWT Token) | ❌ | ✅ | ✅ | ✅ |
| | Đổi mật khẩu cá nhân, xem thông tin tài khoản | ❌ | ✅ | ✅ | ✅ |
| | Quản lý tài khoản người dùng, tạo tài khoản mới, phân quyền Role | ❌ | ❌ | ❌ | ✅ |
| **Danh mục & Vị trí kho** | Xem danh mục loại nông sản, sản phẩm, đối tác, nhà cung cấp | ❌ | ✅ | ✅ | ✅ |
| | Thêm/Sửa/Xóa Nhóm nông sản, Nông sản, Nhà cung cấp, Khách mua sỉ | ❌ | ❌ | ✅ | ✅ |
| | Thiết lập sơ đồ kho: Khu vực, Kệ, Tầng (`Location`) | ❌ | ❌ | ✅ | ✅ |
| **Nhập kho & Lô hàng** | Lập phiếu nhập kho từ nhà cung cấp | ❌ | ✅ | ✅ | ✅ |
| | Khởi tạo mã Lô (`BatchCode`), MFG, EXP, giá nhập, số lượng nhập | ❌ | ✅ | ✅ | ✅ |
| | In/Xuất mã tem barcode/QR cho từng lô hàng | ❌ | ✅ | ✅ | ✅ |
| | Cập nhật vị trí cất giữ lô hàng vào Khu - Kệ - Tầng | ❌ | ✅ | ✅ | ✅ |
| | Hủy/Sửa phiếu nhập kho (trong thời hạn cho phép) | ❌ | ❌ | ✅ | ✅ |
| **Xuất kho (FEFO)** | Lập yêu cầu xuất kho (chọn đối tác, nông sản, số lượng) | ❌ | ✅ | ✅ | ✅ |
| | Hệ thống tự động đề xuất lô xuất theo hạn sử dụng (FEFO) | ❌ | ✅ | ✅ | ✅ |
| | Can thiệp điều chỉnh chọn lô xuất thực tế khác với gợi ý | ❌ | ❌ | ✅ | ✅ |
| | Duyệt phiếu xuất kho giá trị lớn / bất thường | ❌ | ❌ | ❌ | ✅ |
| | In phiếu xuất kho PDF | ❌ | ✅ | ✅ | ✅ |
| **Kiểm kê & Hao hụt** | Lập phiếu kiểm kê định kỳ theo Khu vực / Danh mục | ❌ | ✅ | ✅ | ✅ |
| | Nhập số lượng thực tế đếm được | ❌ | ✅ | ✅ | ✅ |
| | Ghi nhận nguyên nhân hao hụt (dập nát, thối hỏng, quá hạn) | ❌ | ✅ | ✅ | ✅ |
| | Phê duyệt cân bằng kho tự động từ kết quả kiểm kê | ❌ | ❌ | ✅ | ✅ |
| **Báo cáo & Dashboard** | Xem Dashboard tồn kho, cảnh báo lô cận hạn (7, 15, 30 ngày) | ❌ | ✅ | ✅ | ✅ |
| | Xem thống kê doanh thu, chi phí nhập, tổng giá trị tồn kho | ❌ | ❌ | ❌ | ✅ |
| | Xuất danh sách tồn kho & hao hụt ra file Excel | ❌ | ❌ | ✅ | ✅ |
| | Xuất báo cáo tài chính, công nợ nhà cung cấp ra Excel/PDF | ❌ | ❌ | ❌ | ✅ |

---

## III. THIẾT KẾ CẤU TRÚC GIAO DIỆN & SITEMAP TRANG WEB

Hệ thống được chia thành 2 không gian trải nghiệm:
1. **Public Portal (Dành cho Khách hàng & Đối tác)**:
   - `/`: Trang giới thiệu nông sản đạt chuẩn, bộ lọc nhóm hàng, quy cách đóng gói, thông tin liên hệ kho.
   - `/login`: Cổng đăng nhập cho cán bộ nhân viên nội bộ.
2. **Internal App (Dành cho Quản trị viên, Thủ kho, Nhân viên)**:
   - `/app`: Dashboard trung tâm điều khiển (Thống kê sản lượng, giá trị, cảnh báo cận hạn).
   - `/app/categories`: Quản lý nhóm nông sản & loại bảo quản.
   - `/app/products`: Quản lý danh mục chi tiết nông sản.
   - `/app/locations`: Quản lý sơ đồ vị trí lưu trữ (Khu - Kệ - Tầng).
   - `/app/partners`: Quản lý khách mua sỉ & đối tác phân phối.
   - `/app/suppliers`: Quản lý nhà cung cấp / hợp tác xã thu gom.
   - `/app/receipts`: Lập phiếu nhập kho & Lịch sử phiếu nhập.
   - `/app/batches`: Danh sách Lô hàng, tra cứu HSD, in nhãn Barcode / QR Code.
   - `/app/issues`: Lập phiếu xuất kho thông minh (FEFO Engine), in phiếu xuất PDF.
   - `/app/audits`: Phiếu kiểm kê kho định kỳ & cân bằng tồn kho.
   - `/app/waste`: Báo cáo hao hụt, hư hại, thối hỏng, quá hạn.
   - `/app/reports`: Báo cáo chuyên sâu, xuất Excel tồn kho & PDF.
   - `/app/users`: Quản lý người dùng và phân quyền (Dành riêng cho Quản trị viên).

---

## IV. ĐẶC TẢ CHI TIẾT 6 LUỒNG HOẠT ĐỘNG (WORKFLOWS)

### Luồng 1: Xác thực & Quản trị tài khoản
1. **Đăng nhập**: Người dùng nhập tên tài khoản và mật khẩu. Backend xác thực BCrypt, tạo JWT Access Token (hạn 60 phút) và Refresh Token (hạn 1 ngày), kèm mảng `roles: ["ROLE_ADMIN", ...]`.
2. **Phân quyền giao diện (Client-side Routing)**:
   - Frontend lưu JWT và `roles` vào `localStorage`.
   - Sidebar tự động ẩn/hiện các tab chức năng tương ứng:
     - `STAFF`: Nhập kho, Xuất kho, Kiểm kê, Xem cảnh báo hạn.
     - `WAREHOUSE_MANAGER`: Toàn bộ quyền STAFF + Quản lý danh mục/kho, In tem nhãn, Điều chỉnh lô xuất, Duyệt cân bằng tồn kho, Xuất Excel tồn kho.
     - `ADMIN`: Toàn quyền toàn hệ thống + Quản lý User/Roles + Xem báo cáo tài chính/doanh thu.
3. **Bảo mật API (Server-side Enforcement)**: Mọi API nội bộ được bảo vệ bởi lớp decorator `role_required("ADMIN", "WAREHOUSE_MANAGER", ...)`. Nếu vi phạm sẽ trả về mã lỗi HTTP 403 Forbidden.

---

### Luồng 2: Quản lý Danh mục & Vị trí Kho
1. **Nhóm nông sản**: Quản lý các nhóm (Rau củ, Trái cây nhiệt đới, Thủy sản, Hạt khô) kèm theo loại điều kiện bảo quản (`COOL`: Kho mát, `FROZEN`: Kho đông lạnh, `DRY`: Kho khô thoáng).
2. **Chi tiết nông sản**: Mã nông sản, tên, hình ảnh minh họa, đơn vị tính (`kg`, `tấn`, `thùng`), ngưỡng tồn an toàn (`safety_stock`), nhiệt độ tiêu chuẩn (ví dụ: `2°C - 8°C`), chiến lược xuất kho mặc định (`FEFO` hoặc `FIFO`).
3. **Quản lý vị trí lưu trữ**: Mô hình hóa kho hàng theo cấu trúc 3 cấp độ: **Khu vực (Zone) -> Kệ (Shelf) -> Tầng (Level)**. Ví dụ: `Khu A - Kệ 02 - Tầng 1 (A-02-1)`. Hỗ trợ xem nhanh vị trí nào còn trống, vị trí nào đang chứa lô hàng nào.
4. **Đối tác**: Quản lý Nhà cung cấp nông sản (địa chỉ thu gom/hợp tác xã, mã số thuế, số điện thoại) và Khách hàng sỉ/siêu thị/chợ đầu mối.

---

### Luồng 3: Quản lý Nhập kho & Sinh mã Lô hàng (Batch Code)
1. **Lập phiếu nhập**: Thủ kho chọn Nhà cung cấp, nhập danh sách nông sản, số lượng nhập ban đầu, đơn giá nhập, vị trí kho dự kiến cất giữ, ngày sản xuất (MFG) và hạn sử dụng (EXP).
2. **Tự động sinh mã Lô**: Hệ thống tự động sinh mã `LOT-[MÃ_SP]-[YYMMDD]-[STT]`. Khởi tạo bản ghi `Batch` với `qty_initial = số lượng nhập` và `qty_current = số lượng nhập`.
3. **In tem nhãn**: Hỗ trợ in tem nhãn trực tiếp (Mã vạch Code128 / QR Code) dán lên pallet hoặc bao bì trước khi đưa vào kệ.

---

### Luồng 4: Quản lý Xuất kho Thông minh theo Thuật toán FEFO
1. **Lập yêu cầu xuất**: Nhân viên chọn Khách hàng, Nông sản và Tổng số lượng cần xuất.
2. **FEFO Engine quét tồn kho**:
   - Truy vấn các lô hàng của sản phẩm đó có `qty_current > 0` và `exp_date >= ngày hiện tại`.
   - Sắp xếp tăng dần theo `exp_date` (Lô nào hạn gần nhất lên trước).
   - Nếu tổng tồn kho khả dụng < số lượng cần xuất: Báo lỗi ngay lập tức (HTTP 400 Bad Request) và không cho xuất.
   - Nếu đủ tồn kho: Tự động phân bổ số lượng cần xuất lần lượt qua từng lô.
3. **Can thiệp thủ kho**: Cho phép thủ kho xem trước danh sách lô gợi ý, và có quyền điều chỉnh lô thực tế nếu lô ngoài kho có vấn đề (Ví dụ dập nát chưa kịp hủy).
4. **Trừ tồn kho nguyên tử (`transaction.atomic`)**:
   - Giảm `qty_current` tương ứng của từng Lô.
   - Tạo phiếu xuất `Issue` và các dòng chi tiết `IssueDetail`.
   - Sinh file PDF Phiếu xuất kho hoàn chỉnh.

---

### Luồng 5: Kiểm kê Định kỳ & Ghi nhận Hao hụt
1. **Lập đợt kiểm kê**: Chọn phạm vi kiểm kê theo Khu vực kho hoặc Danh mục. Hệ thống kết xuất bảng kiểm kê với số lượng tồn trên sổ sách.
2. **Nhập số lượng thực tế**: Nhân viên đếm tại kho và ghi nhận số lượng thực tế.
3. **Ghi nhận nguyên nhân chênh lệch**: Nếu thiếu hụt, ghi nhận lý do: Dập nát bốc xếp, thối hỏng do nhiệt độ, hết hạn hoặc hao hụt tự nhiên.
4. **Cân bằng tồn kho**: Thủ kho/Quản trị viên duyệt kết quả, hệ thống cập nhật `qty_current` của các lô về đúng thực tế và lưu vết kiểm toán.

---

### Luồng 6: Dashboard Thống kê & Xuất Chứng từ
1. **Bảng điều khiển trực quan**:
   - Thống kê tổng tồn, giá trị tồn kho, tỷ lệ hao hụt.
   - Biểu đồ xuất - nhập kho theo thời gian.
   - Phân khúc cảnh báo hạn dùng 3 mức: Dưới 7 ngày (Đỏ), 7-15 ngày (Vàng), Trên 15 ngày (Xanh).
2. **Xuất báo cáo**:
   - In phiếu nhập / xuất kho chuẩn PDF.
   - Xuất danh sách tồn kho & hao hụt ra Excel.
