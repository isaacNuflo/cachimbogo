$(document).ready(function () {
    var tema, subtema, asignatura;

    var selectAsiganaturas = $("#selectAsignaturas").attr("id");
    var selectTemas = $("#selectTemas").attr("id");
    var selectSubTemas = $("#selectSubTemas").attr("id");

    $(".form-control").change(function () {
        var id = $(this).attr("id");
        if (id === selectAsiganaturas) {
            asignatura = $(this).val();

            var url = "http://127.0.0.1:8000/servicios/tema-asignatura/" + asignatura; // cargar url del servicio de temas
            $("#" + selectTemas).empty();
            cargarSelect(url, selectTemas, "temas");
        } else if (id === selectTemas) {
            tema = $(this).val();
            $("#" + selectSubTemas).empty();

            var url = "http://127.0.0.1:8000/servicios/subtema-tema/" + tema; // cargar url de servicio de subtemas

            cargarSelect(url, selectSubTemas, "subtemas");
        } else if (id === selectSubTemas) {
            subtema = $(this).val();
        }    
    });
    $("#buscar").click(function () {
        var url = "http://127.0.0.1:8000/servicios/preguntaT/" + subtema;
        cargarTabla(url);
    });

    function cargarTabla(url) {
        var table = $("#tabla tr");
        table.remove();
        table = $("#tabla");
        var trHId = document.createElement("tr");
        table.append(trHId);
        var thId = document.createElement("th");
        trHId.appendChild(thId);
        thId.append("Id_pregunta");
        var thEnunciado = document.createElement("th");
        trHId.appendChild(thEnunciado);
        thEnunciado.append("Enunciado");
        var thDetalles = document.createElement("th");
        trHId.appendChild(thDetalles);
        thDetalles.append("Detalles");
        $.get(url, function (datos) {
            for (var value in datos) {
                var tr = document.createElement("tr");
                table.append(tr);
                var tdId = document.createElement("td");
                var tdEnunciado = document.createElement("td");
                var btn = document.createElement("button");
                btn.setAttribute('className','btn btn-outline-primary');
                btn.setAttribute('id','detalles');
                btn.onclick = function(){window.location.href = "http://127.0.0.1:8000/webadmin/questionUpdate/"+datos[value].id_pregunta; };
                tr.appendChild(tdId);
                tr.appendChild(tdEnunciado);
                tr.appendChild(btn);
                var txtId = document.createTextNode(datos[value].id_pregunta);
                var txtEnunciado = document.createTextNode(datos[value].enunciado);
                tdId.appendChild(txtId);
                tdEnunciado.appendChild(txtEnunciado);
                btn.append("Detalles");
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