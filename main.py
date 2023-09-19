from flask import Flask

app = Flask(__name__)

@app.route("/")
def root():
    return "Hello from World! 🚀"
def hello_world():
 prefix_google = """
 <!-- Google tag (gtag.js) -->
<script async
src="https://www.googletagmanager.com/gtag/js?id=YOUR_GA_CODE"></script>
<script>
 window.dataLayer = window.dataLayer || [];
 function gtag(){dataLayer.push(arguments);}
 gtag('js', new Date());
 gtag('config', 'G-DVK1THXJ2C');
</script>
 """
 return prefix_google + "Hello World"
