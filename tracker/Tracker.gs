/**
 * Learn AI the Right Way: learner and revenue tracker.
 *
 * Fills the tabs of this spreadsheet from three places:
 *   1. Registrations: the Google Form responses tab linked to this spreadsheet.
 *   2. Payments: Razorpay (read only), using API keys kept in Script Properties, never in a cell.
 *   3. YouTube: views, watch time, subscribers, videos, search terms and traffic sources.
 *
 * Setup steps are on the README tab. Menu: Tracker.
 */

const TABS = {
  dash: 'Dashboard', learners: 'Learners', payments: 'Payments', deliveries: 'Deliveries',
  ytDaily: 'YouTube daily', ytVideos: 'Videos', search: 'Search terms', traffic: 'Traffic sources', setup: 'Setup'
};

// Entrance quiz areas, in the order the quiz reports them. Must match the Learners tab headers L to S.
const AREA_NAMES = ['Linux', 'Permissions', 'Install', 'SSH', 'Git', 'Cloud', 'GPU', 'Python'];
const LEARNER_COLS = 11 + AREA_NAMES.length + 2; // A..U, written by the script; V onwards are formulas

function onOpen() {
  SpreadsheetApp.getUi().createMenu('Tracker')
    .addItem('Sync everything now', 'syncAll')
    .addSeparator()
    .addItem('Sync registrations', 'syncLearners')
    .addItem('Sync Razorpay payments', 'syncPayments')
    .addItem('Sync YouTube statistics', 'syncYouTube')
    .addSeparator()
    .addItem('Set Razorpay keys', 'setRazorpayKeys')
    .addItem('Turn on daily sync', 'installDailyTrigger')
    .addToUi();
}

function ss_() { return SpreadsheetApp.getActiveSpreadsheet(); }

function sheet_(name) {
  const sh = ss_().getSheetByName(name);
  if (!sh) throw new Error('Tab "' + name + '" is missing.');
  return sh;
}

/** Reads a value from the Setup tab by its label in column A. */
function setting_(label) {
  const rows = sheet_(TABS.setup).getRange('A2:B20').getValues();
  for (const [k, v] of rows) { if (String(k).trim() === label) return v; }
  throw new Error('Setting "' + label + '" not found on the Setup tab.');
}

/** Replaces the data rows (from row 2) of the first `ncols` columns of a tab. */
function writeRows_(name, rows, ncols) {
  const sh = sheet_(name);
  const last = sh.getLastRow();
  if (last > 1) sh.getRange(2, 1, last - 1, ncols).clearContent();
  if (rows.length) sh.getRange(2, 1, rows.length, ncols).setValues(rows);
  return rows.length;
}

/** Runs every sync, records the time and any problems on the Dashboard. */
function syncAll() {
  const msgs = [];
  const steps = [['Registrations', syncLearners], ['Razorpay', syncPayments], ['YouTube', syncYouTube]];
  for (const [label, fn] of steps) {
    try { msgs.push(label + ': ' + fn() + ' rows'); }
    catch (e) { msgs.push(label + ' FAILED: ' + e.message); }
  }
  const dash = sheet_(TABS.dash);
  dash.getRange('B2').setValue(new Date());
  dash.getRange('B3').setValue(msgs.join(' | '));
}

/* ---------- 1. Registrations ---------- */

function syncLearners() {
  const tabName = String(setting_('Form responses tab')).trim();
  const src = ss_().getSheetByName(tabName);
  if (!src) throw new Error('No tab called "' + tabName + '". Link the registration form to this spreadsheet (README, step 2).');
  const data = src.getDataRange().getValues();
  if (data.length < 2) return writeRows_(TABS.learners, [], LEARNER_COLS);
  const head = data[0].map(h => String(h).toLowerCase());
  const col = (...keys) => head.findIndex(h => keys.some(k => h.indexOf(k) >= 0));
  const c = {
    ts: col('timestamp'), name: col('name'), email: col('email'),
    phone: col('phone', 'whatsapp', 'mobile', 'contact number'), place: col('country', 'city', 'location'),
    student: col('student'), result: col('entrance'), heard: col('hear', 'source', 'referr')
  };
  const rows = data.slice(1).filter(r => r.some(x => x !== '')).map((r, i) => {
    const g = k => (c[k] >= 0 ? r[c[k]] : '');
    const res = String(g('result'));
    const m = res.match(/(\d+)\s*\/\s*(\d+)/);
    const placement = /PASSED/i.test(res) ? 'PASSED' : (/NOT YET/i.test(res) ? 'NOT YET' : '');
    const modules = (res.split('Course 0:')[1] || '').trim();
    // Per-area scores, e.g. "Areas: Linux 2/3, Git 0/3, ..." -> one fraction per area, plus weak and strong lists.
    const areaPart = (res.match(/Areas:\s*([^·]*)/) || [])[1] || '';
    const scores = {};
    areaPart.split(',').forEach(s => { const mm = s.trim().match(/^(.+?)\s+(\d+)\/(\d+)$/); if (mm) scores[mm[1]] = Number(mm[2]) / Number(mm[3]); });
    const areaCells = AREA_NAMES.map(a => (a in scores ? scores[a] : ''));
    const weak = AREA_NAMES.filter(a => a in scores && scores[a] < 0.5).join(', ');
    const strong = AREA_NAMES.filter(a => a in scores && scores[a] === 1).join(', ');
    const phone = String(g('phone')).trim();
    return [
      'L' + String(i + 1).padStart(4, '0'), g('ts'), g('name'), String(g('email')).trim().toLowerCase(),
      phone ? "'" + phone : '', g('place'), g('student'), m ? Number(m[1]) / Number(m[2]) : '',
      placement, modules, g('heard')
    ].concat(areaCells, [weak, strong]);
  });
  return writeRows_(TABS.learners, rows, LEARNER_COLS);
}

/* ---------- 2. Razorpay payments (read only) ---------- */

function setRazorpayKeys() {
  const ui = SpreadsheetApp.getUi();
  const a = ui.prompt('Razorpay Key ID', 'Razorpay Dashboard > Account & Settings > API Keys. Paste the Key ID:', ui.ButtonSet.OK_CANCEL);
  if (a.getSelectedButton() !== ui.Button.OK) return;
  const b = ui.prompt('Razorpay Key Secret', 'Paste the Key Secret. It is stored in this script\'s private settings, not in any cell.', ui.ButtonSet.OK_CANCEL);
  if (b.getSelectedButton() !== ui.Button.OK) return;
  PropertiesService.getScriptProperties().setProperties({
    RAZORPAY_KEY_ID: a.getResponseText().trim(), RAZORPAY_KEY_SECRET: b.getResponseText().trim()
  });
  ui.alert('Saved. Run Tracker > Sync Razorpay payments to test.');
}

function syncPayments() {
  const props = PropertiesService.getScriptProperties();
  const id = props.getProperty('RAZORPAY_KEY_ID'), secret = props.getProperty('RAZORPAY_KEY_SECRET');
  if (!id || !secret) throw new Error('Razorpay keys not set. Use Tracker > Set Razorpay keys.');
  const from = Math.floor(new Date(setting_('Track payments from')).getTime() / 1000);
  const auth = 'Basic ' + Utilities.base64Encode(id + ':' + secret);
  let all = [], skip = 0;
  while (true) {
    const url = 'https://api.razorpay.com/v1/payments?count=100&skip=' + skip + '&from=' + from;
    const res = UrlFetchApp.fetch(url, { headers: { Authorization: auth }, muteHttpExceptions: true });
    if (res.getResponseCode() !== 200) throw new Error('Razorpay answered ' + res.getResponseCode() + ': ' + res.getContentText().slice(0, 200));
    const items = JSON.parse(res.getContentText()).items || [];
    all = all.concat(items);
    if (items.length < 100) break;
    skip += 100;
  }
  all.sort((x, y) => x.created_at - y.created_at);
  const product = p => {
    const n = p.notes;
    if (n && !Array.isArray(n)) return n.product || n.Product || Object.values(n).join('; ') || p.description || '';
    return p.description || '';
  };
  const rupees = v => (v ? v / 100 : 0);
  const rows = all.map(p => [
    p.id, new Date(p.created_at * 1000), rupees(p.amount), p.currency, p.method || '', p.status,
    p.captured ? 'Yes' : 'No', String(p.email || '').toLowerCase(), p.contact ? "'" + p.contact : '',
    product(p), p.order_id || '', rupees(p.fee), rupees(p.tax), rupees(p.amount_refunded),
    p.refund_status || '', p.description || ''
  ]);
  writeRows_(TABS.payments, rows, 16);

  // Every captured payment gets a delivery row once, so nothing paid for goes undelivered.
  const del = sheet_(TABS.deliveries);
  const lastDel = del.getLastRow();
  const have = new Set(lastDel > 1 ? del.getRange(2, 5, lastDel - 1, 1).getValues().flat().filter(String) : []);
  const add = all.filter(p => p.status === 'captured' && !have.has(p.id))
    .map(p => [new Date(p.created_at * 1000), String(p.email || '').toLowerCase(), product(p), 'Paid', p.id, '', 'Pending']);
  if (add.length) del.getRange(Math.max(lastDel, 1) + 1, 1, add.length, 7).setValues(add);
  return rows.length;
}

/* ---------- 3. YouTube (needs the YouTube and YouTube Analytics services, README step 4) ---------- */

function syncYouTube() {
  const tz = 'UTC';
  const start = Utilities.formatDate(new Date(setting_('Launch date')), tz, 'yyyy-MM-dd');
  const end = Utilities.formatDate(new Date(), tz, 'yyyy-MM-dd');
  const q = o => YouTubeAnalytics.Reports.query(Object.assign({ ids: 'channel==MINE', startDate: start, endDate: end }, o));

  const daily = q({ metrics: 'views,estimatedMinutesWatched,subscribersGained,subscribersLost,likes', dimensions: 'day', sort: 'day' });
  const n = writeRows_(TABS.ytDaily, (daily.rows || []).map(r => [r[0], r[1], r[2], r[3], r[4], r[5]]), 6);

  const vids = q({ metrics: 'views,estimatedMinutesWatched,averageViewDuration,likes,subscribersGained', dimensions: 'video', sort: '-views', maxResults: 50 });
  const vrows = vids.rows || [];
  const titles = {};
  if (vrows.length) {
    const res = YouTube.Videos.list('snippet', { id: vrows.map(r => r[0]).join(',') });
    (res.items || []).forEach(v => { titles[v.id] = v.snippet.title; });
  }
  writeRows_(TABS.ytVideos, vrows.map(r => [r[0], titles[r[0]] || '', r[1], r[2], r[3], r[4], r[5]]), 7);

  const search = q({ metrics: 'views,estimatedMinutesWatched', dimensions: 'insightTrafficSourceDetail', filters: 'insightTrafficSourceType==YT_SEARCH', sort: '-views', maxResults: 25 });
  writeRows_(TABS.search, (search.rows || []).map(r => [r[0], r[1], r[2]]), 3);

  const traffic = q({ metrics: 'views,estimatedMinutesWatched', dimensions: 'insightTrafficSourceType', sort: '-views' });
  writeRows_(TABS.traffic, (traffic.rows || []).map(r => [r[0], r[1], r[2]]), 3);
  return n;
}

/* ---------- Daily schedule ---------- */

function installDailyTrigger() {
  ScriptApp.getProjectTriggers().filter(t => t.getHandlerFunction() === 'syncAll').forEach(t => ScriptApp.deleteTrigger(t));
  ScriptApp.newTrigger('syncAll').timeBased().everyDays(1).atHour(6).create();
  SpreadsheetApp.getUi().alert('Daily sync is on. It runs every morning around 6 am.');
}
