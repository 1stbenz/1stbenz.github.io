---
layout: post
title: エンジンオイルのSDS（安全データシート）でよく見られる成分とCAS番号対照表
lang: ja
date: 2024-05-24 10:00:00
categories: Auto
tags: [Engine Oil, SDS, CAS Number, Base Oil, Additives, Lubricants]
description: エンジンオイルの安全データシート（SDS）に記載されている一般的な化学成分とCAS番号の対照表をまとめました。Group IからGroup Vのベースオイル（PAO, VHVI, GTL, エステル類）や、摩耗防止、清浄、分散などの主要添加剤について、日本語と英語での対応を示し、オイル成分の見方を解説します。
keywords: エンジンオイル, SDS, CAS番号, ベースオイル, PAO, VHVI, GTL, 添加剤, ZDDP, エステル類
image: /images/engine-oil-sds.webp
faq:
  - question: "エンジンオイルのSDS（安全データシート）とは何ですか？"
    answer: SDS (Safety Data Sheet) は化学製品の安全データシートであり、オイルの主要な化学成分とCAS番号が記載されています。これは、ユーザーや専門家がオイルのベースオイルの種類（例：PAO、水素化裂化油）や添加剤の比率を理解するための重要な参考資料です。
  - question: "なぜ同じベースオイル分類なのに複数の異なるCAS番号があるのですか？"
    answer: ベースオイルは複雑な炭化水素混合物であるため、異なる製造工程（例：水素化裂化、異性化）、炭素鎖の長さや粘度によって、それぞれ異なる化学登録番号が割り当てられます。注意点として、CAS番号だけではベースオイルの等級を100%断定することはできず、時には粘度指数 (VI) を総合的に判断する必要があります。
  - question: "リストでよく見かけるZDDPとはどのような役割がありますか？"
    answer: ZDDP（ジアルキルジチオホスフェート亜鉛）は、オイルにおける最も重要な耐摩耗性および抗酸化添加剤です。これはエンジン金属表面に非常に薄いリン/亜鉛を含む保護膜を形成し、極端な高温・高圧下でのエンジン部品の直接的な金属接触と摩耗を大幅に減少させます。
---
多くのカーオーナーがエンジンオイルを選ぶ際、「フルシンセティック」という表記が、本当にPAO（Group IV）、エステル類（Group V）、それとも高度水素化クラックされたVHVI（Group III）ベースオイルなのか疑問に思うことがあります。オイルの配合の神秘的なベールを剥ぐ最も客観的かつ直接的な方法は、そのオイルの安全データシート（SDS / MSDS）を確認することです。

<figure>
  <img src="/images/sds_mobil_1_0w40_2026.webp" alt="モビル1 0W-40 SDS">
  <figcaption align="center">SDS：モビル1 0W-40</figcaption>
</figure>

SDSファイルでは、すべての化学成分に固有のCAS番号（化学物質登録コード）が記載されており、これはその化学物質の「身分証明書」のようなものです。読者の皆様がこれらのまるで天書のようなコードを迅速に解読できるよう、本記事ではエンジンオイル配合物で最も一般的なベースオイル（Group I～V）と主要添加剤（ZDDP、清浄分散剤など）のCAS番号の中英対照表を網羅的にまとめました。


<div style="margin-bottom: 20px; padding: 15px; background-color: #161b22; border-radius: 5px; border: 1px solid #ddd;">
  <label for="casSearchInput" style="font-weight: bold; margin-right: 10px;">クイック検索：</label>
  <input type="text" id="casSearchInput" placeholder="CAS番号を入力（例: 68037-01-4)" style="padding: 8px; width: 250px; border: 1px solid #ccc; border-radius: 4px;">
  <button onclick="searchCAS()" style="padding: 8px 15px; background-color: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer;">検索</button>
  <span id="searchResultMsg" style="color: #dc3545; margin-left: 10px; font-weight: bold;"></span>
</div>
<script>
function searchCAS() {
    // 取得使用者輸入的值並去除前後空白
    const input = document.getElementById("casSearchInput").value.trim().toLowerCase();
    const msg = document.getElementById("searchResultMsg");
    msg.innerText = ""; // 清除先前的提示訊息

    if (input === "") {
        msg.innerText = "CAS番号を入力してください！";
        return;
    }

    // 抓取頁面上的第一個表格
    const table = document.querySelector("table");
    if (!table) return;

    const rows = table.getElementsByTagName("tr");
    let found = false;

    // 遍歷所有資料列 (跳過表頭的第 0 列)
    for (let i = 1; i < rows.length; i++) {
        // 還原所有列的背景顏色
        rows[i].style.backgroundColor = "";
        rows[i].style.transition = "background-color 0.5s ease";

        // CAS 號碼在第二個欄位 (索引值為 1)
        const casCell = rows[i].getElementsByTagName("td")[1];
        if (casCell) {
            const casText = casCell.innerText || casCell.textContent;
            
            // 如果比對成功
            if (casText.toLowerCase().includes(input)) {
                // 平滑滾動到該列，並將其置中
                rows[i].scrollIntoView({ behavior: 'smooth', block: 'center' });
                // 加入醒目提示的背景色
                rows[i].style.backgroundColor = "#007A00"; 
                found = true;
                break; // 找到第一筆吻合的就停止
            }
        }
    }

    if (!found) {
        msg.innerText = "このCAS番号は見つかりませんでした。入力形式を確認してください。";
    }
}

// 綁定 Enter 鍵事件
document.addEventListener("DOMContentLoaded", function() {
    const inputField = document.getElementById("casSearchInput");
    if (inputField) {
        inputField.addEventListener("keypress", function(event) {
            // 確認按下的是 Enter 鍵
            if (event.key === "Enter") {
                event.preventDefault(); // 避免如果有表單外掛時觸發預設提交
                searchCAS();            // 執行搜尋
            }
        });
    }
});
</script>
| 分類 | <span style="display: inline-block; width:110px">CAS 號碼</span> | 英文化學名稱 / 產品描述 | 日本語訳 / 対応名称 |
| :--- | :--- | :--- | :--- |
| **Group IV<br>(PAO 合成油)** | 68037-01-4 | 1-Decene, homopolymer, hydrogenated | 水素化 1-デセン ホモポリマー |
| | 68649-12-7 | 1-decene Tetramer, Mixed With 1-decene Trimer, hydrogenated | 水素化 1-デセン テトラマーと 1-デセン トライマーの混合物 |
| | 68649-11-6 | 1-Decene, Dimer, Hydrogenated | 水素化 1-デセン ダイマー |
| | 163149-29-9<br>*(及 8002-05-9)* | 1-Decene, Homopolymer, Hydrogenated; Polymer of Octene, Decene, 163149-29-9; (8002-05-9), and Dodecene, Hydrogenated; C8, C12 Olefin Polymer, Hydrogenated | 水素化 1-デセン ホモポリマー; オクテン、デセン (163149-29-9) およびドデセンポリマー (8002-05-9) の水素化物; C8, C12 水素化オレフィンポリマー |
| | 151006-63-2 | 1-Dodecene, Homopolymer, Hydrogenated | 水素化 1-ドデセン ホモポリマー |
| | 151006-62-1 | 1-Dodecene, Trimer, Hydrogenated | 水素化 1-ドデセン トライマー |
| | 151006-60-9 | 1-DODECENE, POLYMER WITH 1-DECENE, HYDROGENATED | 水素化 1-ドデセンと 1-デセンのポリマー |
| | 163149-28-8 | 1-DECENE, POLYMER WITH 1-OCTENE AND 1-DODECENE, HYDROGENATED | 水素化 1-デセン、1-オクテン、および 1-ドデセンのポリマー |
| **Group III<br>(GTL 天然氣合成)**| 848301-69-9 | Distillates (Fischer-Tropsch), heavy, C18-50–branched, cyclicand linear | 分解油（フィッシャー・トロプシュ法）、重質、C18–50 — 側鎖、環状および直鎖 |
| | 1262661-88-0| Distillates (Fischer-Tropsch), heavy, C18-50-branched and linear | 分解油（フィッシャー・トロプシュ法）、重質、C18–50 — 側鎖および直鎖 |
| **Group III<br>(VHVI 加氫裂化)** | 64741-89-5 | HIGHLY HYDROTREATED PARAFFINIC BASE OILS | 高度水素化パラフィン系ベースオイル |
| | 64742-54-7 | HIGHLY HYDROTREATED PARAFFINIC BASE OILS | 高度水素化パラフィン系ベースオイル |
| | 64742-55-8 | HIGHLY HYDROTREATED PARAFFINIC BASE OILS | 高度水素化パラフィン系ベースオイル |
| | 64742-70-7 | Paraffin oils (petroleum), catalytic dewaxed heavy | 触媒脱蝋重質パラフィン油（石油） |
| | 72623-87-1 | Severely Hydrotreated Paraffinic Hydrocarbons (Oil) | 高度水素化パラフィン炭化水素（オイル） |
| | 72623-85-9 | Lubricating oils (petroleum), C20-50, hydrotreated neutral oil-based, high-viscosity | 潤滑油（石油）、C20-50、水素化処理中性オイルベース、高粘度 |
| | 72623-86-0 | Hydrotreated Neutral Oil-Based | 水素化処理中性オイルベース |
| | 178603-64-0 | Gas oils, petroleum, vacuum, hydrocracked, hydroisomerized, hydrogenated, C15-30, branched and cyclic, **high viscosity index**; Severely hydrotreated, hydorcracked, hydroisomerized, **high viscosity synthetic iso-alkane** | ガス油（石油）、水素化クラッキング、水素化異性化、水素化、C15-30 側鎖および環状、**高粘度指数**；高度水素化処理、水素化クラッキング、水素化異性化、**高粘度合成イソアルカン** |
| | 178603-65-1 | Gas oils, petroleum, vacuum, hydrocracked, hydroisomerized, hydrogenated, C20-40, branched and cyclic, **high viscosity index** | 真空ガス油（石油）、水素化分解、水素化異性化、水素化、C20-40 分枝および環状、**高粘度指数** |
| | 178603-66-2 | Gas oils, petroleum, vacuum, hydrocracked, hydroisomerized, hydrogenated, C25-55, branched and cyclic, **high viscosity index** | 真空ガス油（石油）、水素化分解、水素化異性化、水素化、C25-55 分枝および環状、**高粘度指数** |
| **Group I / II<br>(鉱物油)** | 64741-50-0 | Distillates, petroleum, light paraffinic | 軽量パラフィン系留分油（石油） |
| | 64741-50-5 | Distillates(Petroleum), Light Paraffinic | 軽量パラフィン系留分油（石油） |
| | 64741-52-2 | Distillates, petroleum, light naphthenic | 軽量ナフテン系留分油（石油） |
| | 64742-65-0 | Distillates (petroleum), solvent-dewaxed heavy paraffinic | 溶剤脱蝋重パラフィン系留分油（石油） |
| | 64742-55-8 | HIGHLY HYDROTREATED PARAFFINIC BASE OILS | 高度水素化処理パラフィン系基礎油 |
| | 64742-58-1 | Lubricating oils (petroleum), hydrotreated spent | 水素化処理廃潤滑油（石油） |
| | 64742-56-9 | Distillates (petroleum), solvent-dewaxed light paraffinic | 溶剤脱蝋軽量パラフィン系留分油 (一般的なGroup I軽油) |
| | 64742-62-7 | Residual oils (petroleum), solvent-dewaxed | 溶剤脱蝋残渣油 (一般的に光沢油 Bright Stock、増粘用) |
| **Group V<br>(エステル/その他)** | 27178-16-1 | DIISODECYL ADIPATE | ジイソデシルアジペート |
| | 16958-92-2 | ESTER SYNTHETIC BASE OILS | エステル合成基礎油 |
| | 28472-97-1 | di-isodecyl azelate is a diester basestock | ジイソデシルアゼレート（ジエステル基礎油） |
| | 9003-13-8 | Polyalkylene glycol (PAG) | ポリアリキレングリコール (一般的なPAG基礎油) |
| **耐摩耗添加剤<br>(ZDTP / ZDDP)** | 68649-42-3 | ZINC DIALKYL DITHIOPHOSPHATE ZDTP | ジアルキルジチオホスフェート亜鉛 (ZDTP) |
| | 84605-29-8 | Phosphorodithioic acid, mixed O,O-bis(1,3-dimethylbutyl and iso-Pr) esters, zinc salts | 混合(1,3-ジメチルブチル/イソプロピル)二チオホスフェート亜鉛塩 (非常に一般的なZDDPバリエーション) |
| **耐摩耗添加剤<br>(MoDTC / MoDTP)**| 68958-92-7 | Moly Dithiophosphate | ジチオホスフェートモリブデン酸塩 |
| | 68958-92-9 | molybdenum di(2-ethylhexyl) phosphorodithioate | ジ(2-エチルヘキシル)二チオホスフェートモリブデン酸塩 |
| **抗酸化剤<br>(Antioxidants)**| 36878-20-3 | Bis(nonylphenyl)amine | ジ(ノニルフェニル)アミン（最も一般的なアミン系抗酸化剤） |
| | 128-39-2 | 2,6-di-tert-butylphenol | 2,6-ジ-tert-ブチルフェノール（最も一般的なフェノール系抗酸化剤） |
| **洗浄剤<br>(Detergents)**| 61789-86-4 | Calcium petroleum sulfonate | 石油スルホン酸カルシウム（エンジンオイルの酸アルカリ中和および洗浄の主成分） |
| | | 石油分酸、カルシウム塩、過塩基性 |
| | 115733-09-0 | カルシウム長鎖アルキルフェナト硫化物 | 硫化長鎖アルキルフェナトカルシウム |
| **分散剤<br>(Dispersants)** | CASなし | ポリオレフィンポリアミンスクシニミド、ポリオール | ポリオレフィンポリアミンスクシニミド、ポリオール |
| | 296-404-1<br>*(注：EC番号)*| リン酸エステル (PHOSPHORIC ACID ESTERS) | リン酸エステル |
| | 84605-20-9 | ポリイソブチレンスクシニミド (PIBSI) | ポリイソブチレンスクシニミド (現代エンジンオイルの最も重要な無灰分散剤) |
| **粘度指数改善剤<br>(VM)** | 25038-36-2 | オレフィン共重合体 (Olefin Copolymer) | オレフィン共重合体 |
| | 127883-08-3 | アリルポリオレフィン、エチレン/プロピレン (Aryl polyolefin, Ethylene/Propylene) | アリルポリオレフィン、エチレン/プロピレン共重合体 |
| **消泡剤<br>(PPD)** | CASなし | ポリメチルアクリレートエステル (POLY METHYL METHACRYLATE ESTER) | ポリメチルアクリレートエステル |
| **消泡剤<br>(Anti-foam)**| 63148-62-9 | ポリジメチルシロキサン (Polydimethylsiloxane) | ポリジメチルシロキサン (非常に一般的なシリコーンオイルの消泡剤) |

## 参考資料

* [Изучаем состав масла - ПАО Group IV, GTL, Гидрокрекинг - VHVI Group III, минеральное масло Group I; Group II, эстеры итд. Oil-Club.ru](https://www.oil-club.ru/forum/topic/2120-izuchaem-sostav-masla-pao-group-iv-gtl-gidrokreking-vhvi-group-iii-mineralnoe-maslo-group-i-ili-ii-estery-itd/page/31/)