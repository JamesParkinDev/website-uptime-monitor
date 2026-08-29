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
                    <p>URL: ${url}</p>
                    <p>Status: ${info.status}</p>
                </div>`;
            }

            document.getElementById("username").textContent = user;
        });
});
