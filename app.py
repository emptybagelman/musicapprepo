from apk import app
from apk.albums import route
from apk.realms import route
from apk.installations import route

if __name__ == "__main__":
    app.run(host="0.0.0.0")