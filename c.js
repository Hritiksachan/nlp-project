document.getElementById('translate-button').addEventListener('click', async function() {
    const inputText = document.getElementById('input-text').value;
    const languagePair = document.getElementById('language-select').value;

    const endpoint = languagePair === 'en-hi' ? '/translate/en-hi' : '/translate/hi-en';

    try {
        const response = await fetch(endpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: inputText }),
        });

        if (response.ok) {
            const result = await response.json();
            document.getElementById('output-text').innerText = result.translation;
        } else {
            throw new Error('Translation error');
        }
    } catch (error) {
        console.error("Error:", error);
        document.getElementById('output-text').innerText = "Error during translation.";
    }
});

