
$(document).ready(function(){


    /* para obtener la geolocalizacion */

    if(navigator.geolocation){
        /* alert("si autoriza"); */

        navigator.geolocation.getCurrentPosition(ObtenerLocalizacion);


    }else{
        alert("No autoriza");
    }


    /* aqui obtiene las coordenadas de la persona */
    function ObtenerLocalizacion(position){
        /* console.log(+" "+position.coords.longitude);
        alert("Coordenadas \n"+position.coords.latitude+" "+position.coords.longitude); */
        $.get("https://api.open-meteo.com/v1/forecast?latitude="+position.coords.latitude+"&longitude="+position.coords.longitude+"&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
        ,function(data){
            
            
            /* console.log(data);
            console.log(data["current_weather"]["temperature"]);
            console.log(data["current_weather"]["windspeed"]); */

            $("#Temperatura").html("La temperatura es: "+data["current_weather"]["temperature"]);
            $("#otroDato").html("La velocidad del viento es: "+data["current_weather"]["windspeed"]);
            

        });

    };





    /* Codigo que describe lo que se hara al presionar el boton de enviar 
    en el contactenos */
    $("#btnEnviarU ").click(function(e){
        if(validaFormularioC() != ""){
            swal("Error de Envio",validaFormularioC(),"warning");
        }else{
            swal("Datos enviados","Nos pondremos en contacto con usted a la ","sucess");
            /* swal("Good job!", "You clicked the button!", "success"); */
        }

        e.preventDefault();
    });

    

}); 

function validaFormularioC(){

        /* variables a ocupar en las validaciones */
        var html ="";
        var nombre =$("#txtNombreCompleto").val();
        var edad =$("#txtEdad").val();
        var correo =$("#txtemail").val();
        var contraseña =$("#txtContraseña").val();
        var nroContacto =$("#txtnumero").val();
        var ciudad =$("#cbxCiudad").val();
        var comuna =$("#cbxComuna").val();
        var comentario =$("#txtAreaComentario").val();

        if(nombre==""){
            html+="-Debe ingresar un Nombre\n";
        }
        if(edad==""){
            html+="-Debe ingresar una edad \n";
        }
        /* aqui valida que seleccione un tipo de documento  */
        if(($("#RadioRut")).is(":not(:checked)")&&($("#RadioPasaporte")).is(":not(:checked)")){
            html+="-Debe seleccionar un tipo de documento verificador \n"
        }else{
            /* aqui valida si es que el rut es valido si selecciona esta opcion */
            if(($("#RadioRut")).is(":checked")){
                if(validarRut($("#txtNroDocumento").val())==false){
                    html += "- Debe Ingresar un RUT Valido \n";
                }
            }
        }

        if(correo==""){
            html+="-Debe ingresar un correo \n";
        }
        if(contraseña==""){
            html+="-Debe ingresar una contraseña \n"
        }else{
            if((contraseña).length< 8){
                html+="-Debe ingresar una contraseña de minimo 8 caracteres\n"
            }
        }
        if(nroContacto==""){
            html+="-Debe ingresar un Nro de Contacto \n";
        }else{
            if((nroContacto).length <8){
                html+="-Debe ingresar un Nro de Contacto Valido\n";
            }
        }
        if(($("#RadioMasculino")).is(":not(:checked)")&&($("#RadioFemenino")).is(":not(:checked)")&&($("#RadioOtro")).is(":not(:checked)")){
            html+="-Debe seleccionar un tipo de Genero \n"
        }
        if(parseInt(ciudad)==0){
            html+="-Debe seleccionar una ciudad \n";
        }
        if(parseInt(comuna)==0){
            html+="-Debe seleccionar una comuna \n";
        }
        if(comentario.trim().length < 50){
            html+="-el Comentario debe tener minimo 50 caracteres \n";
        }

        return html;

    };

    function validarRut(rutCompleto) {
        // Primero eliminamos cualquier caracter que no sea número o k/K
        rutCompleto = rutCompleto.replace("‐", "-");
    
        // Luego validamos que el formato del RUT sea válido
        if (!/^[0-9]+[-|‐]{1}[0-9kK]{1}$/.test(rutCompleto))
            return false;
    
        // Separamos el número del dígito verificador    
        var tmp = rutCompleto.split('-');
        // Calculamos el dígito verificador esperado
        var digv = tmp[1];
        var rut = tmp[0];
        if (digv == 'K') digv = 'k';
        // Comparamos el dígito verificador ingresado con el esperado
        return (dv(rut) == digv);
    };
    
    function dv(T) {
        var M = 0,
            S = 1;
        for (; T; T = Math.floor(T / 10))
            S = (S + T % 10 * (9 - M++ % 6)) % 11;
        return S ? S - 1 : 'k';
    };
