#!/usr/bin/env node

/**
 * Generate admin/config.yml from admin/config.template.yml
 * Replaces ${VAR_NAME} placeholders with environment variables.
 * If admin/config.template.yml doesn't exist, exits silently.
 */

import fs from 'fs';
import path from 'path';

const ROOT     = process.cwd();
const template = path.join(ROOT, 'admin', 'config.template.yml');
const output   = path.join(ROOT, 'admin', 'config.yml');

if (!fs.existsSync(template)) {
  // No CMS template — skip silently
  process.exit(0);
}

let content = fs.readFileSync(template, 'utf-8');

// Replace ${VAR_NAME} with environment variable values
content = content.replace(/\$\{([A-Z_]+)\}/g, (match, varName) => {
  return process.env[varName] || match;
});

fs.writeFileSync(output, content);
console.log('  Generated admin/config.yml');
