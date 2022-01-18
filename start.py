import utility.utility as utils
import sys
import os

# sys.argv[1] is the environment passed from command line, default - dev
env = "dev"
if len(sys.argv) > 1:
    if sys.argv[1].lower() in ["dev", "test"]:
        env = sys.argv[1].lower()
os.environ["FLASK_ENV"] = env
cfg = utils.get_environment_configs()

from rest.rest import app


if __name__ == "__main__":
    app.run(host=cfg.application_host, debug=True, port=cfg.application_port)
