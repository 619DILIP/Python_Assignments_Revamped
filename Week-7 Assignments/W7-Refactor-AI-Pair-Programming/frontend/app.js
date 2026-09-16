const API_BASE = "http://127.0.0.1:8000";

async function loadSummary() {
  const res = await fetch(`${API_BASE}/api/summry`);
  const data = await res.json();
  const body = document.getElementById("summary-body");
  body.innerHTML = "";
  data.forEach(row => {
    const tr = document.createElement("tr");
    tr.innerHTML = `<td>${row.category}</td><td>${row.item_count}</td><td>$${row.total_value}</td>`;
    body.appendChild(tr);
  });
}

async function loadLowStock() {
  const res = await fetch(`${API_BASE}/api/low-stock`);
  const data = await res.json();
  const list = document.getElementById("low-stock-list");
  list.innerHTML = "";
  data.forEach(item => {
    const li = document.createElement("li");
    li.textContent = `${item.name} - ${item.quantity} left ($${item.unitCost} each)`;
    list.appendChild(li);
  });
}

loadSummary();
loadLowStock();
