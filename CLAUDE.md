# story.knittinghiyori.com：給 Claude Code 的規則

- story 首頁（hub）＋所有作品頁。**資料夾就代表負責人**：`books/` 書與小說 → Alison；`drama/` 影視劇集（含 5 部原創追劇）、`comics/` 漫畫 → Zoe。
- 首頁 hub 外框兩人共管；第一層的舊作品網址是轉址頁，不要刪。
- 新頁用 `_template/`，上線前跑 `python3 _template/check.py`。

## 每次開工

1. **確認是誰**：Zoe 的桌機預設是 Zoe；網頁版沒說是誰就先問。
2. **讀規範**（knittinghiyori-specs）：`core.md`、`registry.md`、`CHANGELOG.md`＋`story.md`。
   - 桌機：`~/Sites/knittinghiyori/knittinghiyori-specs` 先 `git pull` 再讀。
   - 網頁版：`https://raw.githubusercontent.com/happyfamilyintaiwan-bot/knittinghiyori-specs/main/<檔名>`
   - 第一句回報各檔版本號與 CHANGELOG 最新一筆；讀不到就停下，不用記憶代替。
3. 分工、不越界、放錯位置、存檔流程（DELIVERY 五項）、收工的規範更新包、spec-version，一律照 `core.md` §0。

## Alison

兩人共用同一個 GitHub 帳號，靠分支區分：Alison 一律在 `alison/<主題>` 分支工作、不直接推 main，收工開 PR。動到 Zoe 的範圍或共管部分，先停下來提醒。

本檔由 Zoe 維護；要改請寫在 PR 說明。
