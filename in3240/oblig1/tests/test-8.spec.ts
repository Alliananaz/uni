import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('https://parabank.parasoft.com/parabank/index.htm');
  await page.getByRole('link', { name: 'contact', exact: true }).click();
  await page.locator('#name').click();
  await page.locator('#name').fill('Peter Parker');
  await page.locator('#email').click();
  await page.locator('#email').fill('peter_parker@gmail.com');
  await page.locator('#phone').click();
  await page.locator('#phone').fill('1234567890');
  await page.locator('#message').click();
  await page.locator('#message').fill('I am not able to log in with my account. ');
  await page.getByRole('button', { name: 'Send to Customer Care' }).click();
});