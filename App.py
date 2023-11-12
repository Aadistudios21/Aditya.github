from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    social_media_links = {
        'INSTAGRAM': 'https://instagram.com/adi.eth18?igshid=MWRmOGVxcWM5Y3h2cw==',
        'LinkedIn': 'https://www.linkedin.com/in/your-linkedin-profile',
        # Add more social media links as needed
    }

    return render_template('index.html', social_media_links=social_media_links)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

