import { defineConfig } from 'cypress';
import { nxE2EPreset } from '@nrwl/cypress/plugins/cypress-preset';

export default defineConfig({
  projectId: 'j7dkfr',
  e2e: nxE2EPreset(__dirname),
});
