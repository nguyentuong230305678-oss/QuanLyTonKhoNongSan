import { useEffect, useState } from "react";
import api from "../api";

export default function PublicProducts() {
  const [rows, setRows] = useState([]);

  useEffect(() => {
    api.get("/public/products/").then((r) => setRows(r.data));
  }, []);

  return (
    <div className="container mt-4">
      <h3>Danh mục nông sản hiện có</h3>
      <table className="table">
        <thead>
          <tr><th>Mã</th><th>Tên</th><th>ĐVT</th><th>Nhóm</th><th>Nhiệt độ</th></tr>
        </thead>
        <tbody>
          {rows.map((r) => (
            <tr key={r.code}>
              <td>{r.code}</td><td>{r.name}</td><td>{r.unit}</td>
              <td>{r.category_name}</td><td>{r.storage_temp}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}