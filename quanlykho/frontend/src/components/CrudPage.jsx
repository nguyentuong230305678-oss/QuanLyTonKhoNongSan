import { useEffect, useState } from "react";
import api from "../api";

export default function CrudPage({ title, endpoint, fields }) {
  const [rows, setRows] = useState([]);
  const [q, setQ] = useState("");
  const [form, setForm] = useState({});
  const [error, setError] = useState("");

  const load = () =>
    api.get(`/${endpoint}/`, { params: { search: q } }).then((r) => setRows(r.data));
  useEffect(() => { load(); }, [q]);

  const save = async (e) => {
    e.preventDefault();
    try {
      form.id ? await api.put(`/${endpoint}/${form.id}/`, form)
              : await api.post(`/${endpoint}/`, form);
      setForm({}); setError(""); load();
    } catch (err) {
      setError(JSON.stringify(err.response?.data || "Lỗi"));
    }
  };
  
  const remove = async (id) => {
    if (confirm("Xóa bản ghi này?")) {
      try { await api.delete(`/${endpoint}/${id}/`); load(); }
      catch { alert("Không xóa được (có thể đang được dùng hoặc bạn không có quyền)"); }
    }
  };

  return (
    <div>
      <h4>{title}</h4>
      <input className="form-control mb-3" placeholder="Tìm kiếm..."
             value={q} onChange={(e) => setQ(e.target.value)} />
      <form onSubmit={save} className="row g-2 mb-3">
        {fields.map((f) => (
          <div className="col" key={f.name}>
            <input className="form-control" placeholder={f.label}
                   value={form[f.name] ?? ""}
                   onChange={(e) => setForm({ ...form, [f.name]: e.target.value })} />
          </div>
        ))}
        <div className="col-auto"><button className="btn btn-success">Lưu</button></div>
      </form>
      {error && <div className="alert alert-danger">{error}</div>}
      <table className="table table-sm">
        <thead><tr>{fields.map((f) => <th key={f.name}>{f.label}</th>)}<th /></tr></thead>
        <tbody>{rows.map((r) => (
          <tr key={r.id}>
            {fields.map((f) => <td key={f.name}>{r[f.name]}</td>)}
            <td>
              <button className="btn btn-sm btn-outline-primary me-1" onClick={() => setForm(r)}>Sửa</button>
              <button className="btn btn-sm btn-outline-danger" onClick={() => remove(r.id)}>Xóa</button>
            </td>
          </tr>
        ))}</tbody>
      </table>
    </div>
  );
}