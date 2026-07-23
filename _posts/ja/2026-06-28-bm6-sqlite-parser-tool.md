---
layout: post
title:  "BM6 バッテリーテストデータベース (SQLite) パーサー"
lang: ja
date:   2026-06-28 09:30:00
categories: Auto
tags: [自動車バッテリー, バッテリーモニター, DIYツール, データ分析]
description: "BM6 Bluetoothバッテリーモニター専用のSQLiteローカルデータベースパーサー。BM6.sqliteファイルを読み取り、完全な走行履歴、クランキングテスト波形、充電リップルテストを解析し、豊富なズーム可能なチャートと検出統計を提供します。"
keywords: "BM6, SQLite解析, クランキング波形, クランキング電圧, ドライブ検出, 温度分析, 充電リップル, バッテリー監視"
image: /images/bm6-sqlite-preview2.webp
faq:
  - question: "このパーサーは月次記録ファイル分析ツールとどう異なりますか？"
    answer: "このツールは、BM6アプリが携帯電話にローカルに保存する完全なSQLiteデータベースファイルを直接読み取ります。月次履歴電圧と走行ルートを分析できるだけでなく、高周波（100Hz）のエンジン始動テスト電圧波形（クランキング波形）と充電/リップル検出記録も解析できます。"
  - question: "BM6.sqliteファイルはどのように取得できますか？"
    answer: "iPhoneまたはAndroid携帯電話では、ファイル共有またはバックアップソフトウェア（iTunes、iMazing、Androidファイル転送など）を介して、BM6アプリのサンドボックスディレクトリ（Documents）に入ると、BM6.sqliteまたはBM6.dbという名前のデータベースファイルを見つけることができます。"
  - question: "SQLiteファイルをアップロードするとプライバシー漏洩のリスクがありますか？"
    answer: "全くありません。このツールはSQL.jsローカルWebAssembly技術を使用しており、すべてのデータベースの読み込み、クエリ、グラフ描画はブラウザのサンドボックス内で完結し、いかなるデータも外部サーバーに送信されません。"
  - question: "クランキング波形に赤点とオレンジ点があるのはなぜですか？"
    answer: "赤点 (Min) はスターターモーターが作動しているときの最低瞬時電圧を表します。オレンジ点 (Starter) は動的しきい値アルゴリズムによって判定され、スターターモーターの電源が切れてオルタネーターが発電を引き継ぐ瞬間の転換点です。"
---


<style>
    #bm6-sqlite-app-container {
        max-width: 950px;
        margin: 20px auto;
        font-family: 'Segoe UI', 'Microsoft JhengHei', sans-serif;
        background: #0d1117;
        color: #c9d1d9;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        border: 1px solid #30363d;
        position: relative;
    }
    #bm6-sqlite-app-container h2 {
        color: #c9d1d9;
        border-bottom: 1px solid #30363d;
        padding-bottom: 8px;
        margin-top: 25px;
    }
    #bm6-sqlite-app-container .chart-container {
        width: 100%;
        height: 300px;
        margin-top: 10px;
    }
    #bm6-sqlite-app-container .section {
        display: none;
        margin-top: 30px;
    }
    #bm6-sqlite-app-container .stats-grid {
        display: none;
        grid-template-columns: repeat(4, 1fr);
        gap: 15px;
        margin-bottom: 25px;
    }
    #bm6-sqlite-app-container .stat-card {
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.2);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    #bm6-sqlite-app-container .stat-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 15px rgba(0,0,0,0.4);
    }
    @media (max-width: 768px) {
        #bm6-sqlite-app-container .stats-grid {
            grid-template-columns: repeat(2, 1fr);
        }
    }
    @media (max-width: 480px) {
        #bm6-sqlite-app-container .stats-grid {
            grid-template-columns: 1fr;
        }
    }
    #bm6-sqlite-app-container .stats-grid-2 {
        display: none;
        grid-template-columns: repeat(2, 1fr);
        gap: 15px;
        margin-bottom: 25px;
    }
    @media (max-width: 480px) {
        #bm6-sqlite-app-container .stats-grid-2 {
            grid-template-columns: 1fr;
        }
    }
    #bm6-sqlite-app-container table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 15px;
        table-layout: fixed;
        word-wrap: break-word;
        color: #c9d1d9;
        border: 1px solid #30363d;
    }
    #bm6-sqlite-app-container th, #bm6-sqlite-app-container td {
        padding: 12px;
        border: 1px solid #30363d;
        text-align: left;
    }
    #bm6-sqlite-app-container th {
        background-color: #21262d;
        color: #c9d1d9;
    }
    #bm6-sqlite-app-container tr:nth-child(even) {
        background-color: #161b22;
    }
    #bm6-sqlite-app-container tr:nth-child(odd) {
        background-color: #0d1117;
    }
</style>

<div id="bm6-sqlite-app-container">

    <h2 id="ui-title" style="text-align: center; color: #c9d1d9; margin-bottom: 10px; margin-top: 10px;">BM6 バッテリーテストデータベース (SQLite) パーサー</h2>
    
    <div class="upload-section" style="margin-bottom: 30px; padding: 20px; background: #161b22; border-radius: 8px; border: 2px dashed #1f6feb; text-align: center;">
        <p><b>BM6.sqlite</b> ファイルを選択してください（データはすべてお使いのコンピューターで処理され、アップロードされません）：</p>
        <input type="file" id="dbfile" accept=".sqlite,.db" style="color: #c9d1d9;">
    </div>

    <div id="filter-section" style="display: none; background: #161b22; padding: 20px; border-radius: 8px; margin-bottom: 30px; border: 1px solid #30363d; text-align: center;">
        <div style="display: flex; gap: 20px; flex-wrap: wrap; align-items: center; justify-content: center;">
            <div style="display: flex; align-items: center; gap: 8px;">
                <label style="font-weight: bold; color: #c9d1d9;">デバイスを選択 (MAC)：</label>
                <select id="deviceSelector" style="padding: 8px 12px; border-radius: 8px; border: 1px solid #30363d; font-size: 14px; background: #0d1117; color: #c9d1d9; min-width: 180px;"></select>
            </div>
            <div style="display: flex; align-items: center; gap: 8px;">
                <label style="font-weight: bold; color: #c9d1d9;">月を選択：</label>
                <select id="monthSelector" style="padding: 8px 12px; border-radius: 8px; border: 1px solid #30363d; font-size: 14px; background: #0d1117; color: #c9d1d9; min-width: 140px;"></select>
            </div>
        </div>
    </div>

    <div id="history-section" class="section">
        <h2>📈 履歴月次データと走行分析</h2>
        <div style="background: rgba(210, 153, 34, 0.1); padding: 15px 20px; border-radius: 10px; margin-bottom: 25px; border-left: 5px solid #d29922; font-size: 14.5px; line-height: 1.6; color: #8b949e;">
            <strong style="color: #d29922;">履歴走行分析</strong><br>
            <span>履歴電圧と温度変動を自動解析し、走行ルートを識別してオルタネーターとバッテリーの健康状態を統計します。スクロールホイール/ピンチズームとドラッグパンに対応。</span>
        </div>

        <div style="background: #161b22; border: 1px solid #30363d; padding: 15px 25px; border-radius: 10px; margin-bottom: 25px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px;">
            <div style="display: flex; gap: 10px; align-items: center;">
                <label style="font-weight: bold; color: #c9d1d9; font-size: 14px;">表示範囲：</label>
                <select id="dateSelector" style="padding: 8px 12px; border-radius: 8px; border: 1px solid #30363d; font-size: 14px; min-width: 160px; cursor: pointer; background: #0d1117; color: #c9d1d9;">
                    <option value="all">-- 全て表示 --</option>
                </select>
            </div>
        </div>

        <div id="stats-container" class="stats-grid">
            <div class="stat-card" style="background: rgba(31, 111, 235, 0.1); border: 1px solid rgba(31, 111, 235, 0.3);">
                <div style="font-size: 13px; color: #58a6ff; margin-bottom: 5px; font-weight: 500;">総走行回数</div>
                <div id="stat-trips" style="font-size: 24px; font-weight: bold; color: #79c0ff;">0</div>
            </div>
            <div class="stat-card" style="background: rgba(35, 134, 54, 0.1); border: 1px solid rgba(35, 134, 54, 0.3);">
                <div style="font-size: 13px; color: #3fb950; margin-bottom: 5px; font-weight: 500;">総走行時間</div>
                <div id="stat-time" style="font-size: 24px; font-weight: bold; color: #56d364;">0 <span style="font-size: 12px; font-weight: normal;">分</span></div>
            </div>
            <div class="stat-card" style="background: rgba(227, 76, 38, 0.1); border: 1px solid rgba(227, 76, 38, 0.3);">
                <div style="font-size: 13px; color: #f0883e; margin-bottom: 5px; font-weight: 500;">最低電圧 (冷間時)</div>
                <div id="stat-minv" style="font-size: 24px; font-weight: bold; color: #ff945e;">0.00 <span style="font-size: 12px; font-weight: normal;">V</span></div>
            </div>
            <div class="stat-card" style="background: rgba(137, 87, 229, 0.1); border: 1px solid rgba(137, 87, 229, 0.3);">
                <div style="font-size: 13px; color: #a371f7; margin-bottom: 5px; font-weight: 500;">走行平均電圧 (オルタネーター)</div>
                <div id="stat-avgv" style="font-size: 24px; font-weight: bold; color: #d2a8ff;">0.00 <span style="font-size: 12px; font-weight: normal;">V</span></div>
            </div>
        </div>

        <div style="background: #161b22; padding: 15px; border-radius: 10px; border: 1px solid #30363d; margin-bottom: 25px;">
            <div style="height: 280px; width: 100%; margin-bottom: 10px;">
                <canvas id="voltageChart"></canvas>
            </div>
            <div style="height: 280px; width: 100%;">
                <canvas id="tempChart"></canvas>
            </div>
        </div>

        <div id="trip-section" style="margin-top: 20px; padding: 15px; background: #161b22; border-radius: 10px; border: 1px dashed #30363d; display: none; margin-bottom: 30px;">
            <h3 id="ui-trip-title" style="color: #c9d1d9; font-size: 16px; margin-top: 0; margin-bottom: 15px;">検出された走行</h3>
            <div id="trip-list" style="display: flex; flex-direction: column; gap: 8px;"></div>
        </div>
    </div>

    <div id="charging-section" class="section">
        <h2>⚡ 充電とリップルテスト記録</h2>
        <p>この表には、アイドル/高速充電電圧、ダイオードリップル電圧などのデータが記録されています。</p>
        <table id="charging-table">
            <thead>
                <tr>
                    <th style="width: 25%;">デバイスと時間情報</th>
                    <th style="width: 75%;">解析された主要データ (アプリと同期)</th>
                </tr>
            </thead>
            <tbody></tbody>
        </table>
    </div>

    <div id="cranking-section" class="section">
        <h2>🚗 クランキングテスト波形</h2>
        <p>この表には高周波の電圧変動値が記録されており、自動的にグラフ化されています。</p>
        <div id="cranking-stats-container" class="stats-grid-2">
            <div class="stat-card" style="background: rgba(31, 111, 235, 0.1); border: 1px solid rgba(31, 111, 235, 0.3);">
                <div style="font-size: 13px; color: #58a6ff; margin-bottom: 5px; font-weight: 500;">平均クランキング時間</div>
                <div id="stat-avg-crank-time" style="font-size: 24px; font-weight: bold; color: #79c0ff;">0.00 <span style="font-size: 12px; font-weight: normal;">秒</span></div>
            </div>
            <div class="stat-card" style="background: rgba(227, 76, 38, 0.1); border: 1px solid rgba(227, 76, 38, 0.3);">
                <div style="font-size: 13px; color: #f0883e; margin-bottom: 5px; font-weight: 500;">平均クランキング電圧</div>
                <div id="stat-avg-crank-vol" style="font-size: 24px; font-weight: bold; color: #ff945e;">0.00 <span style="font-size: 12px; font-weight: normal;">V</span></div>
            </div>
        </div>
        <div id="cranking-content"></div>
    </div>

</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.8.0/sql-wasm.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-adapter-date-fns"></script>
<script src="https://cdn.jsdelivr.net/npm/hammerjs"></script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-zoom"></script>

<script>

    let SQL;
    let currentDb = null;
    let selectedDevice = "";
    let selectedMonth = "all";
    
    // SQL.jsを初期化
    initSqlJs({ locateFile: file => `https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.8.0/${file}` }).then(function(sqlModule){
        SQL = sqlModule;
    });

    document.getElementById('dbfile').addEventListener('change', function(event) {
        const file = event.target.files[0];
        if (!file) return;

        const reader = new FileReader();
        reader.onload = function() {
            if(!SQL) {
                alert("SQL.jsがまだ読み込み中です。しばらくお待ちください。");
                return;
            }
            
            try {
                const Uints = new Uint8Array(reader.result);
                currentDb = new SQL.Database(Uints);
                
                initDeviceSelector(currentDb);
                
            } catch (err) {
                alert("データベースの読み込みに失敗しました。ファイルが正しいか確認してください。エラーメッセージ：" + err.message);
            }
        };
        reader.readAsArrayBuffer(file);
    });

    // 軽量なAppleバイナリPlist (bplist00) とNSKeyedArchiverパーサー
    function parseBPlist(uint8Array) {
        if (!uint8Array || uint8Array.length < 40) return null;
        
        const buffer = uint8Array.buffer;
        const offset = uint8Array.byteOffset;
        const len = uint8Array.byteLength;
        const view = new DataView(buffer, offset, len);
        
        const header = String.fromCharCode(...uint8Array.slice(0, 8));
        if (header !== 'bplist00') return null;
        
        const trailerOffset = len - 32;
        const offsetIntSize = view.getUint8(trailerOffset + 6);
        const objectRefSize = view.getUint8(trailerOffset + 7);
        const numObjects = view.getUint32(trailerOffset + 12);
        const topObject = view.getUint32(trailerOffset + 20);
        const offsetTableOffset = view.getUint32(trailerOffset + 28);
        
        const offsets = [];
        for (let i = 0; i < numObjects; i++) {
            const ptr = offsetTableOffset + i * offsetIntSize;
            let val = 0;
            if (offsetIntSize === 1) val = view.getUint8(ptr);
            else if (offsetIntSize === 2) val = view.getUint16(ptr);
            else if (offsetIntSize === 4) val = view.getUint32(ptr);
            else if (offsetIntSize === 8) val = view.getUint32(ptr + 4);
            offsets.push(val);
        }
        
        function parseObject(objIndex) {
            if (objIndex >= offsets.length) return null;
            const objOffset = offsets[objIndex];
            const marker = view.getUint8(objOffset);
            const type = marker & 0xF0;
            const info = marker & 0x0F;
            
            if (marker === 0x00) return null;
            if (marker === 0x08) return false;
            if (marker === 0x09) return true;
            
            if (type === 0x10) {
                const bytes = 1 << info;
                if (bytes === 1) return view.getUint8(objOffset + 1);
                if (bytes === 2) return view.getUint16(objOffset + 1);
                if (bytes === 4) return view.getUint32(objOffset + 1);
                if (bytes === 8) return Number(view.getBigInt64(objOffset + 1));
            }
            
            if (type === 0x20) {
                const bytes = 1 << info;
                if (bytes === 4) return view.getFloat32(objOffset + 1);
                if (bytes === 8) return view.getFloat64(objOffset + 1);
            }
            
            if (type === 0x80) {
                const bytes = info + 1;
                let val = 0;
                for (let i = 0; i < bytes; i++) {
                    val = (val << 8) | view.getUint8(objOffset + 1 + i);
                }
                return { '$UID': val };
            }
            
            if (type === 0x50) {
                let length = info;
                let strOffset = 1;
                if (info === 0x0F) {
                    const lenMarker = view.getUint8(objOffset + 1);
                    const lenBytes = 1 << (lenMarker & 0x0F);
                    if (lenBytes === 1) length = view.getUint8(objOffset + 2);
                    else if (lenBytes === 2) length = view.getUint16(objOffset + 2);
                    else if (lenBytes === 4) length = view.getUint32(objOffset + 2);
                    strOffset = 2 + lenBytes;
                }
                const chars = [];
                for (let i = 0; i < length; i++) {
                    chars.push(String.fromCharCode(view.getUint8(objOffset + strOffset + i)));
                }
                return chars.join('');
            }
            
            if (type === 0x60) {
                let length = info;
                let strOffset = 1;
                if (info === 0x0F) {
                    const lenMarker = view.getUint8(objOffset + 1);
                    const lenBytes = 1 << (lenMarker & 0x0F);
                    if (lenBytes === 1) length = view.getUint8(objOffset + 2);
                    else if (lenBytes === 2) length = view.getUint16(objOffset + 2);
                    else if (lenBytes === 4) length = view.getUint32(objOffset + 2);
                    strOffset = 2 + lenBytes;
                }
                const chars = [];
                for (let i = 0; i < length; i++) {
                    chars.push(String.fromCharCode(view.getUint16(objOffset + strOffset + i * 2)));
                }
                return chars.join('');
            }
            
            if (type === 0xA0) {
                let length = info;
                let arrOffset = 1;
                if (info === 0x0F) {
                    const lenMarker = view.getUint8(objOffset + 1);
                    const lenBytes = 1 << (lenMarker & 0x0F);
                    if (lenBytes === 1) length = view.getUint8(objOffset + 2);
                    else if (lenBytes === 2) length = view.getUint16(objOffset + 2);
                    else if (lenBytes === 4) length = view.getUint32(objOffset + 2);
                    arrOffset = 2 + lenBytes;
                }
                const arr = [];
                for (let i = 0; i < length; i++) {
                    const ptr = objOffset + arrOffset + i * objectRefSize;
                    let ref = 0;
                    if (objectRefSize === 1) ref = view.getUint8(ptr);
                    else if (objectRefSize === 2) ref = view.getUint16(ptr);
                    else if (objectRefSize === 4) ref = view.getUint32(ptr);
                    arr.push(parseObject(ref));
                }
                return arr;
            }
            
            if (type === 0xD0) {
                let length = info;
                let dictOffset = 1;
                if (info === 0x0F) {
                    const lenMarker = view.getUint8(objOffset + 1);
                    const lenBytes = 1 << (lenMarker & 0x0F);
                    if (lenBytes === 1) length = view.getUint8(objOffset + 2);
                    else if (lenBytes === 2) length = view.getUint16(objOffset + 2);
                    else if (lenBytes === 4) length = view.getUint32(objOffset + 2);
                    dictOffset = 2 + lenBytes;
                }
                const keys = [];
                const values = [];
                for (let i = 0; i < length; i++) {
                    const ptr = objOffset + dictOffset + i * objectRefSize;
                    let keyRef = 0;
                    if (objectRefSize === 1) keyRef = view.getUint8(ptr);
                    else if (objectRefSize === 2) keyRef = view.getUint16(ptr);
                    else if (objectRefSize === 4) keyRef = view.getUint32(ptr);
                    keys.push(parseObject(keyRef));
                }
                for (let i = 0; i < length; i++) {
                    const ptr = objOffset + dictOffset + (length + i) * objectRefSize;
                    let valRef = 0;
                    if (objectRefSize === 1) valRef = view.getUint8(ptr);
                    else if (objectRefSize === 2) valRef = view.getUint16(ptr);
                    else if (objectRefSize === 4) valRef = view.getUint32(ptr);
                    values.push(parseObject(valRef));
                }
                const dict = {};
                for (let i = 0; i < length; i++) {
                    dict[keys[i]] = values[i];
                }
                return dict;
            }
            
            return null;
        }
        
        function resolveUid(uid, objects) {
            const obj = objects[uid];
            if (obj && typeof obj === 'object') {
                if (obj['$UID'] !== undefined) {
                    return resolveUid(obj['$UID'], objects);
                }
                const resolved = Array.isArray(obj) ? [] : {};
                for (const key in obj) {
                    if (key === '$class') continue;
                    const val = obj[key];
                    if (val && typeof val === 'object' && val['$UID'] !== undefined) {
                        resolved[key] = resolveUid(val['$UID'], objects);
                    } else if (Array.isArray(val)) {
                        resolved[key] = val.map(item => (item && item['$UID'] !== undefined) ? resolveUid(item['$UID'], objects) : item);
                    } else {
                        resolved[key] = val;
                    }
                }
                return resolved;
            }
            return obj;
        }

        const rootObj = parseObject(topObject);
        if (rootObj && rootObj['$archiver'] === 'NSKeyedArchiver') {
            const objects = rootObj['$objects'];
            if (Array.isArray(objects)) {
                const rootUid = rootObj['$top'] && rootObj['$top']['root'] ? rootObj['$top']['root']['$UID'] : null;
                if (rootUid !== null && rootUid !== undefined) {
                    return resolveUid(rootUid, objects);
                }
            }
        }
        return rootObj;
    }

    // tbl_charging (リップルと充電) を処理
    function parseChargingTable(db, serial, month) {
        document.getElementById('charging-section').style.display = 'block';
        const tbody = document.querySelector('#charging-table tbody');
        tbody.innerHTML = '';

        try {
            // tbl_chargingでは、列名は'mac'ではなく'serial'
            let sql = `SELECT * FROM tbl_charging WHERE serial = '${serial}'`;
            if (month && month !== 'all') {
                sql += ` AND day LIKE '${month}%'`;
            }
            sql += ` ORDER BY rowid DESC LIMIT 20`;

            const res = db.exec(sql);
            if (res.length === 0) {
                tbody.innerHTML = '<tr><td colspan="2">このデバイス/月には充電テスト記録がありません。</td></tr>';
                return;
            }

            const columns = res[0].columns;
            const values = res[0].values;
            const dataIndex = columns.indexOf('data');
            const macIndex = columns.indexOf('serial') !== -1 ? columns.indexOf('serial') : columns.indexOf('mac');
            const timelineIdx = columns.indexOf('timeline');
            const dayIdx = columns.indexOf('day');

            values.forEach(row => {
                const tr = document.createElement('tr');
                const blob = row[dataIndex];
                const mac = row[macIndex] || "不明なデバイス";
                
                let date = "不明な時間";
                if (timelineIdx !== -1 && row[timelineIdx]) {
                    const ts = parseInt(row[timelineIdx]);
                    if (!isNaN(ts)) {
                        const dateObj = new Date(ts * 1000);
                        const yyyy = dateObj.getFullYear();
                        const mm = String(dateObj.getMonth() + 1).padStart(2, '0');
                        const dd = String(dateObj.getDate()).padStart(2, '0');
                        const hh = String(dateObj.getHours()).padStart(2, '0');
                        const min = String(dateObj.getMinutes()).padStart(2, '0');
                        const ss = String(dateObj.getSeconds()).padStart(2, '0');
                        date = `${yyyy}-${mm}-${dd} ${hh}:${min}:${ss}`;
                    }
                } else if (dayIdx !== -1 && row[dayIdx]) {
                    date = row[dayIdx];
                }
                
                let rippleVolStr = "データなし";
                let loadVolStr = "データなし";
                let noLoadVolStr = "データなし";
                let parseSuccess = false;

                if (blob) {
                    try {
                        const parsedData = parseBPlist(blob);
                        if (parsedData) {
                            // 1. ダイオードリップル電圧 (Ripple) と単位変換 (V -> mV) を処理
                            if (parsedData.rippleVol !== undefined) {
                                let rVal = Number(parsedData.rippleVol);
                                // データが1未満の場合 (例: 0.001 V)、ミリボルト (1 mV) に変換
                                if (rVal > 0 && rVal < 1) {
                                    rVal = rVal * 1000;
                                }
                                rippleVolStr = `${rVal.toFixed(0)} mV`;
                            }

                            // 2. 高速充電電圧 (Load) を処理
                            loadVolStr = parsedData.loadVol !== undefined ? `${Number(parsedData.loadVol).toFixed(2)} V` : "データなし";
                            
                            // 3. アイドル充電電圧 (NoLoad) を処理
                            noLoadVolStr = parsedData.noLoadVol !== undefined ? `${Number(parsedData.noLoadVol).toFixed(2)} V` : "データなし";
                            
                            parseSuccess = true;
                        }
                    } catch (err) {
                        console.error("bplist解析失敗:", err);
                    }
                }

                tr.innerHTML = `
                    <td>
                        <b>MAC:</b> ${mac} <br>
                        <b>時間:</b> ${date}
                    </td>
                    <td>
                        <b>アイドル充電電圧 (NoLoad):</b> <span style="color:#58a6ff; font-weight:bold;">${noLoadVolStr}</span> <br>
                        <b>高速充電電圧 (Load):</b> <span style="color:#3fb950; font-weight:bold;">${loadVolStr}</span> <br>
                        <b>ダイオードリップル電圧 (Ripple):</b> <span style="color:#d2a8ff; font-weight:bold;">${rippleVolStr}</span> <br>
                        <small style="color:gray;">解析状態: ${parseSuccess ? "🟢 成功的に解析" : "🔴 解析失敗"}</small>
                    </td>
                `;
                tbody.appendChild(tr);
            });
        } catch (e) {
            tbody.innerHTML = `<tr><td colspan="2">解析エラー: ${e.message}</td></tr>`;
        }
    }

    function getLocalMinima(arr) {
        let minima = [];
        for (let i = 1; i < arr.length - 1; i++) {
            if (arr[i] < arr[i - 1] && arr[i] < arr[i + 1]) minima.push(i);
        }
        return minima;
    }

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
            chart.options.scales.y.min = Math.floor(minV * 5) / 5;
            chart.options.scales.y.max = Math.ceil(maxV * 5) / 5;
        }
    }

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

    // tbl_cranking (クランキング波形) を処理
    function parseCrankingTable(db, serial, month) {
        document.getElementById('cranking-section').style.display = 'block';
        const container = document.getElementById('cranking-content');
        container.innerHTML = '';

        // チャートのデフォルト設定
        Chart.defaults.color = '#8b949e';
        Chart.defaults.borderColor = '#30363d';

        try {
            let sql = `SELECT * FROM tbl_cranking WHERE serial = '${serial}'`;
            if (month && month !== 'all') {
                sql += ` AND day LIKE '${month}%'`;
            }
            sql += ` ORDER BY rowid DESC`;

            const res = db.exec(sql);
            if (res.length === 0) {
                container.innerHTML = '<p>このデバイス/月にはクランキング波形記録がありません。</p>';
                document.getElementById('cranking-stats-container').style.display = 'none';
                return;
            }

            const columns = res[0].columns;
            const values = res[0].values;

            let totalCrankVol = 0;
            let totalCrankTime = 0;
            let validCrankCount = 0;
            
            const arrayIndex = columns.indexOf('valueArray') !== -1 ? columns.indexOf('valueArray') : columns.indexOf('data');
            const dateIndex = columns.indexOf('date');
            const tempIndex = columns.indexOf('temp');
            const timelineIndex = columns.indexOf('timeline');

            values.forEach((row, index) => {
                const rawArray = row[arrayIndex];
                let extractedNumbers = [];
                let parsedData = null;
                
                if (rawArray) {
                    try {
                        parsedData = parseBPlist(rawArray);
                        if (parsedData && parsedData.valueArray) {
                            let valArr = parsedData.valueArray;
                            if (valArr['NS.objects']) {
                                valArr = valArr['NS.objects'];
                            }
                            extractedNumbers = valArr.map(n => parseFloat(n));
                        }
                    } catch (err) {
                        console.error("bplist解析失敗:", err);
                    }
                }

                if (extractedNumbers.length > 0) {
                    let voltages = extractedNumbers;
                    let times = voltages.map((_, i) => i * 0.01);
                    let chartData = voltages.map((v, i) => ({ x: i * 0.01, y: v }));

                    // 1. 最低点 (Min Cranking)
                    let minVol = Math.min(...voltages);
                    let minIdx = voltages.indexOf(minVol);
                    let localMins = getLocalMinima(voltages);

                    // 2. 動的上昇点 (Dynamic Threshold) 
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

                    // 3. スターターモーター解除点 (Starter Disengaged)
                    let validMinsForStarter = localMins.filter(idx => idx >= minIdx && idx < climbIdx);
                    let starterIdx = validMinsForStarter.length > 0 ? validMinsForStarter[validMinsForStarter.length - 1] : minIdx;

                    const minPoint = { x: times[minIdx], y: voltages[minIdx] };
                    const starterPoint = { x: times[starterIdx], y: voltages[starterIdx] };

                    // 起動時間と累積統計の計算 (スターターモーター解除/オレンジ点まで)
                    let startIdx = minIdx;
                    while (startIdx > 0 && voltages[startIdx] < vInitial - 0.15) {
                        startIdx--;
                    }
                    const crankingDuration = (starterIdx - startIdx) * 0.01;

                    totalCrankVol += minVol;
                    totalCrankTime += crankingDuration;
                    validCrankCount++;

                    // ラベル描画プラグイン
                    const pointLabelsPlugin = {
                        id: 'pointLabels',
                        afterDraw: chart => {
                            const ctx = chart.ctx;
                            const meta = chart.getDatasetMeta(1); // スキャッターデータセット
                            if (!meta.hidden && meta.data.length >= 2) {
                                ctx.save();
                                ctx.font = 'bold 12px "Segoe UI", sans-serif';
                                ctx.fillStyle = '#c9d1d9';
                                ctx.textBaseline = 'middle'; 

                                // Minラベル
                                const ptMin = meta.data[0];
                                if (ptMin.x >= chart.chartArea.left && ptMin.x <= chart.chartArea.right) {
                                    ctx.textAlign = 'left';
                                    ctx.fillText(`Min: ${minPoint.y.toFixed(2)}V`, ptMin.x + 10, ptMin.y);
                                }
                                
                                // Starterラベル
                                const ptStarter = meta.data[1];
                                if (ptStarter.x >= chart.chartArea.left && ptStarter.x <= chart.chartArea.right) {
                                    ctx.textAlign = 'left';
                                    ctx.fillText(` Starter: ${starterPoint.y.toFixed(2)}V`, ptStarter.x + 10, ptStarter.y);
                                }
                                ctx.restore();
                            }
                        }
                    };

                    // UIコンテナの作成
                    const wrapperDiv = document.createElement('div');
                    wrapperDiv.style.cssText = "background: #161b22; padding: 15px; border-radius: 10px; border: 1px solid #30363d; width: 100%; box-sizing: border-box; margin-bottom: 20px;";
                    
                    let dateStr = "";
                    let ts = null;
                    if (timelineIndex !== -1 && row[timelineIndex]) {
                        ts = parseInt(row[timelineIndex]);
                    } else if (parsedData && parsedData.timeline) {
                        ts = parseInt(parsedData.timeline);
                    }
                    if (ts && !isNaN(ts)) {
                        const dateObj = new Date(ts * 1000);
                        const yyyy = dateObj.getFullYear();
                        const mm = String(dateObj.getMonth() + 1).padStart(2, '0');
                        const dd = String(dateObj.getDate()).padStart(2, '0');
                        const hh = String(dateObj.getHours()).padStart(2, '0');
                        const min = String(dateObj.getMinutes()).padStart(2, '0');
                        const ss = String(dateObj.getSeconds()).padStart(2, '0');
                        dateStr = `${yyyy}-${mm}-${dd} ${hh}:${min}:${ss}`;
                    }

                    let eventTemp = null;
                    const serialIndex = columns.indexOf('serial');
                    if (serialIndex !== -1 && row[serialIndex] && ts) {
                        const serial = row[serialIndex];
                        try {
                            const tempRes = db.exec(`
                                SELECT temp FROM history 
                                WHERE serial = '${serial}' 
                                ORDER BY ABS(timeline - ${ts}) 
                                LIMIT 1
                            `);
                            if (tempRes.length > 0 && tempRes[0].values.length > 0) {
                                eventTemp = tempRes[0].values[0][0];
                            }
                        } catch (tempErr) {
                            console.error("履歴温度のクエリに失敗しました:", tempErr);
                        }
                    }

                    let titleText = `クランキング波形分析 - 始動時間: ${crankingDuration.toFixed(2)}秒 - `;
                    if (dateStr) {
                        titleText += ` (時間: ${dateStr})`;
                    } else if (dateIndex !== -1 && row[dateIndex]) {
                        titleText += ` 時間: ${row[dateIndex]}`;
                    }
                    if (eventTemp !== null && eventTemp !== undefined) {
                        titleText += ` (温度: ${eventTemp}°C)`;
                    } else if (tempIndex !== -1 && row[tempIndex] !== undefined) {
                        titleText += ` (温度: ${row[tempIndex]}°C)`;
                    }
                    titleText += ` (初期: ${vInitial.toFixed(2)}V)`;

                    const titleElement = document.createElement('div');
                    titleElement.style.cssText = "color: #c9d1d9; font-size: 16px; font-weight: bold; text-align: center; margin-bottom: 15px;";
                    titleElement.innerText = titleText;
                    wrapperDiv.appendChild(titleElement);

                    const canvasDiv = document.createElement('div');
                    canvasDiv.style.cssText = "width: 100%; height: 400px; position: relative;";
                    
                    const canvas = document.createElement('canvas');
                    canvas.id = `chart-${index}`;
                    canvasDiv.appendChild(canvas);
                    wrapperDiv.appendChild(canvasDiv);
                    container.appendChild(wrapperDiv);

                    const ctx = canvas.getContext('2d');
                    new Chart(ctx, {
                        type: 'line',
                        data: {
                            datasets: [
                                {
                                    label: '電圧 (V)',
                                    data: chartData,
                                    borderColor: '#58a6ff',
                                    borderWidth: 2,
                                    pointRadius: 0,
                                    tension: 0.2,
                                    order: 2
                                },
                                {
                                    label: '主要ポイント',
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
                                        title: function(tooltipItems) {
                                            if (tooltipItems.length > 0) {
                                                const item = tooltipItems[0];                                
                                                return `電圧: ${item.parsed.y}V`;
                                            }
                                            return '';
                                        },
                                        label: function(context) {
                                            if (context.dataIndex !== context.chart.tooltip.dataPoints[0].dataIndex || 
                                                context.datasetIndex !== context.chart.tooltip.dataPoints[0].datasetIndex) {
                                                return null;
                                            }
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
                } else {
                    const wrapper = document.createElement('div');
                    wrapper.innerHTML = `<h3>テスト記録 #${row[0] || index + 1}</h3><p style="color:red; margin: 15px 0;">この記録から連続した電圧値を解析できませんでした。</p><hr>`;
                    container.appendChild(wrapper);
                }
            });

            if (validCrankCount > 0) {
                const avgCrankVol = (totalCrankVol / validCrankCount).toFixed(2);
                const avgCrankTime = (totalCrankTime / validCrankCount).toFixed(2);
                document.getElementById('stat-avg-crank-time').innerHTML = `${avgCrankTime} <span style="font-size:12px; font-weight:normal;">秒</span>`;
                document.getElementById('stat-avg-crank-vol').innerHTML = `${avgCrankVol} <span style="font-size:12px; font-weight:normal;">V</span>`;
                document.getElementById('cranking-stats-container').style.display = 'grid';
            } else {
                document.getElementById('cranking-stats-container').style.display = 'none';
            }

        } catch (e) {
            container.innerHTML = `<p>読み込み失敗: ${e.message}</p>`;
            document.getElementById('cranking-stats-container').style.display = 'none';
        }
    }

    let vChart, tChart;
    let allData = [];
    let globalDetectedTrips = { trips: [], mode: "" };
    let isResetting = false; 

    function initHistoryCharts() {
        if (vChart && tChart) return;
        vChart = new Chart(document.getElementById('voltageChart'), createChartConfig('電圧 (V)', '#58a6ff', '電圧 (V)'));
        tChart = new Chart(document.getElementById('tempChart'), createChartConfig('温度 (℃)', '#f85149', '温度 (℃)'));
    }

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
                interaction: {
                    mode: 'index',
                    intersect: false,
                },
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

    function syncCharts({chart}) {
        if (isResetting) return;
        const other = (chart === vChart) ? tChart : vChart;
        other.options.scales.x.min = chart.scales.x.min;
        other.options.scales.x.max = chart.scales.x.max;
        autoScaleYHistory(chart); autoScaleYHistory(other);
        chart.update('none'); other.update('none');
    }

    function parseHistoryTable(db, serial, month) {
        document.getElementById('history-section').style.display = 'block';
        initHistoryCharts();

        try {
            let sql = `SELECT timeline, vol, temp FROM history WHERE serial = '${serial}'`;
            if (month && month !== 'all') {
                const parts = month.split('-');
                const yyyy = parseInt(parts[0]);
                const mm = parseInt(parts[1]);
                const startTs = Math.floor(new Date(yyyy, mm - 1, 1).getTime() / 1000);
                const endTs = Math.floor(new Date(yyyy, mm, 1).getTime() / 1000);
                sql += ` AND timeline >= ${startTs} AND timeline < ${endTs}`;
            }
            sql += ` ORDER BY timeline ASC`;

            const res = db.exec(sql);
            if (res.length === 0) {
                resetViewAndUpdateData([], 'all');
                document.getElementById('dateSelector').innerHTML = '<option value="all">-- 日付なし --</option>';
                return;
            }

            const columns = res[0].columns;
            const values = res[0].values;
            
            const timelineIdx = columns.indexOf('timeline');
            const volIdx = columns.indexOf('vol');
            const tempIdx = columns.indexOf('temp');

            let extracted = [];
            let dates = new Set();

            values.forEach(row => {
                const ts = row[timelineIdx];
                const vVal = parseFloat(row[volIdx]);
                const tVal = parseFloat(row[tempIdx]);
                
                if (ts && !isNaN(vVal)) {
                    const timeMs = ts * 1000;
                    const dateObj = new Date(timeMs);
                    const yyyy = dateObj.getFullYear();
                    const mm = String(dateObj.getMonth() + 1).padStart(2, '0');
                    const dd = String(dateObj.getDate()).padStart(2, '0');
                    const hh = String(dateObj.getHours()).padStart(2, '0');
                    const min = String(dateObj.getMinutes()).padStart(2, '0');
                    const timeStr = `${yyyy}-${mm}-${dd} ${hh}:${min}`;

                    extracted.push({
                        x: timeMs,
                        xStr: timeStr,
                        v: vVal,
                        t: tVal
                    });
                    dates.add(timeStr.split(' ')[0]);
                }
            });

            allData = extracted.sort((a, b) => a.x - b.x);
            globalDetectedTrips = detectTripsByCurve(allData);

            const dateSelector = document.getElementById('dateSelector');
            dateSelector.innerHTML = '<option value="all">-- 全て表示 --</option>';
            Array.from(dates).sort().forEach(d => {
                const opt = document.createElement('option');
                opt.value = d;
                opt.innerText = d;
                dateSelector.appendChild(opt);
            });

            resetViewAndUpdateData(allData, 'all');
            
            dateSelector.onchange = function() {
                const filtered = (this.value === 'all') ? allData : allData.filter(d => d.xStr.startsWith(this.value));
                resetViewAndUpdateData(filtered, this.value);
            };

        } catch (e) {
            console.error("履歴の解析に失敗しました:", e);
        }
    }

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
        return { trips: mergedTrips, mode: isLiFePO4 ? "LiFePO4" : "Lead-Acid" };
    }

    function updateStatCards(filteredData, result) {
        const statsContainer = document.getElementById('stats-container');
        if (!filteredData || filteredData.length === 0) { statsContainer.style.display = 'none'; return; }
        statsContainer.style.display = 'grid';

        document.getElementById('stat-trips').innerText = result.trips.length;
        const totalMins = result.trips.reduce((acc, t) => acc + t.duration, 0);
        document.getElementById('stat-time').innerHTML = `${totalMins} <span style="font-size:12px;">分</span>`;

        const minV = Math.min(...filteredData.map(d => d.v));
        const minVElement = document.getElementById('stat-minv');
        minVElement.innerHTML = `${minV.toFixed(2)} <span style="font-size:12px;">V</span>`;
        minVElement.style.color = minV < 12.6 ? "#f85149" : "#ff945e";

        let drivePoints = 0, sumV = 0;
        filteredData.forEach(d => {
            const isDriving = result.trips.some(t => {
                return d.x >= t.start && d.x <= t.end;
            });
            if (isDriving) { drivePoints++; sumV += d.v; }
        });
        document.getElementById('stat-avgv').innerHTML = `${drivePoints > 0 ? (sumV / drivePoints).toFixed(2) : "N/A"} <span style="font-size:12px;">V</span>`;
    }

    function renderTrips(result) {
        const tripSection = document.getElementById('trip-section');
        const tripList = document.getElementById('trip-list');
        tripList.innerHTML = '';
        if (!result.trips || result.trips.length === 0) { tripSection.style.display = 'none'; return; }
        tripSection.style.display = 'block';
        
        const modeSuffix = result.mode === 'LiFePO4' ? ' [LiFePO4モード]' : ' [鉛酸 / 充電制御モード]';
        document.getElementById('ui-trip-title').innerText = '検出された走行' + modeSuffix;

        result.trips.forEach((t, i) => {
            const rowDiv = document.createElement('div');
            rowDiv.style.cssText = "display: flex; align-items: center; justify-content: space-between; background: #0d1117; padding: 10px 16px; border-radius: 8px; border: 1px solid #30363d; margin-bottom: 8px;";
            rowDiv.innerHTML = `<span style="font-size: 14px; color: #c9d1d9;"><b style="color:#58a6ff;">走行 ${i+1}</b>：${t.startStr} ~ ${t.endStr} (所要時間 ${t.duration} 分)</span>`;

            const btn = document.createElement('button');
            btn.innerHTML = '🔍 チャートズーム';
            btn.style.cssText = "background: #21262d; border: 1px solid #30363d; color: #58a6ff; padding: 5px 15px; border-radius: 6px; cursor: pointer; font-size: 13px; font-weight: bold; transition: 0.2s; white-space: nowrap;";
            btn.onclick = () => {
                const s = t.start - 600000, e = t.end + 600000;
                [vChart, tChart].forEach(c => { c.options.scales.x.min = s; c.options.scales.x.max = e; autoScaleYHistory(c); c.update(); });
            };
            rowDiv.appendChild(btn);
            tripList.appendChild(rowDiv);
        });
    }

    function autoScaleYHistory(chart) {
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

    function resetViewAndUpdateData(dataList, selectedDate) {
        isResetting = true;

        if (dataList.length === 0) {
            isResetting = false;
            return;
        }

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
                const times = dataList.map(d => d.x);
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

    function initDeviceSelector(db) {
        let serials = new Set();
        try {
            const res1 = db.exec("SELECT DISTINCT serial FROM history");
            if (res1.length > 0) res1[0].values.forEach(v => { if (v[0]) serials.add(v[0]); });
        } catch(e) {}
        try {
            const res2 = db.exec("SELECT DISTINCT serial FROM tbl_cranking");
            if (res2.length > 0) res2[0].values.forEach(v => { if (v[0]) serials.add(v[0]); });
        } catch(e) {}
        try {
            const res3 = db.exec("SELECT DISTINCT serial FROM tbl_charging");
            if (res3.length > 0) res3[0].values.forEach(v => { if (v[0]) serials.add(v[0]); });
        } catch(e) {}

        const deviceSelector = document.getElementById('deviceSelector');
        deviceSelector.innerHTML = '';
        
        if (serials.size === 0) {
            alert("データベースにデバイスMACデータが見つかりませんでした！");
            return;
        }

        serials.forEach(s => {
            const opt = document.createElement('option');
            opt.value = s;
            opt.innerText = s;
            deviceSelector.appendChild(opt);
        });

        document.getElementById('filter-section').style.display = 'block';

        selectedDevice = deviceSelector.value;
        initMonthSelector(db, selectedDevice);
    }

    function initMonthSelector(db, serial) {
        let months = new Set();
        try {
            const res = db.exec(`SELECT timeline FROM history WHERE serial = '${serial}' ORDER BY timeline ASC`);
            if (res.length > 0) {
                res[0].values.forEach(v => {
                    const ts = v[0];
                    if (ts) {
                        const date = new Date(ts * 1000);
                        const yyyy = date.getFullYear();
                        const mm = String(date.getMonth() + 1).padStart(2, '0');
                        months.add(`${yyyy}-${mm}`);
                    }
                });
            }
        } catch(e) {}

        try {
            const res = db.exec(`SELECT timeline FROM tbl_cranking WHERE serial = '${serial}' ORDER BY timeline ASC`);
            if (res.length > 0) {
                res[0].values.forEach(v => {
                    const ts = v[0];
                    if (ts) {
                        const date = new Date(ts * 1000);
                        const yyyy = date.getFullYear();
                        const mm = String(date.getMonth() + 1).padStart(2, '0');
                        months.add(`${yyyy}-${mm}`);
                    }
                });
            }
        } catch(e) {}

        const monthSelector = document.getElementById('monthSelector');
        monthSelector.innerHTML = '<option value="all">-- 全ての月 --</option>';
        
        Array.from(months).sort().reverse().forEach(m => {
            const opt = document.createElement('option');
            opt.value = m;
            opt.innerText = m;
            monthSelector.appendChild(opt);
        });

        selectedMonth = "all";
        monthSelector.value = "all";

        reloadData();
    }

    function reloadData() {
        if (!currentDb || !selectedDevice) return;
        
        parseChargingTable(currentDb, selectedDevice, selectedMonth);
        parseCrankingTable(currentDb, selectedDevice, selectedMonth);
        parseHistoryTable(currentDb, selectedDevice, selectedMonth);
    }

    document.getElementById('deviceSelector').addEventListener('change', function() {
        selectedDevice = this.value;
        initMonthSelector(currentDb, selectedDevice);
    });

    document.getElementById('monthSelector').addEventListener('change', function() {
        selectedMonth = this.value;
        reloadData();
    });

</script>