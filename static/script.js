document.getElementById('url-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    const url = document.getElementById('youtube-url').value;
    const videoInfoContainer = document.getElementById('video-info');
    const loading = document.getElementById('loading');
    const errorContainer = document.getElementById('error');
    const errorMessage = document.getElementById('error-message');

    videoInfoContainer.classList.add('hidden');
    errorContainer.classList.add('hidden');
    loading.classList.remove('hidden');

    try {
        const response = await fetch('/get_video_info', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ url: url })
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || 'Something went wrong');
        }

        const data = await response.json();
        document.getElementById('video-title').textContent = data.title;
        const formatsContainer = document.getElementById('formats-container');
        formatsContainer.innerHTML = '';

        data.formats.forEach(format => {
            const formatElement = document.createElement('div');
            formatElement.classList.add('format-item');

            let formatDescription = `${format.ext} - ${format.resolution}`;
            if (format.filesize) {
                formatDescription += ` (${(format.filesize / 1024 / 1024).toFixed(2)} MB)`;
            }

            formatElement.innerHTML = `<span>${formatDescription}</span>`;
            formatsContainer.appendChild(formatElement);
        });

        videoInfoContainer.classList.remove('hidden');
    } catch (error) {
        errorMessage.textContent = error.message;
        errorContainer.classList.remove('hidden');
    } finally {
        loading.classList.add('hidden');
    }
});
