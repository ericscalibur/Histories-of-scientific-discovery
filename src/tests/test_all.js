const path = require('path');
const { chromium } = require('playwright');
const plans = require(path.join(__dirname, 'test_plans.json'));
const LESSONS = path.join(__dirname, '..', '..', 'lessons');

(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' }
    ).catch(async () => await chromium.launch());
  let allOK = true;
  for (const [fname, plan] of Object.entries(plans)) {
    // 1500px viewport so margin figures render during the run
    const page = await browser.newPage({ viewport: { width: 1500, height: 1000 } });
    const errors = [];
    page.on('pageerror', e => errors.push(e.message));
    await page.goto('file://' + path.join(LESSONS, fname));
    await page.fill('#playerName', 'Test Student');

    // margin-figure smoke test on the first visible chapter
    const nFigs = await page.locator('.mn-fig img[data-full]').count();
    let figNote = 'figs: ' + nFigs;
    const ch1Fig = page.locator('#ch1 .mn-fig').first();
    if (await ch1Fig.count()) {
      const vis = await ch1Fig.isVisible();
      await ch1Fig.hover();
      await page.waitForTimeout(1100);
      await ch1Fig.hover(); // re-hover in case the page settled
      await page.waitForTimeout(400);
      const scroll = await ch1Fig.locator('.scroll-paper').isVisible();
      const zoom = await ch1Fig.locator('img').evaluate(el => el.style.cursor);
      figNote += vis && scroll && zoom === 'zoom-in' ? ' (ch1 scroll OK)' : ' (CH1 SCROLL FAIL)';
      if (!vis || !scroll || zoom !== 'zoom-in') allOK = false;
      await page.mouse.move(5, 5);
    }

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
      '| JS errors:', errors.length ? errors.join('; ') : 'none', '|', figNote);
    if (!fin || gold !== plan.length || errors.length) allOK = false;
    await page.close();
  }
  console.log(allOK ? 'ALL PASS' : 'FAILURES PRESENT');
  await browser.close();
})();
