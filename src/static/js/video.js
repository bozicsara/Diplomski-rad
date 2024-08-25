export function create_call() {
  let callFrame = window.DailyIframe.createFrame({
    showLeaveButton: true,
    iframeStyle: {
      position: "fixed",
      background: "#fff",
      top: "7vh",
      left: "0",
      width: "100%",
      height: "93vh",
    },
  });
  callFrame.join({ url: "https://moja-apoteka.daily.co/apoteka" });
}
