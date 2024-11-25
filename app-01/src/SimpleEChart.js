import React from "react";
import ReactECharts from "echarts-for-react"; // Import the React wrapper for ECharts

const SimpleEChart = () => {
  // Define the chart options
  const options = {
    title: {
      text: "Simple Bar Chart", // Chart title
    },
    tooltip: {}, // Tooltip on hover
    xAxis: {
      type: "category", // X-axis type (categorical)
      data: ["Apple", "Banana", "Orange", "Grapes", "Mango"], // X-axis labels
    },
    yAxis: {
      type: "value", // Y-axis type (numerical)
    },
    series: [
      {
        name: "Fruits", // Name for the legend
        type: "bar", // Chart type
        data: [5, 10, 15, 8, 12], // Data for the bar chart
      },
    ],
  };

  return (
    <div>
      <h2>React ECharts Example</h2>
      {/* Render the ECharts component */}
      <ReactECharts option={options} style={{ height: "400px", width: "100%" }} />
    </div>
  );
};

export default SimpleEChart;
