# story.knittinghiyori.com

編織日和・故事 —— 作品分析主站首頁。

## 這個 repo 的角色

| 網址 | 對應 repo |
|---|---|
| `story.knittinghiyori.com/` | 這個 repo（GitHub Pages 使用者頁，命名為 `你的帳號.github.io`） |
| `story.knittinghiyori.com/confession/` | repo `confession` |
| `story.knittinghiyori.com/hidden-love/` | repo `hidden-love`（未來） |

**注意：`CNAME` 只放在這個 repo，其他作品 repo 千萬不要放**，否則自訂網域會打架。

## 上線步驟

1. 把這個資料夾的檔案推到 `你的帳號.github.io` repo 的 `main` 分支。
2. Settings → Pages → Source 選 `main` / `root`。
3. Custom domain 填 `story.knittinghiyori.com`，勾選 Enforce HTTPS（憑證發放要等幾分鐘）。
4. 到網域商後台新增一筆 DNS：類型 `CNAME`，主機名稱 `story`，指向 `你的帳號.github.io`
5. 作品 repo（如 `confession`）只要開啟 Pages，就會自動出現在 `/confession/`，不需要另外設定網域。

上線後到 Google Search Console 加入 `https://story.knittinghiyori.com/` 並送出 `sitemap.xml`。

## 新增一部作品（要改兩個地方）

**① 目錄卡片**：找到「範本卡片」註解，複製整段 `<li class="work">` 貼進 `<ul class="grid">`。

- `id`：取一個英文代號，例如 `w-hidden-love`
- `data-type`：`drama` / `novel` / `comic` / `film`
- `data-state`：`ready`（可閱讀）/ `soon`（整理中）
- `style="--thread:var(--m-rose)"`：七種莫蘭迪色可選
- 還沒寫完的，把 `<a class="card" href="…">` 換成 `<div class="card card--soon">`

**② 首屏拍立得**：`.reel-track` 裡有**兩份完全一樣**的清單，跑馬燈靠這兩份無縫接回去，所以新增時**兩份都要各加一張**。

```html
<a class="pola" href="#w-你的代號" style="--thread:var(--m-sage); --tilt:1.6deg; --d:1.3s">
  <span class="pola-shot">
    <img src="劇照網址" alt="《作品名》劇照" loading="lazy" decoding="async">
    <i class="dev"></i>
  </span>
  <span class="pola-cap"><b class="pola-name">作品名</b><span class="pola-by">原著：作者名</span></span>
</a>
```

- `--tilt`：±1～2.6deg 之間隨意，讓照片看起來像隨手擺的
- `--d`：顯影延遲，依序往後加 0.13s
- 第二份要加上 `aria-hidden="true" tabindex="-1"`，`alt` 留空

### 劇照規格

- 相片區是**正方形**，圖片用 `object-fit:cover` 置中裁切，直式圖再往上偏一點（`object-position:center 28%`）讓人臉留在畫面裡。
- 手機 2 倍螢幕下，短邊建議至少 **400px**，太小會糊。
- 橫式劇照會裁掉左右兩側，所以**主角要在畫面中央**。
- 圖片放在母站 WordPress 沒問題，但如果主機有開防盜連（hotlink protection），要把 `story.knittinghiyori.com` 加進白名單。

## 視覺設定

配色與字體集中在 `index.html` 最上方的 `:root`：

- 紙面 `--paper` / `--paper-2` / `--paper-3`（暖米色系）
- 墨色 `--ink` / `--ink-2` / `--ink-3`（暖褐灰）
- 七色相紙 `--m-rose` / `--m-clay` / `--m-wheat` / `--m-sage` / `--m-mist` / `--m-lilac` / `--m-jade`

底色那層極淡的布紋在 `body` 的 `background-image`，兩道 `repeating-linear-gradient`，改 `.030` 那個數字就能調深淺。

## 待辦

- [ ] 做一張 1200×630 分享圖，命名 `og-cover.jpg` 放根目錄
- [ ] 《偷偷藏不住》《難哄》《折月亮》三張卡片的一句話定位（目前是 TODO）
- [ ] 《折月亮》補原著／編劇資訊
- [ ] 《逐玉》劇照原圖只有 480×270，換一張大一點的比較不會糊
