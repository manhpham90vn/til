const express = require('express')
const os = require('os')
if (process.env.NODE_ENV !== 'production') {
  require('dotenv').config()
}

const app = express()
const port = process.env.PORT || 3000

app.get('/', (req, res) => {
  res.json({
    clientIP: req.headers['x-forwarded-for'] || null,
    remoteAddress: req.socket.remoteAddress,
    localAddress: req.socket.localAddress,
    hostname: os.hostname(),
    platform: os.platform(),
    cpus: os.cpus().length
  })
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})