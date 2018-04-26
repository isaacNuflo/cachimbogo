//Solo para pruebas
var datos=[ // FORMATO DEL JSON QUE SE VA A RECIBIR PARA CARGAR TEMAS Y SUBTEMAS
     {"id":1,
      "asignatura":"asignatura1"
  },
     {"id":2,
      "asignatura":"asignatura2"
  },
     {"id":3,
      "asignatura":"asignatura3"}
];
// ------

$(document).ready(function () {
    var tema, subTema, asignatura, pregunta, alternativa1, alternativa2, alternativa3,
            alternativa4, alternativa5, informacion, dificultad, correcta;

    var selectAsiganaturas = $("#selectAsiganturas").attr("id");
    var selectTemas = $("#selectTemas").attr("id");
    var selectSubTemas = $("#selectSubTemas").attr("id");
    var selectAlternativa = $("#selectAlternativa").attr("id");
    var selectDificultad = $("#selectDificultad").attr("id");

    $(".form-control").change(function () {
        var id = $(this).attr("id");
        if (id === selectAsiganaturas) {
            asignatura = $(this).val();
            
             var url = "http://localhost:8000/servicios/tema-asignatura/" + asignatura; // cargar url del servicio de temas 
             $("#"+selectTemas).empty();
            cargarSelect(url,selectTemas,"temas");
        } else if (id === selectTemas) {
             tema = $(this).val();
              $("#"+selectSubTemas).empty();
              
             var url = "http://localhost:8000/servicios/subtema-tema/" + tema;// cargar url de servicio de subtemas
             
            cargarSelect(url, selectSubTemas,"subtemas");
        } else if (id === selectSubTemas) {
            subTema = $(this).val();
        } else if (id === selectAlternativa) {
            correcta = $(this).val();
        } else if (id === selectDificultad) {
            dificultad = $(this).val();
        }
    });
    $("#guardar").click(function () {

        pregunta = $("#Pregunta").val();
        alternativa1 = $("#Alternativa1").val();
        alternativa2 = $("#Alternativa2").val();
        alternativa3 = $("#Alternativa3").val();
        alternativa4 = $("#Alternativa4").val();
        alternativa5 = $("#Alternativa5").val();
        informacion = $("#info").val();



        var obj = new crearObj(subTema, pregunta, alternativa1, alternativa2, alternativa3,
                alternativa3, alternativa4, alternativa5, informacion, dificultad, correcta);


        enviarData(obj);
    });

    function enviarData(obj) { 
            event.preventDefault();
            $.ajax({
              type : "POST",
              url : "http://localhost:8000/servicios/preguntaT/",
              csrfmiddlewaretoken: "{{ csrf_token }}",
              data : JSON.stringify(obj),
              headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
                },
              success: function(){
                  alert("Saved! It worked.");
                },
              error: function(XMLHttpRequest, textStatus, errorThrown) {
                alert("some error " + String(errorThrown) + String(textStatus) + String(XMLHttpRequest.responseText));
                }
              });
          
    }

    function cargarSelect(url, id, name) {
        var select = $("#" + id);
        var option = document.createElement("option");
                option.text = "Seleccione "+name;
                select.append(option);
        $.get(url, function (datos) {
            for (var value in datos) {
                var option = document.createElement("option");
                option.text = datos[value].nombre;
                if(name === "temas"){
                    option.value=datos[value].id_tema;
                }else{
                    option.value=datos[value].id_subtema;
                }  
                option.classList.add("mystyle");
                select.append(option);
            }
       });
    }

});
function crearObj(subTema, pregunta, alternativa1, alternativa2, alternativa3,
        alternativa3, alternativa4, alternativa5, informacion, dificultad, correcta) {
    this.id_pregunta = null;
    this.enunciado = pregunta;
    this.clave1 = alternativa1;
    this.clave2 = alternativa2;
    this.clave3 = alternativa3;
    this.clave4 = alternativa4;
    this.clave5 = alternativa5;
    this.correcta = correcta;
    this.estado = 1;
    this.informacion_id_informacion = informacion;
    this.subtema_id_subtema = subTema;
    this.tipo_pregunta_id_tipopregunta = 2;
    this.dificultad_id_dificultad = dificultad;
}