# Imports

from flask import Flask, request, redirect, render_template, Blueprint, jsonify, send_from_directory
import json
import logging


# Constants

LOGS_PATH = "logs/log.log"
POSTS_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


# Logging

logger = logging.getLogger("logger")
logger.setLevel(logging.INFO)
_file_handler = logging.FileHandler(LOGS_PATH)
_format = logging.Formatter("%(levelname)s : %(asctime)s >>> %(message)s")
_file_handler.setFormatter(_format)
logger.addHandler(_file_handler)
