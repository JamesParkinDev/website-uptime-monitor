alert("app.js loaded!");
const userSelect = document.getElementById("user-select");
const refreshBtn = document.getElementById("refresh-btn");

// TODO: Add functionality to the Add Website button

refreshBtn.addEventListener("click", () => {
    const user = userSelect.value;
    fetch(`/monitor/${user}`)
        .then(response => response.json())
        .then(data => {
            console.log(data);

            const sites = document.getElementById("sites");

            sites.innerHTML = "";

            for (const [url, info] of Object.entries(data)) {
                if (info.status === "UP") {
                    // formatting for active website
                    sites.innerHTML += `    
                    <div class="card_up">
                        <p class="display_name"> Name: ${info.name}</p>
                        <p class="url">URL: ${url}</p>
                        <p class="status">Status: ${info.status}</p>
                        <p class="ping">Ping: ${info.response_time_ms}</p>
                    </div>`;
                } else {
                    // alternate formatting for inactive or unavailable website
                    sites.innerHTML += `
                    <div class="card_down">
                        <p class="display_name"> Name: ${info.name}</p>
                        <p class="url">URL: ${url}</p>
                        <p class="status">Status: ${info.status}</p>
                        <p class="error">Error Type: ${info.error}</p>
                    </div>`;
                }

            }

            document.getElementById("username").textContent = user;
        });
});