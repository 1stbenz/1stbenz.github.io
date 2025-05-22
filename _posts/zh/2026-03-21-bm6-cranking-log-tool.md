---
layout: post
title:  "BM6/BM200 100Hz啟動日誌解析工具"
lang: zh-Hant
date:   2026-03-21 10:00:00
categories: Auto
tags: [BM6, 電瓶監控, 啟動波形, 數據分析, 轉換工具, 汽車電池]
description: "專為 BM6 藍牙電瓶監控器設計的啟動波形解析工具。可將原始 Log 檔案中的 16 進位封包解碼，精準繪製高解析度的引擎啟動電壓曲線，並透過動態門檻演算法自動標記最低點與啟動馬達脫離點。"
keywords: "BM6, 藍牙電瓶監控, 啟動波形, 啟動電壓, Cranking, Log解析, 汽車電池, 鋰鐵電池"
image: /images/bm6-cranking-preview2.webp
faq:
  - question: "這個工具主要解決什麼問題？"
    answer: "原廠 APP 無法提供高解析度的啟動波形匯出。本工具可以直接讀取藍牙側錄的原始 Log 檔案，解碼內部的 16 進位封包，還原 100Hz 高精度的啟動電壓曲線，幫助判斷電瓶瞬間放電能力與啟動馬達狀態。"
  - question: "圖表上的紅點與橘點代表什麼？"
    answer: "紅點 (Min) 代表啟動馬達重拖瞬間，電瓶被拉到的最低電壓；橘點 (Starter) 則是透過演算法推算，啟動馬達電源切斷、引擎順利接手發電的瞬間轉折點。"
  - question: "如何取得可以上傳的 Log 檔案？"
    answer: "您可以透過手機端的藍牙分析工具，或是 BM6 原廠 APP 內建的日誌匯出功能，將側錄到的廣播數據存檔為 .txt 或 .log 格式。請確保檔案內涵蓋了發動當下的時間段。"
  - question: "上傳 Log 檔案會有隱私或資料外洩的疑慮嗎？"
    answer: "完全不會。本工具採用純前端 (JavaScript) 技術開發，所有的資料解析、16 進位解碼與圖表繪製，都是在您的瀏覽器內部獨立完成的，沒有任何資料會被上傳到雲端伺服器。"
  - question: "啟動最低電壓 (Min) 掉到多少代表電瓶可能快壞了？"
    answer: "一般健康的 12V 鉛酸或 AGM 電瓶，在常溫下啟動引擎時，最低電壓通常會維持在 9.6V 以上。如果您的紅點經常落在 9.0V 甚至更低，可能代表電瓶老化、內阻變大，建議提早進行專業檢測。"
  - question: "為什麼上傳檔案後顯示「未找到有效的啟動波形」？"
    answer: "這通常是因為 Log 檔案中沒有擷取到發動瞬間的完整封包。請確認檔案內是否有 'cranking.add:ok' 的成功標記。此外，若發動時手機離車子太遠導致藍牙掉包，也會造成波形不完整而無法解析。"
  - question: "演算法是如何判定橘點 (啟動馬達脫離點) 的？"
    answer: "本工具採用「動態門檻」演算法。程式會先自動偵測發動前的「初始靜置電壓」，當啟動後電壓回彈接近該初始電壓時（代表馬達已斷電或發電機接手），再往回推算找出電壓谷底反彈過程中的最後一個局部低點。這使得工具不僅適用於傳統鉛酸電池，也能完美相容靜置電壓較高的鋰鐵電池。"
---

<div id="car-app-container"
    style="max-width: 950px; margin: 20px auto; font-family: 'Segoe UI', 'Microsoft JhengHei', sans-serif; background: #0d1117; color: #c9d1d9; padding: 25px; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 1px solid #30363d; position: relative;">

    <h2 id="ui-title" style="text-align: center; color: #c9d1d9; margin-bottom: 10px; margin-top: 10px;">BM6 啟動波形解析工具</h2>

    <div
        style="background: rgba(210, 153, 34, 0.1); padding: 15px 20px; border-radius: 10px; margin-bottom: 25px; border-left: 5px solid #d29922; font-size: 14.5px; line-height: 1.6; color: #8b949e;">
        <strong id="ui-desc-title" style="color: #d29922;">支援動態門檻偵測 (相容鉛酸與鋰鐵電池)</strong><br>
        <span id="ui-desc-body">本工具能直接讀取擷取的 <b style="color:#c9d1d9;">.log 原始日誌檔</b>，將 16
            進位封包轉換為 100Hz 高解析度波形，並透過動態演算法自動找出電壓最低點與啟動馬達脫離點，方便檢視電瓶極限效能。</span>
    </div>

    <div
        style="background: #161b22; border: 1px solid #30363d; padding: 15px 25px; border-radius: 10px; margin-bottom: 25px; display: flex; align-items: center; justify-content: center;">
        <button id="uploadTrigger"
            style="background: #1f6feb; color: white; border: none; padding: 12px 24px; border-radius: 8px; cursor: pointer; font-weight: bold; font-size: 15px; transition: 0.2s;">📁
            上傳 Log 檔案 (.txt / .log)</button>
        <input type="file" id="logFileInput" accept=".txt,.log" style="display:none">
    </div>

    <div id="status-text"
        style="text-align: center; color: #8b949e; margin-bottom: 20px; font-size: 14px; font-weight: bold;">請上傳包含廣播數據的
        Log 檔案以進行分析</div>

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

        // 十字準星插件 (同 03-20)
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

            statusText.innerHTML = `正在解析 <b style="color:#58a6ff;">${file.name}</b> ...`;
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
            
            // 1. 預先掃描：建立「歷史時間戳 -> 溫度」的專屬資料庫
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
            let currentLogTime = "未知";
            let rollingRealTimeTemp = "未知";

            // 2. 逐行解析：分離歷史波形與即時波形
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
                                    let eventTemp = "未知";

                                    if (isHistorical && activeTimeline) {
                                        let ts = parseInt(activeTimeline);
                                        let date = new Date(ts * 1000);
                                        let mm = String(date.getMonth() + 1).padStart(2, '0');
                                        let dd = String(date.getDate()).padStart(2, '0');
                                        let hh = String(date.getHours()).padStart(2, '0');
                                        let min = String(date.getMinutes()).padStart(2, '0');
                                        let ss = String(date.getSeconds()).padStart(2, '0');
                                        eventTimeStr = `${mm}/${dd} ${hh}:${min}:${ss} (歷史)`;

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
                statusText.innerHTML = '<span style="color:#f85149;">❌ 未在檔案中找到有效的啟動波形。請確認這是否為包含 cranking 紀錄的檔案。</span>';
                return;
            }

            statusText.innerHTML = `✅ 解析完成！共偵測到 <b style="color:#58a6ff;">${crankingEvents.length}</b> 次引擎啟動紀錄。`;

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

        // 動態 Y 軸縮放邏輯
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
                // 下限：畫面中最低點的下一個整數
                chart.options.scales.y.min = Math.floor(minV * 5) / 5;
                // 上限：畫面中最高點往上取 0.2 的倍數
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

            // 1. 最低點 (Min Cranking)
            let minVol = Math.min(...voltages);
            let minIdx = voltages.indexOf(minVol);
            let localMins = getLocalMinima(voltages);

            // 2. 動態爬升點 (Dynamic Threshold) 
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

            // 3. 啟動馬達脫離點 (Starter Disengaged)
            let validMinsForStarter = localMins.filter(idx => idx >= minIdx && idx < climbIdx);
            let starterIdx = validMinsForStarter.length > 0 ? validMinsForStarter[validMinsForStarter.length - 1] : minIdx;

            const minPoint = { x: times[minIdx], y: voltages[minIdx] };
            const starterPoint = { x: times[starterIdx], y: voltages[starterIdx] };

            // 標籤繪製插件 (取代 Plotly 的 markers+text)
            const pointLabelsPlugin = {
                id: 'pointLabels',
                afterDraw: chart => {
                    const ctx = chart.ctx;
                    const meta = chart.getDatasetMeta(1); // Scatter dataset
                    if (!meta.hidden && meta.data.length >= 2) {
                        ctx.save();
                        ctx.font = 'bold 12px "Segoe UI", sans-serif';
                        ctx.fillStyle = '#c9d1d9';
                        
                        // 設定垂直置中對齊，讓文字與點在同一水平線上
                        ctx.textBaseline = 'middle'; 

                        // Min 標籤 (放在紅點的右側)
                        const ptMin = meta.data[0];
                        if (ptMin.x >= chart.chartArea.left && ptMin.x <= chart.chartArea.right) {
                            ctx.textAlign = 'left';
                            // x 座標向右偏移 10px 避開點的本體，y 座標與點相同
                            ctx.fillText(`Min: ${minPoint.y.toFixed(2)}V`, ptMin.x + 10, ptMin.y);
                        }
                        
                        // Starter 標籤 (放在橘點的右側)
                        const ptStarter = meta.data[1];
                        if (ptStarter.x >= chart.chartArea.left && ptStarter.x <= chart.chartArea.right) {
                            ctx.textAlign = 'left';
                            // 同樣向右偏移 10px 避開橘點
                            ctx.fillText(` Starter dise: ${starterPoint.y.toFixed(2)}V`, ptStarter.x + 10, ptStarter.y);
                        }
                        ctx.restore();
                    }
                }
            };

            // 建立 UI 容器
            const wrapperDiv = document.createElement('div');
            wrapperDiv.style.cssText = "background: #161b22; padding: 15px; border-radius: 10px; border: 1px solid #30363d; width: 100%; box-sizing: border-box;";
            
            // 加入自訂標題
            const titleElement = document.createElement('div');
            titleElement.style.cssText = "color: #c9d1d9; font-size: 16px; font-weight: bold; text-align: center; margin-bottom: 15px;";
            titleElement.innerHTML = `啟動波形分析 - 紀錄 #${eventNumber} (時間: ${eventTime} | 溫度: ${eventTemp}°C | 初始: ${vInitial.toFixed(2)}V)`;
            wrapperDiv.appendChild(titleElement);

            const canvasDiv = document.createElement('div');
            canvasDiv.style.cssText = "width: 100%; height: 400px; position: relative;";
            
            const canvas = document.createElement('canvas');
            canvas.id = `chart-${eventNumber}`;
            canvasDiv.appendChild(canvas);
            wrapperDiv.appendChild(canvasDiv);
            chartsWrapper.appendChild(wrapperDiv);

            // 初始化 Chart.js
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
                            tension: 0.2, // 平滑曲線
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
                            // 預先計算合適的 Y 軸範圍
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
                                // 標題 (上)：顯示電壓，並判斷是不是特殊紅橘點
                                title: function(tooltipItems) {
                                    if (tooltipItems.length > 0) {
                                        const item = tooltipItems[0];                                
                                        return `電壓: ${item.parsed.y}V`;
                                    }
                                    return '';
                                },
                                // 內容 (下)：顯示時間
                                label: function(context) {
                                    // 關鍵修改：不論是哪一組資料集，只顯示抓到的「第一個」資料項的時間標籤
                                    if (context.dataIndex !== context.chart.tooltip.dataPoints[0].dataIndex || 
                                        context.datasetIndex !== context.chart.tooltip.dataPoints[0].datasetIndex) {
                                        return null;
                                    }
                                    // 使用 context.raw.x 確保抓到的是原始數據中的秒數
                                    return `時間: ${context.raw.x.toFixed(2)} 秒`;
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