const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' }
    ).catch(async () => await chromium.launch());
  const page = await browser.newPage({ viewport: { width: 1100, height: 900 } });
  const errors = [];
  page.on('pageerror', e => errors.push('PAGEERROR: ' + e.message));
  page.on('console', m => { if (m.type() === 'error') errors.push('CONSOLE: ' + m.text()); });

  await page.goto('file:///home/claude/out/Tycho_and_Kepler_Interactive_Story.html');
  await page.fill('#playerName', 'Test Student');

  const visible = async id => await page.locator('#' + id).isVisible();

  // initial state: only ch1 visible
  console.log('ch1 visible:', await visible('ch1'));
  console.log('ch2 hidden:', !(await visible('ch2')));
  console.log('cp8 hidden:', !(await visible('cp8')));

  // wrong answer test
  await page.fill('#a1', '99');
  await page.click('#cp1 .check-btn');
  console.log('wrong feedback:', await page.textContent('#f1'));
  console.log('ch2 still hidden:', !(await visible('ch2')));

  const numeric = { 1: '14', 2: '30', 3: '4', 4: '6000', 5: '300', 6: '20', 7: '4', 8: '4', 9: '6', 11: '26', 12: '5', 13: '6', 14: '8', 15: '0.5', 16: '150', 17: '1425' };
  const order = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'MC', 11, 12, 13, 14, 15, 16, 17];
  for (const step of order) {
    if (step === 'MC') {
      // wrong MC first
      await page.click('#mcRow .mc-btn:nth-child(1)');
      console.log('MC wrong feedback:', (await page.textContent('#f10')).slice(0, 40));
      await page.click('#mcRow .mc-btn:nth-child(2)');
      console.log('MC solved:', (await page.textContent('#f10')).slice(0, 20));
    } else {
      await page.fill('#a' + step, numeric[step]);
      await page.click('#cp' + step + ' .check-btn');
      const fb = await page.textContent('#f' + step);
      if (!fb.startsWith('✓')) console.log('FAIL at', step, fb);
    }
    await page.waitForTimeout(120);
  }

  await page.waitForTimeout(600);
  console.log('finale visible:', await visible('finale'));
  console.log('cert name:', await page.textContent('#certName'));
  const planTotal = 17;
  const gold = await page.evaluate(() =>
    [...document.querySelectorAll('#trackStars path')].filter(p => p.getAttribute('fill') === '#e8a90c').length);
  console.log('gold stars lit:', gold, '/', planTotal);

  await page.screenshot({ path: '/home/claude/out/story_top.png' });
  await page.locator('#ch8').scrollIntoViewIfNeeded();
  await page.waitForTimeout(300);
  await page.screenshot({ path: '/home/claude/out/story_ch8.png' });
  await page.locator('#finale').scrollIntoViewIfNeeded();
  await page.waitForTimeout(300);
  await page.screenshot({ path: '/home/claude/out/story_finale.png' });

  console.log('JS errors:', errors.length ? errors : 'none');
  await browser.close();
})();
