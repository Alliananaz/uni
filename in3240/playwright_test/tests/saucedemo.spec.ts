import { test, expect } from '@playwright/test';

test.beforeEach(async ({page}) => {
    await page.goto('https://www.saucedemo.com');
    await expect(page).toHaveURL('https://www.saucedemo.com');
    await page.getByPlaceholder('Username').fill('standard_user');
    await page.getByTestId('password').fill('secret_sauce');
    await page.locator('#login-button').click(); 

    await expect(page).toHaveURL('https://www.saucedemo.com/inventory.html');
})


test('saucedemo logg inn og mer', async ({ page }) => {
    await page.locator('[name="add-to-cart-sauce-labs-backpack"]').click();
    await page.getByTestId('remove-sauce-labs-backpack').click();
    await expect(page.locator('[name="add-to-cart-sauce-labs-backpack"]')).toBeVisible()
})

// test fra test-1.spec.ts