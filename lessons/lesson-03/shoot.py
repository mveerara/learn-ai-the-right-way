import asyncio, sys
from playwright.async_api import async_playwright
d=sys.argv[1]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1920,'height':1080})
        await pg.goto(f'file://{d}/deck.html'); await pg.wait_for_timeout(600)
        n=await pg.evaluate('document.querySelectorAll(".slide").length')
        for i in range(1,n+1): await pg.locator(f'#p{i}').screenshot(path=f'{d}/slides/s{i:02d}.png')
        await b.close()
asyncio.run(main())
