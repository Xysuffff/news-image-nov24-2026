// Entry for make.fun's "news-image-20261124" bounty: one image that sums up
// the world news of Tuesday, 24 November 2026.
//
// The image itself lives in the repository as entry.png, drawn offline by
// render_entry.py from reporting published that day (Reuters, AP, BBC, FT,
// UN News). This program validates that PNG and places it where the grader
// reads it.
//
// Standard library only, no network, deterministic: both grader runs copy
// the same bytes out of the repository.

import { copyFileSync, mkdirSync, readFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const repoDir = dirname(fileURLToPath(import.meta.url));
const source = join(repoDir, 'entry.png');
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

// The PNG signature: 89 50 4E 47 0D 0A 1A 0A.
const PNG_SIGNATURE = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);

const MAX_BYTES = 1024 * 1024;
const MAX_SIDE = 1024;

const image = readFileSync(source);
if (!image.subarray(0, PNG_SIGNATURE.length).equals(PNG_SIGNATURE)) {
  throw new Error('entry.png is not a PNG file');
}
if (image.length > MAX_BYTES) {
  throw new Error(`entry.png is ${image.length} bytes, over the ${MAX_BYTES} byte limit`);
}

// The IHDR chunk starts at byte 8: length (4), type "IHDR" (4), then width
// and height as two big-endian 32-bit integers.
const width = image.readUInt32BE(16);
const height = image.readUInt32BE(20);
if (width > MAX_SIDE || height > MAX_SIDE) {
  throw new Error(`entry.png is ${width}x${height}, over the ${MAX_SIDE}px limit`);
}

mkdirSync(outputDir, { recursive: true });
copyFileSync(source, join(outputDir, 'entry.png'));
