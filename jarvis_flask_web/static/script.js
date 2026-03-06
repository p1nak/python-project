function startListening() {
  const recognition = new webkitSpeechRecognition();
  recognition.lang = 'en-US';
  recognition.start();

  // 🧠 Speak "Jarvis activated" when listening starts
  const synth = window.speechSynthesis;
  const activationUtterance = new SpeechSynthesisUtterance("Jarvis activated");
  synth.speak(activationUtterance);

  // Show waveform
  document.getElementById("waveform").style.visibility = "visible";

  recognition.onresult = function(event) {
    const command = event.results[0][0].transcript;
    document.getElementById("userCommand").innerText = "You: " + command;

    fetch("/process", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ command: command })
    })
    .then(response => response.json())
    .then(data => {
      const reply = data.response;
      document.getElementById("jarvisReply").innerText = "Jarvis: " + reply;

      const utter = new SpeechSynthesisUtterance(reply);
      synth.speak(utter);
    })
    .catch(error => {
      console.error("Error:", error);
      document.getElementById("jarvisReply").innerText = "Jarvis: Sorry, something went wrong.";
    });

    // Hide waveform when done
    document.getElementById("waveform").style.visibility = "hidden";
  };

  recognition.onerror = function() {
    document.getElementById("waveform").style.visibility = "hidden";
  }

  recognition.onend = function() {
    document.getElementById("waveform").style.visibility = "hidden";
  }
}
