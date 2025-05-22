---
layout: post
title: "BM6/BM200 月間ログファイル分析ツール"
lang: ja
date: 2026-03-20 17:00:00
categories: Auto
tags: [BM6, バッテリー監視, リン酸鉄リチウムバッテリー, データ分析, 走行検出, 変換ツール, 車載バッテリー]
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
<div id="car-app-container" style="max-width: 950px; margin: 20px auto; font-family: 'Segoe UI', 'Microsoft JhengHei', sans-serif; background: #0d1117; color: #c9d1d9; padding: 25px; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 1px solid #30363d; position: relative;">
    
    <h2 id="ui-title" style="text-align: center; color: #c9d1d9; margin-bottom: 10px; margin-top: 10px;">BM6/BM200 記録データ解析ツール</h2>
    
    <div style="background: rgba(210, 153, 34, 0.1); padding: 15px 20px; border-radius: 10px; margin-bottom: 25px; border-left: 5px solid #d29922; font-size: 14.5px; line-height: 1.6; color: #8b949e;">
        <strong id="ui-desc-title" style="color: #d29922;">このツールが必要な理由？</strong><br>
        <span id="ui-desc-body">BM6/BM200 はエンジン停止後の継続記録をサポートしていますが、アプリケーションでは走行サイクルの判断が不正確で、波形の詳細な観察も困難です。<b style="color:#c9d1d9;">本ツールはこの問題を修正し</b>、独自設計の解析方式を採用することで、電圧変動を正確に分析し、各走行サイクルを再現できます。さらに、直感的な電圧と温度の視覚化解析を提供します。</span>
    </div>

    <div style="background: #161b22; border: 1px solid #30363d; padding: 15px 25px; border-radius: 10px; margin-bottom: 25px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px;">
<div style="display: flex; gap: 10px;">
            <button id="uploadTrigger" style="background: #1f6feb; color: white; border: none; padding: 10px 20px; border-radius: 8px; cursor: pointer; font-weight: bold; font-size: 14px;">📁 Excelファイルをアップロード</button>
            
            <button id="loadSampleBtn" style="background: #30363d; color: #c9d1d9; border: 1px solid #8b949e; padding: 9px 20px; border-radius: 8px; cursor: pointer; font-weight: bold; font-size: 14px; display: flex; align-items: center; transition: 0.2s;">📄 サンプルファイルを直接読み込む</button>            
     </div>
        <div style="display: flex; gap: 10px; align-items: center;">
            <label id="ui-display-range" style="font-weight: bold; color: #c9d1d9; font-size: 14px;">表示範囲：</label>
            <select id="dateSelector" style="padding: 8px 12px; border-radius: 8px; border: 1px solid #30363d; font-size: 14px; min-width: 160px; cursor: pointer; background: #0d1117; color: #c9d1d9;">
                <option value="all" id="ui-show-all">-- 全て表示 --</option>
            </select>
        </div>
        <input type="file" id="fileInput" accept=".xls,.xlsx" style="display:none">
    </div>
<div id="status-text" style="text-align: center; color: #8b949e; margin-bottom: 20px; font-size: 14px;">BM6/BM200からエクスポートされたExcelファイルをアップロードするか、または先にサンプルファイルをダウンロードしてテストを行ってください。</div>
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
        <div class="stat-card" style="background: rgba(31, 111, 235, 0.1); border: 1px solid rgba(31, 111, 235, 0.3);">
            <div style="font-size: 13px; color: #58a6ff; margin-bottom: 5px; font-weight: 500;">総走行回数</div>
            <div id="stat-trips" style="font-size: 24px; font-weight: bold; color: #79c0ff;">0</div>
        </div>
        <div class="stat-card" style="background: rgba(35, 134, 54, 0.1); border: 1px solid rgba(35, 134, 54, 0.3);">
            <div style="font-size: 13px; color: #3fb950; margin-bottom: 5px; font-weight: 500;">総走行時間</div>
            <div id="stat-time" style="font-size: 24px; font-weight: bold; color: #56d364;">0 <span style="font-size: 12px; font-weight: normal;">分</span></div>
        </div>
        <div class="stat-card" style="background: rgba(227, 76, 38, 0.1); border: 1px solid rgba(227, 76, 38, 0.3);">
            <div style="font-size: 13px; color: #f0883e; margin-bottom: 5px; font-weight: 500;">最低電圧（冷蔵車）</div>
            <div id="stat-minv" style="font-size: 24px; font-weight: bold; color: #ff945e;">0.00 <span style="font-size: 12px; font-weight: normal;">V</span></div>
        </div>
        <div class="stat-card" style="background: rgba(137, 87, 229, 0.1); border: 1px solid rgba(137, 87, 229, 0.3);">
            <div style="font-size: 13px; color: #a371f7; margin-bottom: 5px; font-weight: 500;">平均電圧（発電機）</div>
            <div id="stat-avgv" style="font-size: 24px; font-weight: bold; color: #d2a8ff;">0.00 <span style="font-size: 12px; font-weight: normal;">V</span></div>
        </div>
    </div>
<div style="height: 280px; width: 100%; margin-bottom: 10px;"><canvas id="voltageChart"></canvas></div>
    <div style="height: 280px; width: 100%;">
        <canvas id="tempChart"></canvas>
    </div>

    <div id="trip-section" style="margin-top: 20px; padding: 15px; background: #161b22; border-radius: 10px; border: 1px dashed #30363d; display: none;">
        <h3 id="ui-trip-title" style="color: #c9d1d9; font-size: 16px; margin-top: 0; margin-bottom: 15px;">検出プロセス</h3>
        <div id="trip-list" style="display: flex; flex-direction: column; gap: 8px;"></div>
    </div>
<script src="https://cdn.sheetjs.com/xlsx-latest/package/dist/xlsx.full.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-adapter-date-fns"></script>
<script src="https://cdn.jsdelivr.net/npm/hammerjs"></script>
這