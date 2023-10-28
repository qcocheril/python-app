from flask import Flask, request, render_template, jsonify
import requests
import logging
import time
from pytrends.request import TrendReq




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
    req2 = requests.get("https://analytics.google.com/analytics/web/#/p407487549/reports/intelligenthome")
    return f"{req2.text}"

# @app.route('/GAnalytics_cookie', methods=['GET'])
# def check_analytics_request_cookies():
#    try:
#        response = requests.get("https://analytics.google.com/analytics/web/#/p407487549/reports/intelligenthome")
#        response.raise_for_status()
#        cookies = response.cookies
#        cookies_html = "<h2>Google Analytics Request Cookies:</h2><ul>"
#        for cookie in cookies:
#           cookies_html += f"<li><strong>{cookie.name}:</strong> {cookie.value}</li>"
#        cookies_html += "</ul>"
#        return cookies_html
#    except requests.exceptions.RequestException as e:
#        return f"Error checking Google Analytics Request Cookies: {str(e)}"

@app.route('/chart_data')
def chart_data():
    pytrends = TrendReq(hl='en-US', tz=360)
    keywords = ["Bowling", "Karting"]
    pytrends.build_payload(keywords, timeframe='today 12-m', geo='US')
    interest_over_time_df = pytrends.interest_over_time()

    data = {
        'dates': interest_over_time_df.index.strftime('%Y-%m-%d').tolist(),
        'Bowling': interest_over_time_df['Bowling'].tolist(),
        'Karting': interest_over_time_df['Karting'].tolist()
    }

    return jsonify(data)

@app.route('/chart_data_render')
def index():
    return render_template('chart_data.html')

