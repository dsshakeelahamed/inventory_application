from rest.rest import app
import config.config as cfg

if __name__ == "__main__":
    app.run(host=cfg.application_host, debug=True, port=cfg.application_port)
