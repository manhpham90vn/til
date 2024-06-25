import express from "express";
import { createClient } from "redis";

const app = express();
const port = 3000;

const client = createClient({ url: "redis://redis:6379" });

client.on("error", (err) => console.log("Redis Client Error", err)).connect();

client.on("connect", () => {
  console.log("Connected to Redis");
  app.listen(port, () => {
    console.log(`Example app listening on port ${port}`);
  });
});

app.get("/", async (req, res) => {
  res.send({ messages: "OK" });
});

app.get("/set", async (req, res) => {
  const id = req.query.id;
  client.set("id", id);
  res.send({ result: id });
});

app.get("/mset", async (req, res) => {
  const id = req.query.id;
  const obj = {
    mset: id,
    mset2: id,
  };
  client.mSet(obj);
  res.send({ result: id });
});

app.get("/pub", async (req, res) => {
  const message = req.query.message;
  client.publish("channel", message);
  res.send({ message });
});

app.get("/json", async (req, res) => {
  const obj = {
    name: req.query.name,
    age: req.query.age,
  };
  if (await client.exists("json")) {
    await client.json.del("json");
  }
  client.json.set("json", ".", obj, 'NX');
  const result = await client.json.get("json", ".");
  res.send({ result: result });
});