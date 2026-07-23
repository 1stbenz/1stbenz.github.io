---
layout: post
title: "Inspección integral de la salud del sistema eléctrico del vehículo: análisis a largo plazo de datos BM6"
lang: es
date: 2026-04-14 09:52:00
categories: Auto
tags: [Batería de coche, Monitor de batería, Conocimiento de coche]
description: "¿Cómo determinar científicamente si una batería necesita reemplazo? Este artículo presenta un sistema de inspección integral para la salud del sistema eléctrico vehicular, que evalúa en profundidad las fugas eléctricas en reposo, la eficiencia de generación durante el funcionamiento y la potencia explosiva al instante de arranque mediante el análisis de datos de monitoreo a 1 Hz y registros de alta frecuencia (100 Hz) tras un encendido."
keywords: "Salud de la batería, Batería de hierro-litio, LiFePO4, Baterías al ácido plomo, Prueba de corriente fugitiva (corriente de fuga), Voltaje de arranque, Detección del generador, Análisis de registros Bluetooth, Electricidad para vehículos"
image: /images/battery-health-report-analysis.webp
faq:
  - question: "¿Qué indicadores clave detecta principalmente este sistema?"
    answer: "El sistema evalúa cuatro indicadores centrales: 1. Salud de la batería (voltaje en reposo), 2. Estado del consumo fantasma (caída de voltaje nocturno), 3. Sistema de generación (voltaje medio durante el viaje), 4. Potencia de arranque (voltaje mínimo al arrancar)."
  - question: "¿Cuál es la diferencia en los criterios de determinación entre las baterías de hierro-litio y las baterías de ácido plomo?"
    answer: "El sistema establece dos estándares dobles. Por ejemplo, el voltaje de reposo óptimo para una batería de hierro-litio (LiFePO4) debe ser mayor a 13,2 V, mientras que para una batería de ácido plomo estándar es de 12,5 V; en cuanto al voltaje instantáneo durante el arranque, el estándar para las baterías de hierro-litio es de 11,5 V y para las de ácido plomo es de 10,5 V."
  - question: "¿Cómo determinar si el vehículo presenta fugas de corriente (corriente oculta)?"
    answer: "El sistema calcula la \"caída diaria de voltaje (V/día)\" mediante registros a largo plazo durante períodos de inactividad. Si la caída es mayor que 0,3 V (LiFePO4) o 0,4 V (plomo-ácido), se determina una fuga excesiva y se recomienda verificar si el registrador de viaje, el sistema antirrobo o los dispositivos OBD2 no han entrado en modo suspensión correctamente."
  - question: "¿Por qué se necesita un dato de 100 Hz para analizar el voltaje del arranque?"
    answer: "El momento inicial del encendido dura menos de un segundo; los registros estándar a 1 Hz (una vez por segundo) pueden fácilmente perderse en el punto más bajo del voltaje. Mediante una muestra de alta frecuencia de 100 Hz, se puede capturar con precisión la caída de tensión durante el funcionamiento del motor de arranque y determinar si la resistencia interna de las celdas ha aumentado o si el motor de arranque está envejecido."
  - question: "¿Cuál es la base para determinar una anomalía en el generador?"
    answer: "El sistema filtra los datos después del arranque del motor; si la tensión media de conducción está por debajo de 13,5 V (o superior a 15,0 V), se considera que el generador ha envejecido o existe un fallo en el regulador. Para los vehículos equipados con un sistema de control de carga (AMS), el sistema también realiza comentarios especiales sobre las bajas tensiones durante los modos de ahorro energético."
  - question: "¿Qué hacer si la batería de hierro litio muestra 'baja capacidad' en el informe?"
    answer: "Si la tensión estática de la batería de hierro litio no alcanza los 13,2 V, se recomienda realizar un viaje largo o utilizar un cargador especializado para cargarla completamente, con el fin de activar la función de equilibrio activo de las celdas del BMS y garantizar la vida útil y el rendimiento de la batería."
---

<!-- Cargar los paquetes externos necesarios para analizar Excel -->  
<script src="https://cdn.jsdelivr.net/npm/xlsx/dist/xlsx.full.min.js"></script>

<style>
    /* Los estilos aquí solo se aplicarán a los elementos de esta página */
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
        background-color: rgba(56, 139, 253, 0.1); padding: 20px; border-radius: 10px;
        borde-izquierdo: 5px sólido #388bfd; línea-de-alto: 1.6;
    }

<div class="app-container">
    <h1>Sistema de informe de inspección del estado del sistema eléctrico vehicular</h1>
</div>

<div class="control-panel">
        <div class="file-input-group">
            <label>📁 1. Registro a largo plazo en línea (evaluación de fugas estáticas)</label>
            <input type="file" id="fileOffline" accept=".xls,.xlsx,.csv">
            <span class="file-hint">Formato compatible con hojas de cálculo Excel exportadas</span>
        </div>
        <div class="file-input-group">
            <label>📁 2. Registro Bluetooth original (evaluación de generación y arranque)</label>
            <input type="file" id="fileRaw" accept=".txt,.log" multiple>
            <span class="file-hint">Selección múltiple permitida. Análisis automático de paquetes mixtos a 1 Hz y 100 Hz</span>
        </div>
        <div class="file-input-group">
            <label>⚙️ Configuración del material químico de la batería</label>
            <select id="batteryType">
                <option value="lifepo4">Batería LiFePO4 (Litio-ferrofosfato)</option>
                <option value="leadacid">Batería ácida plástica estándar (Lead-Acid)</option>
            </select>
        </div>
    </div>

<button class="btn-generate" onclick="generateReport()">Generar informe integral de salud</button>

<div class="report-section" id="reportSection">
    <div class="patient-info">
        <span id="reportDate">Fecha del informe: YYYY/MM/DD</span>
        <span id="reportConfig">Configuración de análisis: referencia para baterías de ion de litio</span>
    </div>

<table id="reportTable">
            <thead>
                <tr>
                    <th width="20%">Ítem de verificación</th>
                    <th width="20%">Datos actuales</th>
                    <th width="20%">Estándar óptimo</th>
                    <th width="20%">Estándar anómalo</th>
                    <th width="20%">Determinación integral</th>
                </tr>
            </thead>
            <tbody id="tableBody">
            </tbody>
        </table>

<div class="doctor-notes">
            <h3 style="margin-top:0; color:#58a6ff;">📋 Recomendaciones de diagnóstico integral del sistema</h3>
            <div id="aiDiagnosis">Por favor, suba los datos para obtener un análisis completo.</div>
        </div>
    </div>
</div>

<script>
    const umbrales = {
        lifepo4: {
            voltajeDescanso: { bueno: 13.2, malo: 13.0, unidad: 'V' },
            caídaVoltaje: { excelente: 0.01, bueno: 0.02, malo: 0.05, unidad: 'V/día' },
            voltajeCarga: { buenMinimo: 13.8, buenMaximo: 14.4, malMinimo: 13.5, unidad: 'V' },
            voltajeArranque: { bueno: 11.5, malo: 10.0, unidad: 'V' }
        },
        leadacid: {
            voltajeDescanso: { bueno: 12.5, malo: 12.0, unidad: 'V' },
            caídaVoltaje: { bueno: 0.15, malo: 0.4, unidad: 'V/día' },
            voltajeCarga: { buenMinimo: 13.8, buenMaximo: 14.8, malMinimo: 13.3, unidad: 'V' },
            voltajeArranque: { bueno: 10.5, malo: 9.0, unidad: 'V' }
        }
    };
</script>

async function procesarArchivoExcel(file, bType) {
            return new Promise((resolve) => {
                const lector = new FileReader();
                lector.onload = function(e) {
                    const datos = new Uint8Array(e.target.result);
                    const libroDeTrabajo = XLSX.read(datos, {tipo: 'array'});
                    const nombreHoja = libroDeTrabajo.SheetNames[0];
                    const json = XLSX.utils.sheet_to_json(libroDeTrabajo.Hojas[nombreHoja], {encabezado: 1});

// 1. Obtener todos los voltajes originales (excluir la fila de encabezados y valores anómalos)
                    const allVoltages = json.slice(1)
                        .map(row => parseFloat(row[1]))
                        .filter(v => !isNaN(v) && v > 5.0 && v < 16.0);

if (allVoltages.length < 20) {
                        resolver = { rest: null, drop: null };
                        return;
                    }

// 2. Establecer el umbral según el tipo de batería
                    // filterThreshold: cualquier valor superior se considera que la batería está cargando, por lo tanto no se incluye en el análisis de reposo
                    // stableStartV: solo si es inferior a este valor se considera que "la tensión superficial ha desaparecido", iniciándose así el cálculo del verdadero caída de voltaje
                    const filterThreshold = (bType === 'lifepo4') ? 13.6 : 13.2;
                    const stableStartV = (bType === 'lifepo4') ? 13.3 : 12.7;

// 3. Calcular la salud de la batería (voltaje en reposo)
                    // Seleccionar el valor del percentil inferior al 5% de todos los datos, lo que representa el voltaje estable más bajo habitual durante el periodo de reposo de esa batería
                    const sortedV = [...allVoltages].sort((a, b) => a - b);
                    const restV = sortedV[Math.floor(sortedV.length * 0.05)];

// 4. Filtrar los intervalos de datos en reposo que no estén cargando
const staticVs = allVoltages.filter(v => v < filtroUmbral);

```javascript
if (staticVs.length < 10) {
            resolve({ rest: restV.toFixed(2), drop: 0 });
            return;
        }
```

// 5. Búsqueda del «punto de inicio real de la caída de tensión»: saltar el intervalo superficial de voltaje que cae desde 13,6 V a 13,3 V justo después de apagar el motor  
let startIndex = staticVs.findIndex(v => v <= stableStartV);  

// Prevención de errores: si todos los datos están por encima del umbral estable o quedan pocos datos restantes, calcular desde el principio  
if (startIndex === -1 || (staticVs.length - startIndex) < 10) {
    startIndex = 0;
}

const endIndex = staticVs.length - 1;

// 6. Obtener el voltaje inicial y final (promedio de 5 puntos para evitar ruido en una sola medición)
const headRange = staticVs.slice(startIndex, startIndex + 5);
const tailRange = staticVs.slice(-5);

const avgFirstV = headRange.reduce((a, b) => a + b, 0) / headRange.length;
const avgLastV = tailRange.reduce((a, b) => a + b, 0) / tailRange.length;

// 7. Calcular el número de días del intervalo de análisis válido (los registros en línea BM6 suelen ser de un punto cada dos minutos).
                    const effectivePoints = endIndex - startIndex;
                    const totalDays = (effectivePoints > 0) ? (effectivePoints * 2) / 1440 : (allVoltages.length * 2) / 1440;

// 8. Calcular la caída diaria de presión: (promedio inicial – promedio final) / días
let realDrop = (avgFirstV - avgLastV) / totalDays;

// Corrección del problema de valores negativos: si el voltaje aumenta en lugar de disminuir, los datos no son adecuados para analizar fugas eléctricas; forzar a cero.
if (realDrop < 0) realDrop = 0;

resolve({ 
                        rest: parseFloat(restV.toFixed(2)), 
                        drop: parseFloat(realDrop.toFixed(2))
                    });
                };
                reader.readAsArrayBuffer(file);
            });
        }

```javascript
async function generateReport() {
    const btn = document.querySelector('.btn-generate');
    btn.innerText = "Analizando datos...";
    btn.disabled = true;
}
```

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

const umbralMotorEnviado = bType === 'lifepo4' ? 13,6 : 13,5;
            const umbralMotorApagado = bType === 'lifepo4' ? 13,3 : 12,8;

for (let i = 0; i < rawFiles.length; i++) {
                const text = await rawFiles[i].text();
                const lines = text.split('\n');
                
                const pattern1Hz = /d1550700[0-9a-fA-F]{6}([0-9a-fA-F]{4})/i;

let esMotorEnMarcha = false;
                let ventana15s = []; 
                let flujoHexTemporal = "";

```javascript
lines.forEach((line) => {
    const lineaEnMinusculaYSinEspaciosExtras = line.limpiar().convertirTodoAMinusculas;
});
```

const match1Hz = lowerLine.match(pattern1Hz);
                    if (match1Hz) {
                        let v = parseInt(match1Hz[1], 16) / 100;
                        
                        window15s.push(v);
                        if (window15s.length > 15) window15s.shift();

if (v >= umbralDeEncendidoMotor) {
    isFuncionandoElMotor = true;
} 

if (isFuncionandoElMotor) {
    if (v < umbralDeEncendidoMotor && window15s.length === 15) {
        let vHaceQuinceSegundos = window15s[0];
        if ((vHaceQuinceSegundos - v) >= 0.10) isFuncionandoElMotor = false;
    }
    if (v <= umbralDeApagadoMotor) isFuncionandoElMotor = false;
}

si (esMotorEnMarcha y v > 10,0 y v < 16,0) {  
            sum1Hz += v;  
            count1Hz++;  
        }

if (v > 6.0 && v < 15.0 && v < fallback1HzMin) fallback1HzMin = v;
                    
    if (lowerLine.includes('receive:')) {
        let contenido = lowerLine.split("receive:")[1].trim();
        if (/^[0-9a-f]+$/.test(contenido) && !contenido.startsWith("d15507")) {
            tempHexStream += contenido;
        }
    }

if ('cranking.add:ok'.includes(lowerLine)) {
let partes = tempHexStream.split("fffffe");
if (partes.length > 1) {
    let ultimaParte = partes[partes.length - 1];
    if (ultimaParte.includes("fffefe")) {
        let datosDeLaCurva = ultimaParte.split("fffefe")[0];
        let localMinimo = 99.0; 

for (let j = 0; j < datosDeLaCurva.length - 2; j += 3) {
    let voltaje = parseInt(datosDeLaCurva.substring(j, j + 3), 16) / 100.0;
if (!isNaN(voltaje) && voltaje >= 3.0 && voltaje <= 15.0) {
        if (voltaje < localMinimo) {
            localMinimo = voltaje;
        }
    }
}

if (localMinimo < 99.0) {
crankMinList.push(localMinimo);
}
}
}
tempHexStream = ""; 
});

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

renderTabla(metrics, std, bType);

btn.innerText = "Generar informe de salud integral";
        btn.disabled = false;
        document.getElementById('reportSection').style.display = 'block';
    }

function evaluate(value, goodRule, badRule, type) {
        if (value === null) return { text: "No se proporcionaron datos", class: "status-none" };
        let v = parseFloat(value);
        if (type === 'higher_is_better') {
            if (v >= goodRule) return { text: "Excelente", class: "status-good" };
            if (v <= badRule) return { text: "Requiere mantenimiento", class: "status-bad" };
            return { text: "Aceptable", class: "status-warn" };
        } else if (type === 'lower_is_better') {
            if (v <= goodRule) return { text: "Excelente", class: "status-good" };
            if (v >= badRule) return { text: "Fuga de corriente excesiva", class: "status-bad" };
            return { text: "Elevado", class: "status-warn" };
        } else if (type === 'range') {
            if (v >= goodRule[0] && v <= goodRule[1]) return { text: "Generador en buen estado", class: "status-good" };
            if (v < badRule || v > 15.0) return { text: "Anomalía del generador", class: "status-bad" };
            return { text: "Carga débil", class: "status-warn" };
        }
    }

function renderTable(m, std, bType) {
    document.getElementById('reportDate').innerText = `Fecha de generación del informe: ${new Date().toLocaleString()}`;
    document.getElementById('reportConfig').innerText = `Configuración del análisis: ${bType === 'lifepo4' ? 'Batería de hierro-litio' : 'Batería plomo-ácido estándar'}`;

No se puede traducir código de programación como este, ya que no es texto natural sino instrucciones para un navegador web en JavaScript. Sin embargo, si necesitas una explicación o documentación sobre qué hace este fragmento de código en español, puedo proporcionarla:  
Este código selecciona el elemento con el ID `tableBody` dentro del documento y vacía su contenido interno (es decir, elimina todas las filas u otros elementos que existían previamente).

const items = [
    {
        name: "Salud de la batería (voltaje en reposo)",
        val: m.restingV, unit: "V",
        goodStr: `> ${std.restV.good}V`, badStr: `< ${std.restV.bad}V`,
        eval: evaluate(m.restingV, std.restV.good, std.restV.bad, 'higher_is_better')
    },
    {
        name: "Estado de corriente fugaz (caída nocturna)",
        val: m.leakageDrop, unit: "V/día",
        goodStr: `< ${std.dropV.good}V`, badStr: `> ${std.dropV.bad}V`,
        eval: evaluate(m.leakageDrop, std.dropV.good, std.dropV.bad, 'lower_is_better')
    },
    {
        name: "Sistema de carga (Promedio)",
        val: m.avgChargeV, unit: "V",
        goodStr: `${std.chargeV.goodMin} - ${std.chargeV.goodMax}V`, badStr: `< ${std.chargeV.badMin}V`,
        eval: evaluate(m.avgChargeV, [std.chargeV.goodMin, std.chargeV.goodMax], std.chargeV.badMin, 'range')
    },
    {
        name: "Voltaje mínimo de arranque (Promedio)",
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

let diagnóstico = "";
if (m.restingV === null && m.avgChargeV === null && m.minCrankV === null) {
    diagnóstico = "No hay suficientes datos para realizar una evaluación integral. Por favor, verifique que se haya subido el archivo correspondiente.";
} else {
    let problemas = [];
    let advertencias = [];
    let puntosPositivos = [];

if (m.restingV !== null) {
    if (m.restingV < std.restV.bad) {
        if (bType === 'lifepo4') {
            issues.push(`<strong>[Anomalía de la batería]</strong> La tensión en reposo (${m.restingV} V) es demasiado baja. Las celdas pueden haberse degradado, provocando una disminución de la capacidad y un aumento excesivo de la resistencia interna, o el vehículo ha estado realizando viajes cortos durante mucho tiempo, lo que impide que el BMS equilibre eficazmente la carga.`);
        } else {
            issues.push(`<strong>[Anomalía de la batería]</strong> La tensión en reposo (${m.restingV} V) es demasiado baja. Las placas del electrodo pueden haberse degradado (sulfatación), reduciendo su capacidad, o el vehículo ha estado realizando viajes cortos durante mucho tiempo, provocando una carga crónica insuficiente.`);
        }
    } else if (m.restingV < std.restV.good) {
        if (bType === 'lifepo4') {
            warnings.push(`<strong>[Batería débil]</strong> La tensión en reposo (${m.restingV} V) no alcanza el estado óptimo. Se recomienda realizar un viaje largo o utilizar un cargador especializado para cargar completamente la batería y activar así la función de equilibrio activo de las celdas del BMS.`);
        } else {
            warnings.push(`<strong>[Batería débil]</strong> La tensión en reposo (${m.restingV} V) no alcanza el estado óptimo. Se recomienda realizar un viaje largo a alta velocidad o utilizar un cargador externo para una carga de mantenimiento profunda que active las placas.`);
        }
    } else {
        goodPoints.push(`La tensión en reposo se mantiene en (${m.restingV} V), con una capacidad de almacenamiento excelente.`);
    }
}

if (m.leakageDrop !== null) {
    const dropVal = parseFloat(m.leakageDrop);
    const dStd = std.dropV;

if (dropVal > dStd.bad) {
    issues.push(`<strong>[Advertencia de fuga eléctrica]</strong> La caída de tensión diaria (${dropVal} V/día) es demasiado alta. Por favor, revise el monitor de estacionamiento del registrador o el dispositivo OBD2.`);
} else if (dropVal > dStd.good) {
    warnings.push(`<strong>[Fuga eléctrica leve]</strong> La caída de tensión diaria (${dropVal} V/día) es ligeramente alta; si se deja en reposo durante mucho tiempo, tenga cuidado con la carga de batería.`);
} else if (dropVal <= dStd.excellent) {
    goodPoints.push(`La caída de tensión diaria solo es de ${dropVal} V/día: el sistema eléctrico no tiene fugas eléctricas y el estado de reposo es perfecto!`);
} else {
    goodPoints.push(`El descenso de presión en reposo (${dropVal} V/día) se presenta bien, cumpliendo con los estándares de salud.`);
}

if (m.avgChargeV !== null) {
    if (m.avgChargeV < std.chargeV.badMin || m.avgChargeV > 15.0) {
        issues.push(`<strong>[Anomalía en la generación]</strong> El voltaje medio de conducción (${m.avgChargeV} V) se encuentra fuera del rango saludable. Si es bajo, podría deberse al desgaste del generador, a los cepillos carbonosos o a una correa que resbala; si está excesivamente alto (mayor de 15 V), el regulador del generador podría estar averiado.`);
    } else if (m.avgChargeV < std.chargeV.goodMin) {
        warnings.push(`<strong>[Voltaje bajo en la generación]</strong> El voltaje medio de conducción (${m.avgChargeV} V) es inferior al esperado. **Nota:** Si está equipado con un «Sistema de control de carga (AMS)», esto es una situación normal de ahorro energético; si no lo está, debe prestar atención a si el rendimiento del generador se ha deteriorado.`);
    } else {
        goodPoints.push(`El sistema de generación funciona correctamente y mantiene un voltaje medio estable durante la conducción (${m.avgChargeV} V), con un buen rendimiento.`);
    }
}

if (m.minCrankV !== null) {
    if (m.minCrankV < std.crankV.bad) {
        issues.push(`<strong>[Arranque con arrastre]</strong> La tensión mínima en el instante de arranque (${m.minCrankV} V) es demasiado baja. Generalmente se debe a un aumento de la resistencia interna de la batería o una degradación del rendimiento al descargar instantáneamente; si la batería es nueva, verifique si el motor de arranque está viejo y arrastrando, o si existe mala conexión entre el polo negativo y tierra.`);
    } else if (m.minCrankV < std.crankV.good) {
        warnings.push(`<strong>[Arranque débil]</strong> La tensión en el instante de arranque (${m.minCrankV} V) es baja. Aún no se ha alcanzado un valor peligroso, pero podría presentarse retraso para arrancar en entornos fríos.`);
    } else {
        goodPoints.push(`La caída de tensión durante el arranque es mínima (la tensión terminal sigue siendo alta: ${m.minCrankV} V), lo que indica una resistencia interna muy baja y un alto rendimiento al descargar grandes corrientes.`);
    }
}

if (issues.length > 0) {
    diagnosis += `<h4 style="color: #f85149; margin-top: 0;">🚨 Se han detectado anomalías de alto riesgo, se recomienda inspeccionar y reparar en la fábrica:</h4><ul style="margin-top: 5px;">`;
    issues.forEach(issue => diagnosis += `<li>${issue}</li>`);
    diagnosis += `</ul>`;
}

if (warnings.length > 0) {
    diagnosis += `<h4 style="color: #d29922;">⚠️ Elementos que requieren observación continua o mantenimiento:</h4><ul style="margin-top: 5px;">`;
    warnings.forEach(warn => diagnosis += `<li>${warn}</li>`);
    diagnosis += `</ul>`;
}

if (issues.length === 0 && warnings.length === 0) {
                 const diagnosis = `<h4 style="color: #3fb950; margin-top: 0;">✅ El sistema está muy saludable!</h4>`;
                 diagnosis += `<p>El análisis de datos a lo largo de varios días muestra un rendimiento excepcional del sistema eléctrico de su vehículo:</p><ul>`;
                 goodPoints.forEach(pt => diagnosis += `<li>${pt}</li>`);
                 diagnosis += `</ul>`;
                 if (bType === 'lifepo4') {
                     diagnosis += `<p style="color: #58a6ff; font-size: 14px; margin-top: 10px;">💡 <strong>Análisis técnico:</strong> Las características de su batería LiFePO₄ se están desempeñando bien, con una tasa de autodescarga extremadamente baja y una capacidad de descarga instantánea potente, lo que la hace perfecta para el entorno actual de uso del vehículo.</p>`;
                 }
            } else if (goodPoints.length > 0) {
                 diagnosis += `<h4 style="color: #3fb950;">✅ Puntos con buen rendimiento:</h4><ul style="margin-top: 5px;">`;
                 goodPoints.forEach(pt => diagnosis += `<li>${pt}</li>`);
                 diagnosis += `</ul>`;
            }
        }
        document.getElementById('aiDiagnosis').innerHTML = diagnosis;
    }
</script>