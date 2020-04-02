# @File: index
# @Author: Kevin Huo
# @LastUpdate: 3/21/2020 6:16 PM


from flask import render_template, make_response


def index_func():
    """
    home page
    """
    html = render_template("index.html")

    res = make_response(html)
    res.status_code = 200
    return res
