const chart = new Chart("chart", {
    type: "line",
    data: {
      datasets: [{
          type: "line",
          borderColor: "#007cfb",
        },
        {
          type: "line",
          borderColor: "#62c500",
        },
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
  
  function updateChart(xValues, yValues1, yValues2) {
    chart.data.labels = xValues
    chart.data.datasets[0].data = yValues1
    chart.data.datasets[1].data = yValues2
    chart.update()
  }