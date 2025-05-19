let isRecording = false;
let mediaRecorder = null;
let audioChunks = [];

document.getElementById('recordButton').addEventListener('click', async () => {
    const recordButton = document.getElementById('recordButton');
    const transcriptionArea = document.getElementById('transcription');

    if (!isRecording) {
        try {
            // Request microphone access
            const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
            mediaRecorder = new MediaRecorder(stream);
            audioChunks = [];

            mediaRecorder.ondataavailable = (event) => {
                console.log('Audio data received:', event.data); // Debug log
                audioChunks.push(event.data);
            };

            mediaRecorder.onstop = async () => {
                console.log('Audio chunks:', audioChunks); // Debug log
                const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
                console.log('Audio blob size:', audioBlob.size); // Debug log
                const formData = new FormData();
                formData.append('audio', audioBlob, 'recording.wav');

                // Send audio to server
                const response = await fetch('/transcribe', {
                    method: 'POST',
                    body: formData
                });
                const result = await response.json();

                if (result.text) {
                    transcriptionArea.value = result.text;
                } else {
                    transcriptionArea.value = 'Error: ' + result.error;
                }
            };

            mediaRecorder.start();
            recordButton.textContent = 'Stop Recording';
            isRecording = true;
        } catch (err) {
            transcriptionArea.value = 'Error accessing microphone: ' + err.message;
            console.error('Microphone error:', err); // Debug log
        }
    } else {
        mediaRecorder.stop();
        recordButton.textContent = 'Start Recording';
        isRecording = false;
    }
});