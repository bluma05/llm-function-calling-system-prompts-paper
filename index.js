// index.js - Scientific Paper LandingPage (LLM + Function Calling + Tools + System Prompts)
// This file provides optional interactivity for the landing page, such as sidebar highlighting, smooth scroll, and section toggling.

document.addEventListener('DOMContentLoaded', function () {
  // Highlight sidebar link on scroll
  const sections = document.querySelectorAll('main section');
  const navLinks = document.querySelectorAll('aside nav a');

  function activateLink() {
    let index = sections.length;
    while (--index && window.scrollY + 120 < sections[index].offsetTop) {}
    navLinks.forEach((link) => link.classList.remove('text-yellow-400', 'font-bold'));
    if (navLinks[index]) {
      navLinks[index].classList.add('text-yellow-400', 'font-bold');
    }
  }
  activateLink();
  window.addEventListener('scroll', activateLink);

  // Smooth scroll for sidebar links
  navLinks.forEach(link => {
    link.addEventListener('click', function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        window.scrollTo({
          top: target.offsetTop - 40,
          behavior: 'smooth'
        });
      }
    });
  });
});
