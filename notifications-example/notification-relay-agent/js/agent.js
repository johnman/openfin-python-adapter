import { init as proxyInit } from "./notification-proxy.js";

export async function init() {
  await proxyInit();
}
