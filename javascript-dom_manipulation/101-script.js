document.addEventListener('DOMContentLoaded', function () {
    const btnTranslate = document.getElementById('btn_translate');
    const languageCode = document.getElementById('language_code');
    const helloDiv = document.getElementById('hello');

    btnTranslate.addEventListener('click', function () {
        const lang = languageCode.value;
        if (lang) {
            fetch(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`)
                .then(response => response.json())
                .then(data => {
                    helloDiv.textContent = data.hello;
                })
                .catch(error => {
                    console.error('Error fetching translation:', error);
                    helloDiv.textContent = 'Error fetching translation';
                });
        } else {
            helloDiv.textContent = 'Please select a language';
        }
    });
});
