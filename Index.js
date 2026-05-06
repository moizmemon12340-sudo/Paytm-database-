const express = require("express");
const axios = require("axios");

const app = express();

// 👇 यहां अपनी RapidAPI key डाल देना
const RAPIDAPI_KEY = "4031d8fca9mshd856dbf4ba5f5e5p1ad3bejsnd6dbde6aa518";

app.get("/bgmi/:id", async (req, res) => {
    const id = req.params.id;

    try {
        const response = await axios.get(
            `https://id-game-checker.p.rapidapi.com/bgmi/${id}`,
            {
                headers: {
                    "x-rapidapi-host": "id-game-checker.p.rapidapi.com",
                    "x-rapidapi-key": RAPIDAPI_KEY
                }
            }
        );

        res.json(response.data);

    } catch (error) {
        res.status(500).json({
            success: false,
            message: error.message
        });
    }
});

module.exports = app;
