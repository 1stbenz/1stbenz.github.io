---
layout: post
title: "車輛電力系統綜合健康檢查：BM6長期數據分析"
lang: zh-Hant
date: 2026-04-14 09:52:00
categories: Auto
tags: [汽車電池, 鋰鐵電池, 鉛酸電池, 發電機診斷, 數據分析, 暗電流, 啟動電壓]
description: "如何科學地判斷電池是否該換了？本文介紹一套車輛電力系統健康檢查系統，透過分析 1Hz 監控數據與 100Hz 高頻啟動紀錄，深度評估靜置漏電、行駛發電效率及啟動瞬間的爆發力。"
keywords: "電池健康度, 鋰鐵電池, LiFePO4, 鉛酸電池, 暗電流測試, 啟動電壓, 發電機檢測, 藍牙日誌分析, 車用電力"
image: /images/battery-health-report-analysis.webp
faq:
  - question: "這套系統主要檢測哪些關鍵指標？"
    answer: "系統針對四項核心指標進行評估：1. 蓄電健康度（靜置電壓）、2. 暗電流狀態（夜間壓降）、3. 發電系統（平均行駛電壓）、4. 啟動爆發力（啟動最低電壓）。"
  - question: "鋰鐵電池與鉛酸電池的判斷標準有何不同？"
    answer: "系統設有雙重基準。例如，鋰鐵電池（LiFePO4）的優良靜置電壓需大於 13.2V，而一般鉛酸電池則為 12.5V；啟動瞬時電壓部分，鋰鐵標準為 11.5V，鉛酸則為 10.5V。"
  - question: "如何判斷車輛是否存在漏電（暗電流）？"
    answer: "系統透過長時間靜置紀錄計算「每日壓降（V/日）」。若壓降大於 0.3V（鋰鐵）或 0.4V（鉛酸），則判定為漏電過高，建議檢查行車紀錄器、防盜器或 OBD2 設備是否未正確休眠。"
  - question: "為什麼需要 100Hz 的數據來分析啟動電壓？"
    answer: "引擎啟動瞬間僅持續不到一秒，標準 1Hz（每秒一次）的紀錄容易錯過電壓最低點。透過 100Hz 高頻採樣，能精準捕捉啟動馬達運轉時的壓降，判斷電芯內阻是否增加或啟動馬達是否老化。"
  - question: "發電機異常的判定依據是什麼？"
    answer: "系統會過濾引擎發動後的數據，若行駛平均電壓低於 13.5V（或高於 15.0V），則視為發電機老化或調節器故障。對於具備充電制御系統（AMS）的車輛，系統也會針對節能模式下的低電壓進行特別註解。"
  - question: "鋰鐵電池在報告中顯示「蓄電偏弱」時該怎麼辦？"
    answer: "鋰鐵電池若靜置電壓未達 13.2V，建議進行長途行駛或使用專用充電器充飽，以觸發 BMS 的主動電芯均衡功能，確保電池壽命與效能。"
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
    <h1>車輛電力系統健康檢查報告系統</h1>

    <div class="control-panel">
        <div class="file-input-group">
            <label>📁 1. 離線長時間紀錄 (評估靜置漏電)</label>
            <input type="file" id="fileOffline" accept=".xls,.xlsx,.csv">
            <span class="file-hint">支援匯出之 Excel 試算表格式</span>
        </div>
        <div class="file-input-group">
            <label>📁 2. 原始藍牙日誌 (評估發電與啟動)</label>
            <input type="file" id="fileRaw" accept=".txt,.log" multiple>
            <span class="file-hint">可多選。自動解析多日份的 1Hz 與 100Hz 混合封包</span>
        </div>
        <div class="file-input-group">
            <label>⚙️ 電池化學材料設定</label>
            <select id="batteryType">
                <option value="lifepo4">鋰鐵電池 (LiFePO4) </option>
                <option value="leadacid">一般鉛酸電池 (Lead-Acid)</option>
            </select>
        </div>
    </div>
    
    <button class="btn-generate" onclick="generateReport()">產出綜合健康報告</button>

    <div class="report-section" id="reportSection">
        <div class="patient-info">
            <span id="reportDate">報告日期：YYYY/MM/DD</span>
            <span id="reportConfig">分析設定：鋰鐵電池基準</span>
        </div>

        <table id="reportTable">
            <thead>
                <tr>
                    <th width="20%">檢查項目</th>
                    <th width="20%">當前數據</th>
                    <th width="20%">良好標準</th>
                    <th width="20%">異常標準</th>
                    <th width="20%">綜合判定</th>
                </tr>
            </thead>
            <tbody id="tableBody">
            </tbody>
        </table>

        <div class="doctor-notes">
            <h3 style="margin-top:0; color:#58a6ff;">📋 系統綜合診斷建議</h3>
            <div id="aiDiagnosis">請上傳資料以取得綜合分析。</div>
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
        btn.innerText = "資料分析中...";
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

        btn.innerText = "產出綜合健康報告";
        btn.disabled = false;
        document.getElementById('reportSection').style.display = 'block';
    }

    function evaluate(value, goodRule, badRule, type) {
        if (value === null) return { text: "未提供資料", class: "status-none" };
        let v = parseFloat(value);
        if (type === 'higher_is_better') {
            if (v >= goodRule) return { text: "優良", class: "status-good" };
            if (v <= badRule) return { text: "需檢修", class: "status-bad" };
            return { text: "尚可", class: "status-warn" };
        } else if (type === 'lower_is_better') {
            if (v <= goodRule) return { text: "優良", class: "status-good" };
            if (v >= badRule) return { text: "漏電過高", class: "status-bad" };
            return { text: "偏高", class: "status-warn" };
        } else if (type === 'range') {
            if (v >= goodRule[0] && v <= goodRule[1]) return { text: "發電健康", class: "status-good" };
            if (v < badRule || v > 15.0) return { text: "發電機異常", class: "status-bad" };
            return { text: "充電偏弱", class: "status-warn" };
        }
    }

    function renderTable(m, std, bType) {
        document.getElementById('reportDate').innerText = `報告生成時間：${new Date().toLocaleString()}`;
        document.getElementById('reportConfig').innerText = `分析設定：${bType === 'lifepo4' ? '鋰鐵電池' : '一般鉛酸電池'}`;

        const tbody = document.getElementById('tableBody');
        tbody.innerHTML = "";

        const items = [
            {
                name: "蓄電健康度<br>(靜置電壓)",
                val: m.restingV, unit: "V",
                goodStr: `> ${std.restV.good}V`, badStr: `< ${std.restV.bad}V`,
                eval: evaluate(m.restingV, std.restV.good, std.restV.bad, 'higher_is_better')
            },
            {
                name: "暗電流狀態<br>(夜間壓降)",
                val: m.leakageDrop, unit: "V/日",
                goodStr: `< ${std.dropV.good}V`, badStr: `> ${std.dropV.bad}V`,
                eval: evaluate(m.leakageDrop, std.dropV.good, std.dropV.bad, 'lower_is_better')
            },
            {
                name: "發電系統(Avg.)",
                val: m.avgChargeV, unit: "V",
                goodStr: `${std.chargeV.goodMin} - ${std.chargeV.goodMax}V`, badStr: `< ${std.chargeV.badMin}V`,
                eval: evaluate(m.avgChargeV, [std.chargeV.goodMin, std.chargeV.goodMax], std.chargeV.badMin, 'range')
            },
            {
                name: "啟動最低電壓(Avg.)",
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
            diagnosis = "無足夠數據進行綜合評估。請確認已上傳相對應的檔案。";
        } else {
            let issues = [];
            let warnings = [];
            let goodPoints = [];

            if (m.restingV !== null) {
                if (m.restingV < std.restV.bad) {
                    if (bType === 'lifepo4') {
                        issues.push(`<strong>[蓄電異常]</strong> 靜置電壓 (${m.restingV}V) 過低。電芯可能已老化導致容量衰退（內阻過大），或車輛長期短途行駛導致 BMS 無法有效均衡充飽。`);
                    } else {
                        issues.push(`<strong>[蓄電異常]</strong> 靜置電壓 (${m.restingV}V) 過低。電池極板可能已老化（硫化）導致蓄電能力下降，或車輛長期短途行駛導致慢性充不飽。`);
                    }
                } else if (m.restingV < std.restV.good) {
                    if (bType === 'lifepo4') {
                        warnings.push(`<strong>[蓄電偏弱]</strong> 靜置電壓 (${m.restingV}V) 未達最佳狀態。建議安排一次長途行駛或使用專用充電器將電池充飽，以觸發 BMS 主動電芯均衡功能。`);
                    } else {
                        warnings.push(`<strong>[蓄電偏弱]</strong> 靜置電壓 (${m.restingV}V) 未達最佳狀態。建議安排一次長途高速行駛，或使用外部充電器進行深度保養充電以活化極板。`);
                    }
                } else {
                    goodPoints.push(`靜置電壓維持在 (${m.restingV}V) ，電池蓄電能力優良。`);
                }
            }

            if (m.leakageDrop !== null) {
                const dropVal = parseFloat(m.leakageDrop);
                const dStd = std.dropV;

                if (dropVal > dStd.bad) {
                    issues.push(`<strong>[漏電警告]</strong> 每日壓降 (${dropVal}V/日) 過高。請檢查行車紀錄器停車監控或 OBD2 設備。`);
                } else if (dropVal > dStd.good) {
                    warnings.push(`<strong>[輕微漏電]</strong> 每日壓降 (${dropVal}V/日) 略高，若長時間停放需注意電量。`);
                } else if (dropVal <= dStd.excellent) {
                    goodPoints.push(`每日壓降僅 (${dropVal}V/日)，電系完全無漏電，休眠狀態非常完美！`);
                } else {
                    goodPoints.push(`靜置壓降 (${dropVal}V/日) 表現良好，符合健康標準。`);
                }
            }

            if (m.avgChargeV !== null) {
                if (m.avgChargeV < std.chargeV.badMin || m.avgChargeV > 15.0) {
                    issues.push(`<strong>[發電異常]</strong> 行駛平均電壓 (${m.avgChargeV}V) 不在健康範圍。若偏低，可能是發電機老化、碳刷磨損或皮帶打滑；若異常偏高 (大於15V)，則發電機調節器可能故障！`);
                } else if (m.avgChargeV < std.chargeV.goodMin) {
                    warnings.push(`<strong>[發電偏低]</strong> 行駛平均電壓 (${m.avgChargeV}V) 偏低。<strong>註：</strong>若配備「充電制御系統 (AMS)」，此為正常節能現象；若無，則需留意發電機效率是否衰退。`);
                } else {
                    goodPoints.push(`發電系統運作正常，行駛平均電壓穩定維持在 (${m.avgChargeV}V) ，發電效能優良。`);
                }
            }

            if (m.minCrankV !== null) {
                if (m.minCrankV < std.crankV.bad) {
                    issues.push(`<strong>[啟動重拖]</strong> 啟動瞬間最低電壓 (${m.minCrankV}V) 過低。通常是電池內阻變大、瞬間放電衰退；若電池為新品，請檢查啟動馬達是否老化重拖，或負極搭鐵接觸不良。`);
                } else if (m.minCrankV < std.crankV.good) {
                    warnings.push(`<strong>[啟動偏弱]</strong> 啟動瞬間電壓 (${m.minCrankV}V) 偏低。尚未達到危險值，但低溫環境下可能會出現啟動遲滯。`);
                } else {
                    goodPoints.push(`啟動瞬間的壓降極小 (端電壓仍高達 ${m.minCrankV}V) 充足，顯示電池內阻極低、大電流放電能力強。`);
                }
            }

            if (issues.length > 0) {
                diagnosis += `<h4 style="color: #f85149; margin-top: 0;">🚨 發現高風險異常，建議進廠檢修：</h4><ul style="margin-top: 5px;">`;
                issues.forEach(issue => diagnosis += `<li>${issue}</li>`);
                diagnosis += `</ul>`;
            }
            
            if (warnings.length > 0) {
                diagnosis += `<h4 style="color: #d29922;">⚠️ 需持續觀察或保養項目：</h4><ul style="margin-top: 5px;">`;
                warnings.forEach(warn => diagnosis += `<li>${warn}</li>`);
                diagnosis += `</ul>`;
            }

            if (issues.length === 0 && warnings.length === 0) {
                 diagnosis = `<h4 style="color: #3fb950; margin-top: 0;">✅ 系統非常健康！</h4>`;
                 diagnosis += `<p>綜合多日的數據分析，您的車輛電力系統表現優異：</p><ul>`;
                 goodPoints.forEach(pt => diagnosis += `<li>${pt}</li>`);
                 diagnosis += `</ul>`;
                 if (bType === 'lifepo4') {
                     diagnosis += `<p style="color: #58a6ff; font-size: 14px; margin-top: 10px;">💡 <strong>技術註解：</strong> 您的鋰鐵電池特性發揮良好，擁有極低的自放電率與強大的瞬間放電能力，完美應對目前的用車環境。</p>`;
                 }
            } else if (goodPoints.length > 0) {
                 diagnosis += `<h4 style="color: #3fb950;">✅ 表現良好項目：</h4><ul style="margin-top: 5px;">`;
                 goodPoints.forEach(pt => diagnosis += `<li>${pt}</li>`);
                 diagnosis += `</ul>`;
            }
        }
        document.getElementById('aiDiagnosis').innerHTML = diagnosis;
    }
</script>
