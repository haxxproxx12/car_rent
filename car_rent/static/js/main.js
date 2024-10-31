document.addEventListener("DOMContentLoaded", function () {
    const themeToggle = document.getElementById("themeToggle");
    const body = document.body;
    var img = document.getElementById('img');
    var cartimg = document.getElementById('cart-img');
    const header = document.querySelector('.header');
    const navMenu = document.querySelector('.nav-menu');
    const auth = document.querySelector('.auth');
    const main = document.querySelector('.main');
    const serviceItems = document.querySelectorAll('.service-item');
    const footer = document.querySelector('.footer');
    const cardItems = document.querySelectorAll('.car-card');
    const infoItems = document.querySelectorAll('.car-info');
    const rental = document.getElementById('rental-form');
    const authForm = document.getElementById('auth-form');
    const priceTable = document.getElementById('price-table');
    const contactForm = document.getElementById('contact-form');
    const conditions = document.querySelectorAll('.condition');


    // Проверяем, есть ли сохранённая тема в localStorage
    var savedTheme = '';
    if (localStorage.getItem("theme") === 'auto') {
        savedTheme = 'light-theme';
    }
    else {
        savedTheme = localStorage.getItem("theme");
    }

    if (savedTheme) {
        applyTheme(savedTheme);
        updateImg(savedTheme);
    }

    // Добавляем обработчик клика на кнопку переключения темы
    if (themeToggle) {
        themeToggle.addEventListener("click", function () {
            const currentTheme = body.classList.contains("light-theme") ? "light-theme" : "dark-theme";
            const newTheme = currentTheme === "light-theme" ? "dark-theme" : "light-theme";

            // Применяем новую тему ко всем элементам
            applyTheme(newTheme);

            // Обновляем текст кнопки
            updateImg(newTheme);

            // Сохраняем выбранную тему в localStorage
            localStorage.setItem("theme", newTheme);     
        }); 
    }



    function applyTheme(theme) {
        // Убираем текущие классы и добавляем новые на body, header и footer
        body.classList.remove("light-theme", "dark-theme");
        if (header && footer) {
            header.classList.remove("light-theme", "dark-theme");
            footer.classList.remove("light-theme", "dark-theme");
            navMenu.classList.remove("light-theme", "dark-theme");
            auth.classList.remove("light-theme", "dark-theme");
        }
        if (main) {
            main.classList.remove("light-theme", "dark-theme");
        }
        if ((authForm)) {
            authForm.classList.remove("light-theme", "dark-theme");
        }
        for (let index = 0; index < serviceItems.length; index++) {
            const element = serviceItems[index];
            element.classList.remove("light-theme", "dark-theme");
        }
        for (let index = 0; index < cardItems.length; index++) {
            const element = cardItems[index];
            element.classList.remove("light-theme", "dark-theme");
        }
        for (let index = 0; index < infoItems.length; index++) {
            const element = infoItems[index];
            element.classList.remove("light-theme", "dark-theme");
        }
        for (let index = 0; index < conditions.length; index++) {
            const element = conditions[index];
            element.classList.remove("light-theme", "dark-theme");
        }
        if (rental) {
            rental.classList.remove("light-theme", "dark-theme");
        }
        if (priceTable) {
            priceTable.classList.remove("light-theme", "dark-theme");
        }
        if (contactForm) {
            contactForm.classList.remove("light-theme", "dark-theme");
        }

        body.classList.add(theme);
        if (header && footer) {
            header.classList.add(theme);
            footer.classList.add(theme);
            navMenu.classList.add(theme);
            auth.classList.add(theme);
        }
        if (main) {
            main.classList.add(theme);
        }
        if (authForm) {
            authForm.classList.add(theme);
        }
        for (let index = 0; index < serviceItems.length; index++) {
            const element = serviceItems[index];
            element.classList.add(theme);       
        }
        for (let index = 0; index < cardItems.length; index++) {
            const element = cardItems[index];
            element.classList.add(theme);       
        }
        for (let index = 0; index < infoItems.length; index++) {
            const element = infoItems[index];
            element.classList.add(theme);       
        }
        for (let index = 0; index < conditions.length; index++) {
            const element = conditions[index];
            element.classList.add(theme);       
        }
        if (rental) {
            rental.classList.add(theme)
        }
        if (priceTable) {
            priceTable.classList.add(theme)
        }
        if (contactForm) {
            contactForm.classList.add(theme)
        }
    }


    function updateImg(theme) {
        if (img) {
            if (theme === "dark-theme") {
                img.setAttribute('src', '/static/img/icons//light.png')
                if (cartimg) {
                    cartimg.setAttribute('src', '/static/img/icons/cart-light.png')
                }
            } else {
                img.setAttribute('src', '/static/img/icons/dark.png')
                if (cartimg) {
                    cartimg.setAttribute('src', '/static/img/icons/cart-dark.png')
                }
            } 
        }
        
    }
});

let currentSlide = 0;

function moveSlides(direction) {
    const slides = document.querySelector('.slides');
    const totalSlides = slides.children.length;
    currentSlide = (currentSlide + direction + totalSlides) % totalSlides;
    const offset = currentSlide * -100;
    slides.style.transform = `translateX(${offset}%)`;
}

document.addEventListener("input", function () {
    let div = document.createElement('div');
    div.setAttribute('id', 'end_error')
    div.innerHTML = 'Конечная дата не должна быть меньше начальной!';


    const start_date = document.getElementById('start_date').value;
    const end_date = document.getElementById('end_date').value;
    const btn = document.getElementById('rent-btn');

    const end_error = document.querySelector('#end_error')

    const end_date_form = document.getElementById('end_date');

    if (end_date) {
        if (end_date < start_date) {
            btn.setAttribute('disabled', 'disabled');
            end_date_form.classList.add('.error');
            if (!document.getElementById('end_error')) {
                end_date_form.after(div);
            }
        }
        else {
            btn.removeAttribute('disabled', 'disabled');
            end_date_form.classList.remove('error');
            if (document.getElementById('end_error')) {
                end_error.remove();
            }
            
        }
    }

});

let visibleCars = 3;
const loadMoreButton = document.getElementById('load-more');
const carItems = document.querySelectorAll('.car-card');

function showCars() {
    carItems.forEach((car, index) => {
        if (index < visibleCars) {
            car.style.display = 'block';
        } else {
            car.style.display = 'none';
        }
    });
    if (visibleCars >= carItems.length) {
        loadMoreButton.style.display = 'none';
    }
}
if (loadMoreButton) {
    loadMoreButton.addEventListener('click', function() {
        visibleCars += 3;
        showCars();
    });
    
    showCars();
}

document.addEventListener("DOMContentLoaded", function () {
    const popup = document.getElementById("popup-message");
    if (popup) {
        popup.classList.add("show");

        // Автоматическое скрытие popup через 3 секунды
        setTimeout(function () {
            closePopup();
        }, 5000);
    }
  });

  function closePopup() {
    const popup = document.getElementById("popup-message");
    if (popup) {
        popup.classList.remove("show");
        popup.classList.add("hidden");
    }
}