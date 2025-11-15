const priceEl = document.getElementById("price");
const coinSelector = document.getElementById("coinSelector");

let chart;

// Fetch price from backend
async function loadPrice(symbol) {
    const res = await fetch(`http://127.0.0.1:5000/price?symbol=${symbol}`);
    const data = await res.json();

    if (data.price_usd) {
        priceEl.textContent = "$ " + data.price_usd;
    } else {
        priceEl.textContent = "Unavailable";
    }
}

// Fetch history from backend
async function loadHistory(symbol) {
    const res = await fetch(`http://127.0.0.1:5000/history?symbol=${symbol}`);
    const data = await res.json();

    if (!Array.isArray(data)) return;

    const labels = data.map(item => new Date(item.timestamp).toLocaleTimeString());
    const prices = data.map(item => item.close);

    renderChart(labels, prices);
}

// Render chart
function renderChart(labels, prices) {
    if (chart) chart.destroy();

    const ctx = document.getElementById("chart").getContext("2d");

    chart = new Chart(ctx, {
        type: "line",
        data: {
            labels: labels,
            datasets: [{
                label: "Price (24h)",
                data: prices,
                borderWidth: 2,
                borderColor: "#00eaff",
                pointRadius: 0,
            }]
        },
        options: {
            responsive: true,
            scales: { x: { display: false } }
        }
    });
}

// Load everything
function refresh() {
    const symbol = coinSelector.value;
    loadPrice(symbol);
    loadHistory(symbol);
}

// Event
coinSelector.addEventListener("change", refresh);

// Auto refresh every 10 seconds
setInterval(refresh, 10000);

// First load
refresh();
