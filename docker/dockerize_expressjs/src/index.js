const express = require("express");
const os = require("os");
require("dotenv").config();

const app = express();
const port = process.env.PORT;
const env = process.env.NODE_ENV;
const nodeVersion = process.version;
const pid = process.pid;

app.get("/", (req, res) => {
  res.json({
    client_ip: req.headers["x-forwarded-for"] || null,
    remote_address: req.socket.remoteAddress,
    local_address: req.socket.localAddress,
    hostname: os.hostname(),
    platform: os.platform(),
    cpus: os.cpus().length,
    env: env,
    port: port,
    node_version: nodeVersion,
    app_version: 2,
    date: new Date(),
    pid: pid,
  });
});

app.listen(port, () => {
  console.log(
    `Example app listening on port ${port}, env: ${env}, pid: ${pid}`
  );
});
