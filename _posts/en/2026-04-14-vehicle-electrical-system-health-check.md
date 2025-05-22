---
layout: post
title: "Comprehensive Vehicle Electrical System Health Check: BM6 Long-term Data Analysis"
lang: en
date: 2026-04-14 09:52:00
categories: Auto
tags: [Car Battery, LiFePO4 Battery, Lead-Acid Battery, Alternator Diagnostics, Data Analysis, Dark Current, Cranking Voltage]
description: "How to scientifically determine if it's time to replace your battery? This article introduces a vehicle electrical system health check system. By analyzing 1Hz monitoring data and 100Hz high-frequency cranking logs, it deeply evaluates resting leakage, driving alternator efficiency, and instantaneous cranking power."
keywords: "Battery Health, LiFePO4, Lead-Acid Battery, Dark Current Test, Cranking Voltage, Alternator Check, Bluetooth Log Analysis, Vehicle Power"
image: /images/battery-health-report-analysis.webp
faq:
  - question: "What key metrics does this system test?"
    answer: "The system evaluates four core metrics: 1. Storage Health (Resting Voltage), 2. Dark Current Status (Overnight Voltage Drop), 3. Charging System (Average Driving Voltage), 4. Cranking Power (Minimum Cranking Voltage)."
  - question: "What is the difference in evaluation criteria between LiFePO4 and lead-acid batteries?"
    answer: "The system uses dual baselines. For example, a good resting voltage for a LiFePO4 battery is >13.2V, whereas for a lead-acid battery it is 12.5V. For instantaneous cranking voltage, the LiFePO4 standard is 11.5V, and lead-acid is 10.5V."
  - question: "How to determine if there is a current leak (dark current) in the vehicle?"
    answer: "The system calculates the 'daily voltage drop (V/day)' through long-term resting logs. If the drop is >0.3V (LiFePO4) or >0.4V (Lead-Acid), it is determined as high leakage. It's recommended to check if dashcams, aftermarket alarms, or OBD2 devices are failing to sleep properly."
  - question: "Why is 100Hz data needed to analyze cranking voltage?"
    answer: "Engine cranking lasts less than a second. A standard 1Hz (once per second) log easily misses the lowest voltage point. Through 100Hz high-frequency sampling, it accurately captures the voltage drop during starter motor operation to determine if cell internal resistance has increased or if the starter motor is aging."
  - question: "What is the basis for determining alternator abnormalities?"
    answer: "The system filters data after the engine starts. If the average driving voltage is below 13.5V (or above 15.0V), it's considered alternator aging or regulator failure. For vehicles with an Alternator Management System (AMS), the system also provides special notes for low voltages under eco modes."
  - question: "What should I do if the report shows 'Weak Storage' for a LiFePO4 battery?"
    answer: "If the resting voltage of a LiFePO4 battery is below 13.2V, it's recommended to take a long drive or use a dedicated charger to fully charge it. This triggers the BMS's active cell balancing function to ensure battery life and performance."
---

<script src="https://cdn.jsdelivr.net/npm/xlsx/dist/xlsx.full.min.js"></script>

<style>
    /* Styles applied only to elements in this page */
    .app-container {
        font-family: 'Segoe UI', sans-serif;
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
    <h1>Vehicle Electrical System Health Report System</h1>

    <div class="control-panel">
        <div class="file-input-group">
            <label>📁 1. Offline Long-term Records (Leakage Evaluation)</label>
            <input type="file" id="fileOffline" accept=".xls,.xlsx,.csv">
            <span class="file-hint">Supports exported Excel spreadsheet formats</span>
        </div>
        <div class="file-input-group">
            <label>📁 2. Raw Bluetooth Logs (Generation & Cranking)</label>
            <input type="file" id="fileRaw" accept=".txt,.log" multiple>
            <span class="file-hint">Multi-select allowed. Auto-parses 1Hz & 100Hz packets</span>
        </div>
        <div class="file-input-group">
            <label>⚙️ Battery Chemistry Setting</label>
            <select id="batteryType">
                <option value="lifepo4">Lithium Iron Phosphate (LiFePO4) </option>
                <option value="leadacid">Standard Lead-Acid</option>
            </select>
        </div>
    </div>
    
    <button class="btn-generate" onclick="generateReport()">Generate Comprehensive Health Report</button>

    <div class="report-section" id="reportSection">
        <div class="patient-info">
            <span id="reportDate">Report Date: YYYY/MM/DD</span>
            <span id="reportConfig">Settings: LiFePO4 Standard</span>
        </div>

        <table id="reportTable">
            <thead>
                <tr>
                    <th width="20%">Check Item</th>
                    <th width="20%">Current Data</th>
                    <th width="20%">Good Standard</th>
                    <th width="20%">Abnormal Standard</th>
                    <th width="20%">Verdict</th>
                </tr>
            </thead>
            <tbody id="tableBody">
            </tbody>
        </table>

        <div class="doctor-notes">
            <h3 style="margin-top:0; color:#58a6ff;">📋 System Comprehensive Diagnosis</h3>
            <div id="aiDiagnosis">Please upload data to obtain a comprehensive analysis.</div>
        </div>
    </div>
</div>

<script>
    const thresholds = {
        lifepo4: {
            restV: { good: 13.2, bad: 13.0, unit: 'V' },
            dropV: { excellent: 0.01, good: 0.02, bad: 0.05, unit: 'V/Day' },
            chargeV: { goodMin: 13.8, goodMax: 14.4, badMin: 13.5, unit: 'V' },
            crankV: { good: 11.5, bad: 10.0, unit: 'V' }
        },
        leadacid: {
            restV: { good: 12.5, bad: 12.0, unit: 'V' },
            dropV: { good: 0.15, bad: 0.4, unit: 'V/Day' },
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

                    const allVoltages = json.slice(1)
                        .map(row => parseFloat(row[1]))
                        .filter(v => !isNaN(v) && v > 5.0 && v < 16.0);

                    if (allVoltages.length < 20) {
                        resolve({ rest: null, drop: null });
                        return;
                    }

                    const filterThreshold = (bType === 'lifepo4') ? 13.6 : 13.2;
                    const stableStartV = (bType === 'lifepo4') ? 13.3 : 12.7;

                    const sortedV = [...allVoltages].sort((a, b) => a - b);
                    const restV = sortedV[Math.floor(sortedV.length * 0.05)];

                    const staticVs = allVoltages.filter(v => v < filterThreshold);

                    if (staticVs.length < 10) {
                        resolve({ rest: restV.toFixed(2), drop: 0 });
                        return;
                    }

                    let startIndex = staticVs.findIndex(v => v <= stableStartV);
                    
                    if (startIndex === -1 || (staticVs.length - startIndex) < 10) {
                        startIndex = 0;
                    }

                    const endIndex = staticVs.length - 1;

                    const headRange = staticVs.slice(startIndex, startIndex + 5);
                    const tailRange = staticVs.slice(-5);
                    
                    const avgFirstV = headRange.reduce((a, b) => a + b, 0) / headRange.length;
                    const avgLastV = tailRange.reduce((a, b) => a + b, 0) / tailRange.length;

                    const effectivePoints = endIndex - startIndex;
                    const totalDays = (effectivePoints > 0) ? (effectivePoints * 2) / 1440 : (allVoltages.length * 2) / 1440; 

                    let realDrop = (avgFirstV - avgLastV) / totalDays;

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
        btn.innerText = "Analyzing data...";
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

        btn.innerText = "Generate Comprehensive Health Report";
        btn.disabled = false;
        document.getElementById('reportSection').style.display = 'block';
    }

    function evaluate(value, goodRule, badRule, type) {
        if (value === null) return { text: "No data provided", class: "status-none" };
        let v = parseFloat(value);
        if (type === 'higher_is_better') {
            if (v >= goodRule) return { text: "Excellent", class: "status-good" };
            if (v <= badRule) return { text: "Repair Required", class: "status-bad" };
            return { text: "Fair", class: "status-warn" };
        } else if (type === 'lower_is_better') {
            if (v <= goodRule) return { text: "Excellent", class: "status-good" };
            if (v >= badRule) return { text: "High Leakage", class: "status-bad" };
            return { text: "Slightly High", class: "status-warn" };
        } else if (type === 'range') {
            if (v >= goodRule[0] && v <= goodRule[1]) return { text: "Charging Healthy", class: "status-good" };
            if (v < badRule || v > 15.0) return { text: "Alternator Abnormal", class: "status-bad" };
            return { text: "Charging Weak", class: "status-warn" };
        }
    }

    function renderTable(m, std, bType) {
        document.getElementById('reportDate').innerText = `Report generated at: ${new Date().toLocaleString()}`;
        document.getElementById('reportConfig').innerText = `Settings: ${bType === 'lifepo4' ? 'LiFePO4' : 'Standard Lead-Acid'}`;

        const tbody = document.getElementById('tableBody');
        tbody.innerHTML = "";

        const items = [
            {
                name: "Storage Health<br>(Static Voltage)",
                val: m.restingV, unit: "V",
                goodStr: `> ${std.restV.good}V`, badStr: `< ${std.restV.bad}V`,
                eval: evaluate(m.restingV, std.restV.good, std.restV.bad, 'higher_is_better')
            },
            {
                name: "Dark Current Status<br>(Daily Drop)",
                val: m.leakageDrop, unit: "V/Day",
                goodStr: `< ${std.dropV.good}V`, badStr: `> ${std.dropV.bad}V`,
                eval: evaluate(m.leakageDrop, std.dropV.good, std.dropV.bad, 'lower_is_better')
            },
            {
                name: "Charging System (Avg.)",
                val: m.avgChargeV, unit: "V",
                goodStr: `${std.chargeV.goodMin} - ${std.chargeV.goodMax}V`, badStr: `< ${std.chargeV.badMin}V`,
                eval: evaluate(m.avgChargeV, [std.chargeV.goodMin, std.chargeV.goodMax], std.chargeV.badMin, 'range')
            },
            {
                name: "Min Cranking Voltage (Avg.)",
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
            diagnosis = "Insufficient data for a comprehensive evaluation. Please ensure corresponding files are uploaded.";
        } else {
            let issues = [];
            let warnings = [];
            let goodPoints = [];

            if (m.restingV !== null) {
                if (m.restingV < std.restV.bad) {
                    if (bType === 'lifepo4') {
                        issues.push(`<strong>[Storage Abnormal]</strong> Static voltage (${m.restingV}V) is too low. The cells may be aging (high internal resistance), or the vehicle is driven too infrequently for the BMS to balance and charge correctly.`);
                    } else {
                        issues.push(`<strong>[Storage Abnormal]</strong> Static voltage (${m.restingV}V) is too low. The plates may be aging (sulfation), leading to decreased capacity, or the battery is chronically undercharged.`);
                    }
                } else if (m.restingV < std.restV.good) {
                    if (bType === 'lifepo4') {
                        warnings.push(`<strong>[Storage Weak]</strong> Static voltage (${m.restingV}V) is not optimal. Suggest a long trip or using a dedicated charger to reach full charge and trigger BMS balancing.`);
                    } else {
                        warnings.push(`<strong>[Storage Weak]</strong> Static voltage (${m.restingV}V) is not optimal. Suggest a long highway drive or using an external charger for deep maintenance to activate the plates.`);
                    }
                } else {
                    goodPoints.push(`Static voltage remains at (${m.restingV}V), battery storage capacity is excellent.`);
                }
            }

            if (m.leakageDrop !== null) {
                const dropVal = parseFloat(m.leakageDrop);
                const dStd = std.dropV;

                if (dropVal > dStd.bad) {
                    issues.push(`<strong>[Leakage Warning]</strong> Daily voltage drop (${dropVal}V/Day) is too high. Check dashcam parking mode or OBD2 devices.`);
                } else if (dropVal > dStd.good) {
                    warnings.push(`<strong>[Minor Leakage]</strong> Daily voltage drop (${dropVal}V/Day) is slightly high. Be cautious if parking for long periods.`);
                } else if (dropVal <= dStd.excellent) {
                    goodPoints.push(`Daily drop is only (${dropVal}V/Day). No leakage detected; sleep mode is perfect!`);
                } else {
                    goodPoints.push(`Static voltage drop (${dropVal}V/Day) is within healthy standards.`);
                }
            }

            if (m.avgChargeV !== null) {
                if (m.avgChargeV < std.chargeV.badMin || m.avgChargeV > 15.0) {
                    issues.push(`<strong>[Alternator Abnormal]</strong> Avg. driving voltage (${m.avgChargeV}V) is out of health range. If low, could be alternator wear or belt slippage; if over 15V, the regulator might be failing!`);
                } else if (m.avgChargeV < std.chargeV.goodMin) {
                    warnings.push(`<strong>[Charging Low]</strong> Avg. driving voltage (${m.avgChargeV}V) is low. <strong>Note:</strong> If equipped with AMS, this might be normal energy-saving behavior; if not, monitor alternator efficiency.`);
                } else {
                    goodPoints.push(`Charging system is normal. Avg. driving voltage is stable at (${m.avgChargeV}V).`);
                }
            }

            if (m.minCrankV !== null) {
                if (m.minCrankV < std.crankV.bad) {
                    issues.push(`<strong>[Cranking Heavy]</strong> Minimum cranking voltage (${m.minCrankV}V) is too low. Usually indicates high battery internal resistance; if the battery is new, check for starter motor aging or poor ground connections.`);
                } else if (m.minCrankV < std.crankV.good) {
                    warnings.push(`<strong>[Cranking Weak]</strong> Startup voltage (${m.minCrankV}V) is low. Not critical yet, but startup delays may occur in cold weather.`);
                } else {
                    goodPoints.push(`Startup voltage dip is minimal (${m.minCrankV}V remains), indicating low internal resistance and strong discharge capability.`);
                }
            }

            if (issues.length > 0) {
                diagnosis += `<h4 style="color: #f85149; margin-top: 0;">🚨 High-risk abnormalities found, inspection recommended:</h4><ul style="margin-top: 5px;">`;
                issues.forEach(issue => diagnosis += `<li>${issue}</li>`);
                diagnosis += `</ul>`;
            }
            
            if (warnings.length > 0) {
                diagnosis += `<h4 style="color: #d29922;">⚠️ Items requiring monitoring or maintenance:</h4><ul style="margin-top: 5px;">`;
                warnings.forEach(warn => diagnosis += `<li>${warn}</li>`);
                diagnosis += `</ul>`;
            }

            if (issues.length === 0 && warnings.length === 0) {
                 diagnosis = `<h4 style="color: #3fb950; margin-top: 0;">✅ System is very healthy!</h4>`;
                 diagnosis += `<p>Based on multi-day data analysis, your vehicle electrical system performs excellently:</p><ul>`;
                 goodPoints.forEach(pt => diagnosis += `<li>${pt}</li>`);
                 diagnosis += `</ul>`;
                 if (bType === 'lifepo4') {
                     diagnosis += `<p style="color: #58a6ff; font-size: 14px; margin-top: 10px;">💡 <strong>Technical Note:</strong> Your LiFePO4 battery characteristics are well-utilized, showing extremely low self-discharge and powerful burst capability.</p>`;
                 }
            } else if (goodPoints.length > 0) {
                 diagnosis += `<h4 style="color: #3fb950;">✅ Healthy Items:</h4><ul style="margin-top: 5px;">`;
                 goodPoints.forEach(pt => diagnosis += `<li>${pt}</li>`);
                 diagnosis += `</ul>`;
            }
        }
        document.getElementById('aiDiagnosis').innerHTML = diagnosis;
    }
</script>