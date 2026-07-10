import { Locator, Page } from '@playwright/test';
import { BasePage } from './base-page';

export class ExamplePage extends BasePage {
  readonly heading: Locator;
  readonly button: Locator;

  constructor(page: Page) {
    super(page);
    this.heading = page.getByRole('heading');
    this.button = page.getByRole('button', { name: /submit/i });
  }

  async openExample() {
    await this.open('/');
    await this.waitForLoaded();
  }

  async submit() {
    await this.click(this.button);
  }
}
