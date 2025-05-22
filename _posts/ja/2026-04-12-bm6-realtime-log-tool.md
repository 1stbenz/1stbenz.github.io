---
layout: post
title: BM6の毎秒リアルタイムデータ解析ツール
lang: ja
date: 2026-04-12 10:00:00
categories: Auto
tags: [BM6, バッテリー監視, データ変換, ログ解析, 車載バッテリー]
description: BM6の生ログに含まれる16進数パケットを、読み取り可能な毎秒の電圧および温度データに変換し、CSVエクスポートと二軸グラフによる視覚化をサポートします。
keywords: BM6, バッテリー監視, リアルタイムデータ, 電圧記録, 温度記録, ログ解析, 16進数デコード, CSVエクスポート, リン酸鉄リチウムバッテリー
image: /images/bm6-cranking-preview.webp
faq:
  - question: "このツールとエンジン始動波形解析ツールとの違いは何ですか？"
    answer: エンジン始動波形ツールは、エンジンの瞬間的な100Hz高速サンプリングデータ（cranking.add）を対象としています。一方、本ツールは通常、毎秒一度のリアルタイムブロードキャストデータ（d15507パケット）を対象としており、長距離運転中の発電機充電電圧の変化や環境温度の傾向を観察するのに適しています。
  - question: "ログファイルから対応するデータを見つけるにはどうすればよいですか？"
    answer: ツールは自動的に`d15507`で始まるパケットを検索します。これはBM6ブロードキャストプロトコルで定義されているリアルタイムステータスデータです。ログファイルに、記録されたBluetoothの受信（receive）記録が含まれていれば解析可能です。
  - question: "処理後のデータのダウンロードはサポートされていますか？"
    answer: はい、可能です。解析が完了すると、「CSVファイルをダウンロード」ボタンが表示されますので、データをExcelやその他の専門的な描画ソフトウェアにエクスポートし、より詳細な長期トレンド分析を行うことができます。
  - question: "なぜグラフを分けて表示するのですか？"
    answer: 異なるスケールの線が互いに干渉するのを避けるため、「電圧 (V)」と「温度 (°C)」を上下の2つのグラフに分割しています。両者は共通の時間軸を使用し、同期ズームに対応しているため、同じ時点でのデータ変動を正確に比較できます。
  - question: "ログファイルをアップロードしてもプライバシー上の懸念はありますか？"
    answer: 全くありません。本ツールも同様に、純粋なフロントエンド（JavaScript）技術を採用しており、すべての計算がお客様のコンピューターブラウザ内で行われるため、データはサーバーに送信されません。
---
<div id="bm6-realtime-container"
    style="max-width: 950px; margin: 20px auto; font-family: 'Segoe UI', 'Microsoft JhengHei', sans-serif; background: #0d1117; color: #c9d1d9; padding: 25px; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 1px solid #30363d; position: relative;">

    <h2 id="ui-title" style="text-align: center; color: #c9d1d9; margin-bottom: 10px; margin-top: 10px;">BM6 秒間リアルタイムデータ解析ツール</h2>

    <div
        style="background: rgba(56, 139, 253, 0.1); padding: 15px 20px; border-radius: 10px; margin-bottom: 25px; border-left: 5px solid #388bfd; font-size: 14.5px; line-height: 1.6; color: #8b949e;">
        <strong id="ui-desc-title" style="color: #58a6ff;">1Hzのリアルタイムデータ抽出とCSVエクスポートに対応</strong><br>
        <span id="ui-desc-body">本ツールは、Log内の <b style="color:#c9d1d9;">d15507 パケット</b>を自動的に検索し、16進数データを毎秒更新される電圧および温度記録に変換します。さらに、同期ズームに対応した動的グラフのプレビューとデータダウンロード機能を提供します。</span>
    </div>

    <div
        style="background: #161b22; border: 1px solid #30363d; padding: 20px; border-radius: 10px; margin-bottom: 25px; display: flex; flex-direction: column; align-items: center; gap: 15px;">
        <div style="display: flex; gap: 10px;">
            <button id="uploadTrigger"
                style="background: #1f6feb; color: white; border: none; padding: 12px 24px; border-radius: 8px; cursor: pointer; font-weight: bold; font-size: 15px; transition: 0.2s;">📁 Logファイル（.txt / .log）をアップロード</button>
            <button id="downloadBtn" style="background: #238636; color: white; border: none; padding: 12px 24px; border-radius: 8px; cursor: pointer; font-weight: bold; font-size: 15px; display: none;">📥 CSVファイルをダウンロード</button>
        </div>
        <input type="file" id="logFileInput" accept=".txt,.log" style="display:none">
        <div id="status-text" style="color: #8b949e; font-size: 14px; font-weight: bold;">リアルタイム放送データを含むファイルを選択してください</div>
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

    // --- Chart.js 初期設定 ---
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

    // 建立兩個圖表實體
    vChart = new Chart(document.getElementById('voltageChart'), createChartConfig('電壓 (V)', '#58a6ff', '電壓 (V)'));
    tChart = new Chart(document.getElementById('tempChart'), createChartConfig('溫度 (℃)', '#f85149', '溫度 (℃)'));


    // --- 檔案解析處理 ---
    uploadTrigger.onclick = () => fileInput.click();

    fileInput.onchange = function(e) {
        const file = e.target.files[0];
        if (!file) return;

        statusText.innerHTML = `現在、<b style="color:#58a6ff;">${file.name}</b>を解析しています...`;
        
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
                
                // 處理跨夜ロジック (例: 23:59:59 から 00:00:00 へ)
                const [h, m, s] = timeStr.split(':').map(Number);
                const currentTimeObj = new Date(2026, 0, currentDay, h, m, s);
                
                if (lastTimeObj && currentTimeObj < lastTimeObj) {
                    currentDay++;
                    currentTimeObj.setDate(currentDay);
                }
                lastTimeObj = currentTimeObj;
                
                // Chart.js 用の Timestamp を取得
                const timeVal = currentTimeObj.getTime();

                vData.push({ x: timeVal, y: voltage });
                tData.push({ x: timeVal, y: tempC });
                
                // CSV エクスポート用の元の文字列を保持
                parsedData.push([timeStr, voltage, tempC]);
            }
        });

        if (parsedData.length > 0) {
            statusText.innerHTML = `✅ 解析成功！合計 <b style="color:#3fb950;">${parsedData.length}</b> 件のリアルタイムデータが抽出されました。`;
            downloadBtn.style.display = 'inline-block';
            
            isResetting = true;

            [vChart, tChart].forEach(chart => {
                if (chart.resetZoom) chart.resetZoom('none');
            });

            // データを更新
            vChart.data.datasets[0].data = vData;
            tChart.data.datasets[0].data = tData;

            // チャートが完全に表示されるようにY軸の境界を事前に計算する
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
            statusText.innerHTML = `<span style="color:#f85149;">❌ 有効なデータが見つかりませんでした。ログに d15507 パケットが含まれているか確認してください。</span>`;
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