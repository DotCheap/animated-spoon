const express = require("express");
const app = express();

app.use(express.json());
app.use(express.text())
app.use(express.urlencoded({extended : true}));

app.post("/", (req, res) => {
    
});


app.get("/", (req, res) => {
    console.log(req.body);
    res.json({ yolo : 'hello'})
});

app.listen(3000, () => console.log(`App is running on port 3000`));