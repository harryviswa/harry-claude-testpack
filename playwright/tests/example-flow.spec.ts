import { test, expect } from '@playwright/test';
import { ExamplePage } from '../page-objects/example-page';

test('example flow renders and can submit', async ({ page }) => {
  const examplePage = new ExamplePage(page);
  await examplePage.openExample();

  await expect(examplePage.heading).toBeVisible();
  await examplePage.submit();
});
