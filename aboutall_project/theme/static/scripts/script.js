document.addEventListener('DOMContentLoaded', () => {
    const logo = document.getElementById('logo');
    const header = document.getElementById('header');
  
    const updateLogo = () => {
        const bgColor = window.getComputedStyle(header).backgroundColor;
        logo.src = bgColor === 'rgb(0, 0, 0)' ? '{% static "assets/logo-dark.svg" %}' : '{% static "assets/logo.svg" %}';
    };

    updateLogo();
});