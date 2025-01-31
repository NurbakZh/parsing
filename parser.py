from urllib.parse import urlparse, parse_qs
from DrissionPage import ChromiumPage, ChromiumOptions
import time

class HeaderParser:
    def __init__(self):
        # Create ChromiumOptions instance
        co = ChromiumOptions().headless()
        co.set_argument('--no-sandbox')
        co.set_argument('--headless=new')

        self.page = ChromiumPage(co)
        
        # Set headers
        self.page.set.headers({
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
            'cookie': 'chakra-ui-color-mode=dark; _ga=GA1.1.1559758038.1738249214; cf_clearance=kAy2d8IrixWlA_efL2nNPVu4MNEVov8.UTuXmZa6q1k-1738322715-1.2.1.1-EN3JvIsVE_U0HH19htCSHQUWJ5Wa1axmNr6D0NdqclBCE29Do7aikTx133VsTQZ8n6WYjqycDyRyq74KqkZD0CJr_ZAjzeUjRIJ3QDoX5mV9Wd17OrWIeYmpmT_yXmgZN3NMdQtp2Y6e5ytjIV_wGfQ.ZOviOPOV5sNGgDXEdrZiuagwNFlHLUnooV7.tcmPh_kQnt3DZwDOVk9VhH5hKr3mRwmZNwR7nRWhU8vOxX8hhJjotlZnCu5drOrzVRAOfVuHl_053lD0QwdHYDWHWhEAk0j_iVvL01dxvy330u.SHoMppBZbCymBTS_LGLtfBt2YHETazPGpzMzdApf11g; _ga_532KFVB4WT=GS1.1.1738321943.3.1.1738322909.29.0.0; __cf_bm=BHbSRMtrO3qsH59ofbGV7MFn92EKAwKUR3VQ0PypuLU-1738332279-1.0.1.1-ugGHUvoWa1Zi_6iqNf.7CQjDxxjIx4aMp_hVmYV.Mwpp27zQSNeJS47Ot.L8XtR5ThjAE1dHhycoOYBEQiERGHEYBUli92B2BVnI5XBqLvM',
            'priority': 'u=0, i',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
            'sec-ch-ua-arch': '"x86"',
            'sec-ch-ua-bitness': '"64"',
            'sec-ch-ua-full-version': '"132.0.6834.160"',
            'sec-ch-ua-full-version-list': '"Not A(Brand";v="8.0.0.0", "Chromium";v="132.0.6834.160", "Google Chrome";v="132.0.6834.160"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1'
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
