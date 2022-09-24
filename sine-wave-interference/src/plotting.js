const chart = new Chart("chart", {
    type: "line",
    data: {
      datasets: [{
          type: "line",
          borderColor: "#007cfb",
        }
      ]
    },
    options: {
      plugins: {
        legend: {display: false},
        tooltip: {enabled: false},
      },
      scales: {
        x: {display: false},
        y: {display: false}
      },
      elements: {
        point: {
          pointStyle: "circle",
          radius: 0,
        },
        line: {
          borderWidth: 1,
        },
      },
    }
  })
  
  function updateChart(xValues, yValues) {
    chart.data.labels = xValues
    chart.data.datasets[0].data = yValues
    chart.update()
  }