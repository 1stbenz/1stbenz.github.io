@echo off
chcp 65001 >nul
echo ====================================================
echo      正在更新全語系熱門文章排行榜 (Top 10)
echo      支援語系：中文 / 英文 / 日文 / 德文 / 西班牙文
echo ====================================================
echo.

cd /d "%~dp0"

python scripts\update_popular.py

if %ERRORLEVEL% EQU 0 (
    echo.
    echo 正在提交變更至 GitHub...
    git add _data\popular_posts.json
    git commit -m "chore: 更新全語系熱門文章排行 (Top 10)"
    git push origin main
    echo.
    echo ====================================================
    echo   [成功] 全語系熱門文章已更新並推送至 GitHub Pages！
    echo ====================================================
) else (
    echo.
    echo [失敗] 解析過程出現錯誤，請確認 Downloads 目錄是否有最新 CSV 報表。
)

echo.
pause
