var cfg = {};
cfg.clientid = process.env.SE_CLIENT_ID || 'keyboard cat';
cfg.secret = process.env.SE_SECRET || 'monitordog';
console.log(cfg.clientid);
