let recognition;
let isListening = false;

function startListening() {
  if (!('webkitSpeechRecognition' in window)) {
    alert("Your browser does not support Web Speech API");
    return;
  }

  recognition = new webkitSpeechRecognition();
  recognition.continuous = true;
  recognition.interimResults = true;
  recognition.lang = 'en-US';

  recognition.onstart = () => {
    isListening = true;
    document.getElementById("status").textContent = "Status: Listening...";
  };

  recognition.onresult = (event) => {
    let fullTranscript = '';
    for (let i = event.resultIndex; i < event.results.length; ++i) {
      fullTranscript += event.results[i][0].transcript;
    }

    const lower = fullTranscript.toLowerCase();

    // Handle "stop recording"
    if (lower.includes("stop recording")) {
      fullTranscript = fullTranscript.replace(/stop recording/gi, '');
      stopListening();
    }

    // Handle "save note"
    if (lower.includes("save note")) {
      fullTranscript = fullTranscript.replace(/save note/gi, '');
      document.getElementById("note").value = fullTranscript.trim();

      summarizeNote().then(() => {
        saveNote();
      });
    }

    // Update textarea without command words
    document.getElementById("note").value = fullTranscript.trim();
  };

  recognition.onerror = (event) => {
    console.error("Speech recognition error:", event);
  };

  recognition.onend = () => {
    isListening = false;
    document.getElementById("status").textContent = "Status: Stopped";
  };

  recognition.start();
}

function stopListening() {
  if (recognition && isListening) {
    recognition.stop();
  }
}

function summarizeNote() {
  const note = document.getElementById("note").value;
  if (!note.trim()) {
    alert("Please enter or record a note first.");
    return Promise.reject("Note is empty");
  }

  document.getElementById("status").textContent = "Status: Summarizing...";

  return fetch("/summarize", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ note })
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("summary").textContent = data.summary;
    document.getElementById("status").textContent = "Status: Summary ready ✅";
  })
  .catch(err => {
    console.error(err);
    alert("Error summarizing note.");
  });
}

function saveNote() {
  const note = document.getElementById("note").value.trim();
  const summary = document.getElementById("summary").textContent.trim();

  if (!note || !summary) {
    alert("You need both a note and its summary before saving.");
    return;
  }

  fetch("/save", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ note, summary })
  })
  .then(res => res.json())
  .then(data => {
    alert(data.message);
    document.getElementById("status").textContent = "Status: Note saved ✅";
  })
  .catch(err => {
    console.error(err);
    alert("Failed to save note.");
  });
}
