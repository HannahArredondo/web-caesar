from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True


form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form{{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea{{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="POST">
       
            <label> Rotate by:
                <input name="rot" type="text" value='0'/>
            </label>
            <textarea name="text">{0}</textarea>
            <input type="submit" value="ENCRYPT YOUR MESSAGE" />
        
        </form>
    </body>
</html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    rot_by = request.form['rot']
    rot_by = int(rot_by)
    some_text = request.form['text']

    rotated_text = rotate_string(some_text,rot_by)
    return form.format(rotated_text)

@app.route("/")
def index():
    return form.format("")

app.run()