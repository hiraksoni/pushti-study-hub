document.addEventListener('DOMContentLoaded', () => {
    const themeToggle = document.querySelector('.theme-toggle');
    const icon = themeToggle.querySelector('i');
    const body = document.body;

    // Set initial icon
    if (body.getAttribute('data-theme') === 'dark') {
        icon.classList.remove('fa-moon');
        icon.classList.add('fa-sun');
    }

    themeToggle.addEventListener('click', () => {
        if (body.getAttribute('data-theme') === 'light') {
            body.setAttribute('data-theme', 'dark');
            localStorage.setItem('pushti-theme', 'dark');
            icon.classList.remove('fa-moon');
            icon.classList.add('fa-sun');
        } else {
            body.setAttribute('data-theme', 'light');
            localStorage.setItem('pushti-theme', 'light');
            icon.classList.remove('fa-sun');
            icon.classList.add('fa-moon');
        }
    });

    const backToTop = document.querySelector('.back-to-top');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
            backToTop.style.display = 'flex';
        } else {
            backToTop.style.display = 'none';
        }
    });

    backToTop.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
});
