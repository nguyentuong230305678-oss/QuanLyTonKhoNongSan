import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api";

export default function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const submit = async (e) => {
    e.preventDefault();
    try {
      // Gửi request tới endpoint login của Django
      const { data } = await api.post("/auth/login/", { username, password });
      
      // Lưu Token để dùng cho các request có bảo mật sau này
      localStorage.setItem("access", data.access);
      localStorage.setItem("roles", JSON.stringify(data.roles));
      
      // Chuyển hướng vào khu vực quản trị
      navigate("/app");
    } catch {
      setError("Sai tài khoản hoặc mật khẩu");
    }
  };

  return (
    <form onSubmit={submit} className="container mt-5" style={{ maxWidth: 400 }}>
      <h3>Đăng nhập</h3>
      {error && <div className="alert alert-danger">{error}</div>}
      <input className="form-control mb-2" placeholder="Tài khoản"
             value={username} onChange={(e) => setUsername(e.target.value)} />
      <input className="form-control mb-3" type="password" placeholder="Mật khẩu"
             value={password} onChange={(e) => setPassword(e.target.value)} />
      <button className="btn btn-success w-100">Đăng nhập</button>
    </form>
  );
}