var boletas = "";

function agregarBoleta(){
    var boleta = document.getElementById('idSilla').value;
    if(boletas == ""){
        boletas = boleta;
    }
    else if(boletas.slice(-2) == boleta){
        alert("Seleccione otra boleta");
    }
    else{
        alert(boletas.slice(-2))
        boletas = boletas + "," + boleta;
    }

    document.getElementById('boletas').value = boletas; 
}
