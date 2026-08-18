// Search.jsx

import { useState } from "react";
import axios from "axios";

function Search() {

    const [query, setQuery] = useState("");
    const [videos, setVideos] = useState([]);

    const searchVideos = async () => {
        try {
            const response = await axios.get(
                "http://localhost:8000/api/videos/search/",
                {
                    params: { q: query }
                }
            );

            setVideos(response.data.results);

        } catch (error) {
            console.error("Search failed:", error);
        }
    };

    return (
        <div>
            <input
                type="text"
                placeholder="Search videos..."
                value={query}
                onChange={(e) => setQuery(e.target.value)}
            />

            <button onClick={searchVideos}>
                Search
            </button>

            {videos.map((video) => (
                <div key={video.id}>
                    <h3>{video.title}</h3>
                    <p>{video.description}</p>
                </div>
            ))}
        </div>
    );
}

export default Search;