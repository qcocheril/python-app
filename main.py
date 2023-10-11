from flask import Flask, request
import logging
import requests


app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)



@app.route("/", methods=["GET","POST"])
def hello_world():
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

    button_input = """
    <form method = "GET" action = "/logger">
	<input type="submit"  value="Go to log">
    </form>
    """
    return prefix_google + "Hello World" + button_input

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
    button_input1 = """
    <form method = "POST" action = "/google_request">
	<input type="submit"  value="Google request">
    </form>
    """

    # Boutton pour accéder à GAnalytics
    button_input2 = """
    <form method = "POST" action = "/GAnalytics">
	<input type="submit"  value="Acces Google Analytics">
    </form>
    """

    return log_msg + browser_log + textbox_input + button_input1 + button_input2

@app.route("/google_request", methods = ["GET","POST"])
def google_request():
    req = requests.get("https://www.google.fr/")

    cookies_text = "\n\nCookies:\n"
    cookies = req.cookies.get_dict()
    
    return f"{req.text} {cookies_text} {str(cookies)}"

@app.route("/GAnalytics", methods = ["GET","POST"])
def GAnalytics():
    req2 = requests.get("https://analytics.google.com/analytics/web/#/p407487549/reports/intelligenthome?params=_u..nav%3Dmaui")
    return f"{req2.text}"