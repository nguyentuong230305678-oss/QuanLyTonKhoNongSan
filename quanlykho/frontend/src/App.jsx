import { BrowserRouter, Routes, Route, Navigate, Link, Outlet } from "react-router-dom";
import Login from "./pages/Login";
import PublicProducts from "./pages/PublicProducts";
import CrudPage from "./components/CrudPage"; // Import CrudPage

function Private() {
  return localStorage.getItem("access") ? <Layout /> : <Navigate to="/login" />;
}

function Layout() {
  const logout = () => { localStorage.clear(); window.location.href = "/login"; };
  return (
    <div className="d-flex">
      <nav className="bg-dark text-white p-3" style={{ width: 220, minHeight: "100vh" }}>
        <h5>Kho nông sản</h5>
        <Link className="d-block text-white mb-2" to="/app">Dashboard</Link>
        <Link className="d-block text-white mb-2" to="/app/products">Nông sản</Link>
        <Link className="d-block text-white mb-2" to="/app/suppliers">Nhà cung cấp</Link>
        <button className="btn btn-sm btn-outline-light mt-3" onClick={logout}>Đăng xuất</button>
      </nav>
      <main className="p-4 flex-fill"><Outlet /></main>
    </div>
  );
}

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<PublicProducts />} />
        <Route path="/login" element={<Login />} />
        <Route path="/app" element={<Private />}>
          <Route index element={<h4>Dashboard (tuần 11)</h4>} />
          <Route path="products" element={<CrudPage title="Nông sản" endpoint="products" fields={[
            { name: "code", label: "Mã" }, { name: "name", label: "Tên" },
            { name: "category", label: "Mã nhóm (ID)" }, { name: "unit", label: "ĐVT" },
            { name: "safety_stock", label: "Tồn an toàn" }, { name: "price", label: "Giá" } ]} />} />
          <Route path="suppliers" element={<CrudPage title="Nhà cung cấp" endpoint="suppliers" fields={[
            { name: "name", label: "Tên" }, { name: "phone", label: "Điện thoại" }, { name: "address", label: "Địa chỉ" } ]} />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}