from urllib.parse import urlparse, parse_qs
from DrissionPage import ChromiumPage, ChromiumOptions
import time

class HeaderParser:
    def __init__(self):
        # Create ChromiumOptions instance
        co = ChromiumOptions().headless()

        self.page = ChromiumPage(chromium_options=co)
        
        # Set headers
        self.page.set.headers({
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'
        })

    def parse_url_params(self, url):
        """Parse URL parameters into a dictionary"""
        parsed_url = urlparse(url)
        params = parse_qs(parsed_url.query)
        return {k: v[0] if len(v) == 1 else v for k, v in params.items()}

    def make_request(self, url):
        """Make a request using DrissionPage and save HTML content to file"""
        try:
            self.page.get(url)
            time.sleep(5)
            html_content = self.page.html
            with open('result.txt', 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            print("HTML content saved to result.txt")
            return True
                
        except Exception as e:
            print(f"Error making request: {e}")
            return False
            
def main():
    parser = HeaderParser()
    url = "https://dexscreener.com/?rankBy=trendingScoreH6&order=desc&chainIds=solana&dexIds=raydium,meteora&minLiq=1000&minMarketCap=3000000&maxAge=24&min24HVol=10000000"
    
    params = parser.parse_url_params(url)
    if parser.make_request(url):
        print("\nHTML content saved successfully")
    else:
        print("\nFailed to save HTML content")
    
if __name__ == "__main__":
    main()
