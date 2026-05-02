"""
AI鏂伴椈鑷姩鎶撳彇鑴氭湰
瀹氭湡浠庡涓潵婧愭姄鍙栨渶鏂扮殑AI璧勮锛屽苟鐢熸垚JSON鏁版嵁渚涚綉绔欎娇鐢?"""

import json
import requests
from datetime import datetime
import time
import os

class AINewsScraper:
    def __init__(self):
        self.news_sources = [
            {
                'name': 'MIT Technology Review - AI',
                'url': 'https://www.technologyreview.com/topic/artificial-intelligence/',
                'type': 'rss'  # 瀹為檯搴斾娇鐢≧SS鎴朅PI
            },
            {
                'name': 'AI News Aggregator',
                'url': 'https://newsapi.org/v2/everything',
                'type': 'api',
                'api_key': 'YOUR_NEWSAPI_KEY',  # 闇€瑕佺敵璇峰厤璐笰PI key
                'query': 'artificial intelligence OR machine learning OR deep learning'
            }
        ]
        
        self.output_file = 'news_data.json'
    
    def fetch_news_from_api(self):
        """
        浣跨敤NewsAPI鎶撳彇AI鏂伴椈锛堥渶瑕佺敵璇峰厤璐笰PI key锛?        娉ㄥ唽鍦板潃: https://newsapi.org/register
        """
        print("馃摪 姝ｅ湪浠嶯ewsAPI鎶撳彇AI鏂伴椈...")
        
        # 濡傛灉娌℃湁API key锛岃繑鍥炴ā鎷熸暟鎹?        if self.news_sources[1]['api_key'] == 'YOUR_NEWSAPI_KEY':
            print("鈿狅笍  鏈厤缃甆ewsAPI瀵嗛挜锛屼娇鐢ㄦā鎷熸暟鎹?)
            return self.generate_mock_news()
        
        api_key = self.news_sources[1]['api_key']
        url = self.news_sources[1]['url']
        
        params = {
            'q': self.news_sources[1]['query'],
            'language': 'zh' or 'en',
            'sortBy': 'publishedAt',
            'pageSize': 20,
            'apiKey': api_key
        }
        
        try:
            response = requests.get(url, params=params, timeout=10)
            if response.status_code == 200:
                data = response.json()
                articles = data.get('articles', [])
                
                news_list = []
                for article in articles[:10]:  # 鍙彇鍓?0鏉?                    news_list.append({
                        'title': article.get('title', ''),
                        'summary': article.get('description', ''),
                        'url': article.get('url', ''),
                        'source': article.get('source', {}).get('name', ''),
                        'date': article.get('publishedAt', '')[:10]  # 鍙繚鐣欐棩鏈熼儴鍒?                    })
                
                print(f"鉁?鎴愬姛鎶撳彇 {len(news_list)} 鏉℃柊闂?)
                return news_list
            else:
                print(f"鉂?API璇锋眰澶辫触: {response.status_code}")
                return self.generate_mock_news()
        
        except Exception as e:
            print(f"鉂?鎶撳彇澶辫触: {e}")
            return self.generate_mock_news()
    
    def generate_mock_news(self):
        """
        鐢熸垚妯℃嫙鏂伴椈鏁版嵁锛堢敤浜庢紨绀烘垨褰揂PI涓嶅彲鐢ㄦ椂锛?        """
        mock_news = [
            {
                'title': 'OpenAI鍙戝竷GPT-5棰勮鐗堬紝澶氭ā鎬佽兘鍔涘ぇ骞呮彁鍗?,
                'summary': '鏈€鏂版ā鍨嬪湪鍥惧儚鐞嗚В銆佷唬鐮佺敓鎴愬拰鎺ㄧ悊鑳藉姏涓婂彇寰楃獊鐮存€ц繘灞曪紝鑳藉鍚屾椂澶勭悊鏂囨湰銆佸浘鍍忓拰闊抽杈撳叆...',
                'url': 'https://openai.com/blog',
                'source': 'OpenAI瀹樻柟鍗氬',
                'date': datetime.now().strftime('%Y-%m-%d')
            },
            {
                'title': 'DeepMind鐨凙lphaFold 3鎴愬姛棰勬祴铔嬬櫧璐ㄧ浉浜掍綔鐢?,
                'summary': '鏂扮増鏈彲浠ュ噯纭娴嬭泲鐧借川涓庡叾浠栧垎瀛愮殑鐩镐簰浣滅敤锛屼负鏂拌嵂鐮斿彂甯︽潵闈╁懡鎬х獊鐮?..',
                'url': 'https://deepmind.google/discover/blog/',
                'source': 'Nature鏈熷垔',
                'date': (datetime.now()).strftime('%Y-%m-%d')
            },
            {
                'title': '涓浗鍙戝竷棣栦釜鑷富鍙帶鐨勫ぇ妯″瀷鏍囧噯浣撶郴',
                'summary': '宸ヤ俊閮ㄧ壍澶村埗瀹氱殑AI澶фā鍨嬪浗瀹舵爣鍑嗘寮忓彂甯冿紝鎺ㄥ姩AI浜т笟瑙勮寖鍖栧彂灞曪紝鎻愬崌鍥介檯绔炰簤鍔?..',
                'url': 'http://www.miit.gov.cn/',
                'source': '鏂板崕绀?,
                'date': (datetime.now()).strftime('%Y-%m-%d')
            },
            {
                'title': 'Meta寮€婧怢lama 4锛屾€ц兘瓒呰秺GPT-4',
                'summary': '鏂颁竴浠ｅ紑婧愬ぇ妯″瀷鍦ㄥ椤瑰熀鍑嗘祴璇曚腑琛ㄧ幇浼樺紓锛屼笖瀹屽叏寮€鏀惧晢鐢紝寮曞彂寮€婧怉I绀惧尯鐑...',
                'url': 'https://ai.meta.com/blog/',
                'source': 'Meta AI',
                'date': (datetime.now()).strftime('%Y-%m-%d')
            },
            {
                'title': 'AI Agent鎶€鏈獊鐮达細鑷富瀹屾垚澶嶆潅浠诲姟鐨凙I鍔╂墜',
                'summary': '鐮旂┒浜哄憳灞曠ず浜嗚兘澶熻嚜涓昏鍒掋€佹墽琛屽拰鍙嶆€濈殑AI Agent绯荤粺锛屽湪杞欢寮€鍙戝拰鏁版嵁鍒嗘瀽浠诲姟涓〃鐜板嚭鑹?..',
                'url': 'https://arxiv.org/',
                'source': 'arXiv preprint',
                'date': (datetime.now()).strftime('%Y-%m-%d')
            },
            {
                'title': '娆х洘AI娉曟姝ｅ紡鐢熸晥锛屽叏鐞傾I鐩戠杩涘叆鏂伴樁娈?,
                'summary': '涓栫晫涓婄涓€閮ㄥ叏闈㈢殑浜哄伐鏅鸿兘娉曟寮€濮嬪疄鏂斤紝瀵逛笉鍚岄闄╃骇鍒殑AI绯荤粺杩涜鍒嗙被鐩戠...',
                'url': 'https://digital-strategy.ec.europa.eu/',
                'source': '娆х洘濮斿憳浼?,
                'date': (datetime.now()).strftime('%Y-%m-%d')
            },
            {
                'title': 'Google鍙戝竷Gemini 2.0锛屽妯℃€佹帹鐞嗚兘鍔涘啀鍗囩骇',
                'summary': 'Gemini 2.0鍦ㄨ棰戠悊瑙ｃ€佷唬鐮佺敓鎴愬拰绉戝鎺ㄧ悊鏂归潰鍙栧緱閲嶅ぇ杩涘睍锛屾寫鎴楪PT-4鐨勯瀵煎湴浣?..',
                'url': 'https://blog.google/technology/ai/',
                'source': 'Google AI',
                'date': (datetime.now()).strftime('%Y-%m-%d')
            },
            {
                'title': 'Anthropic鐨凜laude 3.5 Opus鍦ㄥ椤规祴璇曚腑瓒呰秺浜虹被涓撳',
                'summary': '鏈€鏂扮殑Claude妯″瀷鍦ㄥ尰瀛︺€佹硶寰嬪拰缂栫▼绛変笓涓氶鍩熷睍鐜板嚭瓒呰秺浜虹被涓撳鐨勮兘鍔?..',
                'url': 'https://www.anthropic.com/news',
                'source': 'Anthropic瀹樻柟',
                'date': (datetime.now()).strftime('%Y-%m-%d')
            }
        ]
        
        print(f"鉁?宸茬敓鎴?{len(mock_news)} 鏉℃ā鎷熸柊闂?)
        return mock_news
    
    def save_news_to_file(self, news_list):
        """
        灏嗘柊闂绘暟鎹繚瀛樹负JSON鏂囦欢
        """
        output_data = {
            'last_update': datetime.now().isoformat(),
            'total_count': len(news_list),
            'news': news_list
        }
        
        with open(self.output_file, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)
        
        print(f"馃捑 鏂伴椈鏁版嵁宸蹭繚瀛樺埌: {self.output_file}")
        print(f"   鍏?{len(news_list)} 鏉℃柊闂?)
        print(f"   鏇存柊鏃堕棿: {output_data['last_update']}")
    
    def run(self):
        """
        鎵ц瀹屾暣鐨勬柊闂绘姄鍙栨祦绋?        """
        print("="*60)
        print("馃 AI鏂伴椈鑷姩鎶撳彇绯荤粺")
        print("="*60)
        print()
        
        # 鎶撳彇鏂伴椈
        news_list = self.fetch_news_from_api()
        
        # 淇濆瓨鏁版嵁
        if news_list:
            self.save_news_to_file(news_list)
            
            # 鍚屾椂鏇存柊缃戠珯棣栭〉鐨凧avaScript鏁版嵁
            self.update_website_data(news_list)
            
            print()
            print("鉁?鏂伴椈鎶撳彇瀹屾垚锛?)
            print(f"   涓嬫鏇存柊寤鸿: {(datetime.now()).strftime('%Y-%m-%d')} (寤鸿姣忓ぉ鏇存柊)")
        else:
            print("鉂?鏈兘鑾峰彇鏂伴椈鏁版嵁")
        
        print("="*60)
    
    def update_website_data(self, news_list):
        """
        鏇存柊缃戠珯棣栭〉鐨凧avaScript鏁版嵁
        灏嗘柊闂绘暟鎹祵鍏ュ埌index.html涓?        """
        try:
            # 璇诲彇鐜版湁鐨刬ndex.html
            with open('index.html', 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 鐢熸垚JavaScript鏁版嵁
            js_data = "const mockNews = " + json.dumps(news_list, ensure_ascii=False, indent=4) + ";"
            
            # 鏇挎崲鍘熸湁鐨刴ockNews鏁版嵁
            import re
            pattern = r'const mockNews = \[.*?\];'
            replacement = js_data
            
            # 濡傛灉鏂囦欢涓湁mockNews瀹氫箟锛屽垯鏇挎崲
            if 'const mockNews = [' in content:
                # 杩欓噷闇€瑕佹洿澶嶆潅鐨勬浛鎹㈤€昏緫锛岀畝鍗曡捣瑙侊紝鎴戜滑鍙洿鏂癑SON鏂囦欢
                pass
            
            print("馃挕 鎻愮ず: 璇锋墜鍔ㄥ皢 news_data.json 涓殑鏁版嵁鏇存柊鍒?index.html")
            print(f"   鎴栬€呴厤缃甒eb鏈嶅姟鍣ㄤ互鍔ㄦ€佸姞杞?{self.output_file}")
        
        except Exception as e:
            print(f"鈿狅笍  鏇存柊缃戠珯鏁版嵁澶辫触: {e}")

def main():
    """
    涓诲嚱鏁?    """
    scraper = AINewsScraper()
    scraper.run()
    
    # 濡傛灉閰嶇疆浜嗗畾鏃朵换鍔★紝鍙互鍦ㄨ繖閲屾坊鍔犲畾鏃堕€昏緫
    # 渚嬪锛氭瘡澶╁噷鏅?鐐硅嚜鍔ㄨ繍琛?    print()
    print("馃搮 瀹氭椂浠诲姟閰嶇疆寤鸿:")
    print("   Windows浠诲姟璁″垝绋嬪簭:")
    print("     1. 鎵撳紑浠诲姟璁″垝绋嬪簭")
    print("     2. 鍒涘缓鍩烘湰浠诲姟")
    print("     3. 瑙﹀彂鍣? 姣忓ぉ")
    print("     4. 鎿嶄綔: 鍚姩绋嬪簭")
    print("     5. 绋嬪簭: python")
    print(f"     6. 鍙傛暟: {os.path.abspath(__file__)}")
    print()
    print("   Linux/Mac cron:")
    print("     0 2 * * * cd /path/to/website && python scraper.py")

if __name__ == '__main__':
    main()
