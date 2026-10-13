alert("app.js loaded!");
const userSelect = document.getElementById("user-select");
const confirmBtn = document.getElementById("confirm-btn");

confirmBtn.addEventListener("click", () => {
    const user = userSelect.value;
    fetch(`/monitor/${user}`)
        .then(response => response.json())
        .then(data => {
            console.log(data);

            const sites = document.getElementById("sites");

            sites.innerHTML = "";

            for (const [url, info] of Object.entries(data)) {
                sites.innerHTML += `
                <div class="card">
                    <p class="display_name"> Name: ${info.name}</p>
                    <p class="url">URL: ${url}</p>
                    <p class="status">Status: ${info.status}</p>
                </div>`;
            }

            document.getElementById("username").textContent = user;
        });
});