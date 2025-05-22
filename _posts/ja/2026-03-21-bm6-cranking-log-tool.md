---
layout: post
title:  "BM6/BM200 100Hz始動ログ解析ツール"
lang: ja
date:   2026-03-21 10:00:00
categories: Auto
tags: [BM6, バッテリー監視, 始動波形, データ分析, 変換ツール, 車載バッテリー]
description: "BM6 Bluetoothバッテリーモニター専用の始動波形解析ツール。元のログファイル内の16進数パケットをデコードし、高精度のエンジン始動電圧曲線を正確にプロットし、動的閾値アルゴリズムにより最低点とスターターモーター解除点を自動的にマークします。"
keywords: "BM6, Bluetoothバッテリー監視, 始動波形, 始動電圧, クランキング, ログ解析, 車載バッテリー, リン酸鉄リチウムバッテリー"
image: /images/bm6-cranking-preview2.webp
faq:
  - question: "このツールは主にどのような問題を解決しますか？"
    answer: "純正アプリでは高解像度の始動波形のエクスポートができません。このツールは、Bluetoothで記録された元のログファイルを直接読み取り、内部の16進数パケットをデコードし、100Hzの高精度な始動電圧曲線を復元することで、バッテリーの瞬間放電能力とスターターモーターの状態を判断するのに役立ちます。"
  - question: "グラフ上の赤点とオレンジ色の点は何を意味しますか？"
    answer: "赤点 (Min) は、スターターモーターが重く引きずられた瞬間の、バッテリーが到達した最低電圧を表します。オレンジ色の点 (Starter) は、アルゴリズムによって推測された、スターターモーターの電源が切断され、エンジンが発電を引き継いだ瞬間の転換点です。"
  - question: "アップロードできるログファイルはどのように入手できますか？"
    answer: "スマートフォンのBluetooth分析ツール、またはBM6純正アプリに内蔵されたログエクスポート機能を使用して、記録されたブロードキャストデータを.txtまたは.log形式で保存できます。ファイルにエンジン始動時の期間が含まれていることを確認してください。"
  - question: "ログファイルをアップロードすると、プライバシーやデータ漏洩の懸念はありますか？"
    answer: "全くありません。このツールは純粋なフロントエンド (JavaScript) 技術で開発されており、すべてのデータ解析、16進数デコード、グラフ描画は、お客様のブラウザ内で独立して行われます。いかなるデータもクラウドサーバーにアップロードされることはありません。"
  - question: "始動最低電圧 (Min) がどのくらいまで下がると、バッテリーが故障寸前である可能性が高いですか？"
    answer: "一般的に健康な12V鉛酸またはAGMバッテリーは、常温でエンジンを始動する際、最低電圧は通常9.6V以上を維持します。赤点が頻繁に9.0V以下になる場合は、バッテリーの劣化や内部抵抗の増大を示している可能性があり、早めに専門家による検査を受けることをお勧めします。"
  - question: "ファイルをアップロードした後、「有効な始動波形が見つかりませんでした」と表示されるのはなぜですか？"
    answer: "これは通常、ログファイルに始動瞬間の完全なパケットがキャプチャされていないためです。ファイル内に 'cranking.add:ok' の成功マークがあることを確認してください。また、始動時にスマートフォンが車から遠すぎてBluetoothパケットが欠落した場合も、波形が不完全になり解析できません。"
  - question: "アルゴリズムはどのようにオレンジ色の点 (スターターモーター解除点) を判断しますか？"
    answer: "このツールは「動的閾値」アルゴリズムを採用しています。プログラムはまず、始動前の「初期静止電圧」を自動的に検出し、始動後に電圧がその初期電圧に近づいて回復したとき（モーターが停止したか、発電機が引き継いだことを意味します）、電圧の谷底反発プロセス中の最後の局所的な最低点を逆算して見つけ出します。これにより、このツールは従来の鉛酸バッテリーだけでなく、静止電圧が高いリン酸鉄リチウムバッテリーにも完璧に対応できます。"
---

<div id="car-app-container"
    style="max-width: 950px; margin: 20px auto; font-family: 'Segoe UI', 'Microsoft JhengHei', sans-serif; background: #0d1117; color: #c9d1d9; padding: 25px; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 1px solid #30363d; position: relative;">

    <h2 id="ui-title" style="text-align: center; color: #c9d1d9; margin-bottom: 10px; margin-top: 10px;">BM6 始動波形解析ツール</h2>

    <div
        style="background: rgba(210, 153, 34, 0.1); padding: 15px 20px; border-radius: 10px; margin-bottom: 25px; border-left: 5px solid #d29922; font-size: 14.5px; line-height: 1.6; color: #8b949e;">
        <strong id="ui-desc-title" style="color: #d29922;">動的閾値検出をサポート (鉛酸およびリン酸鉄リチウムバッテリーに対応)</strong><br>
        <span id="ui-desc-body">このツールは、取得した <b style="color:#c9d1d9;">.log 原始ログファイル</b>を直接読み取り、16進数パケットを100Hzの高解像度波形に変換し、動的アルゴリズムによって電圧最低点とスターターモーター解除点を自動的に特定することで、バッテリーの限界性能を簡単に確認できます。</span>
    </div>

    <div
        style="background: #161b22; border: 1px solid #30363d; padding: 15px 25px; border-radius: 10px; gap: 10px; margin-bottom: 25px; display: flex; align-items: center; justify-content: center;">
        <button id="uploadTrigger"
            style="background: #1f6feb; color: white; border: none; padding: 12px 24px; border-radius: 8px; cursor: pointer; font-weight: bold; font-size: 15px; transition: 0.2s;">📁
            ログファイル (.txt / .log) をアップロード</button>
        <input type="file" id="logFileInput" accept=".txt,.log" style="display:none">
        <button id="loadSampleBtn" style="background: #30363d; color: #c9d1d9; border: 1px solid #8b949e; padding: 9px 20px; border-radius: 8px; cursor: pointer; font-weight: bold; font-size: 14px; text-decoration: none; display: flex; align-items: center; transition: 0.2s;">📄 サンプルファイルを読み込んでテスト</button>
         
    </div>

    <div id="status-text"
        style="text-align: center; color: #8b949e; margin-bottom: 20px; font-size: 14px; font-weight: bold;">分析のためにブロードキャストデータを含むログファイルをアップロードしてください</div>

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

        // 十字準星プラグイン (同 03-20)
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

        const loadSampleBtn = document.getElementById('loadSampleBtn');

        // 直接載入範例檔的點擊事件
        loadSampleBtn.onclick = function() {
            // 更新狀態與清空畫面
            statusText.innerHTML = `<b style="color:#58a6ff;">サンプルファイル (bm6_100Hz.log)</b> を読み込み中...`;
            chartsWrapper.innerHTML = ''; 

            // 使用 fetch API 直接從伺服器抓取檔案
            fetch('/files/bm6_100Hz.log')
                .then(response => {
                    if (!response.ok) {
                        throw new Error('サンプルファイルを取得できませんでした (HTTP ' + response.status + ')');
                    }
                    return response.text();
                })
                .then(text => {
                    // 抓取成功後，直接把純文字交給現有的解析函數
                    processLogData(text);
                })
                .catch(error => {
                    statusText.innerHTML = `<span style="color:#f85149;">❌ サンプルファイルの読み込みに失敗しました：${error.message}</span>`;
                });
        };

        fileInput.addEventListener('change', function (e) {
            const file = e.target.files[0];
            if (!file) return;

            statusText.innerHTML = `<b style="color:#58a6ff;">${file.name}</b> を解析中...`;
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
                                        eventTimeStr = `${mm}/${dd} ${hh}:${min}:${ss} (履歴)`;

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
                statusText.innerHTML = '<span style="color:#f85149;">❌ ファイル内で有効な始動波形が見つかりませんでした。クランキング記録を含むファイルであることを確認してください。</span>';
                return;
            }

            statusText.innerHTML = `✅ 解析完了！合計 <b style="color:#58a6ff;">${crankingEvents.length}</b> 回のエンジン始動記録が検出されました。`;

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
                            ctx.fillText(` スターター解除: ${starterPoint.y.toFixed(2)}V`, ptStarter.x + 10, ptStarter.y);
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
            titleElement.innerHTML = `始動波形分析 - 記録 #${eventNumber} (時間: ${eventTime} | 温度: ${eventTemp}°C | 初期: ${vInitial.toFixed(2)}V)`;
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
                            label: '電圧 (V)',
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
                            title: { display: true, text: '時間 (秒)' },
                            max: times[times.length - 1],
                            ticks: { maxTicksLimit: 10 }
                        },
                        y: {
                            title: { display: true, text: '電圧 (V)' },
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
                                        return `電圧: ${item.parsed.y}V`;
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