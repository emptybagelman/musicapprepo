const express = require("express")
const cors = require("cors")
const app = express()

const {logger} = require("./logger")
const songs = require("./songs")

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({extended:true}));
app.use(logger);

app.get("/",(req,res) => {
    res.send(songs)
})

app.get("/alpha",(req,res) => {
    res.send(songs[0])
})

app.get("/alpha/songs",(req,res) => {
    res.send(songs[0].songs)
})

app.get("/beta",(req,res) => {
    res.send(songs[1])
})

app.get("/beta/songs",(req,res) => {
    res.send(songs[1].songs)
})

module.exports = {app};