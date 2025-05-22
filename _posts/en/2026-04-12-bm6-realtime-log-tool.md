---
layout: post
title: "BM6 Real-Time 1Hz Data Parsing Tool"
lang: en
date: 2026-04-12 10:00:00
categories: Auto
tags: [BM6, Battery Monitor, Data Conversion, Log Parsing, Car Battery]
description: "Convert hex packets from raw BM6 logs into readable per-second voltage and temperature data, with CSV export and dual-axis chart visualization support."
keywords: "BM6, Battery Monitor, Real-time Data, Voltage Record, Temperature Record, Log Parsing, Hex Decoding, CSV Export, LiFePO4 Battery"
image: /images/bm6-cranking-preview.webp
faq:
  - question: "How is this tool different from the cranking waveform parser?"
    answer: "The cranking waveform tool is designed for 100Hz high-speed sampling data during engine startup (cranking.add). This tool is for the regular 1Hz real-time broadcast data (d15507 packets), making it suitable for observing alternator charging voltage changes or ambient temperature trends during long drives."
  - question: "How does the tool find the corresponding data in the log file?"
    answer: "The tool automatically searches for packets starting with `d15507`, which are defined as real-time status data in the BM6 broadcast protocol. As long as your log file contains the recorded Bluetooth 'receive' logs, it can be parsed."
  - question: "Is it possible to download the processed data?"
    answer: "Yes. After parsing, a 'Download CSV File' button will appear. You can export the data to Excel or other professional graphing software for deeper long-term trend analysis."
  - question: "Why are the charts displayed separately?"
    answer: "To prevent lines with different scales from interfering with each other, we separated 'Voltage (V)' and 'Temperature (°C)' into top and bottom charts. Both share the same time axis and support synchronized zooming, making it easy to accurately compare data fluctuations at the exact same moment."
  - question: "Are there privacy concerns when uploading log files?"
    answer: "Not at all. This tool is developed using pure front-end (JavaScript) technology. All calculations are performed entirely within your computer's browser, and no data is transmitted to any server."
---

<div id="bm6-realtime-container"
    style="max-width: 950px; margin: 20px auto; font-family: 'Segoe UI', 'Microsoft JhengHei', sans-serif; background: #0d1117; color: #c9d1d9; padding: 25px; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 1px solid #30363d; position: relative;">

    <h2 id="ui-title" style="text-align: center; color: #c9d1d9; margin-bottom: 10px; margin-top: 10px;">BM6 Real-Time Data Parsing Tool</h2>

    <div
        style="background: rgba(56, 139, 253, 0.1); padding: 15px 20px; border-radius: 10px; margin-bottom: 25px; border-left: 5px solid #388bfd; font-size: 14.5px; line-height: 1.6; color: #8b949e;">
        <strong id="ui-desc-title" style="color: #58a6ff;">Supports 1Hz Real-Time Data Extraction and CSV Export</strong><br>
        <span id="ui-desc-body">This tool automatically searches for <b style="color:#c9d1d9;">d15507 packets</b> in the Log, converts hexadecimal data into per-second voltage and temperature records, and provides interactive chart previews with synchronized zooming and data downloading features.</span>
    </div>

    <div
        style="background: #161b22; border: 1px solid #30363d; padding: 20px; border-radius: 10px; margin-bottom: 25px; display: flex; flex-direction: column; align-items: center; gap: 15px;">
        <div style="display: flex; gap: 10px;">
            <button id="uploadTrigger"
                style="background: #1f6feb; color: white; border: none; padding: 12px 24px; border-radius: 8px; cursor: pointer; font-weight: bold; font-size: 15px; transition: 0.2s;">📁 Upload Log File (.txt / .log)</button>
            <button id="downloadBtn" style="background: #238636; color: white; border: none; padding: 12px 24px; border-radius: 8px; cursor: pointer; font-weight: bold; font-size: 15px; display: none;">📥 Download CSV File</button>
        </div>
        <input type="file" id="logFileInput" accept=".txt,.log" style="display:none">
        <div id="status-text" style="color: #8b949e; font-size: 14px; font-weight: bold;">Please select a file containing real-time broadcast data</div>
    </div>

    <div style="background: #161b22; padding: 15px; border-radius: 10px; border: 1px solid #30363d; box-sizing: border-box;">
        <div style="height: 280px; width: 100%; margin-bottom: 10px;">
            <canvas id="voltageChart"></canvas>
        </div>
        <div style="height: 280px; width: 100%;">
            <canvas id="tempChart"></canvas>
        </div>
    </div>

</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-adapter-date-fns"></script>
<script src="https://cdn.jsdelivr.net/npm/hammerjs"></script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-zoom"></script>

<script>
(function() {
    const fileInput = document.getElementById('logFileInput');
    const uploadTrigger = document.getElementById('uploadTrigger');
    const downloadBtn = document.getElementById('downloadBtn');
    const statusText = document.getElementById('status-text');

    let vChart, tChart;
    let parsedData = [];
    let isResetting = false;

    // --- Chart.js Configuration ---
    Chart.defaults.color = '#8b949e';
    Chart.defaults.borderColor = '#30363d';

    const crosshairPlugin = {
        id: 'crosshair',
        beforeDraw: chart => {
            if (chart.tooltip._active && chart.tooltip._active.length) {
                const ctx = chart.ctx;
                const activePoint = chart.tooltip._active[0];
                const x = activePoint.element.x;
                const topY = chart.scales.y.top;
                const bottomY = chart.scales.y.bottom;

                ctx.save();
                ctx.beginPath();
                ctx.moveTo(x, topY);
                ctx.lineTo(x, bottomY);
                ctx.lineWidth = 1;
                ctx.strokeStyle = 'rgba(139, 148, 158, 0.8)';
                ctx.setLineDash([4, 4]);
                ctx.stroke();
                ctx.restore();
            }
        }
    };

    function autoScaleY(chart) {
        const xScale = chart.scales.x, dataset = chart.data.datasets[0].data;
        let minV = Infinity, maxV = -Infinity, found = false;
        for (let i = 0; i < dataset.length; i++) {
            const xVal = new Date(dataset[i].x).getTime();
            if (xVal >= xScale.min && xVal <= xScale.max) {
                if (dataset[i].y < minV) minV = dataset[i].y;
                if (dataset[i].y > maxV) maxV = dataset[i].y;
                found = true;
            }
        }
        if (found) {
            const padding = (maxV - minV) * 0.15 || 0.15;
            chart.options.scales.y.min = minV - padding;
            chart.options.scales.y.max = maxV + padding;
        }
    }

    function syncCharts({chart}) {
        if (isResetting) return;
        const other = (chart === vChart) ? tChart : vChart;
        other.options.scales.x.min = chart.scales.x.min;
        other.options.scales.x.max = chart.scales.x.max;
        autoScaleY(chart); 
        autoScaleY(other);
        chart.update('none'); 
        other.update('none');
    }

    function createChartConfig(label, color, yTitle) {
        return {
            type: 'line',
            data: { datasets: [{ label: label, data: [], borderColor: color, backgroundColor: color + '20', borderWidth: 2, pointRadius: 0, tension: 0.2, fill: true }] },
            options: {
                responsive: true, maintainAspectRatio: false,
                interaction: {
                    mode: 'index',
                    intersect: false,
                },
                scales: {
                    x: { 
                        type: 'time', 
                        time: { 
                            displayFormats: { 
                                second: 'HH:mm:ss',
                                minute: 'HH:mm:ss',
                                hour: 'HH:mm:ss'
                            },
                            tooltipFormat: 'HH:mm:ss' 
                        } 
                    },
                    y: { title: { display: true, text: yTitle } }
                },
                plugins: { 
                    tooltip: {
                        enabled: true,
                        backgroundColor: 'rgba(22, 27, 34, 0.9)',
                        titleColor: '#c9d1d9',
                        bodyColor: '#c9d1d9',
                        borderColor: '#30363d',
                        borderWidth: 1,
                        padding: 10,
                        displayColors: false
                    },
                    zoom: { 
                        pan: { enabled: true, mode: 'x', onPan: syncCharts }, 
                        zoom: { wheel: { enabled: true }, mode: 'x', onZoom: syncCharts } 
                    } 
                }
            },
            plugins: [crosshairPlugin]
        };
    }

    // Initialize the two charts
    vChart = new Chart(document.getElementById('voltageChart'), createChartConfig('Voltage (V)', '#58a6ff', 'Voltage (V)'));
    tChart = new Chart(document.getElementById('tempChart'), createChartConfig('Temperature (°C)', '#f85149', 'Temperature (°C)'));


    // --- File Parsing Logic ---
    uploadTrigger.onclick = () => fileInput.click();

    fileInput.onchange = function(e) {
        const file = e.target.files[0];
        if (!file) return;

        statusText.innerHTML = `Parsing <b style="color:#58a6ff;">${file.name}</b>...`;
        
        const reader = new FileReader();
        reader.onload = function(e) {
            processData(e.target.result);
        };
        reader.readAsText(file);
    };

    function processData(text) {
        const lines = text.split('\n');
        // d15507 + TempHex(2) + Other(2) + SOCHex(2) + VolHex(4)
        const pattern = /^(\d{2}:\d{2}:\d{2}):receive:d1550700([0-9a-fA-F]{2})[0-9a-fA-F]{2}([0-9a-fA-F]{2})([0-9a-fA-F]{4})/;
        
        const vData = [];
        const tData = [];
        parsedData = [];

        let currentDay = 1;
        let lastTimeObj = null;

        lines.forEach(line => {
            const match = line.trim().match(pattern);
            if (match) {
                const timeStr = match[1]; // "HH:MM:SS"
                const tempC = parseInt(match[2], 16);
                const voltage = parseInt(match[4], 16) / 100.0;
                
                // Handle midnight crossover logic (e.g., from 23:59:59 to 00:00:00)
                const [h, m, s] = timeStr.split(':').map(Number);
                const currentTimeObj = new Date(2026, 0, currentDay, h, m, s);
                
                if (lastTimeObj && currentTimeObj < lastTimeObj) {
                    currentDay++;
                    currentTimeObj.setDate(currentDay);
                }
                lastTimeObj = currentTimeObj;
                
                // Get Timestamp for Chart.js
                const timeVal = currentTimeObj.getTime();

                vData.push({ x: timeVal, y: voltage });
                tData.push({ x: timeVal, y: tempC });
                
                // Keep original strings for CSV export
                parsedData.push([timeStr, voltage, tempC]);
            }
        });

        if (parsedData.length > 0) {
            statusText.innerHTML = `✅ Parsing successful! Extracted <b style="color:#3fb950;">${parsedData.length}</b> real-time data points.`;
            downloadBtn.style.display = 'inline-block';
            
            isResetting = true;

            [vChart, tChart].forEach(chart => {
                if (chart.resetZoom) chart.resetZoom('none');
            });

            // Update data
            vChart.data.datasets[0].data = vData;
            tChart.data.datasets[0].data = tData;

            // Pre-calculate Y-axis boundaries to prevent charts from displaying incompletely
            const vValues = vData.map(d => d.y);
            const tValues = tData.map(d => d.y);
            const minV = Math.min(...vValues), maxV = Math.max(...vValues);
            const minT = Math.min(...tValues), maxT = Math.max(...tValues);
            
            const vPad = (maxV - minV) * 0.15 || 0.5;
            const tPad = (maxT - minT) * 0.15 || 2;

            vChart.options.scales.y.min = minV - vPad;
            vChart.options.scales.y.max = maxV + vPad;
            tChart.options.scales.y.min = minT - tPad;
            tChart.options.scales.y.max = maxT + tPad;

            vChart.update('none');
            tChart.update('none');

            setTimeout(() => { isResetting = false; }, 200);

        } else {
            statusText.innerHTML = `<span style="color:#f85149;">❌ No valid data found. Please ensure the log contains d15507 packets.</span>`;
            downloadBtn.style.display = 'none';
        }
    }

    downloadBtn.onclick = function() {
        if (parsedData.length === 0) return;
        let csvContent = "Time,Voltage(V),Temperature(°C)\n";
        parsedData.forEach(row => { csvContent += row.join(",") + "\n"; });
        const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
        const url = URL.createObjectURL(blob);
        const link = document.createElement("a");
        link.setAttribute("href", url);
        link.setAttribute("download", "bm6_per_second_data.csv");
        link.click();
    };
})();
</script>