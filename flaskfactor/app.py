"""Main application for flaskfactor"""

from flask import Flask, render_template
import os
from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def create_app():
  """Create and configures and instance of a flask app"""
  app = Flask(__name__)

  @app.route('/')
  def home():
      return render_template('home.html')

  @app.route('/<variable>', methods=['GET'])
  def factor_page(variable):
      try:
        res = str(factors(int(variable)))
        return res
      except:
        return variable + " is not a valid number."

  return app