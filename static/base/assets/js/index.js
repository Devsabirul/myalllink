const trigger = document.getElementById("model_btn");
const modelWrap = document.querySelector('.model_wrap_');
const img = document.querySelectorAll('.img');
const closeBtn = document.querySelector('.close');

// first model 

trigger.addEventListener('click', function () {
    modelWrap.classList.add('model_active');
});

closeBtn.addEventListener('click', function () {
    modelWrap.classList.remove('model_active');
});

modelWrap.addEventListener('click', function (e) {
    if (e.target !== this) return;
    modelWrap.classList.remove('model_active');
});

document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
        modelWrap.classList.remove('model_active');
    }
});

