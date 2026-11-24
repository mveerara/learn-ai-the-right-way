import asyncio, sys
from playwright.async_api import async_playwright
async def m():
  async with async_playwright() as p:
    b=await p.chromium.launch()
    for n in range(1,6):
      for w in (390,1100):
        pg=await b.new_page(viewport={'width':w,'height':900}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.goto(f'file:///home/claude/c00/out/l{n}/page.html'); await pg.wait_for_timeout(300)
        steps=await pg.eval_on_selector_all('#steps .step','e=>e.length')
        await pg.click('[data-hint="0"]'); hint=await pg.text_content('#steps .hint')
        for k in range(5):
          a=await pg.evaluate('QUIZ[i].a'); await pg.click(f'#opts .opt >> nth={a}'); await pg.click('#nextBtn')
        score=await pg.text_content('#score'); faq=await pg.eval_on_selector_all('#faqList details','e=>e.length')
        qhtml=await pg.evaluate('QUIZ[1].q')
        sw=await pg.evaluate('document.documentElement.scrollWidth')
        if w==390: print(n, 'steps',steps,'faq',faq,'score',score.strip(),'sw',sw,errs, '| hint:',hint[:50])
        else: print(n,'desk sw',sw,errs)
        if n==3 and w==390: await pg.screenshot(path='/home/claude/c00/out/page3_phone.png', full_page=False)
        await pg.close()
    await b.close()
asyncio.run(m())
