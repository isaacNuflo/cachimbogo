$(document).ready(function () {
    var tema = $('#selectTemas').val();
    var subtema = $('#selectSubTemas').val();
    var asignatura = $('#selectAsignaturas').val();
    var pregunta, alternativa1, alternativa2, alternativa3,
        alternativa4, alternativa5, informacion;
    var dificultad = $('#selectDificultad').val();
    var correcta = $('#selectAlternativa').val();

    var selectAsiganaturas = $("#selectAsignaturas").attr("id");
    var selectTemas = $("#selectTemas").attr("id");
    var selectSubTemas = $("#selectSubTemas").attr("id");
    var selectAlternativa = $("#selectAlternativa").attr("id");
    var selectDificultad = $("#selectDificultad").attr("id");

    $(".form-control").change(function () {
        var id = $(this).attr("id");
        if (id === selectAsiganaturas) {
            asignatura = $(this).val();

            var url = "https://cachimbogo.herokuapp.com/servicios/tema-asignatura/" + asignatura; // cargar url del servicio de temas
            $("#" + selectTemas).empty();
            cargarSelect(url, selectTemas, "temas");
        } else if (id === selectTemas) {
            tema = $(this).val();
            $("#" + selectSubTemas).empty();

            var url = "https://cachimbogo.herokuapp.com/servicios/subtema-tema/" + tema; // cargar url de servicio de subtemas

            cargarSelect(url, selectSubTemas, "subtemas");
        } else if (id === selectSubTemas) {
            subtema = $(this).val();
        } else if (id === selectAlternativa) {
            correcta = $(this).val();
        } else if (id === selectDificultad) {
            dificultad = $(this).val();
        }
    });
    $("#actualizar").click(function () {
        pregunta = $("#Pregunta").val();
        alternativa1 = $("#Alternativa1").val();
        alternativa2 = $("#Alternativa2").val();
        alternativa3 = $("#Alternativa3").val();
        alternativa4 = $("#Alternativa4").val();
        alternativa5 = $("#Alternativa5").val();
        informacion = $("#info").val();

        var obj = new crearObj(subtema, pregunta, alternativa1, alternativa2, alternativa3,
            alternativa3, alternativa4, alternativa5, informacion, dificultad, correcta);
        actualizarData(obj);
        $("#Alternativa1").val("");
        $("#Alternativ2").val("");
        $("#Alternativa3").val("");
        $("#Alternativa4").val("");
        $("#Alternativa5").val("");
        $("#info").val("");
    });

        $("#eliminar").click(function () {
                event.preventDefault();
            $.ajax({
                type: "DELETE",
                url: "https://cachimbogo.herokuapp.com/servicios/pregunta/" +$('#idPregunta').val(),
                csrfmiddlewaretoken: "{{ csrf_token }}",
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
    });

    function actualizarData(obj) {
        event.preventDefault();
        $.ajax({
            type: "PUT",
            url: "http://cachimbogo.herokuapp.com/servicios/pregunta/" +$('#idPregunta').val(),
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

    function cargarSelect(url, id, name) {
        var select = $("#" + id);
        var option = document.createElement("option");
        option.text = "Seleccione " + name;
        select.append(option);
        $.get(url, function (datos) {
            for (var value in datos) {
                var option = document.createElement("option");
                option.text = datos[value].nombre;
                if (name === "temas") {
                    option.value = datos[value].id_tema;
                } else {
                    option.value = datos[value].id_subtema;
                }
                option.classList.add("mystyle");
                select.append(option);
            }
        });
    }

});

function crearObj(subtema,pregunta, alternativa1, alternativa2, alternativa3,
    alternativa3, alternativa4, alternativa5, informacion, dificultad, correcta) {

    this.id_pregunta = $('#idPregunta').val();
    this.enunciado = pregunta;
    this.clave1 = alternativa1;
    this.clave2 = alternativa2;
    this.clave3 = alternativa3;
    this.clave4 = alternativa4;
    this.clave5 = alternativa5;
    this.estado = 1;
    this.id_subtema = parseInt(subtema);
    this.id_tipopregunta = 2;
    this.id_dificultad = parseInt(dificultad);
    this.correcta_num = parseInt(correcta);
    this.informacion = informacion;
}