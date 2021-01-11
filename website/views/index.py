import os
import pathlib
from flask import request, session, abort, redirect, render_template, url_for
import website
sys.path.append("../../data")
import lyrics_dict



@website.app.route("/top_words/", methods=["GET", "POST"])
def show_top_words():
    features_path = os.path.join(cur_path, "..", ".." ,"data", "features_dict.py")
    with open(features_path, "r") as f:
        context = json.loads(f)
    return render_template("index.html", **context)