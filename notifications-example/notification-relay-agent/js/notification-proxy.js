export async function init() {
  window.notifications.addEventListener(
    "notification-action",
    async (notificationResponse) => {
      if (
        notificationResponse.result !== undefined &&
        notificationResponse.result.handler === "agent"
      ) {
        let url = notificationResponse.result.url;
        let target = notificationResponse.result.target;
        if (url !== undefined) {
          switch (target) {
            case "openfin":
              await fin.Window.create({
                name: "openfin-agent-notification-url-container-" + Date.now(),
                url
              });
              break;
            case "browser":
            default:
              await fin.System.openUrlWithBrowser(url);
              break;
          }
        }
      }
      await fin.InterApplicationBus.publish(
        "notification-relay/outbox",
        notificationResponse
      );
    }
  );

  await fin.InterApplicationBus.subscribe(
    { uuid: "*" },
    "notification-relay/inbox",
    (notificationToSend) => {
      window.notifications.create(notificationToSend);
    }
  );
}
