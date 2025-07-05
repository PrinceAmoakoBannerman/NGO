// JS: trigger on load and toggle on scroll
document.addEventListener('DOMContentLoaded', () => {
  const heroContent = document.querySelector('.hero-content');
  heroContent.classList.add('h1-visible'); // animate in on page load

  let lastY = window.pageYOffset;
  window.addEventListener('scroll', () => {
    const currentY = window.pageYOffset;
    if (currentY > lastY) {
      // scrolling down
      heroContent.classList.remove('h1-visible');
      heroContent.classList.add('h1-hidden');
    } else {
      // scrolling up
      heroContent.classList.remove('h1-hidden');
      heroContent.classList.add('h1-visible');
    }
    lastY = currentY;
  });
});


document.addEventListener('DOMContentLoaded', () => {
  // SLIDESHOW
  const slides = document.querySelectorAll('.hero .slide');
  let current = 0; // first slide already has `active` class in HTML

  setInterval(() => {
    slides[current].classList.remove('active');
    current = (current + 1) % slides.length;
    slides[current].classList.add('active');
  }, 10000); // switch every 5s

  // BUTTON HANDLERS
  document.querySelector('.watch-more').addEventListener('click', () => {
    console.log('OUR STORY clicked');
    // e.g. document.querySelector('#story').scrollIntoView({ behavior: 'smooth' });
  });
  document.querySelector('.volunteer').addEventListener('click', () => {
    window.location.href = '/volunteer';
  });
  document.querySelector('.donate').addEventListener('click', () => {
    window.location.href = '/donate';
  });
});

document.addEventListener('DOMContentLoaded', () => {
  const dragBtn = document.querySelector('.drag-btn');

  dragBtn.addEventListener('mousedown', () => {
    dragBtn.textContent = 'DRAGGING…';
  });
  document.addEventListener('mouseup', () => {
    dragBtn.textContent = 'DRAG >>>';
  });
});




