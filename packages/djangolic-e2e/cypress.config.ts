import { defineConfig } from 'cypress';
import { nxE2EPreset } from '@nrwl/cypress/plugins/cypress-preset';

export default defineConfig({
  e2e: {
    ...nxE2EPreset(__dirname),
    experimentalRunAllSpecs: true,
    baseUrl: 'http://127.0.0.1:8000',
    defaultCommandTimeout: 10000,// prob overkill but github actions is slow
    retries: 2,
    video: false,
    screenshotOnRunFailure: false,
  },
});
