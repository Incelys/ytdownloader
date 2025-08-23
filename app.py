from flask import Flask, render_template, request, jsonify
import yt_dlp

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_video_info', methods=['POST'])
def get_video_info():
    try:
        url = request.json.get('url')
        if not url:
            return jsonify({'error': 'URL is required'}), 400

        ydl_opts = {'quiet': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
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
    except Exception as e:
        error_message = str(e)
        if 'instagram' in error_message.lower():
            return jsonify({'error': 'This Instagram Reel may be private or require a login to view. This downloader can only access public content.'}), 400
        if 'tiktok' in error_message.lower() and 'ip address is blocked' in error_message.lower():
            return jsonify({'error': 'TikTok is blocking requests from this server. Please try again later.'}), 400
        return jsonify({'error': error_message}), 500

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
    from waitress import serve
    serve(app, host='0.0.0.0', port=8080)
