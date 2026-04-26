// Mouse tracking for subtle glow effect
const glow = document.getElementById('cursor-glow');

document.addEventListener('mousemove', (e) => {
  const x = e.clientX;
  const y = e.clientY;
  glow.style.setProperty('--mouse-x', `${x}px`);
  glow.style.setProperty('--mouse-y', `${y}px`);
});

// Intersection Observer for Active Nav State
const sections = document.querySelectorAll('section');
const navLinks = document.querySelectorAll('.nav a');

const observerOptions = {
  root: null,
  rootMargin: '-50% 0px -50% 0px',
  threshold: 0
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href').substring(1) === entry.target.id) {
          link.classList.add('active');
        }
      });
    }
  });
}, observerOptions);

sections.forEach(section => observer.observe(section));

// Language Toggle Logic
const btnEn = document.getElementById('btn-en');
const btnKo = document.getElementById('btn-ko');
const elementsWithLang = document.querySelectorAll('[data-en][data-ko]');

function setLanguage(lang) {
  // Update buttons
  if (lang === 'en') {
    btnEn.classList.add('active');
    btnKo.classList.remove('active');
  } else {
    btnKo.classList.add('active');
    btnEn.classList.remove('active');
  }

  // Update text content
  elementsWithLang.forEach(el => {
    el.textContent = el.getAttribute(`data-${lang}`);
  });
}

btnEn.addEventListener('click', () => setLanguage('en'));
btnKo.addEventListener('click', () => setLanguage('ko'));

// Detect browser language and set default
const userLang = navigator.language || navigator.userLanguage;
if (userLang.startsWith('ko')) {
  setLanguage('ko');
} else {
  setLanguage('en');
}
