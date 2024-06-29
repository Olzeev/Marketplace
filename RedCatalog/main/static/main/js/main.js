window.addEventListener('scroll', function() {
    const header = document.getElementById('header');
    if (window.scrollY > 0) {
        header.classList.add('scroll');
    } else {
        header.classList.remove('scroll');
    }
})

function login(){
    login_window = document.getElementById('login-window')
    login_window.style.visibility = "visible"
    login_window.style.left = "0px"
    screen = document.getElementById('screen')
    screen.style.visibility = "visible"
    document.body.style.overflow = 'hidden';
}

function close_everything(){
    login_window = document.getElementById('login-window')
    if (login_window.style.visibility == "visible"){
        login_window.style.left = "calc(0px - max(400px, 25%))"
        login_window.style.visibility = "hidden"
    }

    screen = document.getElementById('screen')
    screen.style.visibility = "hidden"
    document.body.style.overflow = 'auto';

}

function login1(){
    button = document.getElementById('login-button')
    button.innerHTML = '<div class="loader"></div>'
    setTimeout(function() {
        $.ajax({
            url: 'login',
            type: 'get',
            data: {
                mail: document.getElementById('input-mail').value,
                password: document.getElementById('input-password').value,
                csrfmiddlewaretoken: '{{ csrf_token }}'
            },
            success: function(response){
                location.reload()
            }
        })
    }, 3000);

}