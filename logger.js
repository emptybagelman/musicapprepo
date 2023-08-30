function logger(req,res,next){
    console.log(req.method,req.originalUrl,"Log")
    next()
};

module.exports = {logger};