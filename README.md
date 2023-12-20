stores the songs & realms.

link here https://github.com/emptybagelman/Music-App

 - clone the repo
 - open docker desktop
 - run: docker run -it --rm --name music_app --mount type=bind,src="$(pwd)",dst=/code -p 5000:5000 python:3.11 bash -c "cd /code && bash
 - pip install pipenv
 - pipenv install
 - pipenv run dev

# ROUTES


