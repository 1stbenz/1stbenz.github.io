---
layout: post
title: "BM6/BM200 月間ログファイル分析ツール"
lang: ja
date: 2026-03-20 17:00:00
categories: Auto
tags: [自動車バッテリー, バッテリーモニター, 自動車の知識, DIYツール, データ分析]
description: "BM6 Bluetoothバッテリー監視器専用のウェブ版ログファイル変換ツールです。スマートアルゴリズムにより、純正アプリがリン酸鉄リチウムバッテリーの高電圧特性によって発生する走行検出の不正確さの問題を解決し、各走行記録を正確に復元します。また、視覚化グラフとExcelレポートのエクスポート機能も提供します。"
keywords: "BM6, Bluetoothバッテリー監視, リン酸鉄リチウムバッテリー, 走行検出, 電圧分析, Excelエクスポート, ログファイル変換, 車載バッテリー, スマートオルタネーター"
image: /images/bm6-tool-preview.webp
faq:
  - question: "このツールが主に解決する問題は何ですか？"
    answer: "BM6/BM200の純正アプリは、静置電圧が高いリン酸鉄リチウムバッテリーを扱う際、エンジンが停止したかどうかを正確に判断できないことがあり、走行記録が異常または途切れる原因となります。本ツールは専用最適化されたスマートアルゴリズムを採用し、電圧変動を正確にフィルタリングして、各回の実際の走行履歴を復元します。"
  - question: "一般的な鉛蓄電池や「スマートオルタネーター（充電制御）」を搭載した車種にも適用できますか？"
    answer: "完全に適用可能です。システムのアルゴリズムが、基本電圧を自動分析し、現在のバッテリーが「リン酸鉄モード」か「鉛蓄電池／スマートオルタネーターモード」かを識別し、走行検出ロジックを動的に調整して正確に記録を取得します。"
  - question: "データをどのように取得してアップロードすればよいですか？"
    answer: "まず、スマートフォン版のBM6/BM200アプリで履歴をExcel（.xlsまたは.xlsx）ファイルとしてエクスポートし、そのファイルを本ツールページにアップロードするだけで、自動的に分析が実行されます。"
  - question: "このツールではどのような分析データを提供しますか？"
    answer: "ツールが自動で以下の値を計算します：総走行回数、総走行時間、最低電圧（コールドスタート参考）、および平均走行電圧（発電機健全性）。さらに、自由に拡大可能な電圧と温度の視覚化折れ線グラフも提供します。"
---
<div id="car-app-container" style="max-width: 950px; margin: 20px auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #ffffff; color: #333333; padding: 25px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e5e7eb; position: relative;">
    
    <h2 id="ui-title" style="text-align: center; color: #04384c !important; margin-bottom: 22px; margin-top: 5px; font-weight: 800; font-size: 22px; background: none; border: none;">BM6/BM200 記録データ解析ツール</h2>
    
    <div style="background: rgba(210, 153, 34, 0.08); padding: 15px 20px; border-radius: 10px; margin-bottom: 25px; border-left: 5px solid #d29922; font-size: 14.5px; line-height: 1.6; color: #475569;">
        <strong id="ui-desc-title" style="color: #b45309;">このツールが必要な理由？</strong><br>
        <span id="ui-desc-body">BM6/BM200 はエンジン停止後の継続記録をサポートしていますが、アプリケーションでは走行サイクルの判断が不正確で、波形の詳細な観察も困難です。<b style="color:#04384c;">本ツールはこの問題を修正し</b>、独自設計の解析方式を採用することで、電圧変動を正確に分析し、各走行サイクルを再現できます。さらに、直感的な電圧と温度の視覚化解析を提供します。</span>
    </div>

    <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 15px 25px; border-radius: 10px; margin-bottom: 25px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px;">
<div style="display: flex; gap: 10px;">
            <button id="uploadTrigger" style="background: #04384c; color: white; border: none; padding: 10px 20px; border-radius: 8px; cursor: pointer; font-weight: bold; font-size: 14px;">📁 Excelファイルをアップロード</button>
            
            <button id="loadSampleBtn" style="background: #ffffff; color: #04384c; border: 1px solid #cbd5e1; padding: 9px 20px; border-radius: 8px; cursor: pointer; font-weight: bold; font-size: 14px; display: flex; align-items: center; transition: 0.2s;">📄 サンプルファイルを直接読み込む</button>            
     </div>
        <div style="display: flex; gap: 10px; align-items: center;">
            <label id="ui-display-range" style="font-weight: bold; color: #04384c; font-size: 14px;">表示範囲：</label>
            <select id="dateSelector" style="padding: 8px 12px; border-radius: 8px; border: 1px solid #cbd5e1; font-size: 14px; min-width: 160px; cursor: pointer; background: #ffffff; color: #333333;">
                <option value="all" id="ui-show-all">-- 全て表示 --</option>
            </select>
        </div>
        <input type="file" id="fileInput" accept=".xls,.xlsx" style="display:none">
    </div>
<div id="status-text" style="text-align: center; color: #64748b; margin-bottom: 20px; font-size: 14px;">BM6/BM200からエクスポートされたExcelファイルをアップロードするか、または先にサンプルファイルをダウンロードしてテストを行ってください。</div>
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
            <div style="font-size: 13px; color: #04384c; margin-bottom: 5px; font-weight: 600;">総走行回数</div>
            <div id="stat-trips" style="font-size: 24px; font-weight: bold; color: #04384c;">0</div>
        </div>
        <div class="stat-card" style="background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.25);">
            <div style="font-size: 13px; color: #047857; margin-bottom: 5px; font-weight: 600;">総走行時間</div>
            <div id="stat-time" style="font-size: 24px; font-weight: bold; color: #047857;">0 <span style="font-size: 12px; font-weight: normal;">分</span></div>
        </div>
        <div class="stat-card" style="background: rgba(227, 76, 38, 0.08); border: 1px solid rgba(227, 76, 38, 0.25);">
            <div style="font-size: 13px; color: #c2410c; margin-bottom: 5px; font-weight: 600;">最低電圧（冷蔵車）</div>
            <div id="stat-minv" style="font-size: 24px; font-weight: bold; color: #c2410c;">0.00 <span style="font-size: 12px; font-weight: normal;">V</span></div>
        </div>
        <div class="stat-card" style="background: rgba(122, 0, 223, 0.08); border: 1px solid rgba(122, 0, 223, 0.25);">
            <div style="font-size: 13px; color: #7a00df; margin-bottom: 5px; font-weight: 600;">平均電圧（発電機）</div>
            <div id="stat-avgv" style="font-size: 24px; font-weight: bold; color: #7a00df;">0.00 <span style="font-size: 12px; font-weight: normal;">V</span></div>
        </div>
    </div>
<div style="height: 280px; width: 100%; margin-bottom: 10px;"><canvas id="voltageChart"></canvas></div>
    <div style="height: 280px; width: 100%;">
        <canvas id="tempChart"></canvas>
    </div>

    <div id="trip-section" style="margin-top: 20px; padding: 15px; background: #f8fafc; border-radius: 10px; border: 1px dashed #cbd5e1; display: none;">
        <h3 id="ui-trip-title" style="color: #04384c; font-size: 16px; font-weight: 700; margin-top: 0; margin-bottom: 15px;">検出プロセス</h3>
        <div id="trip-list" style="display: flex; flex-direction: column; gap: 8px;"></div>
    </div>
<script src="https://cdn.sheetjs.com/xlsx-latest/package/dist/xlsx.full.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-adapter-date-fns"></script>
<script src="https://cdn.jsdelivr.net/npm/hammerjs"></script>
這