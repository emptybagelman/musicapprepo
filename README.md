stores the songs & realms.

link here https://github.com/emptybagelman/Music-App

 - clone the repo
 - open docker desktop
 - run: docker run -it --rm --name music_app --mount type=bind,src="$(pwd)",dst=/code -p 5000:5000 python:3.11 bash -c "cd /code && bash
 - pip install pipenv
 - pipenv install
 - pipenv run dev

# ```/albums```

## Schema:

```typescript
interface Album {
    id: number,
    album_name: string,
    songs: object
}
```

## Routes:

### /
- GET: returns all albums.
- POST: adds new album to db.

### /<int:id>
- GET: returns album by id.
- PATCH: updates attribute of album.
- DELETE: removes album from table.

# ```/realms```

## Schema:

```typescript
interface Realm {
    id: number,
    name: string,
    expired: boolean,
    members: number | null
}
```

## Routes:

### /
- GET: returns all realms.

# ```/installations```

## Schema:

```typescript
interface Installation {
    id: number,
    name: string,
    version: string,
    directory: string,
    resolution: string,
    javaexec: string | null , 
    jvm: string | null
}
```

## Routes:

### /