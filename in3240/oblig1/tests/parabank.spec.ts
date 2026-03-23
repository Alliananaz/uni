import { test, expect } from '@playwright/test';

test.describe("tests for parabank", () => {
    // TC000
    test("submit customer care contact", async ({ page }) => {
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


    test.beforeEach(async ({page}) => {
        await page.goto('https://parabank.parasoft.com/parabank/index.htm');
        await expect(page).toHaveURL('https://parabank.parasoft.com/parabank/index.htm');
        await page.locator('input[name="username"]').fill('spiderman_123');
        await page.locator('input[name="password"]').fill('Mary_jane123');
        await page.locator('input[value="Log In"]').click();

        await expect(page).toHaveURL('https://parabank.parasoft.com/parabank/overview.htm');
    });

    // TC001
    test("transfer funds between accounts", async ({ page }) => {
        await page.getByRole('link', { name: 'Transfer Funds' }).click();
        await page.locator('#amount').click();
        await page.locator('#amount').fill('100');
        await page.locator('#fromAccountId').selectOption('23112');
        await page.locator('#toAccountId').selectOption('23223');
        await page.getByRole('button', { name: 'Transfer' }).click();
        await page.getByRole('link', { name: 'Log Out' }).click();
    })

    // TC002
    test("bill pay function", async ({ page }) => {
        await page.getByRole('link', { name: 'Bill Pay' }).click();
        await page.locator('input[name="payee.name"]').click();
        await page.locator('input[name="payee.name"]').fill('Albert Pettersen');
        await page.locator('input[name="payee.address.street"]').click();
        await page.locator('input[name="payee.address.street"]').fill('212 Baddie Street');
        await page.locator('input[name="payee.address.city"]').click();
        await page.locator('input[name="payee.address.city"]').fill('New York City');
        await page.locator('input[name="payee.address.state"]').click();
        await page.locator('input[name="payee.address.state"]').fill('New York');
        await page.locator('input[name="payee.address.zipCode"]').click();
        await page.locator('input[name="payee.address.zipCode"]').fill('12345');
        await page.locator('input[name="payee.phoneNumber"]').click();
        await page.locator('input[name="payee.phoneNumber"]').fill('1234567890');
        await page.locator('input[name="payee.accountNumber"]').click();
        await page.locator('input[name="payee.accountNumber"]').fill('67890');
        await page.locator('input[name="verifyAccount"]').click();
        await page.locator('input[name="verifyAccount"]').fill('67890');
        await page.locator('input[name="amount"]').click();
        await page.locator('input[name="amount"]').fill('50');
        await page.getByRole('button', { name: 'Send Payment' }).click();
    })

    // TC003
    test("request a new loan", async ({ page }) => {
        await page.getByRole('link', { name: 'Request Loan' }).click();
        await page.locator('#amount').click();
        await page.locator('#amount').fill('10');
        await page.locator('#downPayment').click();
        await page.locator('#downPayment').fill('5');
        await page.locator('#fromAccountId').selectOption('23112');
        await page.locator('#amount').click();
        await page.getByRole('button', { name: 'Apply Now' }).click();
        await page.locator('body').click();
    });

    test.afterEach(async ({page}) => {
        await page.getByRole('link', { name: 'Log Out' }).click();
    });
        
});






