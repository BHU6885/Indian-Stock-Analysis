let stockChart = null;

async function loadStockData() {

const stock = document.getElementById("stockSelect").value;

document.getElementById("loading").innerText = "Fetching stock data...";

document.getElementById("resultSection").style.display = "none";

try {

    const response = await fetch("/get_stock_data", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ stock: stock })
    });

    const data = await response.json();

    if (!response.ok) {
        throw new Error(data.error || "Unable to load stock data");
    }

    document.getElementById("loading").innerText = "";

    document.getElementById("resultSection").style.display = "block";

    document.getElementById("stockTitle").innerText =
        stock + " - Historical Closing Prices";

    const prices = data.prices.map(Number);

    document.getElementById("highestPrice").innerText =
        "₹" + Math.max(...prices).toFixed(2);

    document.getElementById("lowestPrice").innerText =
        "₹" + Math.min(...prices).toFixed(2);

    if (stockChart) {
        stockChart.destroy();
    }

    const ctx = document.getElementById("stockChart");

    stockChart = new Chart(ctx, {
        type: "line",

        data: {
            labels: data.dates,

            datasets: [{
                label: "Closing Price (₹)",
                data: prices,
                borderColor: "#2563eb",
                backgroundColor: "rgba(37, 99, 235, 0.1)",
                fill: true,
                tension: 0.3,
                pointRadius: 0
            }]
        },

        options: {
            responsive: true,

            interaction: {
                intersect: false,
                mode: "index"
            },

            scales: {
                x: {
                    ticks: {
                        maxTicksLimit: 10
                    }
                }
            }
        }
    });

} catch (error) {

    document.getElementById("loading").innerText = error.message;

}
}

window.addEventListener("DOMContentLoaded", loadStockData);
