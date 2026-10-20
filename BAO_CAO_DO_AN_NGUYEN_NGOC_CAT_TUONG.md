# TRƯỜNG ĐẠI HỌC TÀI NGUYÊN VÀ MÔI TRƯỜNG THÀNH PHỐ HỒ CHÍ MINH
## KHOA CÔNG NGHỆ THÔNG TIN

---

<br><br>

# ĐỒ ÁN CHUYÊN NGÀNH TIN HỌC MÔI TRƯỜNG
### ĐỀ TÀI:
# XÂY DỰNG PHẦN MỀM QUẢN LÝ TỒN KHO NÔNG SẢN
### (Áp Dụng Nguyên Tắc Xuất Kho FEFO & Kiểm Soát Hạn Dùng)

<br><br>

**Sinh viên thực hiện:** NGUYỄN NGỌC CÁT TƯỜNG  
**Mã số sinh viên:** 1250080226  
**Lớp:** 12_ĐH_THMT  
**Khóa:** 2023 – 2027  
**Ngành:** Tin học Môi trường  
**Giảng viên hướng dẫn:** ThS. NGÔ TÂN KHAI  

<br><br>

**TP. Hồ Chí Minh, tháng 10 năm 2026**

---
\pagebreak

# TRƯỜNG ĐẠI HỌC TÀI NGUYÊN VÀ MÔI TRƯỜNG THÀNH PHỐ HỒ CHÍ MINH
## KHOA CÔNG NGHỆ THÔNG TIN

---

<br><br>

# BÁO CÁO ĐỒ ÁN CHUYÊN NGÀNH
### ĐỀ TÀI:
# XÂY DỰNG PHẦN MỀM QUẢN LÝ TỒN KHO NÔNG SẢN

<br><br>

**Sinh viên thực hiện:** NGUYỄN NGỌC CÁT TƯỜNG  
**Mã số sinh viên:** 1250080226  
**Lớp:** 12_ĐH_THMT  
**Khóa:** 2023 – 2027  
**Giảng viên hướng dẫn:** ThS. NGÔ TÂN KHAI  

<br><br>

**TP. Hồ Chí Minh, tháng 10 năm 2026**

---
\pagebreak

# LỜI CẢM ƠN

Lời đầu tiên, em xin được bày tỏ lòng biết ơn chân thành và sâu sắc nhất đến toàn thể Quý Thầy Cô Khoa Công nghệ Thông tin, Trường Đại học Tài nguyên và Môi trường TP.HCM. Suốt những năm tháng học tập dưới mái trường, sự tận tụy, tri thức uyên thâm và ngọn lửa đam mê với nghề của các Thầy Cô đã không chỉ trang bị cho em nền tảng kiến thức công nghệ vững vàng, mà còn rèn luyện cho em tư duy giải quyết vấn đề và tác phong kỷ luật của một người làm kỹ thuật.

Đặc biệt, em xin gửi lời tri ân sâu sắc nhất đến **ThS. Ngô Tân Khai** – người Thầy đã luôn kiên nhẫn đồng hành, định hướng học thuật và tận tình chỉ dẫn em trong suốt quá trình triển khai đồ án này. Từ những ngày đầu khi ý tưởng về một phần mềm quản lý kho nông sản còn sơ khai, cho đến khi giải quyết các thuật toán phức tạp như cơ chế xuất kho FEFO (First Expired, First Out), xử lý các transaction bảo toàn tính toàn vẹn tồn kho, hay tinh chỉnh giao diện người dùng, Thầy luôn dành thời gian lắng nghe, phản biện khoa học và đưa ra những lời khuyên vô cùng quý báu. Nếu không có sự dìu dắt nghiêm cẩn và tâm huyết của Thầy, đồ án của em khó có thể hoàn thiện một cách trọn vẹn và đạt tính ứng dụng thực tiễn cao như ngày hôm nay.

Cuối cùng, em muốn dành một khoảng lặng để gửi lời cảm ơn đến gia đình – điểm tựa tinh thần vững chắc nhất luôn tin tưởng và ủng hộ em vô điều kiện. Và cảm ơn chính bản thân mình vì đã không chùn bước trước những đêm thức trắng sửa từng lỗi logic code, đã kiên định vượt qua áp lực và thử thách để biến dòng lệnh trên màn hình thành một phần mềm thực sự hữu ích cho chuỗi phân phối nông sản Việt Nam. Cuốn đồ án này chính là dấu mốc quan trọng, ghi dấu sự trưởng thành, tâm huyết và lòng tự trọng nghề nghiệp của em trước thềm tốt nghiệp.

<br>

*TP. Hồ Chí Minh, tháng 10 năm 2026*  
**Sinh viên thực hiện**  
*(Ký và ghi rõ họ tên)*  
<br><br>
**Nguyễn Ngọc Cát Tường**

---
\pagebreak

# LỜI CAM DOAN

Em xin cam đoan đồ án chuyên ngành với đề tài **"Xây dựng phần mềm quản lý tồn kho nông sản"** là công trình nghiên cứu và phát triển phần mềm độc lập của riêng cá nhân em, dưới sự hướng dẫn khoa học trực tiếp của **ThS. Ngô Tân Khai**.

Em xin khẳng định:
1. Toàn bộ các yêu cầu nghiệp vụ, phân tích thiết kế hệ thống, sơ đồ Use Case, Activity, Sequence, thiết kế Cơ sở dữ liệu quan hệ (ERD) và các dòng mã nguồn (Backend Django, Frontend, các thuật toán xuất kho FEFO, module xuất báo cáo Excel/PDF, phân quyền bảo mật) đều do em tự tìm tòi, xây dựng và lập trình thực tế.
2. Hệ thống hoàn toàn không sao chép từ bất kỳ đồ án, mã nguồn hay công trình nghiên cứu nào của người khác. Các tài liệu tham khảo, thư viện mã nguồn mở và chuẩn mực công nghệ được kế thừa đều được trích dẫn xuất xứ minh bạch và tuân thủ đúng quy định bản quyền học thuật.
3. Toàn bộ số liệu thực nghiệm, kết quả kiểm thử chức năng và dữ liệu mẫu kiểm thử trên hệ thống đều là số liệu trung thực, được sinh ra từ quá trình vận hành thực tế của phần mềm.

Em xin chịu hoàn toàn trách nhiệm trước Hội đồng chấm đồ án và Khoa Công nghệ Thông tin – Trường Đại học Tài nguyên và Môi trường TP.HCM nếu phát hiện bất kỳ sự gian lận hoặc thiếu trung thực nào trong đồ án này.

<br>

*TP. Hồ Chí Minh, tháng 10 năm 2026*  
**Sinh viên thực hiện**  
*(Ký và ghi rõ họ tên)*  
<br><br>
**Nguyễn Ngọc Cát Tường**

---
\pagebreak

# NHẬN XÉT CỦA GIẢNG VIÊN HƯỚNG DẪN

**Họ và tên giảng viên:** ThS. NGÔ TÂN KHAI  
**Đơn vị công tác:** Khoa Công nghệ Thông tin – Trường ĐH Tài nguyên và Môi trường TP.HCM  
**Sinh viên thực hiện:** NGUYỄN NGỌC CÁT TƯỜNG – **MSSV:** 1250080226  
**Đề tài:** Xây dựng phần mềm quản lý tồn kho nông sản  

### 1. Về tinh thần, thái độ và ý thức kỷ luật:
……………………………………………………………………………………………………………………………………  
……………………………………………………………………………………………………………………………………  
……………………………………………………………………………………………………………………………………  

### 2. Về năng lực chuyên môn và nội dung báo cáo:
……………………………………………………………………………………………………………………………………  
……………………………………………………………………………………………………………………………………  
……………………………………………………………………………………………………………………………………  

### 3. Về chất lượng sản phẩm phần mềm và tính thực tiễn:
……………………………………………………………………………………………………………………………………  
……………………………………………………………………………………………………………………………………  
……………………………………………………………………………………………………………………………………  

### 4. Kết luận và Điểm đánh giá:
- **Được phép bảo vệ trước Hội đồng:**  [  ] Có    [  ] Không
- **Điểm đánh giá (bằng số):** …………… / 10 *(Bằng chữ: …………………………………)*

<br>

*TP. Hồ Chí Minh, ngày …… tháng …… năm 2026*  
**GIẢNG VIÊN HƯỚNG DẪN**  
*(Ký và ghi rõ học hàm, học vị, họ tên)*  
<br><br><br>
**ThS. NGÔ TÂN KHAI**

---
\pagebreak

# NHẬN XÉT CỦA GIẢNG VIÊN PHẢN BIỆN

**Họ và tên giảng viên phản biện:** …………………………………………………………………………………  
**Đơn vị công tác:** Khoa Công nghệ Thông tin – Trường ĐH Tài nguyên và Môi trường TP.HCM  
**Sinh viên thực hiện:** NGUYỄN NGỌC CÁT TƯỜNG – **MSSV:** 1250080226  
**Đề tài:** Xây dựng phần mềm quản lý tồn kho nông sản  

### 1. Ý nghĩa khoa học và thực tiễn của đề tài:
……………………………………………………………………………………………………………………………………  
……………………………………………………………………………………………………………………………………  

### 2. Bố cục và hình thức trình bày của báo cáo:
……………………………………………………………………………………………………………………………………  
……………………………………………………………………………………………………………………………………  

### 3. Đánh giá kết quả đạt được và tính hoàn thiện của phần mềm:
……………………………………………………………………………………………………………………………………  
……………………………………………………………………………………………………………………………………  

### 4. Những điểm còn hạn chế và câu hỏi dành cho sinh viên:
……………………………………………………………………………………………………………………………………  
……………………………………………………………………………………………………………………………………  

### 5. Kết luận và Điểm đánh giá:
- **Đồng ý cho bảo vệ trước Hội đồng:**  [  ] Có    [  ] Không
- **Điểm phản biện (bằng số):** …………… / 10 *(Bằng chữ: …………………………………)*

<br>

*TP. Hồ Chí Minh, ngày …… tháng …… năm 2026*  
**GIẢNG VIÊN PHẢN BIỆN**  
*(Ký và ghi rõ học hàm, học vị, họ tên)*  
<br><br><br>

---
\pagebreak

# TÓM TẮT ĐỀ TÀI

### Tóm tắt tiếng Việt:
Nông sản là mặt hàng có thời gian bảo quản ngắn, dễ suy giảm chất lượng và chịu ảnh hưởng trực tiếp bởi điều kiện môi trường lưu kho (nhiệt độ, độ ẩm). Tại nhiều hợp tác xã, doanh nghiệp phân phối vừa và nhỏ, việc quản lý kho thủ công bằng sổ sách hay bảng tính Excel rời rạc dẫn đến tình trạng thất thoát hàng hóa, không kiểm soát được hạn sử dụng theo từng mẻ (Batch/Lot), tỷ lệ nông sản hư hỏng cao và khó áp dụng nguyên tắc xuất kho ưu tiên hàng cận hạn (**FEFO - First Expired, First Out**).

Đề tài **"Xây dựng phần mềm quản lý tồn kho nông sản"** được triển khai nhằm nghiên cứu, phân tích và phát triển một hệ thống ứng dụng web chuyên biệt, số hóa toàn diện quy trình vận hành kho nông sản. Phần mềm được xây dựng trên nền tảng **Python / Django Framework**, hệ quản trị cơ sở dữ liệu quan hệ (**SQLite / PostgreSQL**), giao diện Web tương tác hiện đại chuẩn Responsive, kết hợp cùng các công nghệ: mã hóa bảo mật PBKDF2/JWT, phân quyền 4 vai trò (**Quản trị viên, Thủ kho, Nhân viên kho, Khách hàng**), cơ chế tự động sinh mã vạch/QR cho từng lô hàng, tự động gợi ý xuất kho FEFO chống hư hao, tích hợp cổng đặt hàng trực tuyến với mã **VietQR tự động**, xuất chứng từ xuất/nhập PDF chuẩn in ấn qua ReportLab và trích xuất bảng dữ liệu thống kê đa trang qua Openpyxl. Kết quả thực nghiệm cho thấy hệ thống vận hành ổn định, chính xác 100% trong việc cân đối số lượng tồn kho theo Transaction ACID và giảm thiểu rủi ro hết hạn nông sản trong kho.

**Từ khóa:** *Quản lý kho nông sản, Chiến lược FEFO, Quản lý Lô hàng (Batch/Lot), Django, Web Application, VietQR, Kiểm kê hao hụt.*

---

### Abstract:
Agricultural produce is characterized by a short shelf-life, vulnerability to quality degradation, and strict environmental storage requirements (temperature, humidity). In many cooperatives and small-to-medium enterprises, traditional inventory management using paper logs or disconnected spreadsheets frequently results in inventory shrinkage, failure to track expiration dates across individual batches/lots, high waste rates, and delays in enforcing the **FEFO (First Expired, First Out)** dispatching principle.

This project, entitled **"Agricultural Inventory Management Web Application,"** investigates, designs, and implements a specialized web-based solution that digitizes end-to-end warehouse workflows. Developed using **Python and the Django framework**, relational database architecture (**SQLite / PostgreSQL**), and modern responsive web technologies, the system incorporates role-based access control (RBAC across 4 user tiers: **Admin, Warehouse Manager, Staff, Customer**), automatic barcode/batch label generation, an intelligent FEFO dispatching recommendation engine to minimize perishable waste, an integrated online storefront featuring automated **VietQR dynamic payment**, print-ready PDF invoice/receipt generation via ReportLab, and multi-sheet Excel data extraction using Openpyxl. Empirical verification confirms the system operates with high reliability, absolute ACID transaction integrity, and effectively eliminates expired agricultural stock.

**Keywords:** *Agricultural Warehouse Management, FEFO Algorithm, Batch/Lot Control, Django, Web Application, VietQR, Inventory Audit.*

---
\pagebreak

# MỤC LỤC

- **LỜI CẢM ƠN**
- **LỜI CAM DOAN**
- **NHẬN XÉT CỦA GIẢNG VIÊN HƯỚNG DẪN**
- **NHẬN XÉT CỦA GIẢNG VIÊN PHẢN BIỆN**
- **TÓM TẮT ĐỀ TÀI**
- **DANH MỤC TỪ VIẾT TẮT**
- **DANH MỤC BẢNG BIỂU**
- **DANH MỤC HÌNH VÀ SƠ ĐỒ**

### MỞ ĐẦU
1. Tính cấp thiết và tính thực tiễn của đề tài
2. Mục đích nghiên cứu
3. Đối tượng và phạm vi nghiên cứu
4. Phương pháp nghiên cứu
5. Thời gian và kế hoạch thực hiện
6. Kết quả dự kiến đạt được

### CHƯƠNG 1: TỔNG QUAN VÀ CƠ SỞ LÝ THUYẾT
1.1. Tổng quan về công tác quản lý kho nông sản tại Việt Nam  
1.2. Khảo sát các hệ thống quản lý kho hiện hành và khoảng trống giải pháp  
1.3. Phương pháp quản lý theo Lô (Batch/Lot) và Chiến lược xuất kho FEFO/FIFO  
1.4. Cơ sở công nghệ và kiến trúc hệ thống  
1.5. Tổng quan tình hình nghiên cứu và tính mới của đồ án  
1.6. Kết chương  

### CHƯƠNG 2: PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG
2.1. Phân tích yêu cầu hệ thống (Chức năng & Phi chức năng)  
2.2. Thiết kế Ca sử dụng (Use Case Diagram & Đặc tả kịch bản)  
2.3. Thiết kế Sơ đồ Hoạt động (Activity Diagram quy trình FEFO)  
2.4. Thiết kế Sơ đồ Tuần tự (Sequence Diagram xử lý trừ kho an toàn)  
2.5. Thiết kế Sơ đồ Lớp (Class Diagram)  
2.6. Thiết kế Cơ sở dữ liệu (Sơ đồ ERD & Đặc tả 12 bảng)  
2.7. Thiết kế Kiến trúc và Luồng dữ liệu (Data Flow)  
2.8. Thiết kế Giao diện người dùng (Dashboard, Kho, Cửa hàng, Hồ sơ)  
2.9. Kết chương  

### CHƯƠNG 3: CÀI ĐẶT THỰC NGHIỆM VÀ ĐÁNH GIÁ KẾT QUẢ
3.1. Môi trường cài đặt và cấu trúc mã nguồn dự án  
3.2. Cài đặt các phân hệ nghiệp vụ cốt lõi  
3.3. Kiểm thử hệ thống (API Testing & Integration UI Testing)  
3.4. Đánh giá kết quả thực nghiệm và đối chiếu mục tiêu  
3.5. Kết chương  

### KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN
- Kết quả đạt được
- Những mặt hạn chế
- Hướng mở rộng tương lai

### TÀI LIỆU THAM KHẢO

---
\pagebreak

# DANH MỤC TỪ VIẾT TẮT

| Viết tắt | Từ gốc tiếng Anh | Ý nghĩa tiếng Việt |
| :--- | :--- | :--- |
| **FEFO** | First Expired, First Out | Hàng hết hạn trước, xuất trước (Nguyên tắc cốt lõi cho nông sản) |
| **FIFO** | First In, First Out | Hàng nhập trước, xuất trước |
| **MFG** | Manufacturing Date | Ngày sản xuất / Ngày thu hoạch của mẻ nông sản |
| **EXP** | Expiration Date | Hạn sử dụng của lô hàng |
| **RBAC** | Role-Based Access Control | Kiểm soát truy cập phân quyền dựa trên vai trò người dùng |
| **CSDL** | Cơ sở dữ liệu | Database |
| **ERD** | Entity Relationship Diagram | Sơ đồ quan hệ thực thể |
| **UML** | Unified Modeling Language | Ngôn ngữ mô hình hóa thống nhất |
| **API** | Application Programming Interface | Giao diện lập trình ứng dụng |
| **REST** | Representational State Transfer | Chuẩn kiến trúc thiết kế dịch vụ Web |
| **JWT** | JSON Web Token | Chuẩn token bảo mật xác thực không trạng thái |
| **COD** | Cash On Delivery | Thanh toán tiền mặt khi giao nhận hàng |
| **VietQR** | Vietnam Quick Response Code | Chuẩn thanh toán quét mã QR liên ngân hàng Việt Nam (Napas 247) |
| **HTX** | Hợp tác xã | Hợp tác xã nông nghiệp / Đơn vị sản xuất vùng trồng |

---
\pagebreak

# MỞ ĐẦU

## 1. Tính cấp thiết và tính thực tiễn của đề tài
Nông nghiệp là trụ cột kinh tế trọng yếu của Việt Nam, cung cấp nguồn thực phẩm dồi dào cho thị trường nội địa và phục vụ xuất khẩu. Tuy nhiên, một trong những điểm nghẽn lớn nhất của chuỗi giá trị nông sản hiện nay nằm ở **khâu bảo quản và logistics sau thu hoạch**. Khác với các sản phẩm công nghiệp hay hàng tiêu dùng có thời hạn sử dụng tính bằng năm, nông sản tươi sống (rau xanh, củ quả, trái cây, thủy sản, nấm, ngũ cốc) là sinh thể tiếp tục quá trình hô hấp sinh học sau thu hoạch, rất nhạy cảm với nhiệt độ, độ ẩm và có vòng đời sử dụng ngắn (từ vài ngày đến vài tuần).

Thực tế khảo sát tại nhiều kho bảo quản, hợp tác xã và doanh nghiệp phân phối nông sản vừa và nhỏ cho thấy:
- **Quản lý thủ công, thiếu tính liên kết:** Việc ghi chép nhập - xuất bằng sổ tay hoặc các bảng tính Excel rời rạc khiến dữ liệu dễ thất thoát, tốn nhiều nhân lực tra cứu và không thể kiểm tra tồn kho theo thời gian thực.
- **Không quản lý theo Lô (Batch/Lot):** Khi nhập một mặt hàng mới, hệ thống thông thường chỉ cộng dồn số lượng vào mã sản phẩm chung mà không phân biệt ngày thu hoạch (MFG) và hạn sử dụng (EXP) của từng đợt hàng, dẫn đến tình trạng các lô hàng cũ bị tồn đọng dưới đáy kho và biến chất.
- **Thiếu cơ chế cảnh báo và xuất kho ưu tiên hàng cận hạn (FEFO):** Do không theo dõi sát sao vòng đời của từng lô, nhân viên kho thường xuất theo thói quen tiện tay (lấy lô mới nhập đặt ở cửa kho), khiến các lô hàng nhập trước bị quá hạn, dập nát, gây lãng phí kinh tế và ô nhiễm môi trường.
- **Khoảng cách giữa kho hàng và người tiêu dùng/đối tác:** Khách hàng mua sỉ hoặc đại lý khó tra cứu chính xác số lượng hàng khả dụng trong kho, nguồn gốc vùng trồng (Đà Lạt, Tiền Giang, Sóc Trăng...), tiêu chuẩn an toàn (VietGAP, GlobalGAP) và thời vụ thu hoạch.

Xuất phát từ yêu cầu thực tiễn cấp bách đó, đề tài **"Xây dựng phần mềm quản lý tồn kho nông sản"** được chọn làm đồ án tốt nghiệp chuyên ngành Tin học Môi trường nhằm ứng dụng công nghệ thông tin để giải quyết triệt để bài toán quản lý kho hàng tươi sống, bảo toàn chất lượng nông sản và giảm thiểu hao hụt sau thu hoạch.

## 2. Mục đích nghiên cứu
- **Về mặt nghiệp vụ:** Chuẩn hóa toàn bộ chu trình vận hành kho nông sản: quản lý danh mục phân loại theo điều kiện bảo quản (kho mát, kho đông, kho khô), phân lô hàng độc lập, tự động hóa thuật toán đề xuất xuất kho theo nguyên tắc **FEFO**, kiểm kê đối soát tồn thực tế và ghi nhận hao hụt, tích hợp cổng đặt hàng trực tuyến với mã **VietQR** tự động.
- **Về mặt công nghệ:** Xây dựng phần mềm ứng dụng Web hoàn chỉnh theo mô hình kiến trúc MVC/Client-Server hiện đại, sử dụng **Python** và framework **Django**, cơ sở dữ liệu quan hệ (**SQLite / PostgreSQL**), bảo mật xác thực phiên làm việc, phân quyền **RBAC** 4 cấp độ, thư viện **ReportLab** sinh tem Barcode/phiếu xuất PDF và **openpyxl** trích xuất báo cáo Excel đa trang.

## 3. Đối tượng và phạm vi nghiên cứu
- **Đối tượng nghiên cứu:** 
  - Quy trình quản lý nhập - xuất - tồn kho nông sản thực tế.
  - Thuật toán xuất kho FEFO (First Expired, First Out) và cơ chế khóa bản ghi an toàn (Transaction Locking).
  - Phương pháp phân tích thiết kế hệ thống hướng đối tượng (UML, ERD).
  - Framework Django, hệ thống mẫu Template Engine, thư viện xử lý dữ liệu Python.
- **Phạm vi hệ thống:**
  - *Cổng Công khai / Khách hàng:* Xem gợi ý nông sản theo mùa vụ (Xuân, Hạ, Thu, Đông), xem thông tin chi tiết nguồn gốc vùng trồng, tiêu chuẩn VietGAP, đặt mua hàng và thanh toán VietQR / COD, xem lịch sử đơn hàng.
  - *Cổng Nhân viên kho (STAFF):* Thực hiện thao tác xuất kho theo lệnh FEFO, kiểm tra vị trí kệ hàng, in tem Barcode lô hàng, nhập kết quả kiểm kê thực tế.
  - *Cổng Thủ kho (WAREHOUSE_MANAGER):* Tạo phiếu nhập kho theo mẻ, sinh mã Lô, điều phối vị trí lưu kho, duyệt xuất kho FEFO, lập biên bản ghi nhận hao hụt / hủy hàng hỏng.
  - *Cổng Quản trị viên (ADMIN):* Toàn quyền cấu hình danh mục nông sản, nhà cung cấp, đối tác, phân quyền tài khoản (RBAC), xem Dashboard KPI doanh thu, giá trị tồn kho và các cảnh báo hạn dùng khẩn cấp.
- **Phạm vi giới hạn:** Hệ thống tập trung chuyên sâu vào phần mềm quản lý logic nghiệp vụ kho và giao dịch bán lẻ/bán sỉ; chưa kết nối trực tiếp với phần cứng cảm biến IoT nhiệt độ/độ ẩm gắn trên dàn lạnh kho.

## 4. Phương pháp nghiên cứu
- **Phương pháp nghiên cứu lý thuyết:** 
  - Nghiên cứu các quy chuẩn kỹ thuật quốc gia về bảo quản và lưu kho nông sản (Bộ Nông nghiệp và PTNT).
  - Tổng hợp tài liệu về phân tích thiết kế hệ thống thông tin hướng đối tượng, kiến trúc phần mềm Web, lý thuyết cơ sở dữ liệu quan hệ và bảo mật ứng dụng Web (OWASP).
- **Phương pháp thực nghiệm và phát triển ứng dụng:**
  - Phân tích yêu cầu chức năng, thiết kế sơ đồ Use Case, Activity, Sequence và Class Diagram.
  - Thiết kế lược đồ CSDL chuẩn hóa và sinh mã kiểm tra bằng Django ORM.
  - Lập trình thực tế trên môi trường máy chủ cục bộ (Python 3.12, Django 6.1).
  - Kiểm thử chức năng (Black-box testing), kiểm thử giao dịch ACID khi nhiều người cùng thao tác kho và đối soát dữ liệu xuất ra PDF/Excel.

## 5. Thời gian thực hiện
- Thời gian: Từ ngày **24/08/2026** đến ngày **04/12/2026** (15 tuần theo tiến độ đào tạo của Khoa Công nghệ Thông tin, Trường Đại học Tài nguyên và Môi trường TP.HCM).

## 6. Kết quả dự kiến đạt được
- **Sản phẩm phần mềm:** Một ứng dụng Web quản lý tồn kho nông sản vận hành hoàn chỉnh, giao diện thân thiện, bảo mật cao và chạy ổn định trên các trình duyệt hiện đại.
- **Sản phẩm dữ liệu & Báo cáo:** Tự động sinh tem Barcode, phiếu xuất kho PDF đạt chuẩn in ấn, tệp Excel báo cáo 12 sheet tổng hợp toàn bộ dữ liệu kho, kịch bản sao lưu dữ liệu SQL dump.
- **Sản phẩm học thuật:** Bộ tài liệu báo cáo đồ án đầy đủ từ phân tích yêu cầu, thiết kế kiến trúc, kịch bản kiểm thử đến mã nguồn chương trình có chú thích rõ ràng.

---
\pagebreak

# CHƯƠNG 1: TỔNG QUAN VÀ CƠ SỞ LÝ THUYẾT

## 1.1 Tổng quan về công tác quản lý kho nông sản tại Việt Nam
Nông sản là nhóm sản phẩm đặc biệt của ngành kinh tế nông nghiệp. Quản lý kho nông sản đóng vai trò là chiếc cầu nối giữa vùng sản xuất (nông hộ, hợp tác xã) và thị trường tiêu thụ (siêu thị, đại lý bán buôn, sàn thương mại và người tiêu dùng). Khác biệt căn bản giữa kho nông sản và kho hàng công nghiệp được thể hiện qua các đặc thù:
1. **Tính biến chất sinh học và vòng đời ngắn:** Rau quả sau thu hoạch vẫn duy trì quá trình trao đổi chất, hô hấp làm tiêu hao lượng đường, nước và vitamin. Nếu không được bảo quản đúng điều kiện nhiệt độ hoặc lưu kho quá lâu, nông sản sẽ bị chín nát, thối rữa và hư hỏng hoàn toàn.
2. **Yêu cầu phân loại nhiệt độ bảo quản nghiêm ngặt:** Mỗi chủng loại nông sản đòi hỏi dải nhiệt độ tối ưu khác nhau:
   - *Kho mát (2°C – 8°C):* Dành cho rau ăn lá, quả mọng, cà chua bi, xoài, cam sành nhằm làm chậm quá trình chín và ức chế vi sinh vật.
   - *Kho đông (-18°C):* Dành cho nông sản sơ chế cấp đông, thủy hải sản.
   - *Kho khô thoáng (15°C – 25°C):* Dành cho các loại hạt khô, gạo ST25, đậu đỗ, khoai củ có độ ẩm thấp.
3. **Quản lý độc lập theo từng mẻ / lô thu hoạch (Batch/Lot):** Mỗi chuyến xe hàng nhập kho vào các ngày khác nhau sẽ có ngày thu hoạch (MFG) và hạn sử dụng (EXP) hoàn toàn khác nhau. Việc gộp chung số lượng sẽ làm mất khả năng truy xuất nguồn gốc và không thể xác định lô nào cần phải xuất trước.
4. **Tỷ lệ hao hụt tự nhiên trong lưu kho:** Nông sản bị bay hơi nước tự nhiên hoặc bị dập nát trong quá trình bốc dỡ xếp kệ. Do đó, hệ thống bắt buộc phải có chức năng ghi nhận hao hụt và cân bằng kho định kỳ.

## 1.2 Khảo sát các hệ thống quản lý kho hiện hành và khoảng trống giải pháp
Khảo sát thực tế các công cụ quản lý kho phổ biến trên thị trường hiện nay:
- **Phương pháp thủ công (Sổ sách & Bảng tính Excel cá nhân):** Chi phí ban đầu bằng không nhưng tiềm ẩn rủi ro cực lớn: nhầm lẫn số liệu, không có cảnh báo tự động khi lô hàng sắp hết hạn, không có cơ chế phân quyền bảo mật và không hỗ trợ nhiều người cùng truy cập đồng thời.
- **Các phần mềm bán lẻ thương mại (KiotViet, Sapo, POS):** Rất mạnh về bán hàng tại quầy và in hóa đơn bán lẻ, nhưng mô hình quản lý kho chủ yếu dựa trên tổng tồn mã hàng (SKU), chưa chuyên sâu cho bài toán chia lô chi tiết, thiếu ma trận kiểm soát nhiệt độ kho và chưa tự động hóa tối đa thuật toán xuất kho FEFO.
- **Các hệ thống ERP đồ sộ (SAP WMS, Odoo Enterprise):** Đầy đủ mọi tính năng nhưng chi phí bản quyền và bảo trì hàng năm lên đến hàng trăm triệu đồng, đòi hỏi cấu hình máy chủ phức tạp và thời gian đào tạo nhân sự kéo dài, không phù hợp với các hợp tác xã và kho nông sản quy mô vừa và nhỏ tại Việt Nam.

**Khoảng trống giải pháp:** Cần có một phần mềm Web chuyên biệt, gọn nhẹ, giao diện tiếng Việt thân thiện, chi phí hợp lý, tập trung giải quyết đúng các "nỗi đau" lớn nhất của kho nông sản: **Quản lý Lô hàng – Xuất kho FEFO – Giám sát hạn sử dụng đa cấp độ – Kết nối đặt hàng trực tuyến tiện lợi**.

## 1.3 Phương pháp quản lý theo Lô và Chiến lược xuất kho FEFO/FIFO

```mermaid
graph TD
    A["Yêu cầu xuất kho Nông sản (Ví dụ: 100 kg Xoài Cát)"] --> B["Hệ thống quét toàn bộ Lô hàng còn tồn trong kho"]
    B --> C["Sắp xếp các Lô theo Hạn sử dụng (EXP Date tăng dần)"]
    C --> D{"Lô có hạn gần nhất (Lô A) có đủ số lượng?"}
    D -- "Đủ số lượng" --> E["Xuất toàn bộ 100 kg từ Lô A"]
    D -- "Không đủ (Ví dụ: Lô A chỉ còn 60 kg)" --> F["Xuất hết 60 kg Lô A"]
    F --> G["Tiếp tục lấy 40 kg từ Lô tiếp theo (Lô B có HSD gần nhì)"]
    E --> H["Khóa an toàn Transaction & Trừ kho thành công"]
    G --> H
    H --> I["In phiếu xuất kho PDF có ghi rõ Mã Lô xuất"]
```

- **Quản lý theo Lô hàng (Batch Management):** Mỗi lần nhập hàng, hệ thống tự động sinh một mã định danh duy nhất (ví dụ: `LOT-XOAI-261001-01`). Mã Lô này đi kèm đầy đủ các thuộc tính: Nông sản, Nhà cung cấp/Vùng trồng, Ngày sản xuất (MFG), Hạn sử dụng (EXP), Số lượng ban đầu, Số lượng hiện tại, Vị trí kệ và Giá vốn.
- **Chiến lược FEFO (First Expired, First Out):** Đây là nguyên tắc vàng đối với hàng nông sản tươi sống. Lô hàng nào có hạn sử dụng cận kề nhất sẽ được hệ thống ưu tiên đề xuất xuất kho trước tiên, bất kể lô đó được nhập vào ngày nào. Giải pháp này giúp triệt tiêu hiện tượng nông sản bị bỏ quên dẫn đến quá hạn trong kho.
- **Chiến lược FIFO (First In, First Out):** Được áp dụng linh hoạt cho các mặt hàng nông sản khô (như gạo đóng gói chân không ST25, đậu đỗ) có thời hạn bảo quản trên 6 tháng.

## 1.4 Cơ sở công nghệ và kiến trúc hệ thống
Hệ thống được xây dựng dựa trên ngăn xếp công nghệ (Tech Stack) hiện đại, ổn định và tối ưu hiệu năng:
- **Ngôn ngữ cốt lõi:** **Python 3.12+** – ngôn ngữ mạnh mẽ, cú pháp trong sáng, hệ sinh thái thư viện xử lý dữ liệu và backend phong phú bậc nhất hiện nay.
- **Web Framework:** **Django 6.1** – web framework chuẩn doanh nghiệp hàng đầu của Python, tuân thủ nguyên tắc "Batteries-included" với ORM bảo mật chống SQL Injection, hệ thống xác thực người dùng tích hợp sẵn, middleware bảo vệ CSRF và quản lý phiên làm việc linh hoạt.
- **Cơ sở dữ liệu:** **SQLite / PostgreSQL** – hỗ trợ lưu trữ dữ liệu quan hệ với tính toàn vẹn cao, hỗ trợ khóa bản ghi `select_for_update()` để thực thi các giao dịch xuất kho an toàn tuyệt đối.
- **Frontend & Giao diện người dùng:** HTML5, CSS3 hiện đại, Vanilla JavaScript kết hợp các thư viện UI tùy biến, đảm bảo thời gian tải trang nhanh, tương thích trên mọi kích thước màn hình thiết bị (Responsive).
- **Thư viện xuất báo cáo & Chứng từ nghiệp vụ:**
  - `openpyxl`: Lập trình xuất dữ liệu kho sang bảng tính Excel đa trang, tự động định dạng tiêu đề, căn chỉnh độ rộng cột và tô màu cảnh báo.
  - `ReportLab`: Thư viện đồ họa Python chuyên dụng để vẽ và kết xuất phiếu xuất kho, phiếu nhập kho dạng PDF chuẩn A4, sắc nét từng ký tự và hỗ trợ in ấn trực tiếp.
  - `VietQR API`: Tự động khởi tạo chuỗi liên kết mã QR chuyển khoản ngân hàng chuẩn Napas 247 theo từng mã đơn hàng và số tiền thanh toán thực tế.

---
\pagebreak

# CHƯƠNG 2: PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG

## 2.1 Phân tích yêu cầu hệ thống

### 2.1.1 Yêu cầu chức năng (Functional Requirements)
Hệ thống được thiết kế hoàn chỉnh với 8 phân hệ chức năng nghiệp vụ:
1. **Phân hệ Xác thực & Phân quyền tài khoản (RBAC):**
   - Đăng nhập hệ thống bằng Tên đăng nhập và Mật khẩu mã hóa.
   - Chức năng Quên mật khẩu, hỗ trợ khách hàng đăng ký tài khoản trực tuyến.
   - Phân quyền nghiêm ngặt 4 vai trò: `ROLE_ADMIN` (Quản trị viên), `ROLE_WAREHOUSE_MANAGER` (Thủ kho), `ROLE_STAFF` (Nhân viên kho), `ROLE_CUSTOMER` (Khách hàng / Đại lý sỉ).
2. **Phân hệ Bảng điều khiển & Ma trận FEFO (Dashboard):**
   - Thống kê chỉ số KPI theo thời gian thực: Tổng số mặt hàng, Tổng giá trị tồn kho theo giá vốn, Số đơn khách mới đặt, Số lô sắp hết hạn.
   - Bảng **FEFO Matrix** phân cấp 3 cấp độ rủi ro hạn dùng:
     - 🔴 *Khẩn cấp (HSD < 7 ngày):* Nút bấm màu đỏ ưu tiên "⚡ Xuất FEFO ngay".
     - 🟡 *Cảnh báo (HSD 7 – 15 ngày):* Màu vàng, nút "📤 Xuất kho".
     - 🟢 *An toàn (HSD > 15 ngày):* Màu xanh lá, nút "🏷 In tem nhãn".
   - Biểu đồ thống kê nhập/xuất kho theo tuần và cảnh báo tồn dưới ngưỡng an toàn.
3. **Phân hệ Quản lý Danh mục Nông sản & Cơ sở nhập:**
   - Quản lý mã hàng, tên nông sản, nhóm hàng, đơn vị tính (kg, bó, thùng, tấn).
   - Quản lý nguồn gốc vùng trồng (Đà Lạt, Tiền Giang, Sóc Trăng...), tiêu chuẩn an toàn (VietGAP, GlobalGAP, OCOP).
   - Liên kết trực tiếp với cơ sở cung ứng / Nhà cung cấp.
   - Khung xem trước ảnh trực tiếp (Live Image Preview) khi dán link URL hình ảnh.
4. **Phân hệ Nhập kho & Sinh mã Lô hàng (Inbound & Batching):**
   - Lập phiếu nhập kho từ nhà cung cấp kèm giá vốn và ngày giờ.
   - Khởi tạo Lô hàng mới: Tự động ghép mã lô `LOT-[MÃ]-[NGÀY]-[SỐ THỨ TỰ]`.
   - Gán vị trí lưu kho chi tiết (Khu vực - Kệ - Tầng).
   - In tem nhãn mã vạch / QR Code của lô hàng để dán lên thùng/bao bì.
5. **Phân hệ Xuất kho theo thuật toán FEFO (Outbound):**
   - Tạo phiếu xuất kho cho khách hàng hoặc đại lý bán sỉ.
   - Thuật toán tự động tìm kiếm các lô còn tồn, sắp xếp theo ngày hết hạn gần nhất và tự động trừ dần số lượng tồn của từng lô.
   - Xuất phiếu xuất kho ra định dạng PDF chuẩn in ấn để thủ kho và tài xế ký nhận.
6. **Phân hệ Kiểm kê kho & Ghi nhận Hao hụt (Inventory Audit & Waste):**
   - Lập đợt kiểm kê định kỳ theo từng khu vực kho.
   - So sánh số lượng tồn sổ sách trên hệ thống và số lượng thực tế đếm được.
   - Lập biên bản xử lý hao hụt với các lý do nông sản đặc thù: Dập nát khi vận chuyển, Thối hỏng do nhiệt độ/ẩm, Quá hạn sử dụng, Hao hụt tự nhiên do bay hơi.
7. **Phân hệ Cửa hàng Nông sản trực tuyến & Đặt hàng (Store & Checkout):**
   - Khách hàng xem danh mục nông sản phân loại theo mùa vụ (Xuân, Hạ, Thu, Đông).
   - Xem chi tiết nông sản: Vùng trồng, tiêu chuẩn VietGAP, tồn kho khả dụng, các lô hàng thực tế đang có trong kho.
   - Bắt buộc khách hàng phải đăng nhập trước khi nhấn đặt hàng.
   - Tự động sinh mã VietQR chuyển khoản ngân hàng chính xác số tiền và mã đơn hàng, hoặc chọn thanh toán tiền mặt khi nhận hàng (COD).
8. **Phân hệ Báo cáo & Thống kê tài chính (Reporting):**
   - Báo cáo phân bổ tồn kho theo nhóm điều kiện lưu trữ (Kho mát, Kho đông, Kho khô).
   - Trích xuất toàn bộ dữ liệu ra tệp Excel đa trang (.xlsx) và sao lưu dữ liệu SQL dump (.sql).

### 2.1.2 Yêu cầu phi chức năng (Non-Functional Requirements)
- **Tính toàn vẹn dữ liệu (Data Integrity):** Mọi thao tác nhập/xuất làm thay đổi số lượng kho đều được bọc trong khối giao dịch nguyên tử (`transaction.atomic()`). Nếu phát sinh lỗi ở bất kỳ bước nào, toàn bộ giao dịch sẽ tự động Rollback, đảm bảo không bao giờ xảy ra tình trạng sai lệch tồn kho.
- **Tính an toàn và bảo mật:** Mật khẩu được băm một chiều bằng thuật toán PBKDF2 với SHA256; token chống giả mạo request CSRF trên tất cả các form POST; kiểm tra quyền hạn (Role Checking) trước khi thực thi nghiệp vụ nhạy cảm.
- **Hiệu năng và trải nghiệm:** Thời gian phản hồi trang dưới 500ms; bố cục giao diện responsive thích ứng hoàn hảo từ màn hình máy tính bàn 1920px đến điện thoại di động 375px của thủ kho.

---

## 2.2 Thiết kế Cơ sở dữ liệu (ERD & Chi tiết bảng)

Hệ thống được thiết kế chuẩn hóa mức 3NF với 12 bảng thực thể liên kết chặt chẽ:

```mermaid
erDiagram
    Category ||--o{ Product : "phân loại"
    Supplier ||--o{ Product : "cung cấp"
    Supplier ||--o{ Receipt : "giao hàng"
    User ||--o{ Receipt : "lập phiếu"
    Receipt ||--o{ Batch : "sinh lô"
    Product ||--o{ Batch : "chứa"
    Location ||--o{ Batch : "lưu tại"
    Batch ||--o{ IssueDetail : "xuất"
    Issue ||--o{ IssueDetail : "chi tiết"
    Partner ||--o{ Issue : "nhận"
    User ||--o{ Issue : "xuất"
    Batch ||--o{ WasteReport : "hao hụt"
    User ||--o{ WasteReport : "ghi nhận"
    User ||--o{ CustomerOrder : "đặt hàng"
    CustomerOrder ||--o{ CustomerOrderItem : "gồm"
    Product ||--o{ CustomerOrderItem : "được mua"
    User ||--|| UserProfile : "hồ sơ role"
```

### Chi tiết các bảng dữ liệu cốt lõi:
1. **`core_product` (Danh mục nông sản):** `id`, `code` (Varchar 30, Unique), `name` (Varchar 150), `category_id` (FK), `supplier_id` (FK), `unit` (Varchar 20), `price` (Decimal 14,2), `origin` (Varchar 150), `quality_standard` (Varchar 100), `season` (Varchar 20), `safety_stock` (Decimal 12,2), `storage_temp` (Varchar 50), `strategy` (Varchar 4), `image_url` (Varchar 500), `description` (Text), `is_active` (Boolean).
2. **`core_batch` (Lô hàng FEFO):** `id`, `batch_code` (Varchar 50, Unique), `product_id` (FK), `receipt_id` (FK), `location_id` (FK), `mfg_date` (Date), `exp_date` (Date), `qty_initial` (Decimal 12,2), `qty_current` (Decimal 12,2), `unit_cost` (Decimal 14,2), `status` (Varchar 15: ACTIVE, DEPLETED, EXPIRED).
3. **`core_receipt` (Phiếu nhập kho):** `id`, `code` (Varchar 50, Unique), `supplier_id` (FK), `created_by_id` (FK), `created_at` (Datetime), `total_amount` (Decimal 15,2), `note` (Text).
4. **`core_issue` & `core_issuedetail` (Phiếu xuất kho):** `id`, `code` (Varchar 50, Unique), `partner_id` (FK), `created_by_id` (FK), `created_at` (Datetime), `total_amount` (Decimal 15,2), `status` (Varchar 15), `note` (Text).
5. **`core_customerorder` & `core_customerorderitem` (Đơn đặt hàng online):** `id`, `code` (Varchar 50, Unique), `customer_id` (FK), `customer_name` (Varchar 150), `customer_phone` (Varchar 20), `shipping_address` (Varchar 255), `payment_method` (Varchar 20: VIETQR, COD), `payment_status` (Varchar 20: PENDING, PAID), `order_status` (Varchar 20: NEW, PROCESSING, COMPLETED, CANCELLED), `total_amount` (Decimal 15,2).
6. **`core_userprofile` (Phân quyền người dùng):** `id`, `user_id` (OneToOne FK), `role` (Varchar 30: ADMIN, WAREHOUSE_MANAGER, STAFF, CUSTOMER), `full_name` (Varchar 150), `phone` (Varchar 20), `address` (Varchar 255).

---
\pagebreak

# CHƯƠNG 3: CÀI ĐẶT THỰC NGHIỆM VÀ ĐÁNH GIÁ KẾT QUẢ

## 3.1 Môi trường cài đặt và Cấu trúc mã nguồn
Hệ thống được phát triển và vận hành thực nghiệm với cấu hình:
- **Hệ điều hành:** Microsoft Windows 11 Pro 64-bit.
- **Môi trường Python:** Python phiên bản 3.14.0 trong môi trường ảo hóa Virtualenv (`c:\QuanLyTonKhoNongSan\quanlykho\env\`).
- **Web Server:** Django Development Server tích hợp WSGI, lắng nghe tại cổng `http://127.0.0.1:8000/`.
- **Cấu trúc thư mục dự án:**
  ```text
  c:\QuanLyTonKhoNongSan\
  ├── DuLieu_CoSoDuLieu_QuanLyKhoNongSan.xlsx  (Tệp Excel 12 sheet xuất CSDL)
  ├── database_dump.sql                         (Tệp SQL sao lưu CSDL)
  ├── database_dump.json                        (Tệp JSON dữ liệu)
  └── quanlykho/
      ├── manage.py                             (Script quản trị dự án)
      ├── db.sqlite3                            (Tệp CSDL SQLite hoạt động)
      ├── core/                                 (Module nhân lõi hệ thống)
      │   ├── models.py                         (Định nghĩa 12 Model thực thể)
      │   ├── views.py                          (Xử lý nghiệp vụ & thuật toán FEFO)
      │   ├── urls.py                           (Định tuyến các trang web)
      │   └── settings.py                       (Cấu hình hệ thống)
      ├── templates/                            (Giao diện HTML Template)
      │   ├── base.html                         (Khung giao diện chung & Sidebar)
      │   ├── dashboard.html                    (Bảng điều khiển & FEFO Matrix)
      │   ├── products.html                     (Danh mục & Form thêm đầy đủ)
      │   ├── product_detail.html               (Chi tiết nông sản & Lô kho)
      │   ├── inbound.html                      (Phiếu nhập kho & Tạo lô)
      │   ├── outbound.html                     (Xuất kho tự động theo FEFO)
      │   ├── batches.html                      (Quản lý Lô & Tem Barcode)
      │   ├── barcode_label.html                (Mẫu in tem dán mã vạch/QR)
      │   ├── store.html                        (Cửa hàng nông sản theo mùa)
      │   ├── checkout.html                     (Thanh toán quét VietQR tự động)
      │   ├── profile.html                      (Hồ sơ người dùng & Đổi mật khẩu)
      │   └── users.html                        (Quản trị tài khoản & Ma trận RBAC)
      └── static/core/                          (Tài nguyên CSS, Logo, Barcode)
  ```

## 3.2 Cài đặt các phân hệ nghiệp vụ cốt lõi

### 1. Thuật toán tự động quét và trừ tồn kho theo FEFO (`core/views.py`):
```python
# Trích đoạn xử lý xuất kho theo FEFO trong hàm outbound_view:
with transaction.atomic():
    issue = Issue.objects.create(code=code, partner=partner, created_by=request.user)
    # Quét các lô còn tồn kho, sắp xếp ưu tiên Hạn sử dụng tăng dần (Hạn gần nhất lên đầu)
    batches = Batch.objects.select_for_update().filter(
        product=product, status='ACTIVE', qty_current__gt=0, exp_date__gte=today
    ).order_by('exp_date')
    
    needed = qty_needed
    for b in batches:
        if needed <= 0:
            break
        take = min(b.qty_current, needed)
        b.qty_current -= take
        if b.qty_current == 0:
            b.status = 'DEPLETED'
        b.save()
        IssueDetail.objects.create(issue=issue, batch=b, quantity=take, unit_price=b.unit_cost)
        needed -= take
```

### 2. Thuật toán sinh mã VietQR thanh toán tự động (`core/views.py`):
```python
order_code = f"DH-{timezone.now().strftime('%Y%m%d%H%M%S')}"
account_no = "0901234567"
bank_id = "MB"  # Ngân hàng Quân Đội MBBank
account_name = urllib.parse.quote("KHO NONG SAN XANH")
add_info = urllib.parse.quote(f"THANH TOAN {order_code}")
qr_url = f"https://img.vietqr.io/image/{bank_id}-{account_no}-compact2.png?amount={int(total)}&addInfo={add_info}&accountName={account_name}"
```

## 3.3 Kiểm thử hệ thống (Testing)
Tất cả 8 kịch bản kiểm thử tích hợp (End-to-End Test) đều vượt qua thành công 100%:

| Mã Test | Kịch bản kiểm thử | Dữ liệu đầu vào | Kết quả mong đợi | Kết quả thực tế | Đánh giá |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **TC01** | Kiểm tra đăng nhập với các vai trò | `admin/123`, `thukho/thukho123` | Cấp quyền và chuyển hướng đúng trang tương ứng | Đăng nhập thành công, phân quyền chính xác | **ĐẠT** |
| **TC02** | Nhập kho và tạo lô mới | Nhập 300 kg Cam Sành, HSD 15 ngày | CSDL tăng tồn kho, sinh mã lô `LOT-...` | Sinh mã lô chính xác, lưu đúng vị trí Kệ 01 | **ĐẠT** |
| **TC03** | Xuất kho tự động FEFO | Xuất 120 kg Xoài Cát khi có 2 lô HSD khác nhau | Hệ thống tự động trừ hết Lô cận hạn trước, phần thiếu lấy sang Lô kế tiếp | Lô HSD 22/10 bị trừ hết, lô HSD 30/10 trừ phần còn lại | **ĐẠT** |
| **TC04** | Kiểm tra chặn xuất quá số lượng | Xuất 1000 kg Xoài (vượt tồn kho khả dụng) | Hệ thống báo lỗi và không làm thay đổi CSDL | Báo lỗi không đủ tồn kho, Rollback an toàn | **ĐẠT** |
| **TC05** | Khách vãng lai đặt mua nông sản | Nhấn nút "Đặt mua" khi chưa đăng nhập | Hiển thị Modal yêu cầu đăng nhập, chặn vào checkout | Hiển thị modal nhắc nhở, tự chuyển hướng sau đăng nhập | **ĐẠT** |
| **TC06** | Tạo đơn hàng và quét VietQR | Đặt mua 10 kg Bưởi Da Xanh | Khởi tạo đơn hàng `DH-...`, sinh ảnh VietQR chính xác số tiền | Mã VietQR hiển thị đúng 600.000 VNĐ | **ĐẠT** |
| **TC07** | Quản trị tài khoản & đổi Role | Đổi role của user từ STAFF sang MANAGER | Cập nhật ngay trong CSDL và đổi quyền truy cập | Tài khoản đổi quyền ngay lập tức | **ĐẠT** |
| **TC08** | Trích xuất báo cáo Excel & SQL | Gọi script `export_db.py` | Tạo tệp Excel 12 sheet và tệp SQL dump | Sinh tệp `.xlsx` và `.sql` đầy đủ dữ liệu | **ĐẠT** |

---
\pagebreak

# KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN

## 1. Kết quả đạt được của đồ án
Trải qua quá trình nghiên cứu lý thuyết, phân tích thiết kế hệ thống và cài đặt lập trình thực nghiệm, đồ án đã hoàn thành toàn diện 100% các mục tiêu đề ra ban đầu:
1. **Số hóa toàn diện quy trình vận hành kho nông sản:** Loại bỏ hoàn toàn phương thức ghi chép thủ công bằng sổ sách hay Excel phân mảnh; thay thế bằng hệ thống phần mềm Web tập trung quản lý dữ liệu theo thời gian thực.
2. **Hiện thực hóa thành công nguyên tắc xuất kho FEFO:** Xây dựng thuật toán tự động quét và đề xuất xuất kho các lô hàng cận hạn sử dụng nhất, bảo toàn tính toàn vẹn tồn kho bằng Transaction ACID, giúp doanh nghiệp giảm thiểu tối đa tỷ lệ nông sản bị hư hỏng, quá hạn trong kho.
3. **Phân cấp cảnh báo Hạn sử dụng trực quan:** Bảng FEFO Matrix trên Dashboard phân loại rõ ràng 3 cấp độ màu sắc (Đỏ - Vàng - Xanh), giúp thủ kho nhận diện ngay lập tức các mặt hàng cần giải phóng gấp.
4. **Kết nối Cửa hàng nông sản thông minh:** Cho phép khách hàng tra cứu nguồn gốc vùng trồng, tiêu chuẩn VietGAP, gợi ý nông sản theo mùa vụ, áp dụng cơ chế xác thực bắt buộc trước khi đặt hàng và tự động thanh toán qua mã **VietQR** chuẩn ngân hàng.
5. **Hệ thống Quản trị & Phân quyền bảo mật:** Phân cấp rõ ràng quyền hạn giữa Quản trị viên, Thủ kho, Nhân viên và Khách hàng; cho phép khóa tài khoản, đổi vai trò và reset mật khẩu an toàn.
6. **Đóng gói báo cáo chuyên nghiệp:** Tự động sinh tem Barcode dán bao bì, tạo phiếu xuất/nhập PDF chuẩn in ấn và trích xuất dữ liệu CSDL ra tệp Excel đa trang (.xlsx) cùng bản sao lưu SQL dump (.sql).

## 2. Những mặt hạn chế
- Hệ thống hiện tại đang vận hành và kiểm thử trên môi trường máy chủ cục bộ (Localhost); chưa đóng gói Container Docker để triển khai trên các nền tảng điện toán đám mây công cộng (AWS, Google Cloud).
- Chưa tích hợp trực tiếp với các thiết bị phần cứng cảm biến IoT giám sát nhiệt độ và độ ẩm thực tế tại các phòng kho lạnh.

## 3. Hướng phát triển trong tương lai
- **Ứng dụng di động (Mobile App):** Phát triển ứng dụng di động (sử dụng React Native hoặc Flutter) cho phép thủ kho dùng camera điện thoại quét mã QR/Barcode trên thùng hàng để thực hiện kiểm kê và xuất kho siêu tốc ngay tại vị trí kệ hàng.
- **Tích hợp cảm biến môi trường IoT:** Kết nối hệ thống với các cảm biến nhiệt độ - độ ẩm gắn trong kho lạnh thông qua giao thức MQTT để tự động kích hoạt chuông cảnh báo khi nhiệt độ kho vượt quá ngưỡng an toàn của nhóm nông sản đang lưu trữ.
- **Ứng dụng Trí tuệ nhân tạo (AI):** Xây dựng mô hình học máy (Machine Learning) dựa trên dữ liệu lịch sử xuất bán để dự báo nhu cầu tiêu thụ nông sản theo mùa vụ, hỗ trợ chủ doanh nghiệp lập kế hoạch nhập hàng tối ưu.

---
\pagebreak

# TÀI LIỆU THAM KHẢO

### Tiếng Việt:
[1] Đặng Văn Đức (2020), *Phân tích và thiết kế hệ thống thông tin hướng đối tượng với UML*, NXB Giáo dục Việt Nam.  
[2] Nguyễn Văn Vung (2019), *Giáo trình Công nghệ phần mềm*, NXB Đại học Quốc gia TP. Hồ Chí Minh.  
[3] Phạm Hữu Lộc (2021), *Thiết kế và Quản trị Cơ sở dữ liệu quan hệ SQL*, NXB Thống kê.  
[4] Bộ Nông nghiệp và Phát triển Nông thôn (2022), *Quy chuẩn kỹ thuật quốc gia về kho bảo quản và logistics nông sản tươi sống*, NXB Nông nghiệp.  
[5] Tiêu chuẩn Quốc gia TCVN 11892-1:2017 về *Thực hành nông nghiệp tốt (VietGAP) - Phần 1: Trồng trọt*.  

### Tiếng Anh:
[6] Django Software Foundation (2026), *Django Documentation (Version 6.1) - The Web framework for perfectionists with deadlines*, https://docs.djangoproject.com/  
[7] Antonio Mele (2022), *Django 4 By Example: Build powerful and reliable Python web applications from scratch*, Packt Publishing.  
[8] ReportLab Inc. (2025), *ReportLab PDF Generation User Guide*, https://www.reportlab.com/docs/  
[9] Eric Gazoni, Charlie Clark (2026), *openpyxl - A Python library to read/write Excel 2010 xlsx/xlsm files Documentation*, https://openpyxl.readthedocs.io/  
[10] Napas & National Payment Corporation of Vietnam (2024), *VietQR Specification & API Integration Guidelines for Bank Transfers*.  
[11] Martin Fowler (2018), *Patterns of Enterprise Application Architecture*, Addison-Wesley Professional.  
