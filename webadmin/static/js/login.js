$(document).ready(function () {
    var usuario, password;

    $("#ingresar").click(function () {
        usuario = $("#usuario").val();
        password = $("#password").val();

        var obj = new crearUsuario(usuario,password);
        console.log(obj);
        verificarCuenta(obj);
    });

    function verificarCuenta(obj) {
        event.preventDefault();
        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:8000/servicios/usuarioAuth/",
            csrfmiddlewaretoken: "{{ csrf_token }}",
            data: JSON.stringify(obj),
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            success: function (response) {
                if(response['auth']){
                    window.location.href = "http://127.0.0.1:8000/webadmin/questionBrowser";
                }
                else {
                    alert("usuario o contraseña errónea");
                }
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                alert("some error " + String(errorThrown) + String(textStatus) + String(XMLHttpRequest.responseText));
            }
        });

    }

});

function crearUsuario(usuario, password) {
    this.usuario = usuario;
    this.password = password;
}