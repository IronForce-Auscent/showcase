from flask import *
import jwt

app = Flask(__name__)
app.config["FLAG"] = "NYP{1_l0v3_sn1ck3rd00dl3s!}"
app.config["SECRET_KEY"] = "snickerdoodle" 

cookies = {
    "chocolate chip": "Ah, a classic! ",
    "oatmeal raisin": "Oh, you must like to eat healthy.",
    "peanut butter": "A bit of an interesting decision, but I respect that :D ",
    "snickerdoodle": "Ah, one of our admins love that flavour too! ",
    "double chocolate": "No such thing as too much chocolate. ",
    "red velvet": "An elegant choice indeed. ",
    "flag": "A... flag cookie? Don't think I've heard of that one before. ",
    "flag cookie": "A... flag cookie? Don't think I've heard of that one before. "
}

@app.route("/cookie-picker", methods=["POST"])
def cookie_picker():
    cookie = request.form.get("cookie")
    if cookie:
        payload = {
            "favourite-cookie": cookie,
            "is-admin": False
        }
        
    resp = make_response(redirect(url_for("index")))
    resp.set_cookie("cookie", jwt.encode(payload, app.config["SECRET_KEY"], algorithm=["HS256"]))
    return resp

@app.route('/')
def index():
    msg = ""
    if "cookie" in request.cookies:
        cookie_jwt = request.cookies["cookie"]
        if cookie_jwt:
            data = jwt.decode(cookie_jwt, app.config["SECRET_KEY"], algorithms=["HS256"]) 
            favourite_cookie, is_admin = data.values()
            if favourite_cookie in ["flag", "flag cookie"]:
                if is_admin: 
                    msg = f"Welcome back admin! Here's your favourite cookie: {app.config["FLAG"]}"
                else:
                    msg = cookies[favourite_cookie] + "One of our admins does seem to mention that cookie a lot though, maybe you can ask them for one?"
            else:
                if favourite_cookie in cookies.keys():
                    msg = cookies[favourite_cookie]
                else:
                    msg = "Hmm, don't think I've heard of that one before!"
    return render_template('index.html', msg=msg)

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
