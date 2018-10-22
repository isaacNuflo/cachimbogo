$(document).ready(function () {
    var tema, subtema, asignatura;
    //Captura el ID de los dropdown
    var selectAsiganaturas = $("#selectAsignaturas").attr("id");
    var selectTemas = $("#selectTemas").attr("id");
    var selectSubTemas = $("#selectSubTemas").attr("id");

    $(".form-control").change(function () {
        var url = "";
        var id = $(this).attr("id");
        if (id === selectAsiganaturas) {
            asignatura = $(this).val();
            // cargar url del servicio de temas
            url = "https://cachimbogo.herokuapp.com/servicios/tema-asignatura/" + asignatura; 
            $("#" + selectTemas).empty();
            cargarSelect(url, selectTemas, "temas");
        } else if (id === selectTemas) {
            tema = $(this).val();
            $("#" + selectSubTemas).empty();
            // cargar url de servicio de subtemas
            url = "https://cachimbogo.herokuapp.com/servicios/subtema-tema/" + tema; 

            cargarSelect(url, selectSubTemas, "subtemas");
        } else if (id === selectSubTemas) {
            subtema = $(this).val();
        }    
    });
    $("#buscar").click(function () {
        // Carga las preguntas
        var url = "https://cachimbogo.herokuapp.com/servicios/preguntaT/" + subtema; 
        cargarTabla(url);
    });
    $("#agregar").click(function () {
        //Redireccion
        window.location.href = "https://cachimbogo.herokuapp.com/webadmin/questionCreate";
    });
    //Carga una tabla con las preguntas para que seleccione la que se editará
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
                btn.onclick = function(){window.location.href = "https://cachimbogo.herokuapp.com/webadmin/questionUpdate/"+datos[value].id_pregunta; };
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
    //Funcion que carga el contenido de los dropdown
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