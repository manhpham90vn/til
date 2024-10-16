const express = require("express");
const os = require("os");
require("dotenv").config();

const app = express();
const port = process.env.PORT;

app.get("/", (req, res) => {
  res.json({
    clientIP: req.headers["x-forwarded-for"] || null,
    remoteAddress: req.socket.remoteAddress,
    localAddress: req.socket.localAddress,
    hostname: os.hostname(),
    platform: os.platform(),
    cpus: os.cpus().length,
  });
});

app.listen(port, () => {
  console.log(
    `Example app listening on port ${port}, env: ${process.env.NODE_ENV}`
  );
});
