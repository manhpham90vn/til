import express from "express";
import { createClient } from "redis";

const app = express();
const port = 3001;

const client = createClient({ url: "redis://redis:6379" });
const data_client = createClient({ url: "redis://redis:6379" });

client.on("error", (err) => console.log("Redis Client Error", err)).connect();
data_client
  .on("error", (err) => console.log("Redis Client Error", err))
  .connect();

client.on("connect", () => {
  console.log("Connected to Redis");
  app.listen(port, () => {
    console.log(`Example app listening on port ${port}`);
  });
});

app.get("/", async (req, res) => {
  res.send({ messages: "OK" });
});

client.subscribe("channel", async (message) => {
  console.log("Received message", message);
  const messages = await data_client.get("messages");
  let data;
  if (messages) {
    data = JSON.parse(messages);
    data = [...data, message];
  } else {
    data = [message];
  }
  data_client.set("messages", JSON.stringify(data));
});

app.get("/sub", async (req, res) => {
  const messages = (await data_client.get("messages")) || [];
  const data = JSON.parse(messages);
  res.send({ data });
});
