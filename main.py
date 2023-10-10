from flask import Flask, request
import logging
import requests

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

prefix_google = """
 <!-- Google tag (gtag.js) -->
<script async
src="https://www.googletagmanager.com/gtag/js?id=G-GV4KJPM75M"></script>
<script>
 window.dataLayer = window.dataLayer || [];
 function gtag(){dataLayer.push(arguments);}
 gtag('js', new Date());
 gtag('config', 'G-GV4KJPM75M');
</script>
 """

@app.route("/")
def hello_world():
    return prefix_google + "Hello World"

@app.route("/logger", methods=['GET', 'POST'])
def log():
    # Print a message in Python
    log_msg = "Logger route accessed"
    app.logger.info(log_msg)

    if request.method == 'POST':
        # Retreiived the text in the text box
        text_from_textbox = request.form['textbox']

        # Print a message in the browser console with the text from the text box
        browser_log = f"""
        <script>
            console.log('This is a log message');
            console.log('Text submission : {text_from_textbox}');
        </script>
        """
    else:
        # Print a message in the browser console
        browser_log = """
        <script>
            console.log('This is a log message');
        </script>
        """

    # Formulaire HTML avec une boîte de texte
    textbox_input = """
    <form method="POST">
        <label for="textbox">Text Box :</label><br>
        <input type="text" id="textbox" name="textbox"><br><br>
        <input type="submit" value="Submit text">
    </form>
    """

    # Boutton pour faire une google request 
    button_input = """
    <form method = "POST" action = "/google_request">
	<input type="submit"  value="Google request">
    </form>
    """

    return log_msg + browser_log + textbox_input + button_input

@app.route("/google_request", methods = ["POST"])
def google_request():
    req = requests.get("https://www.google.com/")
    return f"Response from google : {req.text}"
