async function displaySubmissions() {
    const response = await fetch('https://pages.up.pt/~up202303872/scores.php');
    const submissions = await response.json();

    const elements = submissions.map((score) => {
        const row = document.createElement('tr');

        const usernameCell = document.createElement('td');
        usernameCell.textContent = score.username;
        row.appendChild(usernameCell);

        const scoreCell = document.createElement('td');
        scoreCell.classList.add('text-end');
        scoreCell.textContent = score.score.toFixed(2);
        row.appendChild(scoreCell);

        return row;
    });

    const table = document.querySelector('tbody');
    table.replaceChildren(...elements);
}

async function submit() {
    const username = document.querySelector('#username').value;
    const solution = document.querySelector('#solution').value;

    const formData = new FormData();
    formData.append('username', username);
    formData.append('solution', solution);

    await fetch('https://pages.up.pt/~up202303872/submit.php', {
        method: 'POST',
        body: formData
    });
}

async function main() {
    displaySubmissions();

    // Add an event listener to the form
    const form = document.querySelector('form');
    form.addEventListener('submit', async (event) => {
        event.preventDefault();
        await submit();
        displaySubmissions();
    });
}

main();
