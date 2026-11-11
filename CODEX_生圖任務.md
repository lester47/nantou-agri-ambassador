# 給 Codex 的生圖任務：南投食農小旅行 360° 全景圖

> 使用方式：把這整份檔案交給 Codex，並讓它在本資料夾（`南投食農小旅行/`）裡執行。

## 你的任務

這是一個 360° 互動教材專案。教材內容已經寫好（`data/eras.json`），目前 `img/pano/` 裡的五張全景圖只是程式畫的「示意暫用圖」。請你用圖片生成工具，產出 **5 張精美的 360° 等距長方投影（equirectangular）全景圖**，覆蓋掉暫用圖，然後執行同步腳本。

## 必須遵守的規格

| 項目 | 要求 |
| :--- | :--- |
| 投影 | 360° × 180° 等距長方投影（equirectangular） |
| 比例 | **嚴格 2:1**，建議 4096 × 2048（至少 2048 × 1024） |
| 格式 | JPG，品質 85 左右，每張盡量控制在 2 MB 以內 |
| 地平線 | 正好在圖片垂直正中央（y = 50%），完全水平 |
| 視角 | 人站立平視（約 1.5 公尺高），不要魚眼、空拍、俯視、小行星效果 |
| 左右接縫 | 圖片最左邊和最右邊必須能無縫接合 |
| 禁止 | 文字、浮水印、Logo、看鏡頭的人臉 |
| 風格 | 溫暖明亮、細節豐富、繪本插畫級精緻質感，適合國小學生 |

**檔名必須完全一致（不要改 `data/eras.json`）：**

```
img/pano/dongding.jpg   鹿谷・凍頂烏龍茶
img/pano/yuchi.jpg      魚池・日月潭紅茶
img/pano/puli.jpg       埔里・茭白筍
img/pano/xinyi.jpg      信義・梅子
img/pano/zhushan.jpg    竹山・竹筍
```

## 如果生圖工具無法直接輸出 2:1 全景

1. 用工具支援的最大寬幅尺寸生成（例如 1536 × 768 或 1792 × 896），提示詞照樣寫 equirectangular 360 panorama。
2. 用 Python Pillow 以 LANCZOS 放大到 4096 × 2048。
3. 檢查左右接縫：把圖片水平平移 50% 後看中間是否有明顯斷線；若有，對中間約 200 px 的區域做 inpaint 或羽化混合修補，再平移回來。
4. 若圖片比例不是 2:1，不要拉伸變形，改為補畫天空與地面（outpaint）到 2:1。

## 物件位置（讓老師校準線索時更省事）

每個場景的學習線索已預先放在下列位置（x = 從左算起的水平百分比，y = 從上算起的垂直百分比）。請盡量讓對應的物體出現在這附近；若做不到也沒關係，老師之後可以用編輯器的十字準心重新校準。

### 1. dongding.jpg ── 鹿谷・凍頂烏龍茶

| 位置 | 應出現的物體 |
| :--- | :--- |
| x 8%, y 43% | 遠方被雲霧環繞的茶園山坡 |
| x 24%, y 53% | 戴斗笠的茶農正在採「一心二葉」嫩芽 |
| x 40%, y 57% | 竹篩上攤開萎凋的新鮮茶葉 |
| x 57%, y 54% | 製茶工坊裡用布包成大球的茶葉、布球揉捻機 |
| x 74%, y 56% | 炭火上的竹焙籠在烘焙茶葉 |
| x 89%, y 52% | 小徑旁的老茶樹與一塊樸素石碑 |

```
Seamless 360-degree equirectangular panorama, 2:1 aspect ratio, 8K, eye-level camera at 1.5 m standing height, perfectly level horizon at the vertical center, natural human-eye scale. Scene: a terraced oolong tea plantation on Dongding Mountain, Lugu Township, Nantou, Taiwan, mid-altitude hills wrapped in soft morning mist. Neat curved rows of bright green tea bushes on the slopes; a tea farmer in a conical hat picking "one bud two leaves"; bamboo trays of fresh leaves withering in the shade; an open-front traditional tea workshop with a cloth-ball rolling machine and cloth-wrapped tea balls; bamboo roasting baskets over a gentle charcoal fire; a small stone marker and an old tea tree beside the path; distant layered blue mountains. Warm, inviting, highly detailed, beautiful natural light, educational picture-book quality, suitable for elementary school students.
Negative: fisheye, lens distortion, curved horizon, tilted horizon, drone view, aerial view, top-down view, tiny planet, visible seams, people looking at camera, text, watermark, logo.
```

### 2. yuchi.jpg ── 魚池・日月潭紅茶

| 位置 | 應出現的物體 |
| :--- | :--- |
| x 8%, y 47% | 雲霧繚繞的日月潭湖面與群山 |
| x 25%, y 53% | 高大、葉片寬大的阿薩姆茶樹 |
| x 42%, y 54% | 茶桌上一杯紅亮的紅茶與茶葉（台茶18號紅玉） |
| x 58%, y 57% | 萎凋架與發酵盤上變成紅褐色的茶葉 |
| x 75%, y 50% | 日治時期風格的紅磚老茶廠 |
| x 90%, y 53% | 綠意盎然、整理良好的友善茶園 |

```
Seamless 360-degree equirectangular panorama, 2:1 aspect ratio, 8K, eye-level camera at 1.5 m standing height, perfectly level horizon at the vertical center, natural human-eye scale. Scene: a tea garden on a gentle hillside beside Sun Moon Lake, Yuchi Township, Nantou, Taiwan. Tall broad-leaf Assam tea trees; emerald lake with misty mountains behind; a red-brick Japanese-era tea factory with long windows; black tea leaves spread on withering racks and copper-red fermented leaves on trays; cups of bright red-amber black tea on a wooden table; wild mountain tea trees at the forest edge; late-afternoon golden light. Warm, inviting, highly detailed, educational picture-book quality, suitable for elementary school students.
Negative: fisheye, lens distortion, curved horizon, tilted horizon, drone view, aerial view, top-down view, tiny planet, visible seams, people looking at camera, text, watermark, logo.
```

### 3. puli.jpg ── 埔里・茭白筍

| 位置 | 應出現的物體 |
| :--- | :--- |
| x 8%, y 54% | 清澈的小溪與灌溉水圳 |
| x 25%, y 58% | 泡在淺水裡的茭白筍田 |
| x 42%, y 53% | 近景高大的茭白筍植株（可看到莖部膨大） |
| x 58%, y 56% | 工寮籃子裡剝好、白嫩修長的「美人腿」 |
| x 75%, y 57% | 穿青蛙裝在水田裡採收的農夫 |
| x 90%, y 52% | 被群山環繞、一望無際的埔里盆地筍田 |

```
Seamless 360-degree equirectangular panorama, 2:1 aspect ratio, 8K, eye-level camera at 1.5 m standing height, perfectly level horizon at the vertical center, natural human-eye scale. Scene: water bamboo (Manchurian wild rice, jiaobai shoots) paddy fields in the Puli basin, Nantou, Taiwan. Shallow clear irrigation water reflecting the sky between tall green leafy stalks; a farmer in chest waders harvesting stalks; a crisp clear stream and irrigation channel; a small farm shed with peeled ivory-white water bamboo shoots piled in baskets; egrets standing in the paddy; green mountains surrounding the basin; bright clear morning. Warm, inviting, highly detailed, educational picture-book quality, suitable for elementary school students.
Negative: fisheye, lens distortion, curved horizon, tilted horizon, drone view, aerial view, top-down view, tiny planet, visible seams, people looking at camera, text, watermark, logo.
```

### 4. xinyi.jpg ── 信義・梅子

| 位置 | 應出現的物體 |
| :--- | :--- |
| x 8%, y 44% | 幾株還開著白色梅花的梅樹 |
| x 25%, y 53% | 提著竹籃採青梅的農夫、結滿青梅的梅樹 |
| x 42%, y 56% | 木桌上一堆青綠梅子與鹽、糖 |
| x 58%, y 57% | 一排大玻璃罐：脆梅、紫蘇梅、梅汁 |
| x 75%, y 52% | 帶有布農族木雕圖紋的部落建築 |
| x 90%, y 47% | 雲霧中的高山與天空 |

```
Seamless 360-degree equirectangular panorama, 2:1 aspect ratio, 8K, eye-level camera at 1.5 m standing height, perfectly level horizon at the vertical center, natural human-eye scale. Scene: a plum orchard on a cool mountain slope in Xinyi Township, Nantou, Taiwan, near a Bunun indigenous village. Plum trees heavy with green plums; a few trees still with late white plum blossoms; farmers with bamboo baskets of green plums; a processing yard with large glass jars of crispy plums, purple perilla plums and plum syrup; wooden tables with bowls of salt and sugar; carved wooden indigenous motifs on a village building; high mountains with drifting clouds; fresh spring light. Warm, inviting, highly detailed, educational picture-book quality, suitable for elementary school students.
Negative: fisheye, lens distortion, curved horizon, tilted horizon, drone view, aerial view, top-down view, tiny planet, visible seams, people looking at camera, text, watermark, logo.
```

### 5. zhushan.jpg ── 竹山・竹筍

| 位置 | 應出現的物體 |
| :--- | :--- |
| x 8%, y 42% | 高聳筆直的孟宗竹林 |
| x 25%, y 61% | 地面裂縫中剛冒頭的冬筍，旁邊放著鋤頭 |
| x 42%, y 54% | 籃子裡各種新鮮竹筍 |
| x 58%, y 57% | 農家庭院竹架上曬太陽的筍片 |
| x 75%, y 53% | 屋簷下編竹籃的師傅與竹編成品 |
| x 90%, y 47% | 竹林覆蓋、雲霧繚繞的山坡 |

```
Seamless 360-degree equirectangular panorama, 2:1 aspect ratio, 8K, eye-level camera at 1.5 m standing height, perfectly level horizon at the vertical center, natural human-eye scale. Scene: a Moso bamboo forest on a hillside in Zhushan Township, Nantou, Taiwan. Tall straight green bamboo culms with dappled sunlight; cracked soil with a winter bamboo shoot just peeking out and a hoe beside it; baskets of fresh bamboo shoots; a farmhouse courtyard with sliced bamboo shoots drying in the sun on bamboo racks; a craftsman weaving a bamboo basket under the eaves with finished bamboo crafts displayed; misty forested hills; calm, peaceful atmosphere. Warm, inviting, highly detailed, educational picture-book quality, suitable for elementary school students.
Negative: fisheye, lens distortion, curved horizon, tilted horizon, drone view, aerial view, top-down view, tiny planet, visible seams, people looking at camera, text, watermark, logo.
```

## 完成後必做

1. 確認 5 張圖都是 2:1、檔名正確、放在 `img/pano/`。
2. 在本資料夾執行：

   ```
   python sync_pano.py
   ```

   這會把新圖轉成 Base64 寫進 `data/pano_data.js`（離線與匯出都靠它）。
3. **不要修改** `data/eras.json`、`data/eras.js`、`js/`、`css/`、`index.html`、`editor.html`。
4. 回報：每張圖的尺寸、檔案大小，以及有沒有做接縫修補。

## （選做）更精緻的吉祥物、徽章與證書

目前這些是向量插畫，已可正常使用。若要升級，請保持**檔名、尺寸與透明背景**不變：

- `img/mascot.png`（1024×1024，透明背景）：可愛的「茶芽小隊長」，嫩綠茶芽造型的身體、戴小斗笠、黃色領巾，Q 版、友善，正面全身。
- `img/badges/dongding.png`、`yuchi.png`、`puli.png`、`xinyi.png`、`zhushan.png`（512×512，透明背景）：圓形金邊榮譽徽章，中央圖案分別是「冒煙的烏龍茶杯與茶葉」、「紅茶壺」、「水滴與茭白筍」、「梅枝青梅與白梅花」、「竹筍與竹葉」，不要放文字。
- `img/certificate-bg.png`（1754×1240，不透明）：米白紙質證書底圖，四周是茶葉藤蔓與南投農產（茶、梅、竹、水）裝飾邊框，**中央大面積留白**，底部 150 px 內不要放密集圖案（那裡會印頒發單位與日期）。

改完後同樣執行 `python sync_pano.py`（它也會同步吉祥物、徽章和證書）。
