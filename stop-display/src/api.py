from flask import Flask
from src.display import create_display_ttgo
from src.query import query_stop_board

app = Flask(__name__)

@app.route("/ttgo/<string:stop_id>/<string:lines_directions>")
def get_display(stop_id: str, lines_directions: str):
    """
    lines direction should be indicated as 
    'line1:direction1,direction2;line2:direction1,direction2'
    """
    departures = query_stop_board(stop_id)
    lines = lines_directions.split(";")
    _lines = {}
    for line_directions in lines:
        line, directions = line_directions.split(":")
        _lines[line] = set(directions.split(","))
    return create_display_ttgo(departures, _lines, ["EXB", "S"])
