// Pengecek error JS runtime komposisi via CDP (Remote Debugging).
// Pakai:  node cekjs.mjs <file-komposisi-absolut> <timeline-id> [detik-seek]
import { spawn } from 'child_process';
const file = process.argv[2];
const tlid = process.argv[3];
const seek = parseFloat(process.argv[4] || '20');
if (!file || !tlid) { console.error('pakai: node cekjs.mjs <file.html> <timeline-id> [seek]'); process.exit(2); }
const chrome = spawn(process.env.PREFIX + '/bin/chromium-browser', [
  '--headless', '--no-sandbox', '--disable-gpu', '--remote-debugging-port=9333',
  'about:blank'
]);
const sleep = ms => new Promise(r => setTimeout(r, ms));
await sleep(2500);
const list = await fetch('http://127.0.0.1:9333/json').then(r => r.json());
const target = list.find(t => t.type === 'page');
const ws = new WebSocket(target.webSocketDebuggerUrl);
let id = 0;
const send = (method, params) => new Promise(res => {
  const myId = ++id;
  const h = ev => { const m = JSON.parse(ev.data);
    if (m.id === myId) { ws.removeEventListener('message', h); res(m); } };
  ws.addEventListener('message', h);
  ws.send(JSON.stringify({ id: myId, method, params }));
});
await new Promise(r => ws.addEventListener('open', r));
await send('Runtime.enable', {});
await send('Page.enable', {});
const errs = [];
ws.addEventListener('message', ev => {
  const m = JSON.parse(ev.data);
  if (m.method === 'Runtime.exceptionThrown')
    errs.push(m.params.exceptionDetails.exception?.description || m.params.exceptionDetails.text);
  if (m.method === 'Runtime.consoleAPICalled' && m.params.type === 'error')
    errs.push('console: ' + m.params.args.map(a => a.value || a.description).join(' '));
});
await send('Page.navigate', { url: 'file://' + file });
await sleep(4000);
const r = await send('Runtime.evaluate', { expression: `(() => {
  const tl = (window.__timelines||{})[${JSON.stringify(tlid)}];
  if (!tl) return 'TIMELINE TIDAK ADA';
  tl.seek(${seek});
  const w = document.getElementById('world');
  return 'dur=' + tl.duration().toFixed(3) + ' world=' + (w ? w.style.transform : '?');
})()`, returnByValue: true });
console.log('hasil:', JSON.stringify(r.result?.result?.value));
console.log('error:', errs.length ? errs.join('\n---\n') : '(tidak ada)');
chrome.kill();
process.exit(0);
