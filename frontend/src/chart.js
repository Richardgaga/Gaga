# Candlestick chart
import React from "react";
import { Chart as ChartJS } from "react-chartjs-2";

function Chart() {
  const data = {
    labels: ["Candle1", "Candle2", "Candle3"],
    datasets: [
      {
        label: "EUR/USD Candles",
        data: [1.15, 1.16, 1.17],
        borderColor: "blue",
      }
    ]
  };

  return <ChartJS type="line" data={data} />;
}

export default Chart;
