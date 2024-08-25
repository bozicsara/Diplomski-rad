import { create_call } from "./video.js";

const url = "http://localhost:5000";

const socket = io.connect(url);
const shakeKeyframes = [
  { transform: "translate(-50%, -50%) translateX(0px)" },
  { transform: "translate(-50%, -50%) translateX(-5px)" },
  { transform: "translate(-50%, -50%) translateX(5px)" },
  { transform: "translate(-50%, -50%) translateX(0px)" },
];

const shakeTiming = {
  duration: 500,
  iterations: Infinity,
  easing: "cubic-bezier(.36,.07,.19,.97)",
};
let shakeAnimation;

socket.on("call_received", function (msg) {
  console.log(msg);
  shakeAnimation = phoneButton.animate(shakeKeyframes, shakeTiming);
});
document.getElementById("phoneButton").addEventListener("click", function () {
  this.style.animation = "none";
  shakeAnimation.cancel();
  handshake();
  create_call();
  console.log("handshake");
});

function handshake() {
  const socket = io.connect(url);
  socket.emit("handshake", "handshake");
}
