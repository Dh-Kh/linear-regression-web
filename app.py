from flask import Flask, render_template, flash, request
from linear_prediction_flask import user_input_test
from forms import InputForm
import os
from pathlib import Path
from dotenv import load_dotenv
basepath = Path()
basedir = str(basepath.cwd())
envars = basepath.cwd() / '.env'
load_dotenv(envars)
app = Flask(__name__, template_folder="templates")
app.secret_key = os.getenv("SECRET_KEY")

@app.route("/display_page",methods=["GET", "POST"])
def display_page():
    form = InputForm()
    if form.validate_on_submit():
        mapping_data = request.form.get("input_variable")
        predicted_result = user_input_test(int(mapping_data))
        flash(f"Your salary will be: {predicted_result[0]}")
        return render_template("display_page.html", form=form)
    return render_template("display_page.html", form=form)
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
