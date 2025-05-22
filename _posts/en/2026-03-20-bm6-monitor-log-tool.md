---
layout: post
title:  "BM6/BM200 Log Analyzer Tool"
lang: en
date:   2026-03-20 17:00:00
categories: Auto
tags: [BM6, Battery Monitor, LiFePO4, Data Analysis, Trip Detection, Converter Tool, Car Battery]
description: "A web-based log converter tool designed for the BM6 Bluetooth battery monitor. Using smart algorithms, it solves the trip detection accuracy issues caused by the high-voltage characteristics of LiFePO4 batteries in the official app, accurately restoring every driving trip and providing visual charts and Excel report export functions."
keywords: "BM6, Bluetooth battery monitor, LiFePO4, trip detection, voltage analysis, Excel export, log converter, car battery, smart alternator"
image: /images/bm6-tool-preview.webp
faq:
  - question: "What problem does this tool solve?"
    answer: "When dealing with LiFePO4 batteries that have a higher resting voltage, the official BM6/BM200 app often fails to accurately determine if the engine is off, causing abnormal or interrupted trip records. This tool uses a specially optimized smart algorithm to accurately filter voltage fluctuations and restore every real driving trip."
  - question: "Is it suitable for standard lead-acid batteries or vehicles with a Smart Alternator?"
    answer: "Yes, perfectly suitable. The system's algorithm automatically analyzes the base voltage to determine if the current battery is in 'LiFePO4 mode' or 'Lead-Acid / Smart Alternator mode', and dynamically adjusts the detection logic to accurately capture trips."
  - question: "How do I get and upload the data?"
    answer: "First, in the BM6/BM200 app on your phone, export the history records as an Excel (.xls or .xlsx) file. Then, upload that file to this tool's page to automatically perform the analysis."
  - question: "What analytical data does this tool provide?"
    answer: "The tool automatically calculates: total trips, total driving time, minimum voltage (reference for cold start), and average driving voltage (alternator health). It also provides freely zoomable visual line charts for voltage and temperature."
  - question: "Can I save the analyzed data?"
    answer: "Yes! After the analysis is complete, you can click 'Export Excel Report' to download the system-generated 'Daily Health Report', 'Trip Details', and 'Raw Data' to your computer for permanent storage."
---

<div id="car-app-container" style="max-width: 950px; margin: 20px auto; font-family: 'Segoe UI', 'Microsoft JhengHei', sans-serif; background: #0d1117; color: #c9d1d9; padding: 25px; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 1px solid #30363d; position: relative;">
    
    <h2 id="ui-title" style="text-align: center; color: #c9d1d9; margin-bottom: 10px; margin-top: 10px;">BM6/BM200 Log Analyzer Tool</h2>
    
    <div style="background: rgba(210, 153, 34, 0.1); padding: 15px 20px; border-radius: 10px; margin-bottom: 25px; border-left: 5px solid #d29922; font-size: 14.5px; line-height: 1.6; color: #8b949e;">
        <strong id="ui-desc-title" style="color: #d29922;">Why do you need this tool?</strong><br>
        <span id="ui-desc-body">Although the BM6/BM200 supports continuous recording after the engine is off, the official app's trip detection is often inaccurate, and observing waveform details is inconvenient. <b style="color:#c9d1d9;">This tool fixes this issue.</b> Using a custom-designed analysis method, it accurately analyzes voltage fluctuations, restores each trip, and provides intuitive visual analysis of voltage and temperature.</span>
    </div>

    <div style="background: #161b22; border: 1px solid #30363d; padding: 15px 25px; border-radius: 10px; margin-bottom: 25px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px;">
        <div style="display: flex; gap: 10px;">
            <button id="uploadTrigger" style="background: #1f6feb; color: white; border: none; padding: 10px 20px; border-radius: 8px; cursor: pointer; font-weight: bold; font-size: 14px;">📁 Upload Excel File</button>
            <button id="downloadBtn" style="display: none; background: #238636; color: white; border: none; padding: 10px 20px; border-radius: 8px; cursor: pointer; font-weight: bold; font-size: 14px;">📥 Export Excel Report</button>
        </div>
        <div style="display: flex; gap: 10px; align-items: center;">
            <label id="ui-display-range" style="font-weight: bold; color: #c9d1d9; font-size: 14px;">Range:</label>
            <select id="dateSelector" style="padding: 8px 12px; border-radius: 8px; border: 1px solid #30363d; font-size: 14px; min-width: 160px; cursor: pointer; background: #0d1117; color: #c9d1d9;">
                <option value="all" id="ui-show-all">-- Show All --</option>
            </select>
        </div>
        <input type="file" id="fileInput" accept=".xls,.xlsx" style="display:none">
    </div>

    <div id="status-text" style="text-align: center; color: #8b949e; margin-bottom: 20px; font-size: 14px;">Please upload the Excel file exported from the BM6/BM200 App</div>
    
    <style>
        .stats-grid {
            display: none;
            grid-template-columns: repeat(4, 1fr);
            gap: 15px;
            margin-bottom: 25px;
        }
        .stat-card {
            padding: 15px;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 2px 8px rgba(0,0,0,0.2);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        .stat-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 15px rgba(0,0,0,0.4);
        }
        @media (max-width: 768px) { .stats-grid { grid-template-columns: repeat(2, 1fr); } }
        @media (max-width: 480px) { .stats-grid { grid-template-columns: 1fr; } }
    </style>

    <div id="stats-container" class="stats-grid">
        <div class="stat-card" style="background: rgba(31, 111, 235, 0.1); border: 1px solid rgba(31, 111, 235, 0.3);">
            <div style="font-size: 13px; color: #58a6ff; margin-bottom: 5px; font-weight: 500;">Total Trips</div>
            <div id="stat-trips" style="font-size: 24px; font-weight: bold; color: #79c0ff;">0</div>
        </div>
        <div class="stat-card" style="background: rgba(35, 134, 54, 0.1); border: 1px solid rgba(35, 134, 54, 0.3);">
            <div style="font-size: 13px; color: #3fb950; margin-bottom: 5px; font-weight: 500;">Total Driving Time</div>
            <div id="stat-time" style="font-size: 24px; font-weight: bold; color: #56d364;">0 <span style="font-size: 12px; font-weight: normal;">min</span></div>
        </div>
        <div class="stat-card" style="background: rgba(227, 76, 38, 0.1); border: 1px solid rgba(227, 76, 38, 0.3);">
            <div style="font-size: 13px; color: #f0883e; margin-bottom: 5px; font-weight: 500;">Min Voltage (Cold Start)</div>
            <div id="stat-minv" style="font-size: 24px; font-weight: bold; color: #ff945e;">0.00 <span style="font-size: 12px; font-weight: normal;">V</span></div>
        </div>
        <div class="stat-card" style="background: rgba(137, 87, 229, 0.1); border: 1px solid rgba(137, 87, 229, 0.3);">
            <div style="font-size: 13px; color: #a371f7; margin-bottom: 5px; font-weight: 500;">Avg Driving Voltage (Alt)</div>
            <div id="stat-avgv" style="font-size: 24px; font-weight: bold; color: #d2a8ff;">0.00 <span style="font-size: 12px; font-weight: normal;">V</span></div>
        </div>
    </div>

    <div style="background: #161b22; padding: 15px; border-radius: 10px; border: 1px solid #30363d;">
        <div style="height: 280px; width: 100%; margin-bottom: 10px;">
            <canvas id="voltageChart"></canvas>
        </div>
        <div style="height: 280px; width: 100%;">
            <canvas id="tempChart"></canvas>
        </div>
    </div>

    <div id="trip-section" style="margin-top: 20px; padding: 15px; background: #161b22; border-radius: 10px; border: 1px dashed #30363d; display: none;">
        <h3 id="ui-trip-title" style="color: #c9d1d9; font-size: 16px; margin-top: 0; margin-bottom: 15px;">Detected Trips</h3>
        <div id="trip-list" style="display: flex; flex-direction: column; gap: 8px;"></div>
    </div>
</div>

<script src="https://cdn.sheetjs.com/xlsx-latest/package/dist/xlsx.full.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-adapter-date-fns"></script>
<script src="https://cdn.jsdelivr.net/npm/hammerjs"></script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-zoom"></script>

<script>
(function() {
    const fileInput = document.getElementById('fileInput');
    const uploadTrigger = document.getElementById('uploadTrigger');
    const dateSelector = document.getElementById('dateSelector');
    const statusText = document.getElementById('status-text');
    const downloadBtn = document.getElementById('downloadBtn');
    const tripSection = document.getElementById('trip-section');
    const tripList = document.getElementById('trip-list');
    
    let vChart, tChart;
    let allData = [];
    let globalDetectedTrips = { trips: [], mode: "" };
    let isResetting = false; 

    function detectTripsByCurve(data) {
        if (data.length < 10) return { trips: [], mode: "unknown" };
        let sortedV = [...data].map(d => d.v).sort((a, b) => a - b);
        let baseV = sortedV.slice(0, Math.floor(sortedV.length * 0.15)).reduce((a, b) => a + b, 0) / (Math.floor(sortedV.length * 0.15) || 1);
        let highV = sortedV.slice(Math.floor(sortedV.length * 0.95)).reduce((a, b) => a + b, 0) / (Math.floor(sortedV.length * 0.05) || 1);
        if (highV - baseV < 0.25) return { trips: [], mode: "inactive" };

        let isLiFePO4 = (baseV >= 13.0); 
        let rawTrips = [];
        let isOn = false, startIdx = 0;
        let midV = isLiFePO4 ? (baseV + (highV - baseV) * 0.5) : (baseV + 0.35);
        let offV = isLiFePO4 ? midV : (baseV + 0.10); 

        for (let i = 1; i < data.length - 1; i++) {
            const curr = data[i], prev = data[i-1];
            if (!isOn) {
                if (curr.v > midV || (curr.v - prev.v > 0.15 && curr.v > 12.5)) {
                    isOn = true;
                    startIdx = i;
                    for (let j = i; j >= Math.max(0, i - 1); j--) { if (data[j].v <= data[startIdx].v) startIdx = j; }
                }
            } else {
                if (curr.v <= offV) {
                    let lookAhead = Math.min(isLiFePO4 ? 5 : 12, data.length - i - 1); 
                    let isRealEnd = true, jumpIdx = i;
                    for (let j = 1; j <= lookAhead; j++) { if (data[i+j].v > midV) { isRealEnd = false; jumpIdx = i + j; break; } }
                    
                    if (isRealEnd || lookAhead === 0) {
                        isOn = false;
                        let endIdx = i;
                        for (let k = i; k > startIdx; k--) {     
                            if (data[k].v >= midV + 0.15 || (data[k-1].v - data[k].v > 0.05 && data[k-1].v > midV)) {
                                endIdx = k;
                                while (endIdx > startIdx && data[endIdx-1].v >= data[endIdx].v) {
                                    endIdx--;
                                }
                                break;
                            }
                        }
                        let dur = Math.round((new Date(data[endIdx].x) - new Date(data[startIdx].x)) / 60000);
                        if (dur >= 2) rawTrips.push({ start: data[startIdx].x, end: data[endIdx].x, duration: dur });
                    } else { i = jumpIdx - 1; }
                }
            }
        }
        if (isOn) {
           let endIdx = data.length - 1;
           let dur = Math.round((new Date(data[endIdx].x) - new Date(data[startIdx].x)) / 60000);
           if (dur >= 2) rawTrips.push({ start: data[startIdx].x, end: data[endIdx].x, duration: dur });
        }

        let mergedTrips = [];
        let mergeGapMins = isLiFePO4 ? 8 : 25; 
        if (rawTrips.length > 0) {
            let currentTrip = rawTrips[0];
            for (let i = 1; i < rawTrips.length; i++) {
                let gapMins = Math.round((new Date(rawTrips[i].start) - new Date(currentTrip.end)) / 60000);
                if (gapMins <= mergeGapMins) {
                    currentTrip.end = rawTrips[i].end;
                    currentTrip.duration = Math.round((new Date(currentTrip.end) - new Date(currentTrip.start)) / 60000);
                } else { mergedTrips.push(currentTrip); currentTrip = rawTrips[i]; }
            }
            mergedTrips.push(currentTrip);
        }
        return { trips: mergedTrips, mode: isLiFePO4 ? "LiFePO4" : "Lead-Acid" };
    }

    function updateStatCards(filteredData, result) {
        const statsContainer = document.getElementById('stats-container');
        if (!filteredData || filteredData.length === 0) { statsContainer.style.display = 'none'; return; }
        statsContainer.style.display = 'grid';

        document.getElementById('stat-trips').innerText = result.trips.length;
        const totalMins = result.trips.reduce((acc, t) => acc + t.duration, 0);
        document.getElementById('stat-time').innerHTML = `${totalMins} <span style="font-size:12px;">min</span>`;

        const minV = Math.min(...filteredData.map(d => d.v));
        const minVElement = document.getElementById('stat-minv');
        minVElement.innerHTML = `${minV.toFixed(2)} <span style="font-size:12px;">V</span>`;
        minVElement.style.color = minV < 12.6 ? "#f85149" : "#ff945e";

        let drivePoints = 0, sumV = 0;
        filteredData.forEach(d => {
            const isDriving = result.trips.some(t => {
                const time = new Date(d.x).getTime();
                return time >= new Date(t.start).getTime() && time <= new Date(t.end).getTime();
            });
            if (isDriving) { drivePoints++; sumV += d.v; }
        });
        document.getElementById('stat-avgv').innerHTML = `${drivePoints > 0 ? (sumV / drivePoints).toFixed(2) : "N/A"} <span style="font-size:12px;">V</span>`;
    }

    function renderTrips(result) {
        tripList.innerHTML = '';
        if (!result.trips || result.trips.length === 0) { tripSection.style.display = 'none'; return; }
        tripSection.style.display = 'block';
        
        const modeSuffix = result.mode === 'LiFePO4' ? ' [LiFePO4 Mode]' : ' [Lead-Acid / Smart Alternator Mode]';
        document.getElementById('ui-trip-title').innerText = 'Detected Trips' + modeSuffix;

        result.trips.forEach((t, i) => {
            const rowDiv = document.createElement('div');
            rowDiv.style.cssText = "display: flex; align-items: center; justify-content: space-between; background: #0d1117; padding: 10px 16px; border-radius: 8px; border: 1px solid #30363d;";
            rowDiv.innerHTML = `<span style="font-size: 14px; color: #c9d1d9;"><b style="color:#58a6ff;">Trip ${i+1}</b>: ${t.start} ~ ${t.end} (Duration: ${t.duration} min)</span>`;

            const btn = document.createElement('button');
            btn.innerHTML = '🔍 Zoom Chart';
            btn.style.cssText = "background: #21262d; border: 1px solid #30363d; color: #58a6ff; padding: 5px 15px; border-radius: 6px; cursor: pointer; font-size: 13px; font-weight: bold; transition: 0.2s; white-space: nowrap;";
            btn.onclick = () => {
                const s = new Date(t.start).getTime() - 600000, e = new Date(t.end).getTime() + 600000;  
                [vChart, tChart].forEach(c => { c.options.scales.x.min = s; c.options.scales.x.max = e; autoScaleY(c); c.update(); });
            };
            rowDiv.appendChild(btn);
            tripList.appendChild(rowDiv);
        });
    }

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

    function parseCarValue(input) {
        let text = new DOMParser().parseFromString(String(input), 'text/html').documentElement.textContent;
        return parseFloat(text.replace(/[^\d.-]/g, '')) || 0;
    }

    function normalizeTime(timeStr) {
        if (/^\d{4}-\d{2}-\d{2}/.test(timeStr)) return timeStr;
        const enMatch = timeStr.match(/^([a-zA-Z]{3})\s+(\d{1,2})\/(\d{4})\s+(\d{2}:\d{2})/);
        if (enMatch) {
            const months = {jan:'01', feb:'02', mar:'03', apr:'04', may:'05', jun:'06', jul:'07', aug:'08', sep:'09', oct:'10', nov:'11', dec:'12'};
            const m = months[enMatch[1].toLowerCase()];
            if (m) return `${enMatch[3]}-${m}-${enMatch[2].padStart(2, '0')} ${enMatch[4]}`;
        }
        return null;
    }

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
                            unit: 'hour', 
                            displayFormats: { hour: 'MM/dd HH:mm' },
                            tooltipFormat: 'MM/dd HH:mm:ss' 
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
                    zoom: { pan: { enabled: true, mode: 'x', onPan: syncCharts }, zoom: { wheel: { enabled: true }, mode: 'x', onZoom: syncCharts } } 
                }
            },
            plugins: [crosshairPlugin]
        };
    }
    vChart = new Chart(document.getElementById('voltageChart'), createChartConfig('Voltage (V)', '#58a6ff', 'Voltage (V)'));
    tChart = new Chart(document.getElementById('tempChart'), createChartConfig('Temperature (℃)', '#f85149', 'Temperature (℃)'));

    function syncCharts({chart}) {
        if (isResetting) return;
        const other = (chart === vChart) ? tChart : vChart;
        other.options.scales.x.min = chart.scales.x.min;
        other.options.scales.x.max = chart.scales.x.max;
        autoScaleY(chart); autoScaleY(other);
        chart.update('none'); other.update('none');
    }

    function resetViewAndUpdateData(dataList, selectedDate) {
        isResetting = true;

        const vValues = dataList.map(d => d.v);
        const tValues = dataList.map(d => d.t);
        
        const minV = Math.min(...vValues), maxV = Math.max(...vValues);
        const minT = Math.min(...tValues), maxT = Math.max(...tValues);
        const vPad = (maxV - minV) * 0.15 || 0.5;
        const tPad = (maxT - minT) * 0.15 || 2;

        [vChart, tChart].forEach(chart => {
            if (chart.resetZoom) chart.resetZoom('none'); 
            
            const isVoltage = (chart === vChart);
            chart.data.datasets[0].data = dataList.map(d => ({ x: d.x, y: isVoltage ? d.v : d.t }));
            
            chart.options.scales.y.min = isVoltage ? (minV - vPad) : (minT - tPad);
            chart.options.scales.y.max = isVoltage ? (maxV + vPad) : (maxT + tPad);
            
            if (selectedDate !== 'all') {
                const times = dataList.map(d => new Date(d.x).getTime());
                chart.options.scales.x.min = Math.min(...times);
                chart.options.scales.x.max = Math.max(...times);
            } else {
                chart.options.scales.x.min = null;
                chart.options.scales.x.max = null;
            }
        });

        const result = { 
            trips: (selectedDate === 'all' ? globalDetectedTrips.trips : globalDetectedTrips.trips.filter(t => t.start.startsWith(selectedDate))), 
            mode: globalDetectedTrips.mode 
        };
        renderTrips(result); 
        updateStatCards(dataList, result);

        vChart.update('none'); 
        tChart.update('none');
        
        setTimeout(() => { isResetting = false; }, 200);
    }

    uploadTrigger.onclick = () => fileInput.click();
    fileInput.onchange = (e) => {
        const file = e.target.files[0]; if (!file) return;
        statusText.innerHTML = 'Performing smart trip analysis...';
        const reader = new FileReader();
        reader.onload = function(e) {
            const workbook = XLSX.read(new Uint8Array(e.target.result), { type: 'array' });
            const ws = workbook.Sheets[workbook.SheetNames.find(n => n.includes("歷史") || n.includes("History")) || workbook.SheetNames[0]];
            const rows = XLSX.utils.sheet_to_json(ws, { header: 1 });
            let extracted = [], dates = new Set();
            for (let i = 0; i < rows.length; i++) {
                for (let col = 0; col < rows[i].length; col += 5) {
                    const timeStr = normalizeTime(String(rows[i][col] || "").trim());
                    if (timeStr) {
                        const vVal = parseCarValue(rows[i][col+1]);
                        if (vVal > 0) { extracted.push({ x: timeStr, v: vVal, t: parseCarValue(rows[i][col+3]) }); dates.add(timeStr.split(' ')[0]); }
                    }
                }
            }
            allData = extracted.sort((a, b) => new Date(a.x) - new Date(b.x));
            globalDetectedTrips = detectTripsByCurve(allData);
            dateSelector.innerHTML = '<option value="all">-- Show All --</option>';
            Array.from(dates).sort().forEach(d => { const opt = document.createElement('option'); opt.value = d; opt.innerText = d; dateSelector.appendChild(opt); });
            resetViewAndUpdateData(allData, 'all'); 
            statusText.innerHTML = `✅ Successfully parsed <b style="color:#58a6ff;">${allData.length}</b> records.`;
            downloadBtn.style.display = "inline-block";
        };
        reader.readAsArrayBuffer(file);
    };

    dateSelector.onchange = function() {
        const filtered = (this.value === 'all') ? allData : allData.filter(d => d.x.startsWith(this.value));
        resetViewAndUpdateData(filtered, this.value);
    };

    downloadBtn.onclick = () => {
        const wb = XLSX.utils.book_new();
        let tripDetails = globalDetectedTrips.trips.map((trip, index) => {
            const pts = allData.filter(d => { const t = new Date(d.x).getTime(); return t >= new Date(trip.start).getTime() && t <= new Date(trip.end).getTime(); });
            const vList = pts.map(p => p.v), tList = pts.map(p => p.t);
            return [index + 1, trip.start, trip.end, trip.duration, Math.max(...vList)||0, Math.min(...vList)||0, (tList.reduce((a, b) => a+b, 0)/tList.length||0).toFixed(1)];
        });
        const dailyData = [...new Set(allData.map(d => d.x.split(' ')[0]))].sort().map(date => {
            const dayV = allData.filter(d => d.x.startsWith(date)).map(d => d.v), dayT = globalDetectedTrips.trips.filter(t => t.start.startsWith(date));
            return [date, Math.min(...dayV).toFixed(2), Math.max(...dayV).toFixed(2), dayT.length, dayT.reduce((acc, t) => acc + t.duration, 0)];
        });
        XLSX.utils.book_append_sheet(wb, XLSX.utils.aoa_to_sheet([["Date", "Min Voltage", "Max Voltage", "Trip Count", "Total Duration(min)"], ...dailyData]), "Daily Health Report");
        XLSX.utils.book_append_sheet(wb, XLSX.utils.aoa_to_sheet([["No.", "Start", "End", "Duration(min)", "Max V", "Min V", "Avg Temp"], ...tripDetails]), "Trip Details");
        XLSX.utils.book_append_sheet(wb, XLSX.utils.aoa_to_sheet([["Time", "Voltage", "Temperature"], ...allData.map(d => [d.x, d.v, d.t])]), "Raw Data");
        XLSX.writeFile(wb, `BM6_Analysis_Report_${new Date().toISOString().slice(0,10)}.xlsx`);
    };
})();
</script>