import utility.utility as utils
import sys
import os

"""
Shopify Challenge for the Software/Infrastructure Engineering Intern (Summer 2022) position Remote/US.
Candidate: Shakeel Ahamed Davanagere 
Challenge link: https://docs.google.com/document/d/1z9LZ_kZBUbg-O2MhZVVSqTmvDko5IJWHtuFmIu_Xg1A/edit
                https://docs.google.com/document/d/1wir0XQuviR6p-uNEUPzsGvMFwqgMsY8sEjGUx74lNrg/edit
"""
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
