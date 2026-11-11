"""第二站素材同步與學生獨立版打包。

用法：在 360-tour-2 資料夾執行  python sync_pano_v2.py
1. 把 img/pano/*.jpg 轉成 Base64 寫入 data/pano_data.js
2. 把證書底圖、吉祥物、徽章寫入 data/cert_data.js
3. 由 data/eras.json 重新產生 data/eras.js
4. 產生 dist/南投食農小旅行第二站_學生獨立版.html（單一檔案，可離線使用）
"""
import base64
import io
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def p(*parts):
    return os.path.join(HERE, *parts)


def read(path):
    with open(p(path), encoding="utf-8") as f:
        return f.read()


def data_uri(path, as_jpeg=False):
    raw = open(p(path), "rb").read()
    if as_jpeg:
        try:
            from PIL import Image
            im = Image.open(io.BytesIO(raw)).convert("RGB")
            buf = io.BytesIO()
            im.save(buf, "JPEG", quality=88)
            raw = buf.getvalue()
            mime = "image/jpeg"
        except ImportError:
            mime = "image/png"
    else:
        mime = "image/png" if path.lower().endswith(".png") else "image/jpeg"
    return f"data:{mime};base64," + base64.b64encode(raw).decode("ascii")


def main():
    eras = json.loads(read("data/eras.json"))

    with open(p("data/eras.js"), "w", encoding="utf-8") as f:
        f.write("// data/eras.js - 自動同步自 eras.json\nwindow.ERAS_DATA = "
                + json.dumps(eras, ensure_ascii=False, indent=2) + ";\n")

    pano = {}
    for era in eras["eras"]:
        path = era.get("panorama") or f"img/pano/{era['id']}.jpg"
        if os.path.exists(p(path)):
            pano[era["id"]] = data_uri(path)
        else:
            print("找不到全景圖：", path)
    pano_js = ("// data/pano_data.js - 自動同步自 img/pano/ 的 360° 全景圖資料\n"
               "window.PANO_DATA = " + json.dumps(pano, indent=2) + ";\n")
    with open(p("data/pano_data.js"), "w", encoding="utf-8") as f:
        f.write(pano_js)

    cert = {"bg": data_uri("img/certificate-bg.png", as_jpeg=True),
            "mascot": data_uri("img/mascot.png")}
    for era in eras["eras"]:
        path = era.get("badge") or f"img/badges/{era['id']}.png"
        if os.path.exists(p(path)):
            cert[era["id"]] = data_uri(path)
    cert_js = ("// 南投食農小旅行第二站：證書、吉祥物與徽章離線資源（Base64）\n"
               "window.CERT_ASSETS = " + json.dumps(cert, indent=2) + ";\n")
    with open(p("data/cert_data.js"), "w", encoding="utf-8") as f:
        f.write(cert_js)

    # ---- 單檔學生獨立版 ----
    html = read("index.html")
    css = "<style>\n/* pannellum.css */\n" + read("css/pannellum.css") + "\n/* style.css */\n" + read("css/style.css") + "\n</style>"
    html = html.replace('<link rel="stylesheet" href="css/pannellum.css">', "")
    html = html.replace('<link rel="stylesheet" href="css/style.css">', css)

    def tag(code):
        # 避免內容中的 </script> 提早結束標籤
        return "<script>\n" + code.replace("</script>", "<\\/script>") + "\n</script>\n"

    bundle = (tag(read("js/pannellum.js"))
              + tag("window.ERAS_DATA = " + json.dumps(eras, ensure_ascii=False) + ";")
              + tag(pano_js) + tag(cert_js)
              + "".join(tag(read(f"js/{n}.js")) for n in
                        ["markdown", "storage", "audio", "viewer", "quiz", "certificate", "app"]))
    for src in ["js/pannellum.js", "data/eras.js", "data/pano_data.js", "data/cert_data.js",
                "js/markdown.js", "js/storage.js", "js/audio.js", "js/viewer.js",
                "js/quiz.js", "js/certificate.js"]:
        html = html.replace(f'<script src="{src}"></script>', "")
    html = html.replace('<script src="js/app.js"></script>', bundle)
    html = html.replace('src="img/mascot.png"', f'src="{cert["mascot"]}"')
    first = eras["eras"][0]["id"]
    if first in cert:
        html = html.replace(f'src="img/badges/{first}.png"', f'src="{cert[first]}"')

    os.makedirs(p("dist"), exist_ok=True)
    out = p("dist", "南投食農小旅行第二站_學生獨立版.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"完成：{len(pano)} 張全景圖、{len(cert) - 2} 枚徽章；獨立版 {os.path.getsize(out) / 1e6:.1f} MB")


if __name__ == "__main__":
    main()
