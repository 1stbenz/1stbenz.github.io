---
layout: post
title: "BM6/BM200 100Hz Cranking Log Parsing Tool"
lang: en
date: 2026-03-21 10:00:00
categories: Auto
tags: [BM6, Battery Monitor, Cranking Waveform, Data Analysis, Conversion Tool, Car Battery]
description: "A cranking waveform parsing tool designed specifically for the BM6 Bluetooth Battery Monitor. It decodes the hex packets from raw Log files to accurately plot a high-resolution engine cranking voltage curve, automatically marking the minimum point and starter motor disengagement point using a dynamic threshold algorithm."
keywords: "BM6, Bluetooth Battery Monitor, Cranking Waveform, Cranking Voltage, Cranking, Log Parser, Car Battery, LiFePO4 Battery"
image: /images/bm6-cranking-preview2.webp
faq:
  - question: "What problem does this tool solve?"
    answer: "The official APP cannot export high-resolution cranking waveforms. This tool directly reads raw Log files captured via Bluetooth, decodes the internal hex packets, and restores the 100Hz high-precision cranking voltage curve. This helps in assessing the battery's instantaneous discharge capability and the starter motor's condition."
  - question: "What do the red and orange dots on the chart represent?"
    answer: "The red dot (Min) represents the lowest voltage the battery drops to under the heavy load of the starter motor. The orange dot (Starter) is the turning point, calculated via an algorithm, where the starter motor's power is cut off and the engine successfully takes over generating power."
  - question: "How do I get a Log file to upload?"
    answer: "You can use a Bluetooth analysis tool on your phone, or the log export feature built into the official BM6 APP, to save the captured broadcast data as a .txt or .log file. Make sure the file covers the time period when the engine was started."
  - question: "Are there any privacy or data leak concerns when uploading a Log file?"
    answer: "None at all. This tool is developed purely with front-end (JavaScript) technology. All data parsing, hex decoding, and chart rendering are done independently within your browser. No data is uploaded to any cloud servers."
  - question: "How low does the cranking minimum voltage (Min) need to drop to indicate the battery might be failing?"
    answer: "For a healthy 12V lead-acid or AGM battery, the minimum voltage during engine start at room temperature usually stays above 9.6V. If your red dot consistently falls to 9.0V or lower, it may indicate battery aging and increased internal resistance. It is recommended to seek professional testing early."
  - question: "Why does it say 'No valid cranking waveform found' after uploading the file?"
    answer: "This usually happens because the Log file didn't capture the complete packets at the exact moment of starting. Check if there's a successful 'cranking.add:ok' mark in the file. Additionally, if the phone is too far from the car during startup, Bluetooth packet loss will result in incomplete waveforms that cannot be parsed."
  - question: "How does the algorithm determine the orange dot (starter motor disengagement point)?"
    answer: "This tool uses a 'dynamic threshold' algorithm. The program first automatically detects the 'initial resting voltage' before starting. When the voltage rebounds close to this initial voltage (indicating the motor is disconnected or the alternator takes over), it traces backward to find the last local minimum during the valley rebound process. This makes the tool perfectly compatible with both traditional lead-acid batteries and LiFePO4 batteries, which have a higher resting voltage."
---

<div id="car-app-container"
    style="max-width: 950px; margin: 20px auto; font-family: 'Segoe UI', 'Microsoft JhengHei', sans-serif; background: #0d1117; color: #c9d1d9; padding: 25px; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 1px solid #30363d; position: relative;">

    <h2 id="ui-title" style="text-align: center; color: #c9d1d9; margin-bottom: 10px; margin-top: 10px;">BM6 Cranking Waveform Analysis Tool</h2>

    <div
        style="background: rgba(210, 153, 34, 0.1); padding: 15px 20px; border-radius: 10px; margin-bottom: 25px; border-left: 5px solid #d29922; font-size: 14.5px; line-height: 1.6; color: #8b949e;">
        <strong id="ui-desc-title" style="color: #d29922;">Supports Dynamic Threshold Detection (Compatible with Lead-Acid & LiFePO4)</strong><br>
        <span id="ui-desc-body">This tool reads raw <b style="color:#c9d1d9;">.log files</b> directly, converting hex packets into a 100Hz high-resolution waveform. It uses a dynamic algorithm to automatically locate the lowest voltage point and the starter motor disengagement point, allowing you to easily review extreme battery performance.</span>
    </div>

    <div
        style="background: #161b22; border: 1px solid #30363d; padding: 15px 25px; border-radius: 10px; margin-bottom: 25px; display: flex; align-items: center; justify-content: center;">
        <button id="uploadTrigger"
            style="background: #1f6feb; color: white; border: none; padding: 12px 24px; border-radius: 8px; cursor: pointer; font-weight: bold; font-size: 15px; transition: 0.2s;">📁
            Upload Log File (.txt / .log)</button>
        <input type="file" id="logFileInput" accept=".txt,.log" style="display:none">
    </div>

    <div id="status-text"
        style="text-align: center; color: #8b949e; margin-bottom: 20px; font-size: 14px; font-weight: bold;">Please upload a Log file containing broadcast data for analysis</div>

    <div id="chartsWrapper" style="display: flex; flex-direction: column; gap: 20px;"></div>

</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script src="https://cdn.jsdelivr.net/npm/hammerjs"></script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-zoom"></script>

<script>
    (function () {
        const fileInput = document.getElementById('logFileInput');
        const uploadTrigger = document.getElementById('uploadTrigger');
        const statusText = document.getElementById('status-text');
        const chartsWrapper = document.getElementById('chartsWrapper');

        Chart.defaults.color = '#8b949e';
        Chart.defaults.borderColor = '#30363d';

        // Crosshair plugin (Same as 03-20)
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

        uploadTrigger.onclick = () => fileInput.click();

        fileInput.addEventListener('change', function (e) {
            const file = e.target.files[0];
            if (!file) return;

            statusText.innerHTML = `Parsing <b style="color:#58a6ff;">${file.name}</b> ...`;
            chartsWrapper.innerHTML = '';

            const reader = new FileReader();
            reader.onload = function (e) {
                const text = e.target.result;
                processLogData(text);
            };
            reader.readAsText(file);
        });

        function isValidCurve(hexData) {
            if (!hexData || hexData.length < 30) return false;
            let validCount = 0, invalidCount = 0;
            for (let i = 0; i < hexData.length - 2; i += 3) {
                let voltage = parseInt(hexData.substring(i, i + 3), 16) / 100.0;
                if (!isNaN(voltage) && voltage >= 3.0 && voltage <= 35.0) {
                    validCount++;
                } else {
                    invalidCount++;
                }
            }
            let total = validCount + invalidCount;
            return total > 0 && (invalidCount / total) <= 0.1;
        }

        function processLogData(logText) {
            const lines = logText.split('\n');
            
            // 1. Pre-scan: Build a dedicated database for "History Timestamp -> Temperature"
            let historyMap = {};
            const jsonRegex = /"time"\s*:\s*(\d+)\s*,\s*"temp"\s*:\s*(\d+)/g;
            let match;
            while ((match = jsonRegex.exec(logText)) !== null) {
                historyMap[match[1]] = match[2];
            }

            let crankingEvents = [];
            let tempHexStream = "";
            let isRecording = false;
            let isHistorical = false;
            let activeTimeline = null;
            let currentLogTime = "Unknown";
            let rollingRealTimeTemp = "Unknown";

            // 2. Parse line-by-line: Separate historical waveforms from real-time waveforms
            for (let i = 0; i < lines.length; i++) {
                let originalLine = lines[i].trim();
                let line = originalLine.toLowerCase();
                if (!line) continue;

                let timeMatch = originalLine.match(/^(\d{2}:\d{2}:\d{2})/);
                if (timeMatch) currentLogTime = timeMatch[1];

                let tempMatch = line.match(/"temp"\s*:\s*(\d+)/);
                if (tempMatch) rollingRealTimeTemp = tempMatch[1];

                let syncMatch = line.match(/self\.synchistorytimeline:(\d+)/);
                if (syncMatch) {
                    activeTimeline = syncMatch[1];
                    isRecording = true;
                    isHistorical = true;
                    tempHexStream = ""; 
                    continue;
                }

                if (line.includes('receive:')) {
                    let content = line.split("receive:")[1].trim();

                    if (/^[0-9a-f]+$/.test(content)) {
                        if (content.includes('fffffe')) {
                            isRecording = true;
                            isHistorical = false;
                            tempHexStream = content.split('fffffe')[1];
                            continue;
                        }

                        if (isRecording) {
                            if (content.includes('fffefe')) {
                                tempHexStream += content.split('fffefe')[0];
                                
                                if (isValidCurve(tempHexStream) && !crankingEvents.some(e => e.hex === tempHexStream)) {
                                    let eventTimeStr = "";
                                    let eventTemp = "Unknown";

                                    if (isHistorical && activeTimeline) {
                                        let ts = parseInt(activeTimeline);
                                        let date = new Date(ts * 1000);
                                        let mm = String(date.getMonth() + 1).padStart(2, '0');
                                        let dd = String(date.getDate()).padStart(2, '0');
                                        let hh = String(date.getHours()).padStart(2, '0');
                                        let min = String(date.getMinutes()).padStart(2, '0');
                                        let ss = String(date.getSeconds()).padStart(2, '0');
                                        eventTimeStr = `${mm}/${dd} ${hh}:${min}:${ss} (History)`;

                                        if (historyMap[activeTimeline]) {
                                            eventTemp = historyMap[activeTimeline];
                                        } else {
                                            let minDiff = Infinity;
                                            for (let t in historyMap) {
                                                let diff = Math.abs(parseInt(t) - ts);
                                                if (diff < minDiff) {
                                                    minDiff = diff;
                                                    eventTemp = historyMap[t] + "*";
                                                }
                                            }
                                        }
                                    } else {
                                        eventTimeStr = `${currentLogTime}`;
                                        eventTemp = rollingRealTimeTemp;
                                    }

                                    crankingEvents.push({
                                        hex: tempHexStream,
                                        time: eventTimeStr,
                                        temp: eventTemp
                                    });
                                }
                                isRecording = false;
                                isHistorical = false;
                                tempHexStream = "";
                                activeTimeline = null;
                            } else {
                                if (!content.startsWith("d155")) {
                                    tempHexStream += content;
                                }
                            }
                        }
                    }
                }
            }

            if (crankingEvents.length === 0) {
                statusText.innerHTML = '<span style="color:#f85149;">❌ No valid cranking waveform found in the file. Please ensure this file contains a cranking record.</span>';
                return;
            }

            statusText.innerHTML = `✅ Parsing complete! Detected <b style="color:#58a6ff;">${crankingEvents.length}</b> engine start record(s).`;

            crankingEvents.forEach((eventData, index) => {
                drawChartForEvent(eventData, index + 1);
            });
        }

        function getLocalMinima(arr) {
            let minima = [];
            for (let i = 1; i < arr.length - 1; i++) {
                if (arr[i] < arr[i - 1] && arr[i] < arr[i + 1]) minima.push(i);
            }
            return minima;
        }

        // Dynamic Y-axis scaling logic
        function autoScaleY(chart) {
            const xScale = chart.scales.x;
            const dataset = chart.data.datasets[0].data; // Line data
            let minV = Infinity, maxV = -Infinity, found = false;
            for (let i = 0; i < dataset.length; i++) {
                if (dataset[i].x >= xScale.min && dataset[i].x <= xScale.max) {
                    if (dataset[i].y < minV) minV = dataset[i].y;
                    if (dataset[i].y > maxV) maxV = dataset[i].y;
                    found = true;
                }
            }
            if (found) {
                // Lower limit: Next integer below the lowest point in view
                chart.options.scales.y.min = Math.floor(minV * 5) / 5;
                // Upper limit: Next multiple of 0.2 above the highest point in view
                chart.options.scales.y.max = Math.ceil(maxV * 5) / 5;
            }
        }

        function drawChartForEvent(eventData, eventNumber) {
            let hexData = eventData.hex;
            let eventTime = eventData.time;
            let eventTemp = eventData.temp;

            let times = [];
            let voltages = [];
            let currentTime = 0;
            let chartData = [];

            for (let i = 0; i < hexData.length - 2; i += 3) {
                let chunk = hexData.substring(i, i + 3);
                let voltage = parseInt(chunk, 16) / 100.0;
                if (!isNaN(voltage) && voltage >= 3.0 && voltage <= 35.0) {
                    times.push(currentTime);
                    voltages.push(voltage);
                    chartData.push({ x: currentTime, y: voltage });
                    currentTime += 0.01;
                }
            }

            // 1. Minimum Point (Min Cranking)
            let minVol = Math.min(...voltages);
            let minIdx = voltages.indexOf(minVol);
            let localMins = getLocalMinima(voltages);

            // 2. Dynamic Climbing Point (Dynamic Threshold) 
            let sampleSize = Math.min(5, minIdx);
            if (sampleSize === 0) sampleSize = 1; 
            let initialVoltages = voltages.slice(0, sampleSize);
            let vInitial = initialVoltages.reduce((a, b) => a + b, 0) / initialVoltages.length;

            let dynamicThreshold = vInitial - 0.2;

            let climbIdx = minIdx;
            while (climbIdx < voltages.length && voltages[climbIdx] <= dynamicThreshold) {
                climbIdx++;
            }
            if (climbIdx >= voltages.length) climbIdx = voltages.length - 1;

            // 3. Starter Motor Disengaged Point
            let validMinsForStarter = localMins.filter(idx => idx >= minIdx && idx < climbIdx);
            let starterIdx = validMinsForStarter.length > 0 ? validMinsForStarter[validMinsForStarter.length - 1] : minIdx;

            const minPoint = { x: times[minIdx], y: voltages[minIdx] };
            const starterPoint = { x: times[starterIdx], y: voltages[starterIdx] };

            // Label drawing plugin (Replacing Plotly's markers+text)
            const pointLabelsPlugin = {
                id: 'pointLabels',
                afterDraw: chart => {
                    const ctx = chart.ctx;
                    const meta = chart.getDatasetMeta(1); // Scatter dataset
                    if (!meta.hidden && meta.data.length >= 2) {
                        ctx.save();
                        ctx.font = 'bold 12px "Segoe UI", sans-serif';
                        ctx.fillStyle = '#c9d1d9';
                        
                        // Set vertical alignment to middle so text and point are on the same horizontal line
                        ctx.textBaseline = 'middle'; 

                        // Min Label (placed to the right of the red dot)
                        const ptMin = meta.data[0];
                        if (ptMin.x >= chart.chartArea.left && ptMin.x <= chart.chartArea.right) {
                            ctx.textAlign = 'left';
                            // Shift x-coordinate right by 10px to avoid the point body, y-coordinate stays the same
                            ctx.fillText(`Min: ${minPoint.y.toFixed(2)}V`, ptMin.x + 10, ptMin.y);
                        }
                        
                        // Starter Label (placed to the right of the orange dot)
                        const ptStarter = meta.data[1];
                        if (ptStarter.x >= chart.chartArea.left && ptStarter.x <= chart.chartArea.right) {
                            ctx.textAlign = 'left';
                            // Also shift right by 10px to avoid the orange dot
                            ctx.fillText(` Starter dise: ${starterPoint.y.toFixed(2)}V`, ptStarter.x + 10, ptStarter.y);
                        }
                        ctx.restore();
                    }
                }
            };

            // Create UI container
            const wrapperDiv = document.createElement('div');
            wrapperDiv.style.cssText = "background: #161b22; padding: 15px; border-radius: 10px; border: 1px solid #30363d; width: 100%; box-sizing: border-box;";
            
            // Add custom title
            const titleElement = document.createElement('div');
            titleElement.style.cssText = "color: #c9d1d9; font-size: 16px; font-weight: bold; text-align: center; margin-bottom: 15px;";
            titleElement.innerHTML = `Cranking Waveform Analysis - Record #${eventNumber} (Time: ${eventTime} | Temp: ${eventTemp}°C | Initial: ${vInitial.toFixed(2)}V)`;
            wrapperDiv.appendChild(titleElement);

            const canvasDiv = document.createElement('div');
            canvasDiv.style.cssText = "width: 100%; height: 400px; position: relative;";
            
            const canvas = document.createElement('canvas');
            canvas.id = `chart-${eventNumber}`;
            canvasDiv.appendChild(canvas);
            wrapperDiv.appendChild(canvasDiv);
            chartsWrapper.appendChild(wrapperDiv);

            // Initialize Chart.js
            new Chart(canvas, {
                type: 'line',
                data: {
                    datasets: [
                        {
                            label: 'Voltage (V)',
                            data: chartData,
                            borderColor: '#58a6ff',
                            borderWidth: 2,
                            pointRadius: 0,
                            tension: 0.2, // Smooth curve
                            order: 2
                        },
                        {
                            label: 'Key Points',
                            type: 'scatter',
                            data: [minPoint, starterPoint],
                            backgroundColor: ['#f85149', '#d29922'],
                            borderColor: '#161b22',
                            borderWidth: 2,
                            pointRadius: 6,
                            pointHoverRadius: 8,
                            order: 1
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    interaction: {
                        mode: 'index',
                        intersect: false,
                    },
                    scales: {
                        x: {
                            type: 'linear',
                            title: { display: true, text: 'Time (Seconds)' },
                            max: times[times.length - 1],
                            ticks: { maxTicksLimit: 10 }
                        },
                        y: {
                            title: { display: true, text: 'Voltage (V)' },
                            // Pre-calculate a suitable Y-axis range
                            min: Math.floor(Math.min(...voltages) * 5) / 5,
                            max: Math.ceil(Math.max(...voltages) * 5) / 5,
                            ticks: {
                                stepSize: 0.2
                            }
                        }
                    },
                    plugins: {
                        legend: { display: false },
                        tooltip: {
                            backgroundColor: 'rgba(22, 27, 34, 0.9)',
                            titleColor: '#c9d1d9',
                            bodyColor: '#c9d1d9',
                            borderColor: '#30363d',
                            borderWidth: 1,
                            padding: 10,
                            displayColors: false,
                            callbacks: {
                                // Title (Top): Display voltage, and determine if it's a special red/orange dot
                                title: function(tooltipItems) {
                                    if (tooltipItems.length > 0) {
                                        const item = tooltipItems[0];                                
                                        return `Voltage: ${item.parsed.y}V`;
                                    }
                                    return '';
                                },
                                // Content (Bottom): Display time
                                label: function(context) {
                                    // Key modification: Regardless of which dataset, only show the time label for the "first" matched data item
                                    if (context.dataIndex !== context.chart.tooltip.dataPoints[0].dataIndex || 
                                        context.datasetIndex !== context.chart.tooltip.dataPoints[0].datasetIndex) {
                                        return null;
                                    }
                                    // Use context.raw.x to ensure we get the seconds from the raw data
                                    return `Time: ${context.raw.x.toFixed(2)} Seconds`;
                                }
                            }
                        },
                        zoom: {
                            pan: { 
                                enabled: true, 
                                mode: 'x',
                                onPan: function({chart}) {
                                    autoScaleY(chart);
                                    chart.update('none');
                                }
                            },
                            zoom: { 
                                wheel: { enabled: true }, 
                                pinch: { enabled: true },
                                mode: 'x',
                                onZoom: function({chart}) {
                                    autoScaleY(chart);
                                    chart.update('none');
                                }
                            }
                        }
                    }
                },
                plugins: [crosshairPlugin, pointLabelsPlugin]
            });
        }
    })();
</script>