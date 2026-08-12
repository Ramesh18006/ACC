document.addEventListener('DOMContentLoaded', () => {
    const slides = document.querySelectorAll('.slide');
    const dots = document.querySelectorAll('.dot');
    let currentIndex = 0;

    function showSlide(index) {
        slides.forEach(s => s.classList.remove('active'));
        dots.forEach(d => d.classList.remove('active'));

        slides[index].classList.add('active');
        dots[index].classList.add('active');
    }

    function nextSlide() {
        currentIndex = (currentIndex + 1) % slides.length;
        showSlide(currentIndex);
    }

    dots.forEach((dot, idx) => {
        dot.addEventListener('click', () => {
            currentIndex = idx;
            showSlide(currentIndex);
        });
    });

    setInterval(nextSlide, 4500);

    // Brand Chip Switcher (For product page)
    const chipBtns = document.querySelectorAll('.chip-btn');
    if (chipBtns.length > 0) {
        chipBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                chipBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
            });
        });
    }
});