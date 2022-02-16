let trace1 = {
  x: xData,
  y: yData
};

let data = [trace1];

let layout = {
  title: "A Plotly plot"
};

Plotly.newPlot("plot", data, layout);