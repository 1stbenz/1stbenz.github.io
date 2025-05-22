---
layout: post
title:  "機油 SDS 常見成分與 CAS 號碼對照表"
lang: zh-Hant
date:   2024-05-24 10:00:00
categories: Auto
tags: [Engine Oil, SDS, CAS Number, Base Oil, Additives, Lubricants]
description: "整理機油安全資料表 (SDS) 中常見的化學成分與 CAS 號碼對照表，包含 Group I 到 Group V 基礎油（PAO, VHVI, GTL, 酯類）以及抗磨、清淨、分散等核心添加劑的中英對照，教你如何看懂機油成分。"
keywords: "機油, SDS, CAS號碼, 基礎油, PAO, VHVI, GTL, 添加劑, ZDDP, 酯類"
image: /images/engine-oil-sds.webp
faq:
  - question: "什麼是機油的 SDS (安全資料表)？"
    answer: "SDS (Safety Data Sheet) 是化學產品的安全資料表，裡面會列出機油的主要化學成分與 CAS 號碼，是玩家與專業人士了解機油基礎油種類（如 PAO、加氫裂化油）與添加劑比例的重要參考文件。"
  - question: "為什麼同一個基礎油分類會有多個不同的 CAS 號碼？"
    answer: "因為基礎油是複雜的碳氫化合物混合物，不同的製程（如加氫裂化、異構化）、碳鏈長度與黏度，都會對應到不同的化學註冊號碼。需注意的是，單看 CAS 號碼不能 100% 絕對判定基礎油等級，有時需綜合黏度指數 (VI) 來判斷。"
  - question: "清單中常見的 ZDDP 是什麼作用？"
    answer: "ZDDP（二烷基二硫代磷酸鋅）是機油中最核心的抗磨與抗氧化添加劑。它能在引擎金屬表面形成一層極薄的含磷/鋅保護膜，大幅減少引擎零件在極端高溫與高壓下的金屬直接接觸與磨損。"
---

許多車友在挑選機油時，常會好奇瓶身標示的「全合成」究竟是採用真正的 PAO (Group IV)、酯類 (Group V)，還是高度加氫裂化的 VHVI (Group III) 基礎油？要揭開機油配方的神秘面紗，最客觀且直接的方法，就是查閱該款機油的安全資料表 (SDS / MSDS)。

<figure>
  <img src="/images/sds_mobil_1_0w40_2026.webp" alt="美孚1號0W40 SDS">
  <figcaption align="center">SDS：美孚1號 0W-40</figcaption>
</figure>

在 SDS 文件中，每一種化學成分都會標示一組專屬的 CAS 號碼（化學物質登錄碼），這就像是化學物質的「身分證」。為了幫助大家快速解讀這些宛如天書般的代碼，本文完整彙整了機油配方中最常見的基礎油（Group I ~ V）與核心添加劑（如 ZDDP、清淨分散劑等）的 CAS 號碼中英對照表。


<div style="margin-bottom: 20px; padding: 15px; background-color: #161b22; border-radius: 5px; border: 1px solid #ddd;">
  <label for="casSearchInput" style="font-weight: bold; margin-right: 10px;">快速尋找：</label>
  <input type="text" id="casSearchInput" placeholder="輸入 CAS 號碼 (如: 68037-01-4)" style="padding: 8px; width: 250px; border: 1px solid #ccc; border-radius: 4px;">
  <button onclick="searchCAS()" style="padding: 8px 15px; background-color: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer;">搜尋</button>
  <span id="searchResultMsg" style="color: #dc3545; margin-left: 10px; font-weight: bold;"></span>
</div>

<script>
function searchCAS() {
    // 取得使用者輸入的值並去除前後空白
    const input = document.getElementById("casSearchInput").value.trim().toLowerCase();
    const msg = document.getElementById("searchResultMsg");
    msg.innerText = ""; // 清除先前的提示訊息

    if (input === "") {
        msg.innerText = "請輸入 CAS 號碼！";
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
        msg.innerText = "找不到此 CAS 號碼，請確認輸入格式。";
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

| 分類  | <span style="display: inline-block; width:110px">CAS 號碼</span> | 英文化學名稱 / 產品描述 | 中文化學名稱對照 |
| :--- | :--- | :--- | :--- |
| **Group IV<br>(PAO 合成油)** | 68037-01-4 | 1-Decene, homopolymer, hydrogenated | 氫化 1-癸烯均聚物 |
| | 68649-12-7 | 1-decene Tetramer, Mixed With 1-decene Trimer, hydrogenated | 氫化 1-癸烯四聚物與 1-癸烯三聚物混合物 |
| | 68649-11-6 | 1-Decene, Dimer, Hydrogenated | 氫化 1-癸烯二聚物 |
| | 163149-29-9<br>*(及 8002-05-9)* | 1-Decene, Homopolymer, Hydrogenated; Polymer of Octene, Decene, 163149-29-9; (8002-05-9), and Dodecene, Hydrogenated; C8, C12 Olefin Polymer, Hydrogenated | 氫化 1-癸烯均聚物；辛烯、癸烯 (163149-29-9) 與十二烯聚合物 (8002-05-9)，氫化；C8, C12 氫化烯烴聚合物 |
| | 151006-63-2 | 1-Dodecene, Homopolymer, Hydrogenated | 氫化 1-十二烯均聚物 |
| | 151006-62-1 | 1-Dodecene, Trimer, Hydrogenated | 氫化 1-十二烯三聚物 |
| | 151006-60-9 | 1-DODECENE, POLYMER WITH 1-DECENE, HYDROGENATED | 氫化 1-十二烯與 1-癸烯聚合物 |
| | 163149-28-8 | 1-DECENE, POLYMER WITH 1-OCTENE AND 1-DODECENE, HYDROGENATED | 氫化 1-癸烯與 1-辛烯及 1-十二烯聚合物 |
| **Group III<br>(GTL 天然氣合成)**| 848301-69-9 | Distillates (Fischer-Tropsch), heavy, C18-50–branched, cyclicand linear | 餾分物（費托合成），重質，C18–50 — 支鏈、環狀與直鏈 |
| | 1262661-88-0| Distillates (Fischer-Tropsch), heavy, C18-50-branched and linear | 餾分物（費托合成），重質，C18–50 — 支鏈與直鏈 |
| **Group III<br>(VHVI 加氫裂化)** | 64741-89-5 | HIGHLY HYDROTREATED PARAFFINIC BASE OILS | 深度加氫處理石蠟基基礎油 |
| | 64742-54-7 | HIGHLY HYDROTREATED PARAFFINIC BASE OILS | 深度加氫處理石蠟基基礎油 |
| | 64742-55-8 | HIGHLY HYDROTREATED PARAFFINIC BASE OILS | 深度加氫處理石蠟基基礎油 |
| | 64742-70-7 | Paraffin oils (petroleum), catalytic dewaxed heavy | 催化脫蠟重質石蠟油（石油） |
| | 72623-87-1 | Severely Hydrotreated Paraffinic Hydrocarbons (Oil) | 深度加氫處理石蠟烴（油） |
| | 72623-85-9 | Lubricating oils (petroleum), C20-50, hydrotreated neutral oil-based, high-viscosity | 潤滑油（石油），C20-50，加氫處理中性油基，高黏度 |
| | 72623-86-0 | Hydrotreated Neutral Oil-Based | 加氫處理中性油基 |
| | 178603-64-0 | Gas oils, petroleum, vacuum, hydrocracked, hydroisomerized, hydrogenated, C15-30, branched and cyclic, **high viscosity index**; Severely hydrotreated, hydorcracked, hydroisomerized, **high viscosity synthetic iso-alkane** | 減壓瓦斯油（石油），加氫裂化、加氫異構化、氫化，C15-30 支鏈與環狀，**高黏度指數**；深度加氫處理、加氫裂化、加氫異構化、**高黏度合成異烷烴** |
| | 178603-65-1 | Gas oils, petroleum, vacuum, hydrocracked, hydroisomerized, hydrogenated, C20-40, branched and cyclic, **high viscosity index** | 減壓瓦斯油（石油），加氫裂化、加氫異構化、氫化，C20-40 支鏈與環狀，**高黏度指數** |
| | 178603-66-2 | Gas oils, petroleum, vacuum, hydrocracked, hydroisomerized, hydrogenated, C25-55, branched and cyclic, **high viscosity index** | 減壓瓦斯油（石油），加氫裂化、加氫異構化、氫化，C25-55 支鏈與環狀，**高黏度指數** |
| **Group I / II<br>(礦物油)** | 64741-50-0 | Distillates, petroleum, light paraffinic | 輕質石蠟基餾分油（石油） |
| | 64741-50-5 | Distillates(Petroleum), Light Paraffinic | 輕質石蠟基餾分油（石油） |
| | 64741-52-2 | Distillates, petroleum, light naphthenic | 輕質環烷基餾分油（石油） |
| | 64742-65-0 | Distillates (petroleum), solvent-dewaxed heavy paraffinic | 溶劑脫蠟重質石蠟基餾分油（石油） |
| | 64742-55-8 | HIGHLY HYDROTREATED PARAFFINIC BASE OILS | 深度加氫處理石蠟基基礎油 |
| | 64742-58-1 | Lubricating oils (petroleum), hydrotreated spent | 加氫處理廢潤滑油（石油） |
| | 64742-56-9 | Distillates (petroleum), solvent-dewaxed light paraffinic | 溶劑脫蠟輕質石蠟基餾分油 (常見 Group I 輕油) |
| | 64742-62-7 | Residual oils (petroleum), solvent-dewaxed | 溶劑脫蠟渣油 (常見的光亮油 Bright Stock, 增黏用) |
| **Group V<br>(Esters 酯類/其他)** | 27178-16-1 | DIISODECYL ADIPATE | 己二酸二異癸酯 |
| | 16958-92-2 | ESTER SYNTHETIC BASE OILS | 酯類合成基礎油 |
| | 28472-97-1 | di-isodecyl azelate is a diester basestock | 壬二酸二異癸酯（雙酯基礎油） |
| | 9003-13-8 | Polyalkylene glycol (PAG) | 聚亞烷基二醇 (常見 PAG 基礎油) |
| **抗磨添加劑<br>(ZDTP / ZDDP)** | 68649-42-3 | ZINC DIALKYL DITHIOPHOSPHATE ZDTP | 二烷基二硫代磷酸鋅 |
| | 84605-29-8 | Phosphorodithioic acid, mixed O,O-bis(1,3-dimethylbutyl and iso-Pr) esters, zinc salts | 混合(1,3-二甲基丁基/異丙基)二硫代磷酸鋅 (極常見的 ZDDP 變體) |
| **減摩添加劑<br>(MoDTC / MoDTP)**| 68958-92-7 | Moly Dithiophosphate | 二硫代磷酸鉬 |
| | 68958-92-9 | molybdenum di(2-ethylhexyl) phosphorodithioate | 二(2-乙基己基)二硫代磷酸鉬 |
| **抗氧化劑<br>(Antioxidants)**| 36878-20-3 | Bis(nonylphenyl)amine | 雙(壬基苯基)胺 (最常見的胺類抗氧化劑) |
| | 128-39-2 | 2,6-di-tert-butylphenol | 2,6-二叔丁基苯酚 (最常見的酚類抗氧化劑) |
| **清淨劑<br>(Detergents)**| 61789-86-4 | Calcium petroleum sulfonate | 石油磺酸鈣 (機油酸鹼中和與清潔主力) |
| | 68783-96-0 | Sulfonic acids, petroleum, calcium salts, overbased | 高鹼性石油磺酸鈣 |
| | 115733-09-0 | Calcium long-chain alkyl phenate sulfide | 硫化長鏈烷基酚鈣 |
| **分散劑<br>(Dispersants)** | 無 CAS | Polyolefin polyamine succinimide, polyol | 聚烯烴多胺琥珀醯亞胺，多元醇 |
| | 296-404-1<br>*(註：EC 號)*| PHOSPHORIC ACID ESTERS | 磷酸酯 |
| | 84605-20-9 | Polyisobutylene succinimide (PIBSI) | 聚異丁烯琥珀醯亞胺 (現代機油最核心的無灰分散劑) |
| **黏度指數改進劑<br>(VM)** | 25038-36-2 | Olefin Copolymer | 烯烴共聚物 |
| | 127883-08-3 | Aryl polyolefin, Ethylene/Propylene | 芳基聚烯烴，乙烯/丙烯共聚物 |
| **降凝劑<br>(PPD)** | 無 CAS| POLY METHYL METHACRYLATE ESTER | 聚甲基丙烯酸酯 |
| **消泡劑<br>(Anti-foam)**| 63148-62-9 | Polydimethylsiloxane (Silicone oil) | 聚二甲基矽氧烷 (極常見的矽油消泡劑) |

## 參考資料

* [Изучаем состав масла - ПАО Group IV, GTL, Гидрокрекинг - VHVI Group III, минеральное масло Group I; Group II, эстеры итд. Oil-Club.ru](https://www.oil-club.ru/forum/topic/2120-izuchaem-sostav-masla-pao-group-iv-gtl-gidrokreking-vhvi-group-iii-mineralnoe-maslo-group-i-ili-ii-estery-itd/page/31/)