from api import *
from flask import Flask, request, jsonify

robot_wxid = request.form.get("robot_wxid")
send_text_msg(robot_wxid,"wxid_987f0q7mgban22","123")