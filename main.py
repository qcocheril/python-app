from flask import Flask

app = Flask(__name__)

prefix_google = """
<!-- Google tag (gtag.js) -->
<script async
src="https://www.googletagmanager.com/gtag/js?id=G-DVK1THXJ2C"></script>
<script>
 window.dataLayer = window.dataLayer || [];
 function gtag(){dataLayer.push(arguments);}
 gtag('js', new Date());
 gtag('config', 'G-DVK1THXJ2C');
</script>
"""

@app.route("/")

def hello_world():
 return prefix_google + "Hello World"

@app.route("/logger")

def logger():

 log_msg = "Logger route accessed"
 browser_log = """
 <script>
    console.log("This is a log message");
 </script>
 """
 print(log_msg)
 return log_msg + browser_log


