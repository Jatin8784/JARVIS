$(document).ready(function () {
  $(".text").textillate({
    loop: true,
    sync: true,
    in: {
      effect: "bounceIn",
    },
    out: {
      effect: "bounceOut",
    },
  });

  //   SiriWave configuration
  var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 800,
    height: 200,
    style: "ios9",
    amplitude: 1,
    speed: 0.3,
    autoStart: true,
  });

  //   Siri message animation
  $(".siri-message").textillate({
    loop: true,
    sync: true,
    in: {
      effect: "fadeInUp",
      sync: true,
    },
    out: {
      effect: "fadeOutUp",
      sync: true,
    },
  });

  //   Mic button click event
  $("#MicBtn").click(function (e) {
    eel.playAssistantSound();
    $("#oval").attr("hidden", true);
    $("#SiriWave").attr("hidden", false);
  });
});
