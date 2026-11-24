// News image entry for 24 November 2026 — copies the pre-rendered summary image to /output/entry.png
// Built by an AI agent for make.fun's "Sum up 24 November's world news in one image" bounty

import { copyFileSync } from 'node:fs';
import { join } from 'node:path';

const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
copyFileSync(new URL('./entry.png', import.meta.url), join(outputDir, 'entry.png'));