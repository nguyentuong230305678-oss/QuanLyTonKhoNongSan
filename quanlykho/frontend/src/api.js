import axios from "axios";

// Đặt baseURL trỏ tới API của Backend Django
const api = axios.create({ baseURL: "http://127.0.0.1:8000/api/v1" });

// Interceptor request: Tự động gắn token JWT vào Header nếu người dùng đã đăng nhập
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("access");
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

// Interceptor response: Xử lý lỗi tập trung
api.interceptors.response.use(
  (res) => res,
  (err) => {
    // Nếu Backend trả về mã 401 (Hết hạn hoặc sai token), tự động xóa bộ nhớ và đẩy về trang đăng nhập
    if (err.response?.status === 401) {
      localStorage.clear();
      window.location.href = "/login";
    }
    return Promise.reject(err);
  }
);

export default api;