# YouTube, Instagram & TikTok Video & Audio Downloader

This is a simple web application that allows you to download videos and audio from YouTube. You can enter a YouTube URL, see a list of available formats and quality options, and download them directly.

## How to Run

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Install the dependencies:**
    Make sure you have Python and pip installed. Then, run the following command in the project's root directory to install the necessary packages:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application:**
    Start the Flask server by running:
    ```bash
    python app.py
    ```

4.  **Access the application:**
    Open your web browser and navigate to the following address:
    ```
    http://localhost:8080
    ```

You can then paste a YouTube URL into the input box and start downloading videos.

## Limitations

### Instagram Downloads
Downloading from Instagram can be unreliable due to their privacy measures. This tool can only download content that is publicly available and does not require a login to view. If a Reel is private or requires you to be logged in to see it, the download will likely fail. This is a known limitation, and there are no plans to add authentication features for security reasons.

### TikTok Downloads
Similar to Instagram, TikTok may block requests from the server's IP address, which can prevent downloads. If you encounter an error with a TikTok URL, it is likely due to this blocking.
