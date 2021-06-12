from flask import Flask, render_template, redirect, send_from_directory, send_file

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/download')
def download():
    return send_file('./app.apk')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 187, debug= True)

