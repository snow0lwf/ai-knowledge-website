# AI閫氳瘑鍏ㄦ櫙缃戠珯

涓€涓泦鎴愪簡AI閫氳瘑鐭ヨ瘑鍜屾渶鏂癆I璧勮鐨勭綉绔欑郴缁燂紝鏀寔鑷姩鏇存柊銆?
## 馃専 鍔熻兘鐗规€?
- **馃摎 AI鐭ヨ瘑搴?*锛氱郴缁熶粙缁岮I鍙戝睍鍘嗙▼銆佷笁澶ф祦娲俱€佹満鍣ㄥ涔犮€佹繁搴﹀涔犵瓑鐭ヨ瘑
- **馃摪 鏈€鏂拌祫璁?*锛氳嚜鍔ㄦ姄鍙栨渶鏂扮殑AI琛屼笟鍔ㄦ€佸拰鏂伴椈
- **馃 鑷姩鏇存柊**锛氬畾鏃舵姄鍙朅I鏂伴椈锛屼繚鎸佸唴瀹规柊椴?- **馃摫 鍝嶅簲寮忚璁?*锛氭敮鎸丳C銆佸钩鏉裤€佹墜鏈虹瓑澶氱璁惧
- **馃啌 鍏嶈垂閮ㄧ讲**锛氬彲閮ㄧ讲鍒癎itHub Pages绛夊厤璐规墭绠℃湇鍔?
## 馃搧 椤圭洰缁撴瀯

```
ai-website/
鈹溾攢鈹€ index.html          # 缃戠珯棣栭〉锛堝寘鍚柊闂绘澘鍧楋級
鈹溾攢鈹€ knowledge.html      # AI鐭ヨ瘑搴撻〉闈?鈹溾攢鈹€ news_scraper.py    # 鏂伴椈鎶撳彇鑴氭湰
鈹溾攢鈹€ news_data.json      # 鏂伴椈鏁版嵁鏂囦欢锛堣嚜鍔ㄧ敓鎴愶級
鈹溾攢鈹€ README.md          # 椤圭洰璇存槑鏂囨。
鈹斺攢鈹€ .github/
    鈹斺攢鈹€ workflows/
        鈹斺攢鈹€ update-news.yml  # 鑷姩鏇存柊宸ヤ綔娴?```

## 馃殌 蹇€熷紑濮?
### 1. 鏈湴娴嬭瘯

鐩存帴鐢ㄦ祻瑙堝櫒鎵撳紑 `index.html` 鍗冲彲鏌ョ湅缃戠珯鏁堟灉銆?
濡傞渶娴嬭瘯鏂伴椈鎶撳彇鍔熻兘锛?
```bash
# 瀹夎渚濊禆
pip install requests

# 杩愯鏂伴椈鎶撳彇鑴氭湰
python news_scraper.py
```

### 2. 閰嶇疆鏂伴椈API锛堝彲閫夛級

濡傞渶鑾峰彇鐪熷疄AI鏂伴椈锛岃锛?
1. 璁块棶 [NewsAPI瀹樼綉](https://newsapi.org/register) 娉ㄥ唽鍏嶈垂璐﹀彿
2. 鑾峰彇API Key
3. 缂栬緫 `news_scraper.py`锛屽皢 `YOUR_NEWSAPI_KEY` 鏇挎崲涓轰綘鐨凙PI Key

```python
'sources[1]['api_key'] = '浣犵殑鐪熷疄API_Key'
```

### 3. 閮ㄧ讲鍒颁簰鑱旂綉

#### 鏂规A锛氶儴缃插埌GitHub Pages锛堟帹鑽愶級

1. **鍒涘缓GitHub浠撳簱**
   ```bash
   git init
   git add .
   git commit -m "鍒濆鎻愪氦"
   gh repo create ai-knowledge-website --public
   git push -u origin main
   ```

2. **鍚敤GitHub Pages**
   - 杩涘叆浠撳簱璁剧疆锛圫ettings锛?   - 鎵惧埌 "Pages" 閫夐」
   - Source 閫夋嫨 "GitHub Actions"

3. **閰嶇疆鑷姩鏇存柊**
   - 鎺ㄩ€佷唬鐮佸悗锛孏itHub Actions浼氳嚜鍔ㄨ繍琛?   - 姣忓ぉ鑷姩鎶撳彇鏈€鏂版柊闂诲苟鏇存柊缃戠珯

#### 鏂规B锛氶儴缃插埌鍏朵粬鍏嶈垂鎵樼鏈嶅姟

- **Vercel**锛氳繛鎺itHub浠撳簱锛岃嚜鍔ㄩ儴缃?- **Netlify**锛氭嫋鎷戒笂浼犳枃浠跺す锛屾垨杩炴帴Git浠撳簱
- **Cloudflare Pages**锛氱被浼糔etlify鐨勫厤璐规墭绠℃湇鍔?
## 鈴?閰嶇疆鑷姩鏇存柊

### Windows浠诲姟璁″垝绋嬪簭

1. 鎵撳紑"浠诲姟璁″垝绋嬪簭"
2. 鍒涘缓鍩烘湰浠诲姟
3. 瑙﹀彂鍣細姣忓ぉ
4. 鎿嶄綔锛氬惎鍔ㄧ▼搴?5. 绋嬪簭锛歚python.exe`
6. 鍙傛暟锛歚C:\瀹屾暣璺緞\news_scraper.py`
7. 璧峰浣嶇疆锛歚C:\瀹屾暣璺緞\`

### Linux/Mac cron瀹氭椂浠诲姟

```bash
# 缂栬緫crontab
crontab -e

# 娣诲姞浠ヤ笅琛岋紙姣忓ぉ鍑屾櫒2鐐硅繍琛岋級
0 2 * * * cd /path/to/ai-website && python news_scraper.py

# 淇濆瓨閫€鍑?```

### GitHub Actions鑷姩鏇存柊锛堟帹鑽愶級

宸插寘鍚?`.github/workflows/update-news.yml` 閰嶇疆鏂囦欢锛屾帹閫佷唬鐮佸悗浼氳嚜鍔細

- 姣忓ぉ鍑屾櫒3鐐硅嚜鍔ㄨ繍琛屾柊闂绘姄鍙栬剼鏈?- 鑷姩鎻愪氦骞舵洿鏂?`news_data.json`
- 鑷姩閮ㄧ讲鏇存柊鍚庣殑缃戠珯

## 馃帹 鑷畾涔変慨鏀?
### 淇敼缃戠珯鏍囬鍜岄鑹?
缂栬緫 `index.html` 鍜?`knowledge.html` 涓殑CSS鍙橀噺锛?
```css
:root {
    --primary: #1A73E8;  /* 涓婚鑹?*/
    --accent1: #E8704A;  /* 寮鸿皟鑹? */
    --accent2: #34A853;  /* 寮鸿皟鑹? */
}
```

### 娣诲姞鏂扮煡璇嗗唴瀹?
缂栬緫 `knowledge.html`锛屽湪瀵瑰簲鐨?`<div class="chapter">` 涓坊鍔犲唴瀹广€?
### 淇敼鏂伴椈鎶撳彇婧?
缂栬緫 `news_scraper.py` 涓殑 `news_sources` 鍒楄〃锛屾坊鍔犳洿澶氭柊闂绘簮锛?
```python
self.news_sources = [
    {
        'name': 'Your News Source',
        'url': 'https://example.com/rss',
        'type': 'rss'
    }
]
```

## 馃搳 鏁版嵁婧愯鏄?
褰撳墠閰嶇疆鐨勬柊闂绘潵婧愶細

1. **NewsAPI**锛坄newsapi.org`锛夛細闇€瑕佺敵璇峰厤璐笰PI Key
   - 鍙幏鍙栧叏鐞冧富娴佺鎶€濯掍綋鐨凙I鏂伴椈
   - 鍏嶈垂鐗堟瘡鏈?000娆¤姹?
2. **妯℃嫙鏁版嵁**锛氬綋API涓嶅彲鐢ㄦ椂锛岃嚜鍔ㄤ娇鐢ㄥ唴缃殑妯℃嫙鏂伴椈鏁版嵁

鏈潵鍙墿灞曠殑鏁版嵁婧愶細

- arXiv.org锛圓I瀛︽湳璁烘枃锛?- 鍚勫ぇAI鍏徃瀹樻柟鍗氬锛圤penAI銆丏eepMind銆丟oogle AI绛夛級
- 绉戞妧濯掍綋RSS璁㈤槄锛圡IT Tech Review銆乂entureBeat绛夛級

## 馃敡 鎶€鏈爤

- **鍓嶇**锛氱函HTML + CSS + JavaScript锛堟棤妗嗘灦锛屽姞杞藉揩閫燂級
- **鍚庣**锛歅ython 3.x锛堢敤浜庢柊闂绘姄鍙栵級
- **閮ㄧ讲**锛欸itHub Pages / Vercel / Netlify锛堥潤鎬佺綉绔欐墭绠★級
- **鑷姩鏇存柊**锛欸itHub Actions / cron / Windows浠诲姟璁″垝

## 馃摑 甯歌闂

### Q1: 涓轰粈涔堟柊闂绘樉绀虹殑鏄ā鎷熸暟鎹紵

A: 鍥犱负鏈厤缃甆ewsAPI瀵嗛挜銆傝鍙傝€?閰嶇疆鏂伴椈API"灏忚妭杩涜閰嶇疆銆?
### Q2: 濡備綍淇敼鑷姩鏇存柊鐨勯鐜囷紵

A: 缂栬緫 `.github/workflows/update-news.yml` 涓殑 `cron` 琛ㄨ揪寮忥細

```yaml
schedule:
  - cron: '0 3 * * *'  # 姣忓ぉ鍑屾櫒3鐐?  # 鏀逛负 '0 */6 * * *' 姣?灏忔椂涓€娆?```

### Q3: 鑳藉惁娣诲姞涓枃瀛椾綋浼樺寲锛?
A: 宸插湪CSS涓厤缃?`"Microsoft YaHei", "PingFang SC"` 绛変腑鏂囧瓧浣撱€?
### Q4: 濡備綍娣诲姞鏇村鐭ヨ瘑鍐呭锛?
A: 鐩存帴缂栬緫 `knowledge.html`锛屽弬鑰冪幇鏈夌珷鑺傛牸寮忔坊鍔犲嵆鍙€?
## 馃搫 璁稿彲璇?
MIT License - 鑷敱浣跨敤銆佷慨鏀瑰拰鍒嗗彂銆?
## 馃檹 鑷磋阿

- 鏂伴椈鏁版嵁鏉ユ簮锛歂ewsAPI
- AI鐭ヨ瘑鍐呭锛氱患鍚堝鏂规潈濞佽祫鏂欐暣鐞?- 缃戠珯妯℃澘锛氬弬鑰冪幇浠ｅ搷搴斿紡璁捐鏈€浣冲疄璺?
---

**馃帀 寮€濮嬩娇鐢?*

1. 鏈湴娴忚 `index.html` 鏌ョ湅鏁堟灉
2. 閰嶇疆NewsAPI鑾峰彇鐪熷疄鏂伴椈锛堝彲閫夛級
3. 閮ㄧ讲鍒癎itHub Pages璁╁叏鐞冭闂?4. 閰嶇疆鑷姩鏇存柊淇濇寔鍐呭鏂伴矞

濡傛湁闂锛屾杩庢彁Issue鎴朠R锛