import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('https://parabank.parasoft.com/parabank/index.htm');
  await page.locator('input[name="username"]').click();
  await page.locator('input[name="username"]').fill('spiderman_123');
  await page.locator('input[name="password"]').click();
  await page.locator('input[name="password"]').fill('Mary_jane123');
  await page.getByRole('button', { name: 'Log In' }).click();
  await page.getByRole('link', { name: 'Transfer Funds' }).click();
  await page.locator('#amount').click();
  await page.locator('#amount').fill('100');
  await page.locator('#fromAccountId').selectOption('23112');
  await page.locator('#toAccountId').selectOption('23223');
  await page.getByRole('button', { name: 'Transfer' }).click();
  await page.getByRole('link', { name: 'Log Out' }).click();
});