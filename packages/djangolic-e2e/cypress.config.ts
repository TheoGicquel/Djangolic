import { defineConfig } from 'cypress';
import { nxE2EPreset } from '@nrwl/cypress/plugins/cypress-preset';

export default defineConfig({
  projectId: 'j7dkfr',
  e2e: {
    ...nxE2EPreset(__dirname),
    experimentalRunAllSpecs: true,
    baseUrl: 'http://127.0.0.1:8000',
    retries: 2,
    video: false,
    screenshotOnRunFailure: false,
  },
});
