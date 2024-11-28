from flask import Flask, render_template

# Flask app initialization
app = Flask(
    __name__,
    static_folder="../../frontend/static",  # Static files
    template_folder="../../frontend/templates"  # Templates
)

# App route for the index page
@app.route("/")
def index():
    apps = [
        {"name": "Fenix", "url": "/fenix", "icon": "assets/icons/fenix.jpg"},
        {"name": "Navigraph", "url": "/navigraph", "icon": "assets/icons/navigraph.jpg"},
        {"name": "Navigraph", "url": "/placeholder1", "icon": "assets/icons/navigraph.jpg"},
        {"name": "Navigraph", "url": "/placeholder2", "icon": "assets/icons/navigraph.jpg"},
        {"name": "Navigraph", "url": "/placeholder3", "icon": "assets/icons/navigraph.jpg"},
        {"name": "Navigraph", "url": "/placeholder4", "icon": "assets/icons/navigraph.jpg"},
        {"name": "Navigraph", "url": "/placeholder5", "icon": "assets/icons/navigraph.jpg"},
        {"name": "Navigraph", "url": "/placeholder6", "icon": "assets/icons/navigraph.jpg"},
    ]
# Even arrangement for the apps on the home page
    half = len(apps) // 2  # # Deviding Apps in two groups
    return render_template("index.html", row1=apps[:half], row2=apps[half:])

# App route to the Fenix EFB
@app.route("/fenix")
def fenix():
    return render_template("fenix.html")

# App route to the Navigraph Cloud Charts
@app.route("/navigraph")
def navigraph():
    return render_template("navigraph.html")

# App route to placeholder page 1
@app.route("/placeholder1")
def placeholder1():
    return render_template("placeholder1.html")

# App route to placeholder page 2
@app.route("/placeholder2")
def placeholder2():
    return render_template("placeholder2.html")

# App route to placeholder page 3
@app.route("/placeholder3")
def placeholder3():
    return render_template("placeholder3.html")

# App route to placeholder page 4
@app.route("/placeholder4")
def placeholder4():
    return render_template("placeholder4.html")

# App route to placeholder page 5
@app.route("/placeholder5")
def placeholder5():
    return render_template("placeholder5.html")


# Bind to all interfaces
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
