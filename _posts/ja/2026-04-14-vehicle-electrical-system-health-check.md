---
layout: post
title: "車両電力システム総合健康診断：BM6長期データ分析"
lang: ja
date: 2026-04-14 09:52:00
categories: Auto
tags: [自動車バッテリー, リン酸鉄リチウムバッテリー, 鉛蓄電池, 発電機診断, データ分析, 暗電流, 始動電圧]
description: "バッテリー交換のタイミングを科学的に判断するには？本記事では、1Hz監視データと100Hz高周波始動記録を分析し、静止漏電、走行発電効率、始動時の瞬発力を詳細に評価する車両電力システム健康診断システムを紹介します。"
keywords: "バッテリー健康度, リン酸鉄リチウムバッテリー, LiFePO4, 鉛蓄電池, 暗電流テスト, 始動電圧, 発電機検査, Bluetoothログ分析, 車載電力"
image: /images/battery-health-report-analysis.webp
faq:
  - question: "このシステムは主にどのような主要指標を検査しますか？"
    answer: "システムは4つの主要指標を評価します：1. 蓄電健康度（静止電圧）、2. 暗電流状態（夜間電圧降下）、3. 発電システム（平均走行電圧）、4. 始動瞬発力（始動最低電圧）。"
  - question: "リン酸鉄リチウムバッテリーと鉛蓄電池の判断基準に違いはありますか？"
    answer: "システムには二重の基準が設定されています。例えば、リン酸鉄リチウムバッテリー（LiFePO4）の良好な静止電圧は13.2V以上が必要ですが、一般的な鉛蓄電池では12.5Vです。始動瞬時電圧の部分では、リン酸鉄の基準は11.5V、鉛蓄電池は10.5Vです。"
  - question: "車両に漏電（暗電流）があるかどうかをどのように判断しますか？"
    answer: "システムは長時間静止記録から「日次電圧降下（V/日）」を計算します。電圧降下が0.3V（リン酸鉄）または0.4V（鉛蓄電池）を超える場合、漏電過多と判断され、ドライブレコーダー、セキュリティシステム、またはOBD2機器が正しく休眠しているか確認することを推奨します。"
  - question: "始動電圧を分析するために100Hzのデータが必要なのはなぜですか？"
    answer: "エンジン始動の瞬間は1秒未満しか続きません。標準の1Hz（1秒に1回）の記録では、電圧の最低点を見逃しがちです。100Hzの高周波サンプリングにより、スターターモーター作動時の電圧降下を正確に捉え、バッテリー内部抵抗の増加やスターターモーターの劣化を判断できます。"
  - question: "発電機異常の判断基準は何ですか？"
    answer: "システムはエンジン始動後のデータをフィルタリングし、走行平均電圧が13.5V未満（または15.0V超）の場合、発電機の劣化またはレギュレーターの故障と見なします。充電制御システム（AMS）を備えた車両の場合、省エネモード時の低電圧についても特別に注記します。"
  - question: "リン酸鉄リチウムバッテリーの報告書で「蓄電が弱い」と表示された場合、どうすればよいですか？"
    answer: "リン酸鉄リチウムバッテリーの静止電圧が13.2Vに達しない場合、長距離走行を行うか、専用充電器で満充電し、BMSのアクティブセルバランス機能をトリガーして、バッテリー寿命と性能を確保することをお勧めします。"
---

<!-- 載入解析 Excel 需要的外部套件 -->
<script src="https://cdn.jsdelivr.net/npm/xlsx/dist/xlsx.full.min.js"></script>

<style>
    /* 這裡的樣式只會套用到這個頁面的元素 */
    .app-container {
        font-family: 'Segoe UI', 'Microsoft JhengHei', sans-serif;
        background: #0d1117;
        color: #c9d1d9;
        max-width: 1000px;
        margin: 0 auto;
        padding: 30px;
        border-radius: 15px;
        border: 1px solid #30363d;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    .app-container h1 { text-align: center; color: #58a6ff; margin-bottom: 30px; }
    .control-panel {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 20px;
        margin-bottom: 30px;
        background: #0d1117;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #30363d;
    }
    .file-input-group {
        display: flex;
        flex-direction: column;
        gap: 8px;
    }
    .file-input-group label { font-weight: bold; color: #8b949e; font-size: 14px; }
    .app-container input[type="file"], .app-container select {
        background: #21262d; padding: 10px; border-radius: 6px; border: 1px solid #30363d; color: #c9d1d9;
    }
    .file-hint { font-size: 12px; color: #8b949e; margin-top: -5px; }
    .btn-generate {
        width: 100%; padding: 15px; background: #238636; color: white; border: none; border-radius: 8px;
        font-size: 18px; font-weight: bold; cursor: pointer; transition: 0.2s; margin-top: 10px;
    }
    .btn-generate:hover { background: #2ea043; }
    
    .report-section { display: none; margin-top: 40px; }
    .patient-info {
        display: flex; justify-content: space-between; border-bottom: 2px solid #30363d;
        padding-bottom: 10px; margin-bottom: 20px; color: #8b949e;
    }
    .app-container table {
        width: 100%; border-collapse: collapse; margin-bottom: 30px;
        background: #0d1117; border-radius: 8px; overflow: hidden;
    }
    .app-container th, .app-container td { padding: 15px; text-align: center; border: 1px solid #30363d; }
    .app-container th { background: #21262d; color: #c9d1d9; font-weight: bold; }
    .app-container td:first-child { text-align: left; font-weight: bold; color: #58a6ff; }
    
    .status-good { color: #3fb950; font-weight: bold; }
    .status-warn { color: #d29922; font-weight: bold; }
    .status-bad { color: #f85149; font-weight: bold; }
    .status-none { color: #8b949e; font-style: italic; }

    .doctor-notes {
        background: rgba(56, 139, 253, 0.1); padding: 20px; border-radius: 10px;
        border-left: 5px solid #388bfd; line-height: 1.6;
    }
</style>

<div class="app-container">
    <h1>車両電力システム健康診断レポートシステム</h1>

    <div class="control-panel">
        <div class="file-input-group">
            <label>📁 1. オフライン長時間記録 (静止漏電評価)</label>
            <input type="file" id="fileOffline" accept=".xls,.xlsx,.csv">
            <span class="file-hint">エクスポートされたExcelスプレッドシート形式をサポート</span>
        </div>
        <div class="file-input-group">
            <label>📁 2. 生のBluetoothログ (発電と始動の評価)</label>
            <input type="file" id="fileRaw" accept=".txt,.log" multiple>
            <span class="file-hint">複数選択可能。複数日分の1Hzと100Hz混合パケットを自動解析</span>
        </div>
        <div class="file-input-group">
            <label>⚙️ バッテリー化学材料設定</label>
            <select id="batteryType">
                <option value="lifepo4">リン酸鉄リチウムバッテリー (LiFePO4) </option>
                <option value="leadacid">一般的な鉛蓄電池 (Lead-Acid)</option>
            </select>
        </div>
    </div>
    
    <button class="btn-generate" onclick="generateReport()">総合健康レポートを生成</button>

    <div class="report-section" id="reportSection">
        <div class="patient-info">
            <span id="reportDate">レポート日付：YYYY/MM/DD</span>
            <span id="reportConfig">分析設定：リン酸鉄リチウムバッテリー基準</span>
        </div>

        <table id="reportTable">
            <thead>
                <tr>
                    <th width="20%">検査項目</th>
                    <th width="20%">現在のデータ</th>
                    <th width="20%">良好基準</th>
                    <th width="20%">異常基準</th>
                    <th width="20%">総合判定</th>
                </tr>
            </thead>
            <tbody id="tableBody">
            </tbody>
        </table>

        <div class="doctor-notes">
            <h3 style="margin-top:0; color:#58a6ff;">📋 システム総合診断アドバイス</h3>
            <div id="aiDiagnosis">総合分析を取得するにはデータをアップロードしてください。</div>
        </div>
    </div>
</div>

<script>
    const thresholds = {
        lifepo4: {
            restV: { good: 13.2, bad: 13.0, unit: 'V' },
            dropV: { excellent: 0.01, good: 0.02, bad: 0.05, unit: 'V/日' },
            chargeV: { goodMin: 13.8, goodMax: 14.4, badMin: 13.5, unit: 'V' },
            crankV: { good: 11.5, bad: 10.0, unit: 'V' }
        },
        leadacid: {
            restV: { good: 12.5, bad: 12.0, unit: 'V' },
            dropV: { good: 0.15, bad: 0.4, unit: 'V/日' },
            chargeV: { goodMin: 13.8, goodMax: 14.8, badMin: 13.3, unit: 'V' },
            crankV: { good: 10.5, bad: 9.0, unit: 'V' }
        }
    };

        async function processXlsFile(file, bType) {
            return new Promise((resolve) => {
                const reader = new FileReader();
                reader.onload = function(e) {
                    const data = new Uint8Array(e.target.result);
                    const workbook = XLSX.read(data, {type: 'array'});
                    const sheetName = workbook.SheetNames[0];
                    const json = XLSX.utils.sheet_to_json(workbook.Sheets[sheetName], {header: 1});

                    // 1. 取得所有原始電壓 (排除標題列與異常值)
                    const allVoltages = json.slice(1)
                        .map(row => parseFloat(row[1]))
                        .filter(v => !isNaN(v) && v > 5.0 && v < 16.0);

                    if (allVoltages.length < 20) {
                        resolve({ rest: null, drop: null });
                        return;
                    }

                    // 2. 根據電池類型設定門檻
                    // filterThreshold: 高於此值視為發電機在充電，不計入靜置分析
                    // stableStartV: 低於此值才視為「表面電壓已散去」，開始計算真實壓降
                    const filterThreshold = (bType === 'lifepo4') ? 13.6 : 13.2;
                    const stableStartV = (bType === 'lifepo4') ? 13.3 : 12.7;

                    // 3. 計算蓄電健康度 (靜置電壓)
                    // 取整體數據的 5% 低分位數，這代表該電池在靜置期間最常出現的穩定低位電壓
                    const sortedV = [...allVoltages].sort((a, b) => a - b);
                    const restV = sortedV[Math.floor(sortedV.length * 0.05)];

                    // 4. 篩選出非充電中的靜置數據區間
                    const staticVs = allVoltages.filter(v => v < filterThreshold);

                    if (staticVs.length < 10) {
                        resolve({ rest: restV.toFixed(2), drop: 0 });
                        return;
                    }

                    // 5. 尋找「真實壓降起始點」：跳過剛熄火時從 13.6V 掉到 13.3V 的表面電壓區間
                    let startIndex = staticVs.findIndex(v => v <= stableStartV);
                    
                    // 防呆：如果數據全部都高於穩定門檻，或剩餘數據太少，則從頭計算
                    if (startIndex === -1 || (staticVs.length - startIndex) < 10) {
                        startIndex = 0;
                    }

                    const endIndex = staticVs.length - 1;

                    // 6. 取得起始與結束電壓 (取 5 筆平均避免單點雜訊)
                    const headRange = staticVs.slice(startIndex, startIndex + 5);
                    const tailRange = staticVs.slice(-5);
                    
                    const avgFirstV = headRange.reduce((a, b) => a + b, 0) / headRange.length;
                    const avgLastV = tailRange.reduce((a, b) => a + b, 0) / tailRange.length;

                    // 7. 計算有效分析區間的時間天數 (BM6 離線紀錄通常為 2 分鐘一筆)
                    const effectivePoints = endIndex - startIndex;
                    const totalDays = (effectivePoints > 0) ? (effectivePoints * 2) / 1440 : (allVoltages.length * 2) / 1440; 

                    // 8. 計算每日壓降：(起始平均 - 結束平均) / 天數
                    let realDrop = (avgFirstV - avgLastV) / totalDays;

                    // 修正負值問題：若電壓反而上升，代表數據不適合分析漏電，強制歸零
                    if (realDrop < 0) realDrop = 0;

                    resolve({ 
                        rest: restV.toFixed(2), 
                        drop: realDrop.toFixed(2)
                    });
                };
                reader.readAsArrayBuffer(file);
            });
        }


    async function generateReport() {
        const btn = document.querySelector('.btn-generate');
        btn.innerText = "データ分析中...";
        btn.disabled = true;

        const bType = document.getElementById('batteryType').value;
        const std = thresholds[bType];

        let metrics = { restingV: null, leakageDrop: null, avgChargeV: null, minCrankV: null };

        const fileXls = document.getElementById('fileOffline').files[0];
        if (fileXls) {
            const xlsResult = await processXlsFile(fileXls, bType);
            metrics.restingV = xlsResult.rest;
            metrics.leakageDrop = xlsResult.drop;
        }

        const rawFiles = document.getElementById('fileRaw').files;
        if (rawFiles.length > 0) {
            let sum1Hz = 0, count1Hz = 0;
            let crankMinList = []; 
            let fallback1HzMin = 99.0; 

            const engineOnThreshold = bType === 'lifepo4' ? 13.6 : 13.5;
            const engineOffThreshold = bType === 'lifepo4' ? 13.3 : 12.8;

            for (let i = 0; i < rawFiles.length; i++) {
                const text = await rawFiles[i].text();
                const lines = text.split('\n');
                
                const pattern1Hz = /d1550700[0-9a-fA-F]{6}([0-9a-fA-F]{4})/i;

                let isEngineRunning = false;
                let window15s = []; 
                let tempHexStream = ""; 

                lines.forEach(line => {
                    let lowerLine = line.trim().toLowerCase();

                    const match1Hz = lowerLine.match(pattern1Hz);
                    if (match1Hz) {
                        let v = parseInt(match1Hz[1], 16) / 100;
                        
                        window15s.push(v);
                        if (window15s.length > 15) window15s.shift();

                        if (v >= engineOnThreshold) {
                            isEngineRunning = true;
                        } 
                        
                        if (isEngineRunning) {
                            if (v < engineOnThreshold && window15s.length === 15) {
                                let v15sAgo = window15s[0];
                                if ((v15sAgo - v) >= 0.10) isEngineRunning = false;
                            }
                            if (v <= engineOffThreshold) isEngineRunning = false;
                        }

                        if (isEngineRunning && v > 10.0 && v < 16.0) { 
                            sum1Hz += v; 
                            count1Hz++; 
                        }

                        if (v > 6.0 && v < 15.0 && v < fallback1HzMin) fallback1HzMin = v;
                    } 
                    
                    if (lowerLine.includes('receive:')) {
                        let content = lowerLine.split("receive:")[1].trim();
                        if (/^[0-9a-f]+$/.test(content) && !content.startsWith("d15507")) {
                            tempHexStream += content;
                        }
                    }

                    if (lowerLine.includes('cranking.add:ok')) {
                        let parts = tempHexStream.split("fffffe");
                        if (parts.length > 1) {
                            let lastPart = parts[parts.length - 1];
                            if (lastPart.includes("fffefe")) {
                                let curveData = lastPart.split("fffefe")[0];
                                let localMin = 99.0; 
                                
                                for (let j = 0; j < curveData.length - 2; j += 3) {
                                    let voltage = parseInt(curveData.substring(j, j + 3), 16) / 100.0;
                                    if (!isNaN(voltage) && voltage >= 3.0 && voltage <= 15.0) {
                                        if (voltage < localMin) {
                                            localMin = voltage;
                                        }
                                    }
                                }
                                
                                if (localMin < 99.0) {
                                    crankMinList.push(localMin);
                                }
                            }
                        }
                        tempHexStream = ""; 
                    }
                });
            }

            if (count1Hz > 0) metrics.avgChargeV = (sum1Hz / count1Hz).toFixed(2);
            
            if (crankMinList.length > 0) {
                crankMinList.sort((a, b) => a - b);
                let takeCount = Math.min(3, crankMinList.length);
                let sumCrank = 0;
                
                for (let i = 0; i < takeCount; i++) {
                    sumCrank += crankMinList[i];
                }
                
                metrics.minCrankV = (sumCrank / takeCount).toFixed(2);
            } else if (fallback1HzMin < 99.0) {
                metrics.minCrankV = fallback1HzMin.toFixed(2);
            }
        }

        renderTable(metrics, std, bType);

        btn.innerText = "総合健康レポートを生成";
        btn.disabled = false;
        document.getElementById('reportSection').style.display = 'block';
    }

    function evaluate(value, goodRule, badRule, type) {
        if (value === null) return { text: "データなし", class: "status-none" };
        let v = parseFloat(value);
        if (type === 'higher_is_better') {
            if (v >= goodRule) return { text: "優良", class: "status-good" };
            if (v <= badRule) return { text: "要点検", class: "status-bad" };
            return { text: "まあまあ", class: "status-warn" };
        } else if (type === 'lower_is_better') {
            if (v <= goodRule) return { text: "優良", class: "status-good" };
            if (v >= badRule) return { text: "漏電過多", class: "status-bad" };
            return { text: "やや高め", class: "status-warn" };
        } else if (type === 'range') {
            if (v >= goodRule[0] && v <= goodRule[1]) return { text: "発電健康", class: "status-good" };
            if (v < badRule || v > 15.0) return { text: "発電機異常", class: "status-bad" };
            return { text: "充電弱め", class: "status-warn" };
        }
    }

    function renderTable(m, std, bType) {
        document.getElementById('reportDate').innerText = `レポート生成時間：${new Date().toLocaleString()}`;
        document.getElementById('reportConfig').innerText = `分析設定：${bType === 'lifepo4' ? 'リン酸鉄リチウムバッテリー' : '一般的な鉛蓄電池'}`;

        const tbody = document.getElementById('tableBody');
        tbody.innerHTML = "";

        const items = [
            {
                name: "蓄電健康度<br>(静止電圧)",
                val: m.restingV, unit: "V",
                goodStr: `> ${std.restV.good}V`, badStr: `< ${std.restV.bad}V`,
                eval: evaluate(m.restingV, std.restV.good, std.restV.bad, 'higher_is_better')
            },
            {
                name: "暗電流状態<br>(夜間電圧降下)",
                val: m.leakageDrop, unit: "V/日",
                goodStr: `< ${std.dropV.good}V`, badStr: `> ${std.dropV.bad}V`,
                eval: evaluate(m.leakageDrop, std.dropV.good, std.dropV.bad, 'lower_is_better')
            },
            {
                name: "発電システム(平均)",
                val: m.avgChargeV, unit: "V",
                goodStr: `${std.chargeV.goodMin} - ${std.chargeV.goodMax}V`, badStr: `< ${std.chargeV.badMin}V`,
                eval: evaluate(m.avgChargeV, [std.chargeV.goodMin, std.chargeV.goodMax], std.chargeV.badMin, 'range')
            },
            {
                name: "始動最低電圧(平均)",
                val: m.minCrankV, unit: "V",
                goodStr: `> ${std.crankV.good}V`, badStr: `< ${std.crankV.bad}V`,
                eval: evaluate(m.minCrankV, std.crankV.good, std.crankV.bad, 'higher_is_better')
            }
        ];

        items.forEach(i => {
            let valStr = i.val !== null ? `<strong style="font-size:18px;">${i.val}</strong> <span style="font-size:12px;color:#8b949e;">${i.unit}</span>` : "-";
            let tr = `<tr>
                <td>${i.name}</td>
                <td>${valStr}</td>
                <td style="color:#8b949e;">${i.goodStr}</td>
                <td style="color:#8b949e;">${i.badStr}</td>
                <td class="${i.eval.class}">${i.eval.text}</td>
            </tr>`;
            tbody.innerHTML += tr;
        });

        let diagnosis = "";
        if (m.restingV === null && m.avgChargeV === null && m.minCrankV === null) {
            diagnosis = "総合評価に必要なデータが不足しています。対応するファイルがアップロードされているか確認してください。";
        } else {
            let issues = [];
            let warnings = [];
            let goodPoints = [];

            if (m.restingV !== null) {
                if (m.restingV < std.restV.bad) {
                    if (bType === 'lifepo4') {
                        issues.push(`<strong>[蓄電異常]</strong> 静止電圧 (${m.restingV}V) が低すぎます。セルが劣化して容量が低下している（内部抵抗が大きすぎる）か、車両が長期間短距離走行しているためBMSが効果的にバランス充電できていない可能性があります。`);
                    } else {
                        issues.push(`<strong>[蓄電異常]</strong> 静止電圧 (${m.restingV}V) が低すぎます。バッテリー極板が劣化している（サルフェーション）ために蓄電能力が低下しているか、車両が長期間短距離走行しているために慢性的に充電不足になっている可能性があります。`);
                    }
                } else if (m.restingV < std.restV.good) {
                    if (bType === 'lifepo4') {
                        warnings.push(`<strong>[蓄電やや弱い]</strong> 静止電圧 (${m.restingV}V) が最適な状態に達していません。BMSのアクティブセルバランス機能をトリガーするために、一度長距離走行を行うか、専用充電器でバッテリーを満充電することをお勧めします。`);
                    } else {
                        warnings.push(`<strong>[蓄電やや弱い]</strong> 静止電圧 (${m.restingV}V) が最適な状態に達していません。一度長距離高速走行を行うか、外部充電器で深部メンテナンス充電を行い、極板を活性化することをお勧めします。`);
                    }
                } else {
                    goodPoints.push(`静止電圧は (${m.restingV}V) を維持しており、バッテリーの蓄電能力は優良です。`);
                }
            }

            if (m.leakageDrop !== null) {
                const dropVal = parseFloat(m.leakageDrop);
                const dStd = std.dropV;

                if (dropVal > dStd.bad) {
                    issues.push(`<strong>[漏電警告]</strong> 日次電圧降下 (${dropVal}V/日) が高すぎます。ドライブレコーダーの駐車監視機能やOBD2機器を確認してください。`);
                } else if (dropVal > dStd.good) {
                    warnings.push(`<strong>[軽微な漏電]</strong> 日次電圧降下 (${dropVal}V/日) がやや高めです。長時間駐車する場合はバッテリー残量に注意が必要です。`);
                } else if (dropVal <= dStd.excellent) {
                    goodPoints.push(`日次電圧降下はわずか (${dropVal}V/日) で、電装系に全く漏電がなく、休眠状態は非常に完璧です！`);
                } else {
                    goodPoints.push(`静止時の電圧降下 (${dropVal}V/日) は良好で、健康基準を満たしています。`);
                }
            }

            if (m.avgChargeV !== null) {
                if (m.avgChargeV < std.chargeV.badMin || m.avgChargeV > 15.0) {
                    issues.push(`<strong>[発電異常]</strong> 走行平均電圧 (${m.avgChargeV}V) が健康範囲外です。低すぎる場合は、発電機の劣化、カーボンブラシの摩耗、またはベルトの滑りが考えられます。異常に高すぎる場合（15V超）は、発電機レギュレーターの故障の可能性があります！`);
                } else if (m.avgChargeV < std.chargeV.goodMin) {
                    warnings.push(`<strong>[発電やや低め]</strong> 走行平均電圧 (${m.avgChargeV}V) が低めです。<strong>注：</strong>「充電制御システム (AMS)」が搭載されている場合、これは正常な省エネ現象です。搭載されていない場合は、発電機効率の低下に注意が必要です。`);
                } else {
                    goodPoints.push(`発電システムは正常に動作しており、走行平均電圧は安定して (${m.avgChargeV}V) を維持し、発電性能は優良です。`);
                }
            }

            if (m.minCrankV !== null) {
                if (m.minCrankV < std.crankV.bad) {
                    issues.push(`<strong>[始動重負荷]</strong> 始動瞬時の最低電圧 (${m.minCrankV}V) が低すぎます。通常はバッテリー内部抵抗の増大、瞬間放電能力の低下が原因です。バッテリーが新品の場合は、スターターモーターの劣化による重負荷、またはマイナスアースの接触不良を確認してください。`);
                } else if (m.minCrankV < std.crankV.good) {
                    warnings.push(`<strong>[始動やや弱い]</strong> 始動瞬時電圧 (${m.minCrankV}V) が低めです。危険値には達していませんが、低温環境下では始動の遅れが発生する可能性があります。`);
                } else {
                    goodPoints.push(`始動瞬時の電圧降下は極めて小さく (端子電圧はまだ ${m.minCrankV}V と高い)、バッテリーの内部抵抗が非常に低く、大電流放電能力が強いことを示しています。`);
                }
            }

            if (issues.length > 0) {
                diagnosis += `<h4 style="color: #f85149; margin-top: 0;">🚨 高リスクの異常が発見されました。専門業者での点検をお勧めします：</h4><ul style="margin-top: 5px;">`;
                issues.forEach(issue => diagnosis += `<li>${issue}</li>`);
                diagnosis += `</ul>`;
            }
            
            if (warnings.length > 0) {
                diagnosis += `<h4 style="color: #d29922;">⚠️ 継続的な観察またはメンテナンスが必要な項目：</h4><ul style="margin-top: 5px;">`;
                warnings.forEach(warn => diagnosis += `<li>${warn}</li>`);
                diagnosis += `</ul>`;
            }

            if (issues.length === 0 && warnings.length === 0) {
                 diagnosis = `<h4 style="color: #3fb950; margin-top: 0;">✅ システムは非常に健康です！</h4>`;
                 diagnosis += `<p>複数日のデータ分析の結果、お客様の車両電力システムは優れた性能を発揮しています：</p><ul>`;
                 goodPoints.forEach(pt => diagnosis += `<li>${pt}</li>`);
                 diagnosis += `</ul>`;
                 if (bType === 'lifepo4') {
                     diagnosis += `<p style="color: #58a6ff; font-size: 14px; margin-top: 10px;">💡 <strong>技術解説：</strong> お客様のリン酸鉄リチウムバッテリーは、非常に低い自己放電率と強力な瞬間放電能力を発揮し、現在の車両使用環境に完璧に対応しています。</p>`;
                 }
            } else if (goodPoints.length > 0) {
                 diagnosis += `<h4 style="color: #3fb950;">✅ 良好なパフォーマンス項目：</h4><ul style="margin-top: 5px;">`;
                 goodPoints.forEach(pt => diagnosis += `<li>${pt}</li>`);
                 diagnosis += `</ul>`;
            }
        }
        document.getElementById('aiDiagnosis').innerHTML = diagnosis;
    }
</script>