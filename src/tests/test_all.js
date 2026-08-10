const { chromium } = require('playwright');
const plans = require('/home/claude/test_plans.json');

(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' }
    ).catch(async () => await chromium.launch());
  let allOK = true;
  for (const [fname, plan] of Object.entries(plans)) {
    const page = await browser.newPage({ viewport: { width: 1100, height: 1000 } });
    const errors = [];
    page.on('pageerror', e => errors.push(e.message));
    await page.goto('file:///home/claude/out/' + fname);
    await page.fill('#playerName', 'Test Student');
    for (const cp of plan) {
      const vis = await page.locator('#cp' + cp.n).isVisible();
      if (!vis) { console.log(fname, 'FAIL: cp' + cp.n + ' not visible when its turn came'); allOK = false; break; }
      if (cp.type === 'num') {
        // wrong answer first for cp1 only
        if (cp.n === 1) {
          await page.fill('#a1', '999999');
          await page.click('#cp1 .check-btn');
          const fb = await page.textContent('#f1');
          if (!fb.includes('✗')) { console.log(fname, 'FAIL: wrong-answer feedback'); allOK = false; }
        }
        await page.fill('#a' + cp.n, cp.val);
        await page.click('#cp' + cp.n + ' .check-btn');
        const fb = await page.textContent('#f' + cp.n);
        if (!fb.startsWith('✓')) { console.log(fname, 'FAIL at cp' + cp.n + ':', fb); allOK = false; }
      } else {
        const btns = page.locator('#cp' + cp.n + ' .mc-btn');
        await btns.nth(cp.idx).click();
        const fb = await page.textContent('#f' + cp.n);
        if (!fb.startsWith('✓')) { console.log(fname, 'FAIL at MC cp' + cp.n + ':', fb); allOK = false; }
      }
      await page.waitForTimeout(80);
    }
    await page.waitForTimeout(500);
    const fin = await page.locator('#finale').isVisible();
    const cert = await page.textContent('#certName');
    const gold = await page.evaluate(() =>
      [...document.querySelectorAll('#trackStars path')].filter(p => p.getAttribute('fill') === '#e8a90c').length);
    console.log(fname, '| finale:', fin, '| cert:', cert, '| stars:', gold + '/' + plan.length,
      '| JS errors:', errors.length ? errors.join('; ') : 'none');
    if (!fin || gold !== plan.length || errors.length) allOK = false;
    await page.close();
  }
  console.log(allOK ? 'ALL PASS' : 'FAILURES PRESENT');
  await browser.close();
})();
