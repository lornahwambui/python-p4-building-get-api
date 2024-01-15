#!/usr/bin/env python3

from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, User, Review, Game

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True  # Enable pretty-printing of JSON responses

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return "Index for Game/Review/User API"

@app.route('/games')
def games():
    games = []
    for game in Game.query.all():
        game_dict = {
            "title": game.title,
            "genre": game.genre,
            "platform": game.platform,
            "price": game.price,
        }
        games.append(game_dict)

    response = make_response(
        jsonify(games),
        200,
        {"Content-Type": "application/json"}
    )

    return response

@app.route('/games/<int:id>')
def games_by_id(id):
    game = Game.query.filter(Game.id == id).first()
    if game:
        game_dict = {
            "title": game.title,
            "genre": game.genre,
            "platform": game.platform,
            "price": game.price,
        }

        response = make_response(
            jsonify(game_dict),
            200
        )
    else:
        response = make_response(
            jsonify({"error": "Game not found"}),
            404
        )

    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)
