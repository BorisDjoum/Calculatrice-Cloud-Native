async function sendCalculation() {
    const num1 = document.getElementById('num1').value;
    const operator = document.getElementById('operator').value;
    const num2 = document.getElementById('num2').value;
    const resultDiv = document.getElementById('result');

    if (!num1 || !num2 || isNaN(num1) || isNaN(num2)) {
      resultDiv.innerHTML = '<span class="error">Veuillez entrer des nombres valides.</span>';
      return;
    }

    if (operator === '/' && parseFloat(num2) === 0) {
      resultDiv.innerHTML = '<span class="error">Division par zéro non autorisée.</span>';
      return;
    }

    // Vérifie si les champs sont remplis
    if (!num1 || !num2) {
      resultDiv.innerHTML = '<span class="error">Veuillez remplir tous les champs.</span>';
      return;
    }

    // Affiche un loader pendant le calcul
    resultDiv.innerHTML = '<div class="loader"></div>';

    try {
      // Requête POST pour envoyer le calcul
      const response = await fetch('/api/v1/calcul', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ tuple: [num1, operator, num2] })
      });

      const data = await response.json();

      if (data.id) {
        fetchResult(data.id);
      } else {
        resultDiv.innerHTML = '<span class="error">Erreur lors de l\'envoi du calcul.</span>';
      }
    } catch (error) {
      resultDiv.innerHTML = '<span class="error">Erreur de connexion à l\'API.</span>';
      console.error(error);
    }
  }

  async function fetchResult(id) {
    const resultDiv = document.getElementById('result');
    let attempts = 0;
    const maxAttempts = 10; // Maximum de 10 tentatives (10 secondes)

    const interval = setInterval(async () => {
      if (attempts >= maxAttempts) {
        clearInterval(interval);
        resultDiv.innerHTML = '<span class="error">Le calcul a pris trop de temps. Veuillez réessayer.</span>';
        return;
      }

      try {
        const response = await fetch(`/api/v1/calcul/${id}`);
        const data = await response.json();

        if (data.status === 'done') {
          resultDiv.innerHTML = `Résultat : <strong>${data.result}</strong>`;
          clearInterval(interval);
        } else if (data.status === 'error') {
          resultDiv.innerHTML = `<span class="error">Erreur : ${data.result}</span>`;
          clearInterval(interval);
        }
      } catch (error) {
        resultDiv.innerHTML = '<span class="error">Erreur lors de la récupération du résultat.</span>';
        console.error(error);
        clearInterval(interval);
      }

      attempts++;
    }, 1000);
    }