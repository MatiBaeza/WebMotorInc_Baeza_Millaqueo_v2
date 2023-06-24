const nombre = document.getElementById("name")
const apellido = document.getElementById("last-name")
const rut = document.getElementById("rut")
const genero = document.getElementById("gender")
const telefono = document.getElementById("phone")
const correo = document.getElementById("email")
const textarea = document.getElementById("textarea")
const form = document.getElementById("form")
const parrafo = document.getElementById("warnings")

(function () {
    const btnEliminacion=document.querySelectorAll(".btnEliminacion");
    btnEliminacion.forEach(btn=> {
        btn.addEventListener('click', (e)=>{
            const confirmacion=confirm('¿Seguro de eliminar el Paquete?');
            if(!confirmacion){
                e.preventDefault();
            }
        });
    });
})();


form.addEventListener("submit", e=>{
    e.preventDefault()
    let warnings = ""
    let entrar = false
    let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/
    parrafo.innerHTML = ""
    console.log(nombre.value.length <4)
    if(nombre.value.length <3){
        warnings += `Debe ingresar un nombre <br>`
        entrar = true
    }
    if(apellido.value.length <3){
        warnings += `Debe ingresar un apellido <br>`
        entrar = true
    }
    if(rut.value.length <9){
        warnings += `Debe ingresar un rut valido <br>`
        entrar = true
    }
    if(genero.value.length <8){
        warnings += `Debe ingresar un genero valido <br>`
        entrar = true
    }
    if(telefono.value.length < 9){
        warnings += `Telefono invalido <br>`
        entrar = true
    }
    if(!regexEmail.test(correo.value)){
        warnings += `Correo invalido <br>`
        entrar = true
    }
    if(textarea.value.length <1){
        warnings += `Debe llenar el campo de texto <br>`
        entrar = true
    }

    if(entrar){
        parrafo.innerHTML = warnings
    }else{
        parrafo.innerHTML = "Enviado"
    }
})