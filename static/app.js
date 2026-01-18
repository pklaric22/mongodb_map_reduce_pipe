const output = document.getElementById("output");

function loadAnalyzed() {
    fetch("/analyzed-movies")
        .then(r => r.json())
        .then(data => {
            output.innerHTML = "";
            data.forEach(m => {
                output.innerHTML += `
                    <div class="card">
                        <strong>${m.title}</strong><br>
                        Rating: ${m.rating}<br>
                        Views: ${m.views}<br>
                        Score: ${m.finalScore}
                    </div>
                `;
            });
        });
}

function loadBest() {
    fetch("/best-movie")
        .then(r => r.json())
        .then(m => {
            output.innerHTML = `
                <div class="card">
                    <strong>${m.title}</strong><br>
                    Score: ${m.finalScore}
                </div>
            `;
        });
}

function loadByGenre() {
    fetch("/pipeline/ranked-by-genre")
        .then(r => r.json())
        .then(data => {
            output.innerHTML = "";
            for (const genre in data) {
                output.innerHTML += `<h3>${genre}</h3>`;
                data[genre].forEach(m => {
                    output.innerHTML += `
                        <div class="card">
                            ${m.title} – ${m.finalScore}
                        </div>
                    `;
                });
            }
        });
}
