---
layout: post
title: "الفحص الشامل لصحة المنظومة الكهربائية للمركبة: تحليل بيانات BM6 طويلة الأمد"
lang: ar
date: 2026-04-14 09:52:00
categories: Auto
tags: [بطارية السيارة, مراقب البطارية, معلومات السيارات]
description: "كيف تحدد علمياً الوقت المناسب لاستبدال البطارية؟ يقدم هذا المقال نظام فحص صحة المنظومة الكهربائية للسيارة. من خلال دمج بيانات المراقبة اللحظية 1 هرتز وسجلات بدء التشغيل عالية التردد 100 هرتز، يقيم النظام تيار التسريب، كفاءة شحن الدينامو، وقوة تدوير السلف."
keywords: "صحة البطارية, LiFePO4, بطارية رصاص حمضية, فحص تيار التسريب, جهد بدء التشغيل, فحص الدينامو, تحليل سجلات البلوتوث, كهرباء السيارة"
image: /images/battery-health-report-analysis.webp
faq:
  - question: "ما هي المؤشرات الحيوية التي يختبرها هذا النظام؟"
    answer: "يقيم النظام أربعة معايير محورية: 1. صحة تخزين الطاقة (جهد الاستقرار الساكن)، 2. تيار التسريب الطفيلي (معدل هبوط الجهد اليومي)، 3. كفاءة منظومة الشحن (متوسط جهد القيادة)، 4. قدرة بدء التشغيل (أدنى جهد عند تدوير المحرك)."
  - question: "ما هو الفارق في معايير التقييم بين بطاريات LiFePO4 وبطاريات الرصاص؟"
    answer: "يطبق النظام خطين معياريين مختلفين. على سبيل المثال، جهد الاستقرار الممتاز لبطارية LiFePO4 هو >13.2 فولت، بينما لبطارية الرصاص هو 12.5 فولت. وبالنسبة لأدنى جهد لبدء التشغيل، معيار LiFePO4 هو 11.5 فولت، والرصاص 10.5 فولت."
  - question: "كيف يكتشف النظام وجود تسريب تيار (Dark Current) في السيارة؟"
    answer: "يحسب النظام 'هبوط الجهد اليومي (فولت/يوم)' من سجلات التوقف الطويلة. فإذا تجاوز الهبوط 0.3 فولت (LiFePO4) أو 0.4 فولت (للرصاص)، يُصنف كتسريب مرتفع، ويوصى بفحص كاميرات المراقبة، أو أجهزة التتبع، أو منافذ OBD2 التي قد تعيق وضع السكون."
  - question: "لماذا تعد بيانات التردد الفائق 100 هرتز ضرورية لتحليل جهد بدء التشغيل؟"
    answer: "يستغرق تدوير المحرك أقل من ثانية. سجل 1 هرتز المعتاد يفوّت قاع الجهد الأدنى بسهولة. بينما تلتقط عينات 100 هرتز بدقة لحظة هبوط الجهد تحت عبء بادئ الحركة (السلف) لتحديد ما إذا كانت المقاومة الداخلية مرتفعة أو بادئ الحركة متقادماً."
  - question: "على أي أساس يتم تقييم أعطال المولد الكهربائي (الدينامو)؟"
    answer: "يقوم النظام بفلترة البيانات بعد بدء دوران المحرك. إذا كان متوسط جهد القيادة أقل من 13.5 فولت (أو أعلى من 15.0 فولت)، يُعتبر ذلك تقادماً في الدينامو أو خللاً في المنظم، مع مراعاة خصائص أنظمة الشحن الذكي (AMS)."
  - question: "ما الإجراء المطلوب إذا أظهر التقرير 'تخزين ضعيف' لبطارية LiFePO4؟"
    answer: "إذا هبط جهد الاستقرار الساكن لبطارية LiFePO4 دون 13.2 فولت، يوصى برحلة قيادة طويلة أو استخدام شاحن مخصص لشحنها بالكامل لتفعيل وظيفة الموازنة النشطة للخلايا داخل نظام إدارة البطارية (BMS)."
---

<script src="https://cdn.jsdelivr.net/npm/xlsx/dist/xlsx.full.min.js"></script>

<style>
    .app-container {
        font-family: 'Segoe UI', Tahoma, sans-serif;
        background: #ffffff; color: #333333; max-width: 1000px; margin: 0 auto; padding: 30px; border-radius: 12px; border: 1px solid #e5e7eb; box-shadow: 0 4px 20px rgba(0,0,0,0.06);
    }
    .app-container h1 { text-align: center; color: #04384c; margin-bottom: 25px; font-weight: 800; font-size: 24px; border: none; background: none; }
    .control-panel {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 20px;
        margin-bottom: 30px;
        background: #f8fafc;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #e2e8f0;
    }
    .file-input-group {
        display: flex;
        flex-direction: column;
        gap: 8px;
    }
    .file-input-group label { font-weight: bold; color: #04384c; font-size: 14px; }
    .app-container input[type="file"], .app-container select {
        background: #ffffff; padding: 10px; border-radius: 6px; border: 1px solid #cbd5e1; color: #333333;
    }
    .file-hint { font-size: 12px; color: #64748b; margin-top: -5px; }
    .btn-generate {
        width: 100%; padding: 15px; background: #04384c; color: white; border: none; border-radius: 8px;
        font-size: 18px; font-weight: bold; cursor: pointer; transition: 0.2s; margin-top: 10px;
    }
    .btn-generate:hover { background: #064e6b; }
    
    .report-section { display: none; margin-top: 40px; }
    .patient-info {
        display: flex; justify-content: space-between; border-bottom: 2px solid #e2e8f0;
        padding-bottom: 10px; margin-bottom: 20px; color: #64748b;
    }
    .app-container table {
        width: 100%; border-collapse: collapse; margin-bottom: 30px;
        background: #ffffff; border-radius: 8px; overflow: hidden; border: 1px solid #dcdcdc;
    }
    .app-container th, .app-container td { padding: 15px; text-align: center; border: 1px solid #dcdcdc; }
    .app-container th { background: rgba(4, 56, 76, 0.06); color: #04384c; font-weight: bold; }
    .app-container td:first-child { text-align: right; font-weight: bold; color: #04384c; }
    .app-container tr:nth-child(even) { background-color: #fafafa; }
    .app-container tr:nth-child(odd) { background-color: #ffffff; }
    .app-container tr:hover { background-color: rgba(4, 56, 76, 0.03); }
    
    .status-good { color: #3fb950; font-weight: bold; }
    .status-warn { color: #d29922; font-weight: bold; }
    .status-bad { color: #f85149; font-weight: bold; }
    .status-none { color: #8b949e; font-style: italic; }

    .doctor-notes {
        background: rgba(4, 56, 76, 0.05); padding: 20px; border-radius: 10px;
        border-right: 5px solid #04384c; line-height: 1.6; color: #334155;
    }
</style>

<div class="app-container" dir="rtl">
    <h1>نظام التقرير الشامل لصحة المنظومة الكهربائية للسيارة</h1>

    <div class="control-panel">
        <div class="file-input-group">
            <label>📁 1. سجلات التوقف طويلة الأمد (تقييم التسريب)</label>
            <input type="file" id="fileOffline" accept=".xls,.xlsx,.csv">
            <span class="file-hint">يدعم جداول بيانات Excel بصيغة (.xlsx, .xls)</span>
        </div>
        <div class="file-input-group">
            <label>📁 2. ملفات سجلات البلوتوث الخام (الشحن وبدء التشغيل)</label>
            <input type="file" id="fileRaw" accept=".txt,.log" multiple>
            <span class="file-hint">يدعم الاختيار المتعدد. يحلل بيانات 1 هرتز و 100 هرتز تلقائياً</span>
        </div>
        <div class="file-input-group">
            <label>⚙️ نوع كيمياء البطارية</label>
            <select id="batteryType">
                <option value="lifepo4">ليثيوم فوسفات الحديد (LiFePO4)</option>
                <option value="leadacid">رصاص حمضية قياسية / AGM</option>
            </select>
        </div>
    </div>
    
    <button class="btn-generate" onclick="generateReport()">إصدار التقرير الطبي الشامل</button>

    <div class="report-section" id="reportSection">
        <div class="patient-info">
            <span id="reportDate">تاريخ التقرير: YYYY/MM/DD</span>
            <span id="reportConfig">الإعدادات: معيار LiFePO4</span>
        </div>

        <table id="reportTable">
            <thead>
                <tr>
                    <th width="20%">بند الفحص</th>
                    <th width="20%">البيانات المقاسة</th>
                    <th width="20%">المعيار السليم</th>
                    <th width="20%">معيار الخلل</th>
                    <th width="20%">الحكم النهائي</th>
                </tr>
            </thead>
            <tbody id="tableBody">
            </tbody>
        </table>

        <div class="doctor-notes">
            <h3 style="margin-top:0; color:#58a6ff;">📋 التشخيص الهندسي الشامل</h3>
            <div id="aiDiagnosis">يرجى رفع الملفات للحصول على التقرير والتشخيص الدقيق.</div>
        </div>
    </div>
</div>

<script>
    const thresholds = {
        lifepo4: {
            restV: { good: 13.2, bad: 13.0, unit: 'V' },
            dropV: { excellent: 0.01, good: 0.02, bad: 0.05, unit: 'V/يوم' },
            chargeV: { goodMin: 13.8, goodMax: 14.4, badMin: 13.5, unit: 'V' },
            crankV: { good: 11.5, bad: 10.0, unit: 'V' }
        },
        leadacid: {
            restV: { good: 12.5, bad: 12.0, unit: 'V' },
            dropV: { good: 0.15, bad: 0.4, unit: 'V/يوم' },
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
        btn.innerText = "جاري التحليل والمعالجة...";
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

        btn.innerText = "إصدار التقرير الطبي الشامل";
        btn.disabled = false;
        document.getElementById('reportSection').style.display = 'block';
    }

    function evaluate(value, goodRule, badRule, type) {
        if (value === null) return { text: "لم يتم تقديم بيانات", class: "status-none" };
        let v = parseFloat(value);
        if (type === 'higher_is_better') {
            if (v >= goodRule) return { text: "ممتاز", class: "status-good" };
            if (v <= badRule) return { text: "فحص مطلوب", class: "status-bad" };
            return { text: "متوسط", class: "status-warn" };
        } else if (type === 'lower_is_better') {
            if (v <= goodRule) return { text: "ممتاز", class: "status-good" };
            if (v >= badRule) return { text: "تسريب مرتفع", class: "status-bad" };
            return { text: "تسريب طفيف", class: "status-warn" };
        } else if (type === 'range') {
            if (v >= goodRule[0] && v <= goodRule[1]) return { text: "شحن سليم", class: "status-good" };
            if (v < badRule || v > 15.0) return { text: "خلل بالدينامو", class: "status-bad" };
            return { text: "شحن ضعيف", class: "status-warn" };
        }
    }

    function renderTable(m, std, bType) {
        document.getElementById('reportDate').innerText = `تم إصدار التقرير في: ${new Date().toLocaleString()}`;
        document.getElementById('reportConfig').innerText = `الإعدادات: ${bType === 'lifepo4' ? 'معيار LiFePO4' : 'رصاص حمضية قياسية'}`;

        const tbody = document.getElementById('tableBody');
        tbody.innerHTML = "";

        const items = [
            {
                name: "صحة التخزين<br>(الجهد الساكن)",
                val: m.restingV, unit: "V",
                goodStr: `> ${std.restV.good}V`, badStr: `< ${std.restV.bad}V`,
                eval: evaluate(m.restingV, std.restV.good, std.restV.bad, 'higher_is_better')
            },
            {
                name: "تيار التسريب في السكون<br>(الهبوط اليومي)",
                val: m.leakageDrop, unit: "V/يوم",
                goodStr: `< ${std.dropV.good}V`, badStr: `> ${std.dropV.bad}V`,
                eval: evaluate(m.leakageDrop, std.dropV.good, std.dropV.bad, 'lower_is_better')
            },
            {
                name: "منظومة الشحن (المتوسط)",
                val: m.avgChargeV, unit: "V",
                goodStr: `${std.chargeV.goodMin} - ${std.chargeV.goodMax}V`, badStr: `< ${std.chargeV.badMin}V`,
                eval: evaluate(m.avgChargeV, [std.chargeV.goodMin, std.chargeV.goodMax], std.chargeV.badMin, 'range')
            },
            {
                name: "أدنى جهد تدوير (المتوسط)",
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
            diagnosis = "البيانات المقدمة غير كافية لإصدار التقييم الشامل. يرجى التأكد من رفع الملفات المطلوبة.";
        } else {
            let issues = [];
            let warnings = [];
            let goodPoints = [];

            if (m.restingV !== null) {
                if (m.restingV < std.restV.bad) {
                    if (bType === 'lifepo4') {
                        issues.push(`<strong>[تخزين غير طبيعي]</strong> الجهد الساكن (${m.restingV}V) منخفض جداً. قد تعاني الخلايا من تقادم وارتفاع في المقاومة الداخلية، أو أن السيارة لم تُقد لمسافة كافية تتيح لنظام BMS إتمام الموازنة النشطة.`);
                    } else {
                        issues.push(`<strong>[تخزين غير طبيعي]</strong> الجهد الساكن (${m.restingV}V) منخفض جداً. مؤشر على كبرتة الألواح وتراجع السعة التخزينية.`);
                    }
                } else if (m.restingV < std.restV.good) {
                    if (bType === 'lifepo4') {
                        warnings.push(`<strong>[تخزين ضعيف]</strong> الجهد الساكن (${m.restingV}V) دون المعدل المثالي. يوصى برحلة قيادة طويلة أو شحن خارجي لتحفيز موازنة الخلايا.`);
                    } else {
                        warnings.push(`<strong>[تخزين ضعيف]</strong> الجهد الساكن (${m.restingV}V) متواضع. يوصى بإجراء شحن صيانة عميق.`);
                    }
                } else {
                    goodPoints.push(`الجهد الساكن مستقر عند (${m.restingV}V)، كفاءة التخزين ممتازة جداً.`);
                }
            }

            if (m.leakageDrop !== null) {
                const dropVal = parseFloat(m.leakageDrop);
                const dStd = std.dropV;

                if (dropVal > dStd.bad) {
                    issues.push(`<strong>[تحذير تسريب]</strong> معدل هبوط الجهد اليومي (${dropVal}V/يوم) مرتفع جداً. افحص أجهزة المراقبة وكاميرات التسجيل ومنافذ OBD.`);
                } else if (dropVal > dStd.good) {
                    warnings.push(`<strong>[تسريب طفيف]</strong> معدل الهبوط اليومي (${dropVal}V/يوم) أعلى من المعتاد قليلاً. يُرجى الحذر عند إيقاف السيارة لفترات طويلة.`);
                } else if (dropVal <= dStd.excellent) {
                    goodPoints.push(`معدل الهبوط اليومي ضئيل جداً (${dropVal}V/يوم). لا يوجد تسريب طفيلي، وضع السكون مثالي!`);
                } else {
                    goodPoints.push(`معدل هبوط الجهد أثناء السكون (${dropVal}V/يوم) ضمن المعايير الصحية.`);
                }
            }

            if (m.avgChargeV !== null) {
                if (m.avgChargeV < std.chargeV.badMin || m.avgChargeV > 15.0) {
                    issues.push(`<strong>[خلل بالدينامو]</strong> متوسط جهد القيادة (${m.avgChargeV}V) خارج النطاق الآمن. إذا كان أقل من 13.5 فولت: تآكل فحمات أو ارتخاء سير؛ وإذا كان أعلى من 15 فولت: خطر تلف منظم الجهد!`);
                } else if (m.avgChargeV < std.chargeV.goodMin) {
                    warnings.push(`<strong>[شحن منخفض]</strong> متوسط جهد القيادة (${m.avgChargeV}V) منخفض. ملاحظة: إذا كانت سيارتك مزودة بنظام AMS الذكي لإدارة الطاقة، فقد يكون هذا تصرفاً طبيعياً لتوفير الوقود.`);
                } else {
                    goodPoints.push(`منظومة الشحن تعمل بكفاءة. متوسط جهد القيادة مستقر عند (${m.avgChargeV}V).`);
                }
            }

            if (m.minCrankV !== null) {
                if (m.minCrankV < std.crankV.bad) {
                    issues.push(`<strong>[تدوير شاق]</strong> أدنى جهد عند بدء التشغيل (${m.minCrankV}V) منخفض للغاية. يشير عادةً إلى ارتفاع المقاومة الداخلية للبطارية أو تقادم بادئ الحركة (السلف).`);
                } else if (m.minCrankV < std.crankV.good) {
                    warnings.push(`<strong>[تدوير ضعيف]</strong> جهد بدء التشغيل (${m.minCrankV}V) ضعيف. قد تواجه صعوبة في التشغيل أثناء موجات الصقيع الشديد.`);
                } else {
                    goodPoints.push(`ثبات مذهل لجهد بدء التشغيل (${m.minCrankV}V)، دلالة على انخفاض المقاومة الداخلية وقوة التفريغ اللحظي.`);
                }
            }

            if (issues.length > 0) {
                diagnosis += `<h4 style="color: #f85149; margin-top: 0;">🚨 أعطال ومخاطر مرتفعة تتطلب الفحص الفوري:</h4><ul style="margin-top: 5px;">`;
                issues.forEach(issue => diagnosis += `<li>${issue}</li>`);
                diagnosis += `</ul>`;
            }
            
            if (warnings.length > 0) {
                diagnosis += `<h4 style="color: #d29922;">⚠️ نقاط تتطلب المتابعة أو شحن الصيانة:</h4><ul style="margin-top: 5px;">`;
                warnings.forEach(warn => diagnosis += `<li>${warn}</li>`);
                diagnosis += `</ul>`;
            }

            if (issues.length === 0 && warnings.length === 0) {
                 diagnosis = `<h4 style="color: #3fb950; margin-top: 0;">✅ المنظومة الكهربائية في حالة ممتازة وصحية تماماً!</h4>`;
                 diagnosis += `<p>استناداً إلى تحليل البيانات متعددة الأيام، يظهر النظام أداءً فائق الجودة:</p><ul>`;
                 goodPoints.forEach(pt => diagnosis += `<li>${pt}</li>`);
                 diagnosis += `</ul>`;
                 if (bType === 'lifepo4') {
                     diagnosis += `<p style="color: #58a6ff; font-size: 14px; margin-top: 10px;">💡 <strong>ملاحظة هندسية:</strong> يتم استغلال مزايا بطارية LiFePO4 بالشكل الأمثل، حيث ينعدم التفريغ الذاتي وتتوفر قدرة تفريغ لحظية جبارة.</p>`;
                 }
            } else if (goodPoints.length > 0) {
                 diagnosis += `<h4 style="color: #3fb950;">✅ البنود السليمة:</h4><ul style="margin-top: 5px;">`;
                 goodPoints.forEach(pt => diagnosis += `<li>${pt}</li>`);
                 diagnosis += `</ul>`;
            }
        }
        document.getElementById('aiDiagnosis').innerHTML = diagnosis;
    }
</script>
