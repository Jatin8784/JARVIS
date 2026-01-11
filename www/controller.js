$(document).ready(function () {
  // Display Speak Message
  eel.expose(DisplayMessage);
  function DisplayMessage(message) {
    const el = $(".siri-message");

    el.textillate("stop");
    el.find(".texts li").text(message);
    el.textillate("start");
  }

  // Display hood
  eel.expose(ShowHood);
  function ShowHood() {
    $("#oval").attr("hidden", false);
    $("#SiriWave").attr("hidden", true);
  }
});
