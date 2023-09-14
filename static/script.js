document.addEventListener('mousemove', function(e) {
    const mouseX = e.clientX / window.innerWidth * 100;
    const mouseY = e.clientY / window.innerHeight * 100;
    const hiddenBackground = document.querySelector('.hidden-background');

    hiddenBackground.style.backgroundPosition = `${mouseX}% ${mouseY}%`;
  });