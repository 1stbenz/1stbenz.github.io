---
layout: post
title: "أداة تحليل وفك سجلات شاشة مراقبة البطارية BM6 / BM200"
lang: ar
date:   2026-03-20 17:00:00
categories: Auto
tags: [بطاريات السيارات, شاشات مراقبة البطارية, المعرفة الميكانيكية, أدوات الصيانة الذاتية, تحليل البيانات]
description: "أداة سحابية تفاعلية مصممة خصيصاً لمراقبات بطاريات السيارات بتقنية البلوتوث BM6 و BM200. بفضل الخوارزميات الذكية، تحل الأداة مشكلة عدم دقة رصد الرحلات الناتجة عن الجهد العالي لبطاريات LiFePO4، وتعيد بناء سجلات القيادة بدقة مع رسوم بيانية وتصدير تقارير Excel."
keywords: "BM6, مراقب البطارية بلوتوث, LiFePO4, رصد الرحلات, تحليل الجهد, تصدير إكسل, فك السجلات, بطارية السيارة, الدينامو الذكي"
image: /images/bm6-tool-preview.webp
faq:
  - question: "ما هي المشكلة الأساسية التي تعالجها هذه الأداة؟"
    answer: "يعجز تطبيق الهاتف الرسمي لجهاز BM6/BM200 عن تحديد لحظة إطفاء المحرك بدقة عند مراقبة بطاريات الليثيوم LiFePO4 بسبب بقاء جهد ركودها مرتفعاً، مما يؤدي إلى تشويه سجلات الرحلات. تعالج هذه الأداة هذه الثغرة وتفلتر التموجات لتعيد استخراج كل مشوار بدقة تامة."
  - question: "هل الأداة صالحة لبطاريات الرصاص العادية والسيارات المزودة بـ 'الدينامو الذكي'؟"
    answer: "نعم وبدقة مطلقة؛ حيث تحلل الخوارزمية الجهد الأساسي للبطارية، وتحدد ما إذا كانت تعمل بـ 'نمط LiFePO4' أو 'نمط بطارية الرصاص / الدينامو الذكي' لتضبط معايير الكشف تلقائياً."
  - question: "كيف أحصل على البيانات وأرفعها إلى الأداة؟"
    answer: "قم بتصدير ملف السجلات كملف Excel (.xls أو .xlsx) من تطبيق BM6/BM200 على هاتفك، ثم ارفعه مباشرة إلى هذه الصفحة لبدء التحليل الفوري."
  - question: "ما هي البيانات والتقارير التي تستخرجها الأداة؟"
    answer: "تحسب الأداة تلقائياً: إجمالي عدد المشاوير، وزمن القيادة الكلي، وأدنى جهد مسجل عند لحظة نقرة السلف (مؤشر بدء التشغيل على البارد)، ومتوسط جهد الشحن أثناء السير (كفاءة الدينامو)، مع رسوم بيانية تفاعلية تدعم التكبير."
---

<div id="car-app-container" style="max-width: 950px; margin: 20px auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #ffffff; color: #333333; padding: 25px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e5e7eb; position: relative;">
    
    <h2 id="ui-title" style="text-align: center; color: #04384c !important; margin-bottom: 22px; margin-top: 5px; font-weight: 800; font-size: 22px; background: none; border: none;">أداة تحليل وفك سجلات شاشة مراقبة البطارية BM6/BM200</h2>
    
    <div style="background: rgba(210, 153, 34, 0.08); padding: 15px 20px; border-radius: 10px; margin-bottom: 25px; border-right: 5px solid #d29922; border-left: none; font-size: 14.5px; line-height: 1.6; color: #475569;">
        <strong id="ui-desc-title" style="color: #b45309;">لماذا تحتاج إلى هذه الأداة؟</strong><br>
        <span id="ui-desc-body">رغم أن جهاز BM6/BM200 يسجل البيانات باستمرار حتى بعد إطفاء السيارة، إلا أن تطبيق الهاتف الرسمي يفشل في كشف الرحلات بشكل سليم ويصعب معه فحص المنحنيات بدقة. <b style="color:#04384c;">تقوم هذه الأداة بحل هذه المعضلة.</b> إذ تعتمد على خوارزمية ذكية مخصصة لتحليل تقلبات الجهد، واستعادة كل مشوار قيادة بدقة، وعرض منحنيات تفاعلية متزامنة للجهد ودرجة الحرارة.</span>
    </div>

    <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 15px 25px; border-radius: 10px; margin-bottom: 25px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px;">
        <div style="display: flex; gap: 10px;">
            <button id="uploadTrigger" style="background: #04384c; color: white; border: none; padding: 10px 20px; border-radius: 8px; cursor: pointer; font-weight: bold; font-size: 14px;">📁 رفع ملف إكسل (Excel)</button>
            <button id="loadSampleBtn" style="background: #ffffff; color: #04384c; border: 1px solid #cbd5e1; padding: 9px 20px; border-radius: 8px; cursor: pointer; font-weight: bold; font-size: 14px; display: flex; align-items: center; transition: 0.2s;">📄 تجربة ملف عينة</button>            
        </div>
        <div style="display: flex; gap: 10px; align-items: center;">
            <label id="ui-display-range" style="font-weight: bold; color: #04384c; font-size: 14px;">نطاق العرض:</label>
            <select id="dateSelector" style="padding: 8px 12px; border-radius: 8px; border: 1px solid #cbd5e1; font-size: 14px; min-width: 160px; cursor: pointer; background: #ffffff; color: #333333;">
                <option value="all" id="ui-show-all">-- عرض الكل --</option>
            </select>
        </div>
        <input type="file" id="fileInput" accept=".xls,.xlsx" style="display:none">
    </div>

    <div id="status-text" style="text-align: center; color: #64748b; margin-bottom: 20px; font-size: 14px;">يرجى رفع ملف Excel المصدر من تطبيق BM6/BM200 أو الضغط على تجربة ملف العينة للاختبار.</div>
    
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
        <div class="stat-card" style="background: rgba(4, 56, 76, 0.05); border: 1px solid rgba(4, 56, 76, 0.15);">
            <div style="font-size: 13px; color: #04384c; margin-bottom: 5px; font-weight: 600;">إجمالي الرحلات</div>
            <div id="stat-trips" style="font-size: 24px; font-weight: bold; color: #04384c;">0</div>
        </div>
        <div class="stat-card" style="background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.25);">
            <div style="font-size: 13px; color: #047857; margin-bottom: 5px; font-weight: 600;">زمن القيادة الكلي</div>
            <div id="stat-time" style="font-size: 24px; font-weight: bold; color: #047857;">0 <span style="font-size: 12px; font-weight: normal;">دقيقة</span></div>
        </div>
        <div class="stat-card" style="background: rgba(227, 76, 38, 0.08); border: 1px solid rgba(227, 76, 38, 0.25);">
            <div style="font-size: 13px; color: #c2410c; margin-bottom: 5px; font-weight: 600;">أدنى جهد (عند السلف)</div>
            <div id="stat-minv" style="font-size: 24px; font-weight: bold; color: #c2410c;">0.00 <span style="font-size: 12px; font-weight: normal;">V</span></div>
        </div>
        <div class="stat-card" style="background: rgba(122, 0, 223, 0.08); border: 1px solid rgba(122, 0, 223, 0.25);">
            <div style="font-size: 13px; color: #7a00df; margin-bottom: 5px; font-weight: 600;">متوسط جهد القيادة</div>
            <div id="stat-avgv" style="font-size: 24px; font-weight: bold; color: #7a00df;">0.00 <span style="font-size: 12px; font-weight: normal;">V</span></div>
        </div>
    </div>

    <div style="background: #ffffff; padding: 15px; border-radius: 10px; border: 1px solid #e2e8f0; box-shadow: 0 1px 4px rgba(0,0,0,0.04);">
        <div style="height: 280px; width: 100%; margin-bottom: 10px;">
            <canvas id="voltageChart"></canvas>
        </div>
        <div style="height: 280px; width: 100%;">
            <canvas id="tempChart"></canvas>
        </div>
    </div>

    <div id="trip-section" style="margin-top: 20px; padding: 15px; background: #f8fafc; border-radius: 10px; border: 1px dashed #cbd5e1; display: none;">
        <h3 id="ui-trip-title" style="color: #04384c; font-size: 16px; font-weight: 700; margin-top: 0; margin-bottom: 15px;">قائمة الرحلات المكتشفة</h3>
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
        let highV = sortedV.slice(Math.floor(sortedV.length * 0.98)).reduce((a, b) => a + b, 0) / (Math.floor(sortedV.length * 0.02) || 1);
        if (highV - baseV < 0.25) return { trips: [], mode: "inactive" };

        let isLiFePO4 = (baseV >= 13.0); 
        let rawTrips = [];
        let isOn = false, startIdx = 0;
        let midV = isLiFePO4 ? Math.max(baseV + (highV - baseV) * 0.5, 13.45) : (baseV + 0.35);
        let offV = isLiFePO4 ? Math.max(midV - 0.05, 13.38) : (baseV + 0.10); 

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
                    for (let j = 1; j <= lookAhead; j++) { if (data[i + j].v > midV) { isRealEnd = false; jumpIdx = i + j; break; } }

                    if (isRealEnd || lookAhead === 0) {
                        isOn = false;
                        let endIdx = i;                        
                        for (let k = i; k > startIdx; k--) {
                            if (data[k].v >= midV + 0.15 || (data[k - 1].v - data[k].v > 0.05 && data[k - 1].v > midV)) {
                                endIdx = k;
                                while (endIdx > startIdx && data[endIdx - 1].v >= data[endIdx].v) {
                                    endIdx--;
                                }
                                break;
                            }
                        }
                        let dur = Math.round((new Date(data[endIdx].x) - new Date(data[startIdx].x)) / 60000);
                        if (dur >= 2) rawTrips.push({ start: data[startIdx].x, end: data[endIdx].x, startStr: data[startIdx].xStr, endStr: data[endIdx].xStr, duration: dur });
                    } else { i = jumpIdx - 1; }
                }
            }
        }
        if (isOn) {
           let endIdx = data.length - 1;
           let dur = Math.round((new Date(data[endIdx].x) - new Date(data[startIdx].x)) / 60000);
           if (dur >= 2) rawTrips.push({ start: data[startIdx].x, end: data[endIdx].x, startStr: data[startIdx].xStr, endStr: data[endIdx].xStr, duration: dur });
        }

        let mergedTrips = [];
        let mergeGapMins = isLiFePO4 ? 8 : 25; 
        if (rawTrips.length > 0) {
            let currentTrip = rawTrips[0];
            for (let i = 1; i < rawTrips.length; i++) {
                let gapMins = Math.round((rawTrips[i].start - currentTrip.end) / 60000);
                if (gapMins <= mergeGapMins) {
                    currentTrip.end = rawTrips[i].end;
                    currentTrip.endStr = rawTrips[i].endStr; 
                    currentTrip.duration = Math.round((currentTrip.end - currentTrip.start) / 60000);
                } else { mergedTrips.push(currentTrip); currentTrip = rawTrips[i]; }
            }
            mergedTrips.push(currentTrip);
        }
        return { trips: mergedTrips, mode: isLiFePO4 ? "LiFePO4" : "الرصاص الحمضية" };
    }

    function updateStatCards(filteredData, result) {
        const statsContainer = document.getElementById('stats-container');
        if (!filteredData || filteredData.length === 0) { statsContainer.style.display = 'none'; return; }
        statsContainer.style.display = 'grid';

        document.getElementById('stat-trips').innerText = result.trips.length;
        const totalMins = result.trips.reduce((acc, t) => acc + t.duration, 0);
        document.getElementById('stat-time').innerHTML = `${totalMins} <span style="font-size:12px;">دقيقة</span>`;

        const minV = Math.min(...filteredData.map(d => d.v));
        const minVElement = document.getElementById('stat-minv');
        minVElement.innerHTML = `${minV.toFixed(2)} <span style="font-size:12px;">V</span>`;
        minVElement.style.color = minV < 12.6 ? "#f85149" : "#ff945e";

        let drivePoints = 0, sumV = 0;
        filteredData.forEach(d => {
            const isDriving = result.trips.some(t => d.x >= t.start && d.x <= t.end);
            if (isDriving) { drivePoints++; sumV += d.v; }
        });
        document.getElementById('stat-avgv').innerHTML = `${drivePoints > 0 ? (sumV / drivePoints).toFixed(2) : "N/A"} <span style="font-size:12px;">V</span>`;
    }

    function renderTrips(result) {
        tripList.innerHTML = '';
        if (!result.trips || result.trips.length === 0) { tripSection.style.display = 'none'; return; }
        tripSection.style.display = 'block';
        
        const modeSuffix = result.mode === 'LiFePO4' ? ' [نمط LiFePO4]' : ' [نمط بطارية الرصاص / الدينامو الذكي]';
        document.getElementById('ui-trip-title').innerText = 'الرحلات المكتشفة' + modeSuffix;

        result.trips.forEach((t, i) => {
            const rowDiv = document.createElement('div');
            rowDiv.style.cssText = "display: flex; align-items: center; justify-content: space-between; background: #ffffff; padding: 10px 16px; border-radius: 8px; border: 1px solid #e2e8f0;";
            rowDiv.innerHTML = `<span style="font-size: 14px; color: #333333;"><b style="color:#04384c;">الرحلة ${i+1}</b>: ${t.startStr} ~ ${t.endStr} (المدة: ${t.duration} دقيقة)</span>`;

            const btn = document.createElement('button');
            btn.innerHTML = '🔍 تكبير المنحنى';
            btn.style.cssText = "background: #f1f5f9; border: 1px solid #cbd5e1; color: #04384c; padding: 5px 15px; border-radius: 6px; cursor: pointer; font-size: 13px; font-weight: bold; transition: 0.2s; white-space: nowrap;";
            btn.onclick = () => {
                const s = t.start - 600000, e = t.end + 600000;
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
            const xVal = dataset[i].x; 
            if (xVal > xScale.max) break; 
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

    function normalizeTime(val) {
        if (!val) return null;
        if (typeof val === 'number' && val > 40000 && val < 60000) {
            const excelEpoch = new Date(Date.UTC(1899, 11, 30));
            const jsDate = new Date(excelEpoch.getTime() + val * 86400000);
            const yyyy = jsDate.getUTCFullYear();
            const mm = String(jsDate.getUTCMonth() + 1).padStart(2, '0');
            const dd = String(jsDate.getUTCDate()).padStart(2, '0');
            const hh = String(jsDate.getUTCHours()).padStart(2, '0');
            const min = String(jsDate.getUTCMinutes()).padStart(2, '0');
            return `${yyyy}-${mm}-${dd} ${hh}:${min}`;
        }
        let timeStr = String(val).trim();
        if (/^\d{4}-\d{2}-\d{2}/.test(timeStr)) {
            const match = timeStr.match(/^(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2})/);
            return match ? match[1] : timeStr;
        }
        const slashMatch = timeStr.match(/^(\d{4})\/(\d{1,2})\/(\d{1,2})\s+(\d{1,2}:\d{2})/);
        if (slashMatch) {
            const mm = slashMatch[2].padStart(2, '0');
            const dd = slashMatch[3].padStart(2, '0');
            return `${slashMatch[1]}-${mm}-${dd} ${slashMatch[4]}`;
        }
        const enMatch = timeStr.match(/^([a-zA-Z]{3})\s+(\d{1,2})\/(\d{4})\s+(\d{2}:\d{2})/);
        if (enMatch) {
            const months = {jan:'01', feb:'02', mar:'03', apr:'04', may:'05', jun:'06', jul:'07', aug:'08', sep:'09', oct:'10', nov:'11', dec:'12'};
            const m = months[enMatch[1].toLowerCase()];
            if (m) return `${enMatch[3]}-${m}-${enMatch[2].padStart(2, '0')} ${enMatch[4]}`;
        }
        return null;
    }

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

    function createChartConfig(label, color, yTitle) {
        return {
            type: 'line',
            data: { 
                datasets: [{ 
                    label: label, 
                    data: [], 
                    borderColor: color, 
                    backgroundColor: color + '20', 
                    borderWidth: 2, 
                    pointRadius: 0, 
                    tension: 0.2, 
                    fill: true,
                    normalized: true, 
                    parsing: false    
                }] 
            },
            options: {
                responsive: true, maintainAspectRatio: false,
                interaction: { mode: 'index', intersect: false },
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
                        backgroundColor: 'rgba(255, 255, 255, 0.96)',
                        titleColor: '#0f172a',
                        bodyColor: '#334155',
                        borderColor: '#cbd5e1',
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

    vChart = new Chart(document.getElementById('voltageChart'), createChartConfig('الجهد الكهربائي (فولت)', '#1176d4', 'الجهد (V)'));
    tChart = new Chart(document.getElementById('tempChart'), createChartConfig('درجة الحرارة (مئوية)', '#dc2626', 'الحرارة (℃)'));

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
            trips: (selectedDate === 'all' ? globalDetectedTrips.trips : globalDetectedTrips.trips.filter(t => t.startStr.startsWith(selectedDate))), 
            mode: globalDetectedTrips.mode 
        };

        renderTrips(result); 
        updateStatCards(dataList, result);

        vChart.update('none'); 
        tChart.update('none');
        setTimeout(() => { isResetting = false; }, 200);
    }

    const loadSampleBtn = document.getElementById('loadSampleBtn');

    function parseExcelData(arrayBuffer) {
        statusText.innerHTML = '⏳ جارٍ تحليل بيانات الرحلات...';
        setTimeout(() => {
            try {
                const workbook = XLSX.read(new Uint8Array(arrayBuffer), { type: 'array' });
                const ws = workbook.Sheets[workbook.SheetNames.find(n => n.includes("歷史") || n.includes("History")) || workbook.SheetNames[0]];
                const rows = XLSX.utils.sheet_to_json(ws, { header: 1 });
                let extracted = [], dates = new Set();
                
                for (let i = 0; i < rows.length; i++) {
                    for (let col = 0; col < rows[i].length; col += 5) {
                        const timeStr = normalizeTime(rows[i][col]);
                        if (timeStr) {
                            const vVal = parseCarValue(rows[i][col+1]);
                            if (vVal > 0) { 
                                extracted.push({ 
                                    x: new Date(timeStr).getTime(),
                                    xStr: timeStr,
                                    v: vVal, 
                                    t: parseCarValue(rows[i][col+3]) 
                                }); 
                                dates.add(timeStr.split(' ')[0]); 
                            }
                        }
                    }
                }
                allData = extracted.sort((a, b) => new Date(a.x) - new Date(b.x));
                globalDetectedTrips = detectTripsByCurve(allData);
                
                dateSelector.innerHTML = '<option value="all">-- عرض الكل --</option>';
                Array.from(dates).sort().forEach(d => { 
                    const opt = document.createElement('option'); 
                    opt.value = d; 
                    opt.innerText = d; 
                    dateSelector.appendChild(opt); 
                });
                
                resetViewAndUpdateData(allData, 'all'); 
                statusText.innerHTML = `✅ تم التحليل بنجاح: تم استخراج <b style="color:#58a6ff;">${allData.length}</b> سجلاً بدقة.`;
            } catch (error) {
                statusText.innerHTML = `❌ فشل قراءة الملف (${error.message})`;
            }
        }, 50);
    }

    uploadTrigger.onclick = () => fileInput.click();
    fileInput.onchange = (e) => {
        const file = e.target.files[0]; 
        if (!file) return;
        const reader = new FileReader();
        reader.onload = function(event) { parseExcelData(event.target.result); };
        reader.readAsArrayBuffer(file);
    };

    loadSampleBtn.onclick = () => {
        statusText.innerHTML = '📥 جارٍ تنزيل ملف العينة...';
        fetch('/files/bm6_2025_10.xls')
            .then(response => {
                if (!response.ok) throw new Error('تعذر العثور على ملف العينة على الخادم.');
                return response.arrayBuffer();
            })
            .then(buffer => parseExcelData(buffer))
            .catch(error => { statusText.innerHTML = `❌ خطأ في التحميل: ${error.message}`; });
    };

    dateSelector.onchange = function() {
        const filtered = (this.value === 'all') ? allData : allData.filter(d => d.xStr.startsWith(this.value));
        resetViewAndUpdateData(filtered, this.value);
    };

})();
</script>
