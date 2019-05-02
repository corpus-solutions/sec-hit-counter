# sec-hit-counter

Simple examples of calling home.

## PDF containing injected JavaScript

Shows sample JavaScript alert, recently proofed working in **Google Chrome** Version 73.0.3683.103 (Official Build) (64-bit)

Use the `embed.sh` script, that will create evil PDF by injecting code from `embed.js` to to minimal PDF file examples.

> Please update all git submodules before running `examples/pdf-injector/embed.sh`.
 
Sample JS code for embedding displays an alert and attempts to call back to URL [http://micro.thinx.cloud:5000](http://micro.thinx.cloud:5000) where the sample counter resides.

## Microsoft Word with transparent pixel

Shows sample transparent PNG invisible in [Office Word document](./examples/docx-linked-pixel/Passwords.docx), that attempts to call home to URL [http://micro.thinx.cloud:5000](http://micro.thinx.cloud:5000) where the sample counter resides.

