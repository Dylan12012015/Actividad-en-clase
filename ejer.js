var edad=prompt("Digita tu edad: ")
if (edad>=18){
    alert("Si puede conducir")
}
else{
    alert("Aprende a conducir")
}

do{
    var nota=parseInt(prompt("Digita la nota que sacaste"))
    if (nota>=0 && nota<=3){
        alert("muy deficiente")
    }
    else if (nota>3 && nota<=5){
        alert("insuficiente")
    }
    else if (nota>5 && nota<=7){
        alert("bien")
    }
    else if (nota>7 && nota<=9){
        alert("notable")
    }
    else if (nota>9 && nota<=10){
        alert("sobresaliente")
    }
}while(nota<10.1)



do{
    var nombre=prompt("colaca tu nombre: ");
    if(nombre=="cancelar")break;
    var apellido=prompt("coloca tu apellido: ");
    var conca=nombre+"-"+apellido;
    alert(conca);
}while(nombre!="cancelar" && apellido!="cancelar")