const nav = document.querySelector('.normal-nav');
window.addEventListener('scroll', function(){
    if(window.pageYOffset > 70){
        nav.classList.add('bg-dark', 'shadow');
    }else{
        nav.classList.remove('bg-dark', 'shadow');
    }
})