stores the songs.

    - clone the repo
    - `npm i`
    - `npm run dev`
    - go to localhost:3000 to see it working

link here https://github.com/emptybagelman/Music-App


 - open docker desktop
 - run: docker run -it --rm --name flask --mount type=bind,src="$(pwd)",dst=/code -p 5000:5000 python:3.11 bash -c "cd /code && bash