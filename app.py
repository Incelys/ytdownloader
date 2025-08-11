from flask import Flask, render_template, request, jsonify
import yt_dlp

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_video_info', methods=['POST'])
def get_video_info():
    url = request.json.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400

    ydl_opts = {'quiet': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            formats = []
            for f in info['formats']:
                formats.append({
                    'format_id': f['format_id'],
                    'ext': f['ext'],
                    'resolution': f.get('resolution', 'audio only'),
                    'filesize': f.get('filesize', 0),
                    'acodec': f.get('acodec'),
                    'vcodec': f.get('vcodec')
                })
            return jsonify({'title': info['title'], 'formats': formats})
        except yt_dlp.utils.DownloadError as e:
            return jsonify({'error': str(e)}), 500

@app.route('/download')
def download():
    url = request.args.get('url')
    format_id = request.args.get('format_id')
    if not url or not format_id:
        return "URL and format_id are required", 400

    ydl_opts = {
        'format': format_id,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            download_url = info['url']
            from flask import redirect
            return redirect(download_url)
        except Exception as e:
            return str(e), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
