---
layout: post
title: "BM6/BM200 每秒即時數據解析工具"
lang: zh-Hant
date: 2026-04-12 10:00:00
categories: Auto
tags: [汽車電池, 電瓶監控, DIY工具, 數據分析]
description: "將 BM6 原始 Log 中的 16 進位封包轉換為可讀的每秒電壓與溫度數據，並支援 CSV 匯出與雙軸圖表視覺化。"
keywords: "BM6, 電瓶監控, 即時數據, 電壓紀錄, 溫度紀錄, Log解析, 16進位解碼, CSV匯出, 鋰鐵電池"
image: /images/bm6-cranking-preview.webp
faq:
  - question: "這個工具與啟動波形解析工具有什麼不同？"
    answer: "啟動波形工具是針對發動瞬間的 100Hz 高速採樣數據（cranking.add）；而本工具是針對平時每秒一次的即時廣播數據（d15507 封包），適合用來觀察長途駕駛中的發電機充電電壓變化或環境溫度趨勢。"
  - question: "如何從 Log 檔案中找到對應的數據？"
    answer: "工具會自動搜尋符合 `d15507` 開頭的封包，這是 BM6 廣播協定中定義的即時狀態資料。只要您的 Log 檔案包含側錄到的藍牙 receive 紀錄即可解析。"
  - question: "支援下載處理後的數據嗎？"
    answer: "可以。解析完成後會出現「下載 CSV 檔案」按鈕，您可以將數據匯出至 Excel 或其他專業繪圖軟體進行更深入的長期趨勢分析。"
  - question: "為什麼圖表要分開顯示？"
    answer: "為了避免不同刻度的線條互相干擾，我們將「電壓 (V)」與「溫度 (°C)」拆分成上下兩個圖表。兩者共用時間軸且支援同步縮放，方便您精準比對同一時間點的數據波動。"
  - question: "上傳 Log 檔案會有隱私疑慮嗎？"
    answer: "完全不會。本工具同樣採用純前端 (JavaScript) 技術開發，所有運算都在您的電腦瀏覽器內完成，資料不會傳送到伺服器。"
---

<div id="bm6-realtime-container" style="max-width: 950px; margin: 20px auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #ffffff; color: #333333; padding: 25px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e5e7eb; position: relative;">

    <h2 id="ui-title" style="text-align: center; color: #04384c !important; margin-bottom: 22px; margin-top: 5px; font-weight: 800; font-size: 22px; background: none; border: none;">BM6 每秒即時數據解析工具</h2>

    <div
        style="background: rgba(4, 56, 76, 0.05); padding: 15px 20px; border-radius: 10px; margin-bottom: 25px; border-left: 5px solid #04384c; font-size: 14.5px; line-height: 1.6; color: #475569;">
        <strong id="ui-desc-title" style="color: #04384c;">支援 1Hz 即時數據提取與 CSV 匯出</strong><br>
        <span id="ui-desc-body">本工具能自動搜尋 Log 中的 <b style="color:#04384c;">d15507 封包</b>，將 16 進位數據轉換為每秒更新的電壓與溫度紀錄，並提供支援同步縮放的動態圖表預覽與數據下載功能。</span>
    </div>

    <div
        style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 20px; border-radius: 10px; margin-bottom: 25px; display: flex; flex-direction: column; align-items: center; gap: 15px;">
        <div style="display: flex; gap: 10px;">
            <button id="uploadTrigger"
                style="background: #04384c; color: white; border: none; padding: 12px 24px; border-radius: 8px; cursor: pointer; font-weight: bold; font-size: 15px; transition: 0.2s;">📁 上傳 Log 檔案 (.txt / .log)</button>
            <button id="downloadBtn" style="background: #16a34a; color: white; border: none; padding: 12px 24px; border-radius: 8px; cursor: pointer; font-weight: bold; font-size: 15px; display: none;">📥 下載 CSV 檔案</button>
        </div>
        <input type="file" id="logFileInput" accept=".txt,.log" style="display:none">
        <div id="status-text" style="color: #64748b; font-size: 14px; font-weight: bold;">請選擇包含即時廣播數據的檔案</div>
    </div>

    <div style="background: #ffffff; padding: 15px; border-radius: 10px; border: 1px solid #e2e8f0; box-sizing: border-box; box-shadow: 0 1px 4px rgba(0,0,0,0.04);">
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

    // --- Chart.js 初始化配置 ---
    Chart.defaults.color = '#64748b';
    Chart.defaults.borderColor = '#e2e8f0';

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
                ctx.strokeStyle = 'rgba(4, 56, 76, 0.35)';
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
                        backgroundColor: 'rgba(255, 255, 255, 0.96)',
                        titleColor: '#0f172a',
                        bodyColor: '#334155',
                        borderColor: '#cbd5e1',
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

    // 建立兩個圖表實體
    vChart = new Chart(document.getElementById('voltageChart'), createChartConfig('電壓 (V)', '#1176d4', '電壓 (V)'));
    tChart = new Chart(document.getElementById('tempChart'), createChartConfig('溫度 (℃)', '#dc2626', '溫度 (℃)'));


    // --- 檔案解析處理 ---
    uploadTrigger.onclick = () => fileInput.click();

    fileInput.onchange = function(e) {
        const file = e.target.files[0];
        if (!file) return;

        statusText.innerHTML = `正在解析 <b style="color:#58a6ff;">${file.name}</b>...`;
        
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
                
                // 處理跨夜邏輯 (例如從 23:59:59 變成 00:00:00)
                const [h, m, s] = timeStr.split(':').map(Number);
                const currentTimeObj = new Date(2026, 0, currentDay, h, m, s);
                
                if (lastTimeObj && currentTimeObj < lastTimeObj) {
                    currentDay++;
                    currentTimeObj.setDate(currentDay);
                }
                lastTimeObj = currentTimeObj;
                
                // 取得 Timestamp 給 Chart.js
                const timeVal = currentTimeObj.getTime();

                vData.push({ x: timeVal, y: voltage });
                tData.push({ x: timeVal, y: tempC });
                
                // 保留原始字串給 CSV 匯出
                parsedData.push([timeStr, voltage, tempC]);
            }
        });

        if (parsedData.length > 0) {
            statusText.innerHTML = `✅ 解析成功！共提取 <b style="color:#3fb950;">${parsedData.length}</b> 筆即時數據。`;
            downloadBtn.style.display = 'inline-block';
            
            isResetting = true;

            [vChart, tChart].forEach(chart => {
                if (chart.resetZoom) chart.resetZoom('none');
            });

            // 更新數據
            vChart.data.datasets[0].data = vData;
            tChart.data.datasets[0].data = tData;

            // 預先計算 Y 軸邊界以防止圖表顯示不全
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
            statusText.innerHTML = `<span style="color:#f85149;">❌ 未找到有效數據。請確認 Log 是否包含 d15507 封包。</span>`;
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