# 給 Codex 的生圖任務：南投食農小旅行・第二站 360° 全景圖

> 使用方式：把這整份檔案交給 Codex，並讓它在本資料夾（`360-tour-2/`）裡執行。

## 你的任務

這是第二站的 360° 互動教材，內容已寫好（`data/eras.json`）。目前 `img/pano/` 裡的六張全景圖是程式畫的「示意暫用圖」（上面有標籤文字與「示意暫用圖」字樣）。請用圖片生成工具產出 **6 張精美的 360° 等距長方投影（equirectangular）全景圖**，覆蓋暫用圖，然後執行同步腳本。

## 必須遵守的規格

| 項目 | 要求 |
| :--- | :--- |
| 投影 | 360° × 180° 等距長方投影（equirectangular） |
| 比例 | **嚴格 2:1**，建議 4096 × 2048（至少 2048 × 1024） |
| 格式 | JPG，品質 85 左右，每張盡量控制在 2 MB 以內 |
| 地平線 | 正好在圖片垂直正中央（y = 50%），完全水平 |
| 視角 | 人站立平視（約 1.5 公尺高），不要魚眼、空拍、俯視、小行星效果 |
| 左右接縫 | 圖片最左邊和最右邊必須能無縫接合 |
| 禁止 | 文字、浮水印、Logo、店家招牌、品牌標誌、看鏡頭的人臉 |
| 風格 | 溫暖明亮、細節豐富、繪本插畫級精緻質感，適合國小學生 |

**檔名必須完全一致（不要改 `data/eras.json`）：**

```
img/pano/guoxing.jpg     國姓・咖啡
img/pano/jiji.jpg        集集・香蕉
img/pano/zhongliao.jpg   中寮・龍眼
img/pano/renai.jpg       仁愛・高冷蔬菜
img/pano/caotun.jpg      草屯・稻米
img/pano/mingjian.jpg    名間・鳳梨
```

## 如果生圖工具無法直接輸出 2:1 全景

1. 用工具支援的最大寬幅尺寸生成，提示詞照樣寫 equirectangular 360 panorama。
2. 用 Python Pillow 以 LANCZOS 放大到 4096 × 2048。
3. 檢查左右接縫：把圖片水平平移 50% 後看中間是否有明顯斷線；若有，對中間約 200 px 做 inpaint 或羽化混合修補，再平移回來。
4. 比例不是 2:1 時不要拉伸，改為補畫天空與地面（outpaint）到 2:1。

## 物件位置（讓老師校準線索時更省事）

x = 從左算起的水平百分比，y = 從上算起的垂直百分比。請盡量讓對應物體出現在這附近；做不到也沒關係，老師之後可用編輯器的十字準心重新校準。整張圖要是**同一個季節、同一個時刻**的合理場景。

### 1. guoxing.jpg ── 國姓・咖啡

| 位置 | 應出現的物體 |
| :--- | :--- |
| x 8%, y 44% | 遠方山坡，可見已長滿植被的舊崩塌地 |
| x 25%, y 55% | 近景咖啡樹，枝條上紅、黃、綠不同熟度的咖啡果實 |
| x 42%, y 54% | 咖啡樹枝上掛著的紅色小型誘捕器 |
| x 58%, y 58% | 曬場上攤開日曬的紅色果實，旁邊有水洗槽 |
| x 66%, y 50% | 一台不鏽鋼的咖啡果實處理機器（彩蛋） |
| x 75%, y 56% | 挑豆桌上的淺綠色生豆與竹篩 |
| x 90%, y 55% | 麻布袋、小型烘豆機和一杯咖啡 |

```
Seamless 360-degree equirectangular panorama, 2:1 aspect ratio, 8K, eye-level camera at 1.5 m standing height, perfectly level horizon at the vertical center, natural human-eye scale. Scene: a hillside coffee farm in Guoxing Township, Nantou, Taiwan, at low-to-mid altitude in harvest season. Rows of coffee shrubs with clusters of ripe red, yellow and green coffee cherries; small red insect traps hanging in the branches; a drying yard with red coffee cherries spread in the sun on raised beds; a concrete washing channel and fermentation tanks; a compact stainless-steel coffee processing machine; a sorting table with pale green coffee beans and bamboo sieves; burlap sacks, a small drum coffee roaster and a cup of coffee on a wooden bench; distant green hills, one slope showing an old landslide scar now covered with young vegetation. Warm, inviting, highly detailed, educational picture-book quality, suitable for elementary school students.
Negative: fisheye, lens distortion, curved horizon, tilted horizon, drone view, aerial view, top-down view, tiny planet, visible seams, people looking at camera, text, watermark, logo, signboard.
```

### 2. jiji.jpg ── 集集・香蕉

| 位置 | 應出現的物體 |
| :--- | :--- |
| x 8%, y 46% | 遠方坡地上的整片香蕉園，可隱約看到小火車鐵道 |
| x 25%, y 52% | 近景高大的香蕉植株，清楚看到假莖與寬大葉片 |
| x 42%, y 55% | 掛著果串的香蕉植株，旁邊斜撐著防風支柱 |
| x 58%, y 57% | 集貨場：在水槽清洗青香蕉、裝進紙箱 |
| x 67%, y 60% | 一把放在陰涼處、旁邊有溫度計的熟香蕉（彩蛋） |
| x 75%, y 53% | 催熟室（冷藏庫外觀），門口內青蕉、外黃蕉的對比 |
| x 90%, y 56% | 一段被砍下的假莖，切面露出層層纖維，旁邊一捆蕉絲 |

```
Seamless 360-degree equirectangular panorama, 2:1 aspect ratio, 8K, eye-level camera at 1.5 m standing height, perfectly level horizon at the vertical center, natural human-eye scale. Scene: a hillside banana plantation in Jiji Township, Nantou, Taiwan. Tall banana plants with thick pseudostems and huge broad leaves; heavy green banana bunches wrapped in blue protective bags; wooden or bamboo support poles propping up the plants against typhoon winds; a packing shed where hands of green bananas are washed in water tanks and packed into cardboard boxes; a white cold-storage ripening room with green bananas inside and yellow ripe bananas outside; a cut banana pseudostem showing layered fibers beside a bundle of natural banana fiber; distant green slopes covered with banana plants and a small local railway line in the valley. Warm, inviting, highly detailed, educational picture-book quality, suitable for elementary school students.
Negative: fisheye, lens distortion, curved horizon, tilted horizon, drone view, aerial view, top-down view, tiny planet, visible seams, people looking at camera, text, watermark, logo, signboard.
```

### 3. zhongliao.jpg ── 中寮・龍眼

| 位置 | 應出現的物體 |
| :--- | :--- |
| x 8%, y 45% | 起伏淺山上成片的龍眼林 |
| x 25%, y 52% | 近景龍眼樹，掛滿一串串黃褐色龍眼 |
| x 42%, y 56% | 一整排磚砌傳統焙灶，灶上鋪滿龍眼，冒出淡淡燻煙 |
| x 58%, y 58% | 焙灶灶口的柴火、堆疊的木柴與翻焙用竹耙 |
| x 66%, y 52% | 廣場邊掛著燈籠的小棚子（節慶感，不要文字）（彩蛋） |
| x 75%, y 56% | 木桌上對比：新鮮龍眼、帶殼龍眼乾、剝好的桂圓肉 |
| x 90%, y 50% | 果園邊的木製蜂箱與一罐琥珀色龍眼蜜 |

```
Seamless 360-degree equirectangular panorama, 2:1 aspect ratio, 8K, eye-level camera at 1.5 m standing height, perfectly level horizon at the vertical center, natural human-eye scale. Scene: a longan orchard village in the low hills of Zhongliao Township, Nantou, Taiwan, in late summer. Rolling hills covered with dense longan trees; a near longan tree heavy with clusters of tan-brown longan fruit; a long row of traditional red-brick longan roasting kilns with fruit spread on top and thin wood smoke rising; a kiln mouth with a gentle wood fire, stacked firewood and a bamboo rake for turning fruit; a small festive tent with paper lanterns at the edge of a village square; a wooden table showing fresh longans, dried longans in shell and peeled dried longan flesh; wooden beehives and a jar of amber longan honey beside the orchard. Warm golden late-afternoon light, inviting, highly detailed, educational picture-book quality, suitable for elementary school students.
Negative: fisheye, lens distortion, curved horizon, tilted horizon, drone view, aerial view, top-down view, tiny planet, visible seams, people looking at camera, text, watermark, logo, signboard.
```

### 4. renai.jpg ── 仁愛・高冷蔬菜

| 位置 | 應出現的物體 |
| :--- | :--- |
| x 8%, y 44% | 雲霧繚繞的高山稜線、遠處草原與小羊群 |
| x 25%, y 58% | 近景一排排結球高麗菜 |
| x 42%, y 55% | 菜園邊坡的水泥排水溝與綠色草帶（良好示範） |
| x 58%, y 57% | 另一片土壤裸露、被雨水沖出小溝的坡地，溪水黃濁（不良示範） |
| x 66%, y 60% | 田邊一籃剛採收的高麗菜（彩蛋） |
| x 75%, y 48% | 遠方山谷中的水庫，水邊可見淤積的沙洲 |
| x 90%, y 53% | 菜園與森林的交界，有新種的樹苗 |

```
Seamless 360-degree equirectangular panorama, 2:1 aspect ratio, 8K, eye-level camera at 1.5 m standing height, perfectly level horizon at the vertical center, natural human-eye scale. Scene: high-mountain cabbage farms near Cingjing, Ren'ai Township, Nantou, Taiwan, around 1,700 m elevation in summer. Terraced fields of round green cabbages under cool misty mountain ridges with conifer forest; a well-kept field edge with a concrete drainage ditch and a strip of green grass protecting the soil; in contrast, another slope with bare exposed soil and small rain gullies, a muddy brown stream below; a reservoir far down in the valley with visible sediment sandbars; the boundary between farmland and forest with rows of newly planted tree saplings; a basket of freshly harvested cabbages at the field edge; a distant grassy meadow with a few sheep. Fresh, cool, clear light, highly detailed, educational picture-book quality, suitable for elementary school students.
Negative: fisheye, lens distortion, curved horizon, tilted horizon, drone view, aerial view, top-down view, tiny planet, visible seams, people looking at camera, text, watermark, logo, signboard, hotel buildings.
```

### 5. caotun.jpg ── 草屯・稻米

整張圖可用「左半邊插秧期嫩綠、右半邊成熟期金黃」的方式呈現兩個時期（中間以田埂自然分隔）。

| 位置 | 應出現的物體 |
| :--- | :--- |
| x 8%, y 46% | 遠方山脈與流向稻田的灌溉水圳 |
| x 25%, y 57% | 一盤盤育苗箱和插秧機，水田剛插好的秧苗 |
| x 42%, y 58% | 排乾水的稻田，表土出現小裂縫（曬田），稻株已長多分蘗 |
| x 58%, y 55% | 正在抽穗的綠色稻子 |
| x 66%, y 62% | 田埂上的稻草人（彩蛋） |
| x 75%, y 57% | 低頭的金黃稻穗與正在收割的收割機 |
| x 90%, y 52% | 鄉間的稻穀乾燥中心（筒倉與廠房外觀，不要文字） |

```
Seamless 360-degree equirectangular panorama, 2:1 aspect ratio, 8K, eye-level camera at 1.5 m standing height, perfectly level horizon at the vertical center, natural human-eye scale. Scene: flat rice paddies in Caotun Township, Nantou, Taiwan, showing the journey of rice. On one side, flooded paddies with freshly transplanted bright green seedlings, stacks of seedling trays and a rice transplanter; an irrigation canal bringing clear water from distant mountains; a drained paddy with slightly cracked soil and bushy tillering rice plants; rice plants beginning to head; a friendly scarecrow on a field ridge; on the other side, golden ripe rice with drooping heads and a combine harvester at work; a rural grain drying center with silos and a warehouse. Bright clear sky, warm and inviting, highly detailed, educational picture-book quality, suitable for elementary school students.
Negative: fisheye, lens distortion, curved horizon, tilted horizon, drone view, aerial view, top-down view, tiny planet, visible seams, people looking at camera, text, watermark, logo, signboard.
```

### 6. mingjian.jpg ── 名間・鳳梨

| 位置 | 應出現的物體 |
| :--- | :--- |
| x 8%, y 46% | 紅色土壤台地上一壟壟的鳳梨田，遠處有茶園 |
| x 25%, y 57% | 近景一株鳳梨，看得出頂端冠芽、果實下方裔芽與莖旁吸芽 |
| x 42%, y 55% | 正在田間作業的農夫（側身或背影） |
| x 58%, y 58% | 果實上覆蓋紙張或稻草防曬的鳳梨 |
| x 66%, y 52% | 木桌上一顆切開的鳳梨，可見金黃果肉和果芯（彩蛋） |
| x 75%, y 56% | 由綠轉黃不同熟度的鳳梨並排 |
| x 90%, y 55% | 集貨場堆疊的紙箱（不要文字或商標） |

```
Seamless 360-degree equirectangular panorama, 2:1 aspect ratio, 8K, eye-level camera at 1.5 m standing height, perfectly level horizon at the vertical center, natural human-eye scale. Scene: pineapple fields on the red-soil Bagua tableland in Mingjian Township, Nantou, Taiwan, in spring harvest season. Long rows of pineapple plants with spiky sword-shaped leaves in red-orange soil; a close pineapple plant clearly showing the crown on top of the fruit, slips below the fruit and suckers from the stem; some fruits covered with paper or straw for sun protection; a farmer working in the field seen from behind; a wooden table with a sliced golden pineapple showing its core; a row of pineapples from green to golden yellow ripeness; plain cardboard boxes stacked at a small packing area; tea gardens on the distant tableland. Sunny, warm, highly detailed, educational picture-book quality, suitable for elementary school students.
Negative: fisheye, lens distortion, curved horizon, tilted horizon, drone view, aerial view, top-down view, tiny planet, visible seams, people looking at camera, text, watermark, logo, signboard.
```

## 完成後必做

1. 確認 6 張圖都是 2:1、檔名正確、放在 `img/pano/`。
2. 在本資料夾執行：

   ```
   python sync_pano_v2.py
   ```

   這會更新 `data/pano_data.js`、`data/cert_data.js`，並重新產生 `dist/南投食農小旅行第二站_學生獨立版.html`。
3. **不要修改** `data/eras.json`、`data/eras.js`、`js/`、`css/`、`index.html`、`editor.html`。
4. 回報：每張圖的尺寸、檔案大小，以及有沒有做接縫修補。

## （選做）更精緻的徽章

目前 `img/badges/` 是程式畫的文字徽章。若要升級，請保持**檔名、512×512、透明背景**不變，圓形金邊榮譽徽章，中央圖案不放文字：

- `guoxing.png`：紅色咖啡櫻桃與咖啡豆
- `jiji.png`：一串黃香蕉與香蕉葉
- `zhongliao.png`：龍眼串與小小焙灶火焰
- `renai.png`：高麗菜與山形線條
- `caotun.png`：金黃稻穗與一碗白飯
- `mingjian.png`：金黃鳳梨

改完後同樣執行 `python sync_pano_v2.py`。
