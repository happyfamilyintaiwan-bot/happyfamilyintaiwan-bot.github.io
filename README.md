# story.knittinghiyori.com

編織日和・故事 —— 作品分析主站首頁。

## 這個 repo 的角色

| 網址 | 對應 repo |
|---|---|
| `story.knittinghiyori.com/` | 這個 repo（GitHub Pages 使用者頁，命名為 `你的帳號.github.io`） |
| `story.knittinghiyori.com/confession/` | repo `confession` |
| `story.knittinghiyori.com/when-i-meet-the-moon/` | repo `when-i-meet-the-moon` |
| `story.knittinghiyori.com/hidden-love/` | repo `hidden-love` |
| `story.knittinghiyori.com/the-first-frost/` | repo `the-first-frost` |

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

- [ ] 《折月亮》卡片補原著／編劇資訊（目前寫「互動閱讀頁」佔位）
- [ ] 《偷偷藏不住》《難哄》兩張卡片的一句話定位再確認，看有沒有貼合互動頁實際內容
- [ ] 四個互動頁的 `<head>` 貼上 `snippet-favicon.html`
- [ ] 四個互動頁的底部貼上 `snippet-exit.html`
- [ ] 目前九部作品全部是 `ready`，「只看可閱讀」這個篩選暫時等同「全部」，等有新的整理中作品才會再派上用場

---

## 內容漏斗：社群 → 互動頁 → 長文

**連結原則：有互動頁的作品，首頁卡片一律連互動頁；互動頁底部再導回部落格長文。**
沒有互動頁的作品，卡片才直接連長文。

目前的去向：

| 作品 | 卡片連到 |
|---|---|
| 告白 | `/confession/` → 互動頁底部導長文 |
| 折月亮 | `/when-i-meet-the-moon/` → 互動頁底部導長文 |
| 偷偷藏不住 | `/hidden-love/` → 互動頁底部導長文 |
| 難哄 | `/the-first-frost/` → 互動頁底部導長文 |
| 點燃我，溫暖你 · 逐玉 · 折腰 · 天才女友 · 熾夏 | 直接連母站長文（尚無互動頁） |

日後任何一部做了互動頁，記得把卡片的 `href` 從長文換成互動頁，長文的位置改由互動頁底部承接。

### 出口區塊

`snippet-exit.html` 貼在互動頁 `</body>` 之前。樣式全部收在 `.exit` 底下（變數前綴 `--x-`），不會跟互動頁既有的 CSS 打架。

每個作品要改三個地方：

1. `.x-main` 的 `href` → 該作品的長文網址
2. `.x-main` 的 `h2` 與 `p` → 該篇長文的標題與說明
3. `--x-accent` → 換成該作品在首頁用的莫蘭迪色

| 作品 | `--x-accent` |
|---|---|
| 告白 | `#c9a49c` 灰粉 |
| 折月亮 | `#9cadb8` 霧藍 |
| 偷偷藏不住 | `#96aea4` 青灰 |
| 難哄 | `#b0a6b4` 藕紫 |

三個出口的優先序是刻意的：**長文（大卡）→ 電子報 → 作品目錄**。長文才是要吃 SEO 的主體，所以連結文字用實字（「讀完整分析」），不要寫「更多」「點這裡」。

長文那邊也記得回連互動頁，兩邊互指。


---

## 網站圖示（分頁上的小圖）

圖示檔全部放在主站 repo 的 `/icons/`，加上根目錄的 `site.webmanifest`。

| 檔案 | 用途 |
|---|---|
| `favicon.ico` | 瀏覽器分頁，內含 16／32／48 三種尺寸 |
| `favicon-32.png`、`favicon-96.png` | 較新的瀏覽器優先讀這兩個 |
| `apple-touch-icon.png` | iPhone／iPad 加到主畫面時的圖示 |
| `icon-192.png`、`icon-512.png` | Android 與 PWA |
| `og-cover.jpg` | 分享到社群時的預覽圖 |

小尺寸的 `favicon.ico` 和 `favicon-32/96` 是**簡化版**——只留奶茶底色加白色拱形，沒有文字。因為分頁上的圖只有 16 像素寬，「編織日和」四個字縮到那個大小會糊成一團色塊，反而不如一個乾淨的形狀好認。大尺寸（apple-touch、192、512）用的是完整 logo。

### 讓互動頁也吃到同一組圖示

`snippet-favicon.html` 貼進每個互動頁的 `<head>`。

路徑一定要用**開頭有斜線的絕對路徑**（`/icons/favicon.ico`）。因為互動頁在子目錄底下，如果寫成 `icons/favicon.ico`，瀏覽器會去找 `/hidden-love/icons/favicon.ico`，那裡沒有檔案，就會退回灰色地球。

其實瀏覽器找不到任何 icon 標籤時，會自己去要 `網域根目錄/favicon.ico`，所以理論上把 ico 放在主站根目錄就能全站通用。但那只涵蓋最舊的那一種格式，iOS 主畫面圖示和 Android 都不吃，所以還是每頁貼一次最保險。

改了圖示之後瀏覽器會頑固地記住舊的，用無痕視窗開一次才看得到新的。

---

## 關於 sitemap

`sitemap.xml` 是手寫的，這是刻意的選擇。

每個互動頁各自是一個 repo，主站不知道其他 repo 有哪些頁面，要自動產生就得寫一支 GitHub Action 去跨 repo 抓，為了目前這五筆網址不值得。等到頁面多到二三十個、或是開始頻繁增減，再考慮自動化。

新增一個互動頁時，照著現有格式複製一組 `<url>` 貼上去就好，記得同時更新首頁那筆的 `lastmod`。改完到 Google Search Console 重新送出一次，不然可能要等好幾天 Google 才會自己回來抓。
