window.onload = function() {
    const lang = localStorage.getItem('language') || 'en'; 
    setLanguage(lang);
};

function switchLanguage(language) {
    localStorage.setItem('language', language);
    setLanguage(language);
}
function setLanguage(language) {
    if (language === 'fr') {
        document.getElementById('title').innerText = 'Classificateur de spam';
        document.getElementById('emailMessageLabel').innerText = 'Entrez le message de l\'email :';
        document.querySelector('button[type="submit"]').innerText = 'Classer';
        document.getElementById('frBtn').style.backgroundColor = '#B7A7A6';
        document.getElementById('enBtn').style.backgroundColor = '';
    } else {
        document.getElementById('title').innerText = 'Email Classifier';
        document.getElementById('emailMessageLabel').innerText = 'Enter Email Message:';
        document.querySelector('button[type="submit"]').innerText = 'Classify';
        document.getElementById('enBtn').style.backgroundColor = '#B7A7A6 ';
        document.getElementById('frBtn').style.backgroundColor = '';
    }
}
