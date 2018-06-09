$(document).ready(function () {
    var usuario, password;

    $("#ingresar").click(function () {
        usuario = $("#usuario").val();
        password = $("#password").val();

        var obj = new crearObj(usuario,password);

        verificarCuenta(obj);
    });

    function verificarCuenta(obj) {
        event.preventDefault();
        $.ajax({
            type: "POST",
            url: "https://cachimbogo.herokuapp.com/servicios/preguntaT/",
            csrfmiddlewaretoken: "{{ csrf_token }}",
            data: JSON.stringify(obj),
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            success: function () {
                alert("Saved! It worked.");
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                alert("some error " + String(errorThrown) + String(textStatus) + String(XMLHttpRequest.responseText));
            }
        });

    }

});

function crearObj(usuario, password) {
    this.usuario = usuario;
    this.password = password;
}