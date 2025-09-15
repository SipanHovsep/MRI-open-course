Low-cost/modular Magnetic Field Mapping Robot

.. raw:: html

   <div class="readme-wrapper">
     <div id="readme-field-mapper" class="readme-box">Loading README…</div>
     <div class="readme-footer">
       <a href="https://github.com/SipanHovsep/Field_mapper_robot" target="_blank" rel="noopener">
         View on GitHub ↗
       </a>
     </div>
   </div>

   <!-- Markdown renderer -->
   <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>

   <script>
   (async function() {
     const box = document.getElementById('readme-field-mapper');
     try {
       const resp = await fetch('https://raw.githubusercontent.com/SipanHovsep/Field_mapper_robot/main/README.md', {cache: 'no-store'});
       const md = await resp.text();
       box.innerHTML = marked.parse(md);

       // Make images responsive and fix relative URLs
       const imgBase = 'https://raw.githubusercontent.com/SipanHovsep/Field_mapper_robot/main/';
       const linkBase = 'https://github.com/SipanHovsep/Field_mapper_robot/blob/main/';

       box.querySelectorAll('img').forEach(img => {
         const src = img.getAttribute('src') || '';
         if (!/^https?:\/\//i.test(src)) img.src = new URL(src, imgBase).href;
         img.style.maxWidth = '100%';
         img.style.height = 'auto';
       });

       box.querySelectorAll('a').forEach(a => {
         const href = a.getAttribute('href') || '';
         if (href && !/^https?:\/\//i.test(href)) a.href = new URL(href, linkBase).href;
         a.target = '_blank';
         a.rel = 'noopener';
       });
     } catch (e) {
       box.textContent = 'Could not load README.';
     }
   })();
   </script>

   <style>
     .readme-box {
       max-height: 520px;
       overflow: auto;
       padding: 1rem 1.25rem;
       border: 1px solid #e5e7eb;
       border-radius: 12px;
       background: #fff;
       box-shadow: 0 1px 2px rgba(0,0,0,0.04);
     }
     .readme-footer {
       margin-top: 0.5rem;
       text-align: right;
     }
     .readme-footer a {
       text-decoration: none;
       font-weight: 600;
     }
   </style>
Low-cost/modular Magnetic Field Mapping Robot

.. raw:: html

   <div class="readme-wrapper">
     <div id="readme-field-mapper" class="readme-box">Loading README…</div>
     <div class="readme-footer">
       <a href="https://github.com/SipanHovsep/Field_mapper_robot" target="_blank" rel="noopener">
         View on GitHub ↗
       </a>
     </div>
   </div>

   <!-- Markdown renderer -->
   <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>

   <script>
   (async function() {
     const box = document.getElementById('readme-field-mapper');
     try {
       const resp = await fetch('https://raw.githubusercontent.com/SipanHovsep/Field_mapper_robot/main/README.md', {cache: 'no-store'});
       const md = await resp.text();
       box.innerHTML = marked.parse(md);

       // Make images responsive and fix relative URLs
       const imgBase = 'https://raw.githubusercontent.com/SipanHovsep/Field_mapper_robot/main/';
       const linkBase = 'https://github.com/SipanHovsep/Field_mapper_robot/blob/main/';

       box.querySelectorAll('img').forEach(img => {
         const src = img.getAttribute('src') || '';
         if (!/^https?:\/\//i.test(src)) img.src = new URL(src, imgBase).href;
         img.style.maxWidth = '100%';
         img.style.height = 'auto';
       });

       box.querySelectorAll('a').forEach(a => {
         const href = a.getAttribute('href') || '';
         if (href && !/^https?:\/\//i.test(href)) a.href = new URL(href, linkBase).href;
         a.target = '_blank';
         a.rel = 'noopener';
       });
     } catch (e) {
       box.textContent = 'Could not load README.';
     }
   })();
   </script>

   <style>
     .readme-box {
       max-height: 520px;
       overflow: auto;
       padding: 1rem 1.25rem;
       border: 1px solid #e5e7eb;
       border-radius: 12px;
       background: #fff;
       box-shadow: 0 1px 2px rgba(0,0,0,0.04);
     }
     .readme-footer {
       margin-top: 0.5rem;
       text-align: right;
     }
     .readme-footer a {
       text-decoration: none;
       font-weight: 600;
     }
   </style>
