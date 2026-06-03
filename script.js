document.addEventListener('change', function() {
    const licence = document.getElementById('licenceFilter')?.value || "";
    const semestre = document.getElementById('semestreFilter')?.value || "";
    const rows = document.querySelectorAll('tr[data-licence]');

    rows.forEach(row => {
        const rowL = row.getAttribute('data-licence');
        const rowS = row.getAttribute('data-semestre');
        
        const matchesL = (licence === "" || rowL === licence);
        const matchesS = (semestre === "" || rowS === semestre);

        if (matchesL && matchesS) {
            row.style.display = "";
        } else {
            row.style.display = "none";
        }
    });
});
document.addEventListener('input', function() {
    const searchTerm = document.querySelector('.search-bar input')?.value.toLowerCase() || "";
    const licence = document.getElementById('licenceFilter')?.value || "";
    const semestre = document.getElementById('semestreFilter')?.value || "";
    const matiere = document.getElementById('matiereFilter')?.value.toLowerCase() || "";

    // On cible à la fois les lignes de tableau et les cartes
    const items = document.querySelectorAll('tr[data-licence], .glass-card[data-licence]');

    items.forEach(item => {
        const itemL = item.getAttribute('data-licence');
        const itemS = item.getAttribute('data-semestre');
        const itemM = item.getAttribute('data-matiere') || ""; // Pour la page Examen
        const itemText = item.innerText.toLowerCase();

        const matchesSearch = itemText.includes(searchTerm);
        const matchesL = (licence === "" || itemL === licence);
        const matchesS = (semestre === "" || itemS === semestre);
        const matchesM = (matiere === "" || itemM.includes(matiere));

        if (matchesSearch && matchesL && matchesS && matchesM) {
            item.style.display = "";
        } else {
            item.style.display = "none";
        }
    });
});